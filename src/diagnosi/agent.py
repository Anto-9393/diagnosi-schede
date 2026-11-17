"""Agente diagnostico — l'"Autonomia" del PDF (S03 tool calling + memoria; S11 conoscenza in @tool).

Una SessioneDiagnosi = una scheda al banco:
  - l'Agent di datapizza decide da solo quali pagine della wiki leggere (leggi_indice / cerca_wiki / leggi_pagina);
  - stateless=False: ricorda le misure già date nella conversazione (memoria);
  - output_cls=PassoDiagnosi: ogni risposta è strutturata (S02);
  - guardrails.controlla(): sicurezza, valori, sigle, fonti (S15);
  - osservabilità: ContextTracing (token, durata) + una riga JSON per ogni passo in docs/log/sessioni.jsonl.
"""
from __future__ import annotations

import json
import time
from datetime import datetime

from datapizza.agents import Agent
from datapizza.tools import tool
from datapizza.tracing import ContextTracing

from diagnosi import guardrails, wiki_tools
from diagnosi.config import MODEL_DEV, PROVIDER, ROOT, leggi_prompt
from diagnosi.llm import crea_client
from diagnosi.schemas import PassoDiagnosi

LOG_FILE = ROOT / "docs" / "log" / "sessioni.jsonl"


class SessioneDiagnosi:
    def __init__(self, model: str = MODEL_DEV, client=None, max_steps: int = 10):
        self.model = model
        self.pagine_lette: dict[str, str] = {}      # percorso -> testo: serve ai guardrail (sigle e fonti)
        self.chiamate_tool: list[str] = []
        self.id = datetime.now().strftime("%Y%m%d-%H%M%S")
        self.agente = Agent(
            name="diagnosta",
            client=client or crea_client(model),
            system_prompt=leggi_prompt("tecnico") + "\n" + leggi_prompt("agente"),
            tools=self._crea_tool(),
            output_cls=PassoDiagnosi,
            stateless=False,                        # memoria della sessione
            max_steps=max_steps,
        )

    def _crea_tool(self):
        """Gli stessi tre tool di wiki_tools, ma che REGISTRANO cosa legge l'agente (per guardrail e log)."""
        sessione = self

        @tool(name="leggi_indice")
        def leggi_indice() -> str:
            """Legge wiki/index.md, il catalogo di tutte le pagine. Da usare per primo."""
            sessione.chiamate_tool.append("leggi_indice()")
            return wiki_tools.indice()

        @tool(name="leggi_pagina")
        def leggi_pagina(percorso: str) -> str:
            """Legge una pagina della wiki, es. 'componenti/cd3217.md'. Il risultato inizia con 'FONTE: ...'."""
            sessione.chiamate_tool.append(f"leggi_pagina({percorso})")
            testo = wiki_tools.pagina(percorso)
            if testo.startswith("FONTE: "):
                sessione.pagine_lette[testo.split("\n", 1)[0].removeprefix("FONTE: ")] = testo
            return testo

        @tool(name="cerca_wiki")
        def cerca_wiki(query: str) -> str:
            """Cerca nella wiki per parole chiave (sigle, sintomi, modelli). Poi apri le pagine con leggi_pagina."""
            sessione.chiamate_tool.append(f"cerca_wiki({query})")
            return wiki_tools.cerca(query)

        return [leggi_indice, leggi_pagina, cerca_wiki]

    def chiedi(self, messaggio: str) -> tuple[PassoDiagnosi, guardrails.Esito, dict]:
        n_tool_prima = len(self.chiamate_tool)
        t0 = time.perf_counter()
        with ContextTracing().trace(f"diagnosi-{self.id}"):
            risultato = self.agente.run(messaggio, tool_choice="required_first")
        durata = time.perf_counter() - t0
        if not risultato or not risultato.structured_data:
            raise RuntimeError("L'agente non ha prodotto un PassoDiagnosi (aumenta max_steps o riprova).")
        passo, esito = guardrails.controlla(risultato.structured_data[-1], self.pagine_lette)
        info = {
            "sessione": self.id, "ora": datetime.now().isoformat(timespec="seconds"),
            "provider": PROVIDER, "modello": self.model, "durata_s": round(durata, 2),
            "token_in": risultato.usage.prompt_tokens, "token_out": risultato.usage.completion_tokens,
            "tool": self.chiamate_tool[n_tool_prima:], "fonti": passo.fonti,
            "avvisi": esito.avvisi, "bloccato": esito.bloccato,
            "input": messaggio, "dispositivo": passo.dispositivo,
            "ipotesi": [f"[{i.probabilita}] {i.componente}" for i in passo.ipotesi],
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
    print(f"\n--- {info['durata_s']} s · token {info['token_in']}/{info['token_out']} · tool: {len(info['tool'])}")
