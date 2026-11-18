"""Riconosce di quale dispositivo si parla e ne legge la scheda dalla wiki (serve al riquadro laterale della UI).

Deterministico: prima il codice modello (A2316 -> iPad Air 4), poi il nome più lungo che compare nel testo
(così "iPad Air 4" vince su "iPad Air").
"""
from __future__ import annotations

import re
from pathlib import Path

from diagnosi.config import RAW_DIR, ROOT, WIKI_DIR
from diagnosi.wiki_builder import leggi_front_matter


def schede(wiki_dir: Path = WIKI_DIR) -> list[dict]:
    out = []
    for f in sorted((wiki_dir / "dispositivi").glob("*.md")):
        fm, corpo = leggi_front_matter(f.read_text(encoding="utf-8"))
        out.append(fm | {"percorso": f"dispositivi/{f.name}", "corpo": corpo})
    return out


def trova_dispositivo(testo: str, wiki_dir: Path = WIKI_DIR, tutte: list[dict] | None = None) -> dict | None:
    tutte = schede(wiki_dir) if tutte is None else tutte
    for codice in (c.upper() for c in re.findall(r"\bA\d{4}\b", testo, re.I)):     # anche "a2316" scritto minuscolo
        for s in tutte:
            if codice in (s.get("codici_modello") or []):
                return s
    for s in sorted(tutte, key=lambda s: -len(s.get("titolo", ""))):
        if re.search(r"(?<!\w)" + re.escape(s.get("titolo", "§")) + r"(?!\w)", testo, re.I):
            return s
    return None


def casi_del_dispositivo(titolo: str, wiki_dir: Path = WIKI_DIR) -> list[str]:
    """Pagine di wiki/casi/ che nominano il dispositivo tra i `modelli` (calcolate ogni volta: sempre aggiornate)."""
    out = []
    for f in sorted((wiki_dir / "casi").glob("*.md")):
        fm, _ = leggi_front_matter(f.read_text(encoding="utf-8"))
        if any(str(m).split("(")[0].strip().lower() == titolo.lower() for m in fm.get("modelli") or []):  # "iPad Air" ≠ "iPad Air 4"
            out.append(f"casi/{f.name}")
    return out


# ── "Scrivo solo il modello": elenco delle guide, senza LLM (zero token) ──────────────────────────────────────
# Parole che non aggiungono un sintomo: se nel messaggio resta solo questo, il tecnico vuole l'elenco delle guide.
PAROLE_DI_SERVIZIO = set("""
apple ipad iphone modello dispositivo scheda guide guida guides elenco lista mostra mostrami dammi cerca cercami
quali tutte tutti le la lo il i gli l un una di del della dell per su sul sulla a al che ci sono hai ho e info
informazioni casi wifi cellular gen generation generazione
""".split())


def solo_dispositivo(testo: str, d: dict) -> bool:
    """True se il messaggio contiene solo il nome/codice del dispositivo (più parole di servizio), nessun sintomo."""
    resto = re.sub(re.escape(d.get("titolo", "§")), " ", testo, flags=re.I)
    for codice in d.get("codici_modello") or []:
        resto = re.sub(rf"\b{codice}\b", " ", resto, flags=re.I)
    parole = re.findall(r"[a-zà-ù0-9]+", resto.lower())
    return all(p in PAROLE_DI_SERVIZIO or p.isdigit() and len(p) <= 2 for p in parole)


def guide_del_dispositivo(d: dict, wiki_dir: Path = WIKI_DIR, raw_dir: Path = RAW_DIR) -> dict:
    """Guide relative a un dispositivo, in due gruppi:

    - "repairwiki": guide originali (raw/repairwiki/pagine) il cui TITOLO indica proprio questo modello
      (stessa regola di trova_dispositivo: "iPad Air 4 No Backlight" non finisce sotto "iPad Air");
    - "wiki": pagine della nostra wiki (casi, sintomi, componenti, tecniche...) che hanno il modello tra i `modelli`
      oppure che sono state scritte a partire da quelle guide o dai casi del dispositivo.
    """
    tutte = schede(wiki_dir)
    stesso = lambda testo: (t := trova_dispositivo(str(testo), wiki_dir, tutte)) is not None and t["percorso"] == d["percorso"]

    repairwiki = []
    for f in sorted((raw_dir / "repairwiki" / "pagine").glob("*.md")):
        fm, _ = leggi_front_matter(f.read_text(encoding="utf-8"))
        if fm.get("categoria_dispositivo"):      # è la pagina del dispositivo, non una guida
            continue
        if stesso(fm.get("titolo", "")):
            repairwiki.append({"titolo": fm["titolo"], "url": fm.get("url", ""),
                               "percorso": f"raw/repairwiki/pagine/{f.name}"})

    fonti_dispositivo = {g["percorso"] for g in repairwiki}
    for c in casi_del_dispositivo(d.get("titolo", ""), wiki_dir):
        fm, _ = leggi_front_matter((wiki_dir / c).read_text(encoding="utf-8"))
        fonti_dispositivo |= {x for x in fm.get("fonti") or [] if str(x).startswith("raw/")}

    wiki = []
    for f in sorted(wiki_dir.glob("*/*.md")):
        if f.parent.name in ("dispositivi", "fonti"):
            continue
        fm, _ = leggi_front_matter(f.read_text(encoding="utf-8"))
        if any(stesso(m) for m in fm.get("modelli") or []) or fonti_dispositivo & set(fm.get("fonti") or []):
            wiki.append({"titolo": fm.get("titolo", f.stem), "tipo": fm.get("tipo", f.parent.name),
                         "percorso": f"{f.parent.name}/{f.name}"})
    ordine = {"caso": 0, "sintomo": 1, "tecnica": 2, "componente": 3, "strumento": 4}
    wiki.sort(key=lambda p: (ordine.get(p["tipo"], 9), p["titolo"].lower()))
    return {"wiki": wiki, "repairwiki": repairwiki}


def leggi_guida(percorso: str, wiki_dir: Path = WIKI_DIR, root: Path = ROOT) -> str:
    """Testo di una guida da mostrare DENTRO l'app (niente link al sito): una pagina della wiki ("casi/x.md")
    o la copia locale di repair.wiki ("raw/repairwiki/pagine/x.md"). Senza front-matter; i link interni tra pagine
    diventano testo (nell'app non portano da nessuna parte). La riga "> Fonte: ... CC BY-SA" resta: è l'attribuzione
    che la licenza chiede. Si legge solo dentro wiki/ e raw/repairwiki/ (privilegio minimo, come i tool)."""
    base = root if percorso.startswith("raw/") else wiki_dir
    consentite = [(wiki_dir).resolve(), (root / "raw" / "repairwiki").resolve()]
    f = (base / percorso).resolve()
    if not any(f.is_relative_to(c) for c in consentite) or f.suffix != ".md" or not f.exists():
        return "Guida non trovata."
    _, corpo = leggi_front_matter(f.read_text(encoding="utf-8"))
    return re.sub(r"\[([^\]]+)\]\((?!https?://)[^)]+\)", r"\1", corpo)
