"""Riconosce di quale dispositivo si parla e ne legge la scheda dalla wiki (serve al riquadro laterale della UI).

Deterministico: prima il codice modello (A2316 -> iPad Air 4), poi il nome più lungo che compare nel testo
(così "iPad Air 4" vince su "iPad Air").
"""
from __future__ import annotations

import re
from pathlib import Path

from diagnosi.config import WIKI_DIR
from diagnosi.wiki_builder import leggi_front_matter


def schede(wiki_dir: Path = WIKI_DIR) -> list[dict]:
    out = []
    for f in sorted((wiki_dir / "dispositivi").glob("*.md")):
        fm, corpo = leggi_front_matter(f.read_text(encoding="utf-8"))
        out.append(fm | {"percorso": f"dispositivi/{f.name}", "corpo": corpo})
    return out


def trova_dispositivo(testo: str, wiki_dir: Path = WIKI_DIR) -> dict | None:
    tutte = schede(wiki_dir)
    for codice in re.findall(r"\bA\d{4}\b", testo):
        for s in tutte:
            if codice in (s.get("codici_modello") or []):
                return s
    for s in sorted(tutte, key=lambda s: -len(s.get("titolo", ""))):
        if re.search(r"(?<!\w)" + re.escape(s.get("titolo", "§")) + r"(?!\w)", testo, re.I):
            return s
    return None
