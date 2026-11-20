"""Guardrail sulle risposte dell'agente — deterministici, come in S15 ("output handling": l'output del
modello è input non fidato per chi lo usa). Nessun LLM: si testano senza chiave.

Quattro controlli su ogni PassoDiagnosi:
  1. SICUREZZA ELETTRICA — alimentatore/iniezione senza limite di corrente, batteria oltre i limiti Li-ion,
     calore vicino alla batteria, istruzioni pericolose (bloccanti).
  2. VALORI IMPOSSIBILI — tensioni oltre i 20 V (massimo USB-PD per questi dispositivi).
  3. SIGLE NON VERIFICATE — sigle di componenti (U4001, J2201, 343S00264...) che non compaiono in nessuna
     pagina letta: il modello potrebbe averle inventate.
  4. FONTI — le fonti dichiarate devono essere pagine lette davvero; senza fonti la risposta è "da verificare".

I guardrail non cancellano la risposta: la ANNOTANO (avvertenze in testa) e la bloccano solo se pericolosa.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field

from diagnosi.schemas import PassoBreve, PassoDiagnosi, Procedura

MAX_TENSIONE_USB_V = 20.0
MAX_TENSIONE_CELLA_V = 4.4

_PERICOLOSI = [
    (r"cortocircuit\w*\s+(la\s+)?batteria|short\w*\s+the\s+battery", "Mai cortocircuitare la batteria."),
    (r"senza\s+limite\s+di\s+corrente|no\s+current\s+limit", "Mai alimentare senza limite di corrente."),
    # Solo il CALORE APPLICATO dal tecnico. "scalda" da solo no: è anche un sintomo ("con la termocamera vedi cosa
    # scalda per primo... con batteria"), falso blocco del 20 nov.
    (r"(aria\s+calda|hot\s+air|stazione\s+ad\s+aria|pre-?riscald\w*|\b(?:ri)?scaldare)[^.]{0,60}batteria",
     "Mai scaldare vicino alla batteria: va scollegata e allontanata."),
]
_ALIMENTAZIONE = r"alimentator\w*|banco|dc\s+power|iniezion\w*|inject\w*|power\s+supply"
_LIMITE = r"limit\w*\s+(di\s+)?corrente|corrente\s+limitat\w*|current\s+limit"
# Sigle tipiche: designatori (U4001, J2201, C4005, X1548, Q2001, L2020, PP_VCC_MAIN no) e codici di chip.
_SIGLA = re.compile(r"\b(?:[UJCXQLRDF]\d{3,5}|343S\d{4,5}|338S\d{4,5}|CD\d{4}[A-Z]?\d*|610A3B|SN\d{4,5}[A-Z]*)\b")
# Avvertenze di repertorio che il modello aggiunge a ogni risposta: rumore, il tecnico le sa già.
_REPERTORIO = re.compile(r"\bESD\b|antistatic|componenti sensibili|attenzione alla batteria", re.I)


def _utili(avvertenze: list[str]) -> list[str]:
    return [a for a in avvertenze if not _REPERTORIO.search(a)]


_VOLT = re.compile(r"(\d+(?:[.,]\d+)?)\s*V\b")


@dataclass
class Esito:
    avvisi: list[str] = field(default_factory=list)
    bloccato: bool = False
    sigle_non_verificate: list[str] = field(default_factory=list)


def _testo(passo: PassoDiagnosi) -> str:
    m = passo.prossima_misura
    return " ".join([getattr(passo, "riepilogo", ""), m.dove, m.condizioni, m.valore_atteso, m.se_diverso,
                     *[f"{i.componente} {i.motivo}" for i in getattr(passo, "ipotesi", [])]])


# ===== Controllo sulla DOMANDA del tecnico (prima del modello, 0 token) =====
# "butto acqua con la presa attaccata": un'azione pericolosa descritta dal tecnico va fermata subito, in rosso,
# senza aspettare l'LLM (che potrebbe anche assecondarla).
_LIQUIDO = r"(acqua|liquid\w*|alcol\w*|\bipa\b|isopropil\w*|detergent\w*|sgrassant\w*|spray)"
_AZIONE = r"(butt\w*|vers\w*|lav\w*|sciacqu\w*|risciacqu\w*|bagn\w*|spruzz\w*|pulisc\w*|pulir\w*|immerg\w*|metto|mettere)"
_TENSIONE = (r"(presa|attaccat\w*|collegat\w*|inserit\w*|alimentat\w*|acces[oa]|in\s+carica|sotto\s+tensione|"
             r"caricatore|corrente|cavo\s+(?:inserito|attaccato|collegato)|batteria\s+(?:collegata|attaccata|dentro|inserita))")
_SICURO = r"(s?collegat\w*\s+(?:la\s+)?batteria|stacc\w*|scollegat\w*|spent[oa]|senza\s+(?:batteria|corrente|cavo|tensione))"


def pericolo_nella_domanda(messaggio: str) -> str | None:
    """Messaggio di STOP se il tecnico descrive un liquido su una scheda alimentata, altrimenti None.
    "è caduto in acqua e non carica" passa (racconta il guasto, non un'azione); "butto acqua con la presa attaccata" no."""
    m = messaggio.lower()
    if not (re.search(_LIQUIDO, m) and re.search(_AZIONE, m) and re.search(_TENSIONE, m)):
        return None
    if re.search(_SICURO, m) and not re.search(r"\bnon\s+(?:la\s+)?(?:stacc|scolleg)", m):
        return None
    return ("NO, FERMATI: mai liquidi (acqua, alcol o detergenti) su una scheda alimentata. Stacca il cavo e "
            "SCOLLEGA LA BATTERIA prima di qualsiasi pulizia: con la tensione il liquido crea corti e brucia "
            "controller di carica, PMIC e condensatori. Per pulire: IPA 99% a scheda spenta e scollegata, poi "
            "asciugatura completa prima di ridare tensione.")


def controlla(passo: PassoDiagnosi | PassoBreve, pagine_lette: dict[str, str]) -> tuple[PassoDiagnosi | PassoBreve, Esito]:
    """`pagine_lette`: percorso -> testo delle pagine che l'agente ha letto in questa sessione."""
    esito = Esito()
    testo = _testo(passo)
    tutto = testo + " " + " ".join(passo.avvertenze_sicurezza)

    # 1. sicurezza elettrica — campo per campo: un "non" in un altro campo (es. "non carica") non è una negazione
    m = passo.prossima_misura
    campi = [m.dove, m.condizioni, m.valore_atteso, m.se_diverso, getattr(passo, "riepilogo", ""),
             *[i.motivo for i in getattr(passo, "ipotesi", [])]]
    for patt, msg in _PERICOLOSI:
        for campo in campi:
            for trovato in re.finditer(patt, campo, re.I):
                prima = campo[max(0, trovato.start() - 25):trovato.start()]
                # "scollega la batteria prima dell'aria calda" è la regola giusta, non un pericolo (falso positivo, 17 nov)
                intorno = campo[max(0, trovato.start() - 40):trovato.end() + 40]
                messa_in_sicurezza = re.search(r"scolleg\w*|stacc\w*|disconn\w*|rimuov\w*|rimoss\w*|togli\w*|tolt\w*|"
                                               r"allontan\w*|senza\s+batteria|disconnect\w*|remove\w*", intorno, re.I)
                if not re.search(r"\b(non|mai|never|don't|evita\w*)\b", prima, re.I) and \
                        not (msg.startswith("Mai scaldare") and messa_in_sicurezza):
                    esito.avvisi.append(f"BLOCCATO: {msg}")
                    esito.bloccato = True
    testo_misura = " ".join([m.dove, m.condizioni, m.valore_atteso])
    # Iniezione di tensione con la batteria collegata (trovato in una risposta reale, 17 nov): si fa a batteria SCOLLEGATA.
    if re.search(r"iniezion\w*|inject\w*", testo_misura, re.I) and \
            re.search(r"(con\s+(la\s+)?)?batteria\s+(collegata|connessa|inserita)|with\s+(the\s+)?battery\s+connected", m.condizioni, re.I) and \
            not re.search(r"(scollegat|disconness|senza\s+batteria|without\s+battery)", m.condizioni, re.I):
        esito.avvisi.append("Iniezione di tensione con la batteria collegata: SCOLLEGA la batteria prima di iniettare "
                            "(rischio per la cella e per il circuito batteria).")
    if re.search(_ALIMENTAZIONE, testo_misura, re.I) and not re.search(_LIMITE, tutto, re.I):
        esito.avvisi.append("Usa l'alimentatore con LIMITE DI CORRENTE (parti basso, es. 0,5–1 A) e osserva l'assorbimento.")
    # Il limite Li-ion vale se il PUNTO di misura è la batteria (non se "con batteria" è solo una condizione).
    if re.search(r"batteria|battery|vbat", m.dove, re.I):
        for v in _VOLT.findall(m.valore_atteso):
            if float(v.replace(",", ".")) > MAX_TENSIONE_CELLA_V and float(v.replace(",", ".")) < 30:
                esito.avvisi.append(f"Tensione {v} V al connettore batteria: oltre il massimo di una cella Li-ion "
                                    f"(~{MAX_TENSIONE_CELLA_V} V). Verifica.")
                break

    # Valore "su scheda sana" copiato da un CASO (dove i valori sono quelli del GUASTO): risposta reale del 20 nov,
    # "valore atteso 0,026–0,186 V" su X1548, che nel caso A2316 è proprio la misura della scheda guasta.
    casi = " ".join(t for p, t in pagine_lette.items() if "/casi/" in p).replace(".", ",")
    decimali = re.findall(r"\d+[.,]\d+", m.valore_atteso)
    # Almeno 2 numeri (un intervallo come "0,026–0,186 V"): con uno solo scattava anche su risposte giuste che
    # citano un valore del caso come esempio (falso positivo del 20 nov: "nel caso A2316 senza batteria ~4,7 V").
    if casi and len(decimali) >= 2 and all(d.replace(".", ",") in casi for d in decimali):
        esito.avvisi.append("Il valore atteso coincide con un valore MISURATO nel caso della wiki, cioè sulla scheda "
                            "guasta: su una scheda sana il valore è un altro. Verifica prima di misurare.")

    # 2. valori impossibili
    for v in _VOLT.findall(testo):
        if float(v.replace(",", ".")) > MAX_TENSIONE_USB_V:
            esito.avvisi.append(f"Valore {v} V fuori dal plausibile per questi dispositivi (USB-PD max {MAX_TENSIONE_USB_V:g} V).")
            break

    # 3. sigle non verificate
    corpus = " ".join(pagine_lette.values())
    sigle = sorted(set(_SIGLA.findall(testo)))
    esito.sigle_non_verificate = [s for s in sigle if s not in corpus]
    if esito.sigle_non_verificate:
        esito.avvisi.append("Sigle non presenti nelle pagine consultate (da verificare su schema/boardview): "
                            + ", ".join(esito.sigle_non_verificate))

    # 4. fonti: solo pagine lette davvero
    lette = {p.removeprefix("wiki/") for p in pagine_lette}
    dichiarate = [f for f in passo.fonti if f.removeprefix("wiki/") in lette]
    scartate = [f for f in passo.fonti if f not in dichiarate]
    if scartate:
        esito.avvisi.append("Fonti dichiarate ma non lette, rimosse: " + ", ".join(scartate))
    if not dichiarate:
        esito.avvisi.append("Nessuna fonte dalla wiki: risposta basata solo sul modello, da verificare.")

    esito.avvisi = list(dict.fromkeys(esito.avvisi))        # niente doppioni
    passo = passo.model_copy(update={
        "fonti": dichiarate,
        # Nella diagnosi solo gli avvisi dei CONTROLLI (regole fisse). Quelli scritti dal modello erano rumore o
        # sbagliati ("corrente 0,002 A, quindi non forzare carichi", 20 nov): a un tecnico non servono.
        "avvertenze_sicurezza": [a for a in esito.avvisi if not a.startswith("Fonti")],
    })
    return passo, esito


# ── Procedura ("come si fa"): stessi controlli, applicati a tutti i passi ─────────────────────────────────────────
_CALORE = r"aria\s+calda|hot\s+air|dissald\w*|rimuov\w*\s+(il\s+)?(chip|ic)|reball\w*|saldator\w*|stazione\s+saldante|preriscald\w*"
_BATTERIA_SICURA = r"scolleg\w*\s+(la\s+)?batteria|batteria\s+scollegat\w*|stacc\w*\s+(la\s+)?batteria|" \
                   r"rimuov\w*\s+(la\s+)?batteria|disconnect\w*\s+(the\s+)?battery"


def controlla_procedura(proc: Procedura, pagine_lette: dict[str, str]) -> tuple[Procedura, Esito]:
    esito = Esito()
    campi = [*proc.verifica_finale,
             *[t for p in proc.passi for t in (p.titolo, p.azione, p.attrezzo, p.controllo)]]
    testo = " ".join([proc.obiettivo, *campi])
    tutto = testo + " " + " ".join(proc.avvertenze_sicurezza)

    # 1. sicurezza: istruzioni pericolose (bloccanti), con le stesse eccezioni di controlla()
    for patt, msg in _PERICOLOSI:
        for campo in campi:
            for trovato in re.finditer(patt, campo, re.I):
                prima = campo[max(0, trovato.start() - 25):trovato.start()]
                intorno = campo[max(0, trovato.start() - 40):trovato.end() + 40]
                sicura = re.search(r"scolleg\w*|stacc\w*|disconn\w*|rimuov\w*|rimoss\w*|togli\w*|tolt\w*|"
                                   r"allontan\w*|senza\s+batteria|disconnect\w*|remove\w*", intorno, re.I)
                if not re.search(r"\b(non|mai|never|don't|evita\w*)\b", prima, re.I) and \
                        not (msg.startswith("Mai scaldare") and sicura):
                    esito.avvisi.append(f"BLOCCATO: {msg}")
                    esito.bloccato = True
    # Calore senza batteria scollegata da nessuna parte: non blocca, ma lo mette in testa (regola del banco).
    if re.search(_CALORE, testo, re.I) and not re.search(_BATTERIA_SICURA, tutto, re.I):
        esito.avvisi.append("Prima di aria calda o saldatura: SCOLLEGA la batteria e allontanala dalla zona di lavoro.")
    if re.search(_ALIMENTAZIONE, testo, re.I) and not re.search(_LIMITE, tutto, re.I):
        esito.avvisi.append("Usa l'alimentatore con LIMITE DI CORRENTE (parti basso, es. 0,5–1 A) e osserva l'assorbimento.")

    # 2. valori impossibili
    for v in _VOLT.findall(testo):
        if float(v.replace(",", ".")) > MAX_TENSIONE_USB_V:
            esito.avvisi.append(f"Valore {v} V fuori dal plausibile per questi dispositivi (USB-PD max {MAX_TENSIONE_USB_V:g} V).")
            break

    # 3. sigle non verificate, 4. fonti
    corpus = " ".join(pagine_lette.values())
    esito.sigle_non_verificate = [x for x in sorted(set(_SIGLA.findall(testo))) if x not in corpus]
    if esito.sigle_non_verificate:
        esito.avvisi.append("Sigle non presenti nelle pagine consultate (da verificare su schema/boardview): "
                            + ", ".join(esito.sigle_non_verificate))
    lette = {p.removeprefix("wiki/") for p in pagine_lette}
    dichiarate = [f for f in proc.fonti if f.removeprefix("wiki/") in lette]
    scartate = [f for f in proc.fonti if f not in dichiarate]
    if scartate:
        esito.avvisi.append("Fonti dichiarate ma non lette, rimosse: " + ", ".join(scartate))
    if not dichiarate:
        esito.avvisi.append("Nessuna fonte dalla wiki: procedura basata solo sul modello, da verificare.")

    esito.avvisi = list(dict.fromkeys(esito.avvisi))
    proc = proc.model_copy(update={
        "fonti": dichiarate,
        # Nella procedura (aria calda, saldatura) quelle del modello possono servire: al massimo 2, senza frasi di repertorio.
        "avvertenze_sicurezza": [a for a in esito.avvisi if not a.startswith("Fonti")] + _utili(proc.avvertenze_sicurezza)[:2],
    })
    return proc, esito
