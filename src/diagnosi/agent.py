"""Agente diagnostico — l'"Autonomia" del PDF (S03 tool calling + memoria; S11 conoscenza in @tool).

Una SessioneDiagnosi = una scheda al banco:
  - l'Agent di datapizza decide da solo quali pagine della wiki leggere (leggi_indice / cerca_wiki / leggi_pagina);
  - stateless=False: ricorda le misure già date nella conversazione (memoria);
  - output_cls=PassoDiagnosi: ogni risposta è strutturata (S02);
  - se il tecnico chiede "come si fa" (tipo_richiesta), risponde un secondo agente con output_cls=Procedura:
    stessi tool, stessa memoria, schema diverso;
  - guardrails.controlla(): sicurezza, valori, sigle, fonti (S15);
  - osservabilità: ContextTracing (token, durata) + una riga JSON per ogni passo in docs/log/sessioni.jsonl.
"""
from __future__ import annotations

import json
import re
import time
from datetime import datetime

from datapizza.agents import Agent
from datapizza.tools import tool
from datapizza.tracing import ContextTracing

from diagnosi import guardrails, sigle, wiki_tools
from diagnosi.config import MODEL_DEV, PROVIDER, ROOT, leggi_prompt
from diagnosi.llm import crea_client
from diagnosi.schemas import PassoBreve, PassoDiagnosi, Procedura

LOG_FILE = ROOT / "docs" / "log" / "sessioni.jsonl"

# "Come sostituisco il CD3217", "spiegami come programmare la ROM", "procedura reball": il tecnico vuole i PASSI.
# Regola nel codice, non nell'LLM: deterministica, gratis, testabile (come i guardrail di S15).
_PROCEDURA = re.compile(
    r"\bcome\s+(si\s+)?(sostitu|cambi|programm|dissald|sald|smont|rimont|rimuov|tolg|togli|install|legg|scriv|"
    r"trasfer|reball|riball|fa\b|faccio\b|fare\b)|\bprocedura\b|\bspiegami\s+come\b|\bpassaggi\b|\bhow\s+to\b",
    re.I)


# Segni di diagnosi: misure con unità, sintomi, parole da banco di misura.
_DIAGNOSI = re.compile(
    r"\d+(?:[.,]\d+)?\s*(?:v|mv|a|ma|ohm|Ω)\b|\bnon\s+(?:carica|si\s+accende|rileva|parte)|\bmisur|\bdiode|\bcorto|"
    r"\bassorb|\bsintom|\bguast|\bpanic", re.I)


# Parole del banco: se un messaggio non ne contiene nessuna, non è una domanda di riparazione.
_TEMA = re.compile(
    r"carica|accend|spent|batteri|scherm|display|touch|face\s*id|touch\s*id|wi-?fi|bluetooth|audio|microfon|"
    r"altoparl|speaker|fotocamer|camera|tast|usb|lightning|connettor|scheda|logic|board|chip|\bic\b|pmic|tristar|"
    r"tigris|nand|\brom\b|eeprom|cpu|sald|dissald|aria\s+calda|reball|riball|corto|misur|volt|amper|ohm|diod|"
    r"condensator|resistenz|resistor|bobin|indutt|fusibil|pist|piazzol|\bpad\b|ossid|corros|acqua|liquid|cadut|"
    r"riavvi|boot|logo|\bdfu\b|itunes|ripristin|restore|errore|panic|assorb|alimentator|iphone|ipad|apple|"
    r"\ba\d{4}\b|\b[a-z]{1,3}\d{3,5}\b|\b(?:x|u|q|c|r|l|j|f)\d{1,4}\b|guast|ripar|sostitu|programm|"
    r"funzion|segnale|\brete\b|\bsim\b|baseband|nfc|vibr|sensor|tension|corrent|caldo|scalda|surriscald|"
    r"multimetr|oscillosc|boardview|schema|test\s*point|\btp\d|\bv\b|\bma\b|rispondo alle tue domande",
    re.I)


def fuori_tema(messaggio: str, in_corso: bool = False) -> bool:
    """True se il messaggio non riguarda la riparazione (es. "qual è la capitale della Francia?"): l'app risponde
    da sola, senza chiamare il modello. A diagnosi `in_corso`, le risposte brevi ("sì", "no", "nessuna") passano."""
    if _TEMA.search(messaggio) or _DIAGNOSI.search(messaggio) or _PROCEDURA.search(messaggio):
        return False
    return not (in_corso and len(messaggio.split()) <= 4)


