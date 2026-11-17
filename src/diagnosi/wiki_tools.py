"""I tool con cui l'agente consulta la wiki: è il "recupero" della LLM Wiki (al posto del RAG).

Schema di Karpathy per la query: prima l'indice, poi le pagine pertinenti, poi la risposta con citazioni.
Come in S11 (la pipeline RAG avvolta in un @tool), qui avvolgiamo la lettura della wiki in tre @tool.

Le funzioni sono deterministiche (niente LLM): si testano con pytest senza chiave.
"""
from __future__ import annotations

import re
from pathlib import Path

from datapizza.tools import tool

from diagnosi.config import WIKI_DIR

FILE_SPECIALI = {"index.md", "log.md"}
MAX_CARATTERI_PAGINA = 12_000          # protegge il contesto (e il costo) da pagine enormi


def _pagine(wiki_dir: Path) -> list[Path]:
    return sorted(p for p in wiki_dir.rglob("*.md") if p.name not in FILE_SPECIALI)


def _percorso_sicuro(percorso: str, wiki_dir: Path) -> Path:
    """Accetta solo file .md DENTRO la wiki: niente '../../.env' (minimo privilegio, S15)."""
    p = (wiki_dir / percorso.removeprefix("wiki/")).resolve()
    if wiki_dir.resolve() not in p.parents or p.suffix != ".md":
        raise ValueError(f"Percorso non consentito: {percorso}")
    return p


def _parole(testo: str) -> list[str]:
    return [w for w in re.findall(r"[a-z0-9]+", testo.lower()) if len(w) >= 2]


# ----------------------------------------------------------------------------- funzioni pure
def indice(wiki_dir: Path = WIKI_DIR) -> str:
    f = wiki_dir / "index.md"
    if not f.exists():
        return "La wiki non ha ancora un index.md: va prima eseguito il wiki builder."
    return f.read_text(encoding="utf-8")


def pagina(percorso: str, wiki_dir: Path = WIKI_DIR) -> str:
    try:
        f = _percorso_sicuro(percorso, wiki_dir)
    except ValueError as e:
        return str(e)
    if not f.exists():
        return f"Pagina non trovata: {percorso}. Controlla i percorsi in index.md."
    testo = f.read_text(encoding="utf-8")
    if len(testo) > MAX_CARATTERI_PAGINA:
        testo = testo[:MAX_CARATTERI_PAGINA] + "\n\n[... pagina troncata ...]"
    rel = f.relative_to(wiki_dir.resolve()).as_posix()
    return f"FONTE: wiki/{rel}\n\n{testo}"


def cerca(query: str, max_risultati: int = 5, wiki_dir: Path = WIKI_DIR) -> str:
    """Ricerca per parole chiave: conta le parole della query in titolo (peso 3) e testo (peso 1)."""
    parole_query = set(_parole(query))
    if not parole_query:
        return "Query vuota."
    risultati = []
    for f in _pagine(wiki_dir):
        testo = f.read_text(encoding="utf-8")
        parole_testo = _parole(testo)
        parole_titolo = set(_parole(f.stem)) | set(_parole(testo.split("\n", 3)[1] if "\n" in testo else ""))
        punteggio = sum(parole_testo.count(w) for w in parole_query) + 3 * len(parole_query & parole_titolo)
        if punteggio:
            risultati.append((punteggio, f, testo))
    if not risultati:
        return f"Nessuna pagina contiene: {query}"
    righe = []
    for punteggio, f, testo in sorted(risultati, key=lambda r: -r[0])[:max_risultati]:
        rel = f.relative_to(wiki_dir).as_posix()
        corpo = testo.split("---", 2)[-1] if testo.startswith("---") else testo
        estratto = " ".join(corpo.split())[:200]
        righe.append(f"- wiki/{rel} (punteggio {punteggio}): {estratto}")
    return "\n".join(righe)


# ----------------------------------------------------------------------------- tool per l'agente
@tool
def leggi_indice() -> str:
    """Legge wiki/index.md, il catalogo di tutte le pagine (casi, componenti, sintomi, fonti).
    Da usare per primo, per scegliere quali pagine aprire."""
    return indice()


@tool
def leggi_pagina(percorso: str) -> str:
    """Legge una pagina della wiki. `percorso` è relativo alla wiki, es. 'componenti/cd3217.md'.
    Il risultato inizia con 'FONTE: ...': va citata nella risposta."""
    return pagina(percorso)


@tool
def cerca_wiki(query: str) -> str:
    """Cerca nella wiki per parole chiave (sigle, net, sintomi, modelli), es. 'CD3217 non carica'.
    Ritorna le pagine più pertinenti con un estratto; poi aprile con leggi_pagina."""
    return cerca(query)


TOOLS = [leggi_indice, leggi_pagina, cerca_wiki]
