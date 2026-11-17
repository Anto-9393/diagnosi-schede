"""Nomi precisi dei componenti nelle risposte — regola del tecnico (17 nov): prima il CODICE DEL CHIP, la sigla
dello schema solo tra parentesi e con lo schema da cui viene. "X3" da solo non dice niente a chi non ha JC Drawing
aperto (e su un altro schema X3 è un altro componente); "343S00264-A0 (X3 su JC Drawing)" sì.

Deterministico, come i guardrail: la corrispondenza sigla -> codice la prende dalle pagine che l'agente ha letto
(es. "X3 = 343S00264-A0", "ROM 8N040 ... siglato X7"), non dal modello.
"""
from __future__ import annotations

import re
from typing import Iterable

_CODICE = r"(?:\d{3}S\d{5}(?:-A\d)?|CD\d{4}[A-Z]\d+|8N\d{3,4})"
_SIGLA = re.compile(r"\bX\d{1,5}\b")


def _pulisci(t: str) -> str:
    return t.replace("*", "").replace("‑", "-")          # grassetto markdown e trattino non separabile


def mappa_sigle(pagine: Iterable[str]) -> dict[str, str]:
    """{"X3": "343S00264-A0", "X5": "CD3217B12", "X7": "8N040"} dalle pagine lette."""
    mappa: dict[str, str] = {}
    testi = [_pulisci(t) for t in pagine]
    for testo in testi:
        for x, c in re.findall(rf"\b(X\d{{1,5}})\s*=\s*({_CODICE})", testo):          # X3 = 343S00264-A0
            mappa.setdefault(x, c)
        for x, c in re.findall(rf"\b(X\d{{1,5}})\s*\(\s*({_CODICE})", testo):         # X3 (343S00264-A0)
            mappa.setdefault(x, c)
    # ROM: "8N040 (chip piccolo accanto a X5, su JC Drawing siglato X7)": la prima sigla vicina che NON è già un chip.
    for testo in testi:
        for m in re.finditer(r"\b(8N\d{3,4})\b", testo):
            vicine = _SIGLA.findall(testo[m.end():m.end() + 90].split("\n")[0])
            libera = next((x for x in vicine if x not in mappa), None)
            if libera and m.group(1) not in mappa.values():
                mappa[libera] = m.group(1)
    return mappa


def con_nomi_precisi(testo: str, mappa: dict[str, str]) -> str:
    """Prima volta: "X3" -> "343S00264-A0 (X3 su JC Drawing)"; volte successive: solo il codice.
    Se il codice è già scritto lì vicino (es. "X5 = CD3217B12", "CD3217B12 (X5)"), la sigla resta com'è."""
    gia: set[str] = set()

    def sostituisci(m: re.Match) -> str:
        x = m.group(0)
        codice = mappa.get(x)
        if not codice:
            return x
        vicino = _pulisci(testo[max(0, m.start() - 40):m.end() + 40])
        if codice.split("-")[0] in vicino:
            gia.add(x)
            return x
        if x in gia:
            return codice
        gia.add(x)
        return f"{codice} ({x} su JC Drawing)"

    return _SIGLA.sub(sostituisci, testo)


def nomi_precisi(passo, pagine: Iterable[str]):
    """Applica con_nomi_precisi a tutti i testi della risposta (PassoDiagnosi, PassoBreve o Procedura), fonti escluse."""
    mappa = mappa_sigle(pagine)
    if not mappa:
        return passo

    def visita(v, chiave=""):
        if chiave == "fonti":
            return v
        if isinstance(v, str):
            return con_nomi_precisi(v, mappa)
        if isinstance(v, list):
            return [visita(x) for x in v]
        if isinstance(v, dict):
            return {k: visita(x, k) for k, x in v.items()}
        return v

    return type(passo).model_validate(visita(passo.model_dump()))