def tipo_richiesta(messaggio: str, precedente: str | None = None) -> str:
    """'procedura' se il tecnico chiede come si fa un intervento, altrimenti 'diagnosi'.

    `precedente` = tipo del turno prima. Dopo una procedura si RESTA in procedura se il messaggio è una risposta
    (es. "sto usando A2316" alla domanda "che modello è?"), a meno che non porti misure o sintomi
    (risposta reale del 17 nov: "sto usando a2316 come modello" finiva al diagnosta e perdeva la procedura)."""
    if _PROCEDURA.search(messaggio):
        return "procedura"
    # Resta in procedura solo una RISPOSTA all'agente; una domanda nuova ("l'Air 3 ha il Tristar o il CD3217?") no.
    if precedente == "procedura" and not _DIAGNOSI.search(messaggio) and not messaggio.strip().endswith("?"):
        return "procedura"
    return "diagnosi"


class SessioneDiagnosi:
    def __init__(self, model: str = MODEL_DEV, client=None, max_steps: int = 10,
                 dettaglio: str = "completa", lettura: str = "approfondita"):
        """dettaglio: "completa" (ipotesi + misura) o "breve" (solo la prossima misura).
        lettura: "approfondita" (pagine intere, fino a 10 passi) o "rapida" (max 3 pagine, solo l'inizio).
        Le sceglie il riparatore: la lettura rapida è quella che risparmia più token (l'input è ~97% del totale)."""
        self.model, self.dettaglio, self.lettura = model, dettaglio, lettura
        self.max_caratteri = 4_000 if lettura == "rapida" else wiki_tools.MAX_CARATTERI_PAGINA
        istruzioni = []
        if dettaglio == "breve":
            istruzioni.append("Il tecnico vuole SOLO la prossima misura: niente riepilogo né elenco di ipotesi.")
        if lettura == "rapida":
            istruzioni.append("Lettura RAPIDA: leggi al massimo 3 pagine (dispositivo, sintomo, componente principale); "
                              "non leggere l'indice se conosci già i percorsi.")
            max_steps = min(max_steps, 5)
        self.pagine_lette: dict[str, str] = {}      # percorso -> testo: serve ai guardrail (sigle e fonti)
        self.chiamate_tool: list[str] = []
        self.storia: list[str] = []                 # memoria compatta dei turni (vedi _input_con_storia)
        self.ultimo_tipo: str | None = None         # "diagnosi" o "procedura": serve a tipo_richiesta
        self.id = datetime.now().strftime("%Y%m%d-%H%M%S")
        client = client or crea_client(model)
        strumenti = self._crea_tool()               # gli stessi tool per i due agenti: registrano nella stessa sessione
        base = leggi_prompt("tecnico") + "\n" + leggi_prompt("agente")
        self.agente = Agent(
            name="diagnosta",
            client=client,
            system_prompt=base
                          + ("\n\n## Modalità scelta dal tecnico\n" + "\n".join(f"- {i}" for i in istruzioni) if istruzioni else ""),
            tools=strumenti,
            output_cls=PassoBreve if dettaglio == "breve" else PassoDiagnosi,
            stateless=True,                         # memoria COMPATTA gestita da noi (vedi chiedi): niente pagine ripetute
            max_steps=max_steps,
        )
        lettura_rapida = [i for i in istruzioni if i.startswith("Lettura RAPIDA")]   # "breve" non vale per le procedure
        self.agente_procedura = Agent(
            name="istruttore",
            client=client,
            system_prompt=base + "\n" + leggi_prompt("procedura")
                          + ("\n\n## Modalità scelta dal tecnico\n- " + lettura_rapida[0] if lettura_rapida else ""),
            tools=strumenti,
            output_cls=Procedura,
            stateless=True,
            max_steps=max_steps,
        )

    def _crea_tool(self):
        """Gli stessi tre tool di wiki_tools, ma che REGISTRANO cosa legge l'agente (per guardrail e log)."""
        sessione = self

        @tool(name="leggi_indice")
        def leggi_indice() -> str:
            """Legge wiki/index.md, il catalogo di tutte le pagine. Da usare per primo."""
            sessione.chiamate_tool.append("leggi_indice()")
            return wiki_tools.indice(compatto=True)

        @tool(name="leggi_pagina")
        def leggi_pagina(percorso: str) -> str:
            """Legge una pagina della wiki, es. 'componenti/cd3217.md'. Il risultato inizia con 'FONTE: ...'."""
            sessione.chiamate_tool.append(f"leggi_pagina({percorso})")
            testo = wiki_tools.pagina(percorso, max_caratteri=sessione.max_caratteri)
            if testo.startswith("FONTE: "):
                sessione.pagine_lette[testo.split("\n", 1)[0].removeprefix("FONTE: ")] = testo
            return testo

        @tool(name="cerca_wiki")
        def cerca_wiki(query: str) -> str:
            """Cerca nella wiki per parole chiave (sigle, sintomi, modelli). Poi apri le pagine con leggi_pagina."""
            sessione.chiamate_tool.append(f"cerca_wiki({query})")
            return wiki_tools.cerca(query)

        return [leggi_indice, leggi_pagina, cerca_wiki]

    def _input_con_storia(self, messaggio: str) -> str:
        """Memoria compatta: ai turni successivi l'agente riceve COSA si è detto (misure e risposte),
        non il testo delle pagine lette (misurato il 17 nov: un 2° turno con memoria completa = 74.752 token)."""
        if not self.storia:
            return messaggio
        gia_lette = ", ".join(self.pagine_lette) or "nessuna"
        return ("STORIA DELLA DIAGNOSI (turni precedenti, in ordine):\n" + "\n".join(self.storia)
                + f"\n\nPagine già consultate (rileggile solo se servono): {gia_lette}"
                + "\n\nNUOVO MESSAGGIO DEL TECNICO:\n" + messaggio)

    def _ricorda(self, messaggio: str, passo) -> None:
        if isinstance(passo, Procedura):
            self.storia.append(f"- Tecnico: {messaggio.strip()}")
            self.storia.append(f"- Agente: procedura '{passo.obiettivo}' in {len(passo.passi)} passi: "
                               + "; ".join(p.titolo for p in passo.passi) + ".")
            return
        m = passo.prossima_misura
        ipotesi = "; ".join(f"[{i.probabilita}] {i.componente}" for i in getattr(passo, "ipotesi", []))
        self.storia.append(f"- Tecnico: {messaggio.strip()}")
        self.storia.append(f"- Agente: {('ipotesi ' + ipotesi + '. ') if ipotesi else ''}"
                           f"Proposta: misura {m.dove} ({m.modalita}), condizioni: {m.condizioni}, atteso: {m.valore_atteso}.")

    def precarica(self, percorsi: list[str]) -> str:
        """Pagine che l'agente leggerebbe comunque (es. dispositivo scelto dal menu e i suoi casi): gliele diamo già
        nel primo messaggio, così risparmia un giro di tool per pagina (misurato il 20 nov: 6 letture in fila = 22 s).
        Le registriamo come lette: il guardrail delle fonti le accetta come se le avesse aperte lui."""
        blocchi = []
        for p in percorsi:
            testo = wiki_tools.pagina(p, max_caratteri=self.max_caratteri)
            if testo.startswith("FONTE: "):
                self.pagine_lette[testo.split("\n", 1)[0].removeprefix("FONTE: ")] = testo
                blocchi.append(testo)
        if not blocchi:
            return ""
        return ("PAGINE DELLA WIKI GIÀ LETTE PER TE (non rileggerle con leggi_pagina; citale nelle fonti se le usi):\n\n"
                + "\n\n---\n\n".join(blocchi))

    def chiedi(self, messaggio: str, contesto: str = "") -> tuple[PassoDiagnosi | PassoBreve | Procedura, guardrails.Esito, dict]:
        """`contesto`: testo in più solo per QUESTO turno (pagine precaricate). Non va nella memoria dei turni dopo."""
        n_tool_prima = len(self.chiamate_tool)
        tipo = tipo_richiesta(messaggio, self.ultimo_tipo)
        agente = self.agente_procedura if tipo == "procedura" else self.agente
        t0 = time.perf_counter()
        with ContextTracing().trace(f"{tipo}-{self.id}"):
            ingresso = self._input_con_storia(messaggio)
            risultato = agente.run(contesto + "\n\n" + ingresso if contesto else ingresso,
                                   tool_choice="auto" if contesto else "required_first")
        durata = time.perf_counter() - t0
        if not risultato or not risultato.structured_data:
            raise RuntimeError(f"L'agente non ha prodotto una risposta ({tipo}): aumenta max_steps o riprova.")
        controllo = guardrails.controlla_procedura if tipo == "procedura" else guardrails.controlla
        passo, esito = controllo(risultato.structured_data[-1], self.pagine_lette)
        passo = sigle.nomi_precisi(passo, self.pagine_lette.values())      # "X3" -> "343S00264-A0 (X3 su JC Drawing)"
        self._ricorda(messaggio, passo)
        self.ultimo_tipo = tipo
        info = {
            "sessione": self.id, "ora": datetime.now().isoformat(timespec="seconds"),
            "provider": PROVIDER, "modello": self.model, "tipo": tipo,
            "dettaglio": "procedura" if tipo == "procedura" else self.dettaglio, "lettura": self.lettura,
            "durata_s": round(durata, 2),
            "token_in": risultato.usage.prompt_tokens, "token_out": risultato.usage.completion_tokens,
            "token_cache": getattr(risultato.usage, "cached_tokens", 0) or 0,   # sconto automatico di OpenAI
            "turno": len(self.storia) // 2,
            "tool": self.chiamate_tool[n_tool_prima:], "fonti": passo.fonti,
            "avvisi": esito.avvisi, "bloccato": esito.bloccato,
            "input": messaggio, "dispositivo": passo.dispositivo,
            "ipotesi": [f"[{i.probabilita}] {i.componente}" for i in getattr(passo, "ipotesi", [])],
            # per rileggere la risposta (debug, speech)
            "risposta": passo.model_dump(exclude={"fonti", "avvertenze_sicurezza", "dispositivo"}),
            "avvertenze": passo.avvertenze_sicurezza,
        }
        LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
        with LOG_FILE.open("a", encoding="utf-8") as f:
            f.write(json.dumps(info, ensure_ascii=False) + "\n")
        return passo, esito, info


