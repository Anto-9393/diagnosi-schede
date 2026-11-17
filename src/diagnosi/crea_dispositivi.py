"""Crea le pagine wiki/dispositivi/ dalle schede di modello di repair.wiki, SENZA LLM.

Perché senza LLM: le schede di modello contengono dati già strutturati (codici modello, tipo, data di uscita)
e quasi nessun testo. Un LLM costerebbe centinaia di chiamate e potrebbe sbagliare un codice; il codice no.
Regola pratica: l'LLM si usa dove serve capire il testo, non dove basta copiare un campo.

Le pagine esistenti NON vengono sovrascritte: se il wiki builder le ha già arricchite (es. con un caso), si tengono.

Avvio:  python -m diagnosi.crea_dispositivi
"""
from __future__ import annotations

import re
from datetime import date
from pathlib import Path

import yaml

from diagnosi.config import RAW_DIR, ROOT, WIKI_DIR
from diagnosi.wiki_builder import leggi_front_matter, rigenera_indice

PAGINE_RAW = RAW_DIR / "repairwiki" / "pagine"


def nome_italiano(titolo: str) -> str:
    """'IPad Air 4' -> 'iPad Air 4' (repair.wiki mette la maiuscola iniziale ai titoli)."""
    return re.sub(r"^I(Phone|Pad)", r"i\1", titolo)


def crea(pagine_raw: Path = PAGINE_RAW, wiki_dir: Path = WIKI_DIR, root: Path = ROOT) -> list[Path]:
    creati = []
    for f in sorted(pagine_raw.glob("*.md")):
        fm, _ = leggi_front_matter(f.read_text(encoding="utf-8"))
        if "categoria_dispositivo" not in fm:
            continue                                     # non è una scheda di modello
        nome = nome_italiano(fm["titolo"])
        out = wiki_dir / "dispositivi" / f.name
        if out.exists():
            continue
        codici = fm.get("codici_modello", [])
        meta = {
            "titolo": nome,
            "tipo": "dispositivo",
            "riassunto": f"{'Tablet' if fm['categoria_dispositivo'] == 'tablet' else 'Smartphone'} Apple"
                         + (f", codici {', '.join(codici)}" if codici else ""),
            "modelli": [nome],
            "fonti": [f.relative_to(root).as_posix()],
            "aggiornato": date.today().isoformat(),
            "categoria": fm["categoria_dispositivo"],
            "codici_modello": codici,
            "componenti_chiave": [],                     # li aggiunge il wiki builder quando ingerisce casi e guide
            "casi": [],
            "licenza": fm.get("licenza", "CC BY-SA 3.0"),
        }
        corpo = [f"# {nome}", ""]
        if fm.get("data_uscita"):
            corpo += [f"- Uscita: {fm['data_uscita']}"]
        if codici:
            corpo += [f"- Codici modello: {', '.join(codici)}"]
        else:
            corpo += ["- Codici modello: da verificare (non indicati nella fonte)"]
        corpo += ["", "## Guasti tipici e casi", "", "Da completare con i casi reali e le guide (wiki builder).", "",
                  f"Fonte: [{fm['titolo']} — repair.wiki]({fm['url']}), CC BY-SA 3.0."]
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text("---\n" + yaml.safe_dump(meta, allow_unicode=True, sort_keys=False) + "---\n\n"
                       + "\n".join(corpo) + "\n", encoding="utf-8")
        creati.append(out)
    rigenera_indice(wiki_dir)
    return creati


if __name__ == "__main__":
    creati = crea()
    print(f"{len(creati)} pagine dispositivo create in {WIKI_DIR / 'dispositivi'}; index.md rigenerato.")
