"""LINT della wiki — la terza operazione di Karpathy: un controllo di salute, deterministico (niente LLM).

Conta: link rotti, pagine senza fonti, pagine orfane (nessuno le linka e non sono in index), casi che
vengono da fonti non di raw/casi. Dà numeri da confrontare nel tempo (e da mostrare nello speech).

Avvio:  python -m diagnosi.lint_wiki            (solo report)
        python -m diagnosi.lint_wiki --ripara   (corregge/rimuove i link rotti)
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

from diagnosi.config import WIKI_DIR
from diagnosi.wiki_builder import leggi_front_matter, ripara_link

LINK = re.compile(r"\]\(([^)#\s]+\.md)\)")


def controlla(wiki_dir: Path = WIKI_DIR, ripara: bool = False) -> dict:
    pagine = [f for f in sorted(wiki_dir.rglob("*.md")) if f.name not in ("index.md", "log.md")]
    linkate, rotti, senza_fonti, casi_sospetti = set(), [], [], []
    for f in pagine:
        rel = f.relative_to(wiki_dir)
        fm, corpo = leggi_front_matter(f.read_text(encoding="utf-8"))
        if ripara:
            corpo2, _, _ = ripara_link(corpo, rel, wiki_dir)
            if corpo2 != corpo:
                f.write_text("---\n" + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False) + "---\n\n" + corpo2,
                             encoding="utf-8")
                corpo = corpo2
        for dest in LINK.findall(corpo):
            target = (f.parent / dest).resolve()
            if target.exists():
                linkate.add(target)
            else:
                rotti.append(f"{rel.as_posix()} -> {dest}")
        if not fm.get("fonti"):
            senza_fonti.append(rel.as_posix())
        if fm.get("tipo") == "caso" and not any(str(x).startswith("raw/casi") for x in fm.get("fonti", [])):
            casi_sospetti.append(rel.as_posix())
    orfane = [f.relative_to(wiki_dir).as_posix() for f in pagine
              if f.resolve() not in linkate and f.parent.name not in ("dispositivi", "fonti")]
    return {"pagine": len(pagine), "link_rotti": rotti, "senza_fonti": senza_fonti,
            "casi_non_da_raw_casi": casi_sospetti, "orfane": orfane}


if __name__ == "__main__":
    r = controlla(ripara="--ripara" in sys.argv)
    print(f"Pagine: {r['pagine']}")
    for chiave, titolo in [("link_rotti", "Link rotti"), ("senza_fonti", "Pagine senza fonti"),
                           ("casi_non_da_raw_casi", "Casi che non vengono da raw/casi"),
                           ("orfane", "Pagine orfane (nessun link in entrata; normali all'inizio)")]:
        print(f"\n{titolo}: {len(r[chiave])}")
        for voce in r[chiave][:20]:
            print(f"  - {voce}")