def stampa(passo: PassoDiagnosi, esito: guardrails.Esito, info: dict) -> None:
    if esito.bloccato:
        print("\n!!! RISPOSTA BLOCCATA DAI GUARDRAIL !!!")
        print(*esito.avvisi, sep="\n  - ")
        return
    print("\nDISPOSITIVO:", passo.dispositivo)
    if isinstance(passo, Procedura):
        print("PROCEDURA:", passo.obiettivo)
        for n, p in enumerate(passo.passi, 1):
            print(f"\n{n}. {p.titolo}\n   {p.azione}")
            if p.attrezzo:
                print(f"   attrezzo: {p.attrezzo}")
            if p.controllo:
                print(f"   controllo: {p.controllo}")
        if passo.verifica_finale:
            print("\nVERIFICA FINALE:", *passo.verifica_finale, sep="\n  - ")
        if passo.avvertenze_sicurezza:
            print("\nAVVERTENZE:", *passo.avvertenze_sicurezza, sep="\n  - ")
        print("\nFONTI:", *(passo.fonti or ["nessuna"]), sep="\n  - ")
        print(f"\n--- {info['durata_s']} s · token {info['token_in']}/{info['token_out']} · tool: {len(info['tool'])}")
        return
    if hasattr(passo, "ipotesi"):                     # modalità completa
        print("RIEPILOGO:", passo.riepilogo, "\n")
        print("IPOTESI:")
        for i, ip in enumerate(passo.ipotesi, 1):
            print(f"  {i}. [{ip.probabilita}] {ip.componente} — {ip.motivo}")
    m = passo.prossima_misura
    print(f"\nPROSSIMA MISURA: {m.dove} ({m.modalita})")
    print(f"  condizioni:    {m.condizioni}\n  valore atteso: {m.valore_atteso}\n  se diverso:    {m.se_diverso}")
    if passo.avvertenze_sicurezza:
        print("\nAVVERTENZE:", *passo.avvertenze_sicurezza, sep="\n  - ")
    if passo.domande_al_tecnico:
        print("\nDOMANDE:", *passo.domande_al_tecnico, sep="\n  - ")
    print("\nFONTI:", *(passo.fonti or ["nessuna"]), sep="\n  - ")
    print(f"\n--- {info['durata_s']} s · token {info['token_in']}/{info['token_out']} "
          f"(in cache {info['token_cache']}) · tool: {len(info['tool'])}")
