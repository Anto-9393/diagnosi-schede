"""Traduzione in italiano delle guide di repair.wiki, UNA volta sola e salvata su file.

Le guide importate sono in inglese. Nell'app il tecnico può chiederne la traduzione: il modello la fa una volta
(pochi centesimi), il testo va in raw/repairwiki/tradotte/ e dalla volta dopo si legge dal file, a 0 token.
Licenza: CC BY-SA 3.0 permette le traduzioni se si cita la fonte, si dice che è una modifica e si mantiene la
stessa licenza: lo scriviamo in testa a ogni file tradotto.
"""
from __future__ import annotations

import re
from datetime import date
from pathlib import Path

import yaml

from diagnosi.config import ROOT, leggi_prompt
from diagnosi.dispositivi import leggi_guida

CARTELLA = ROOT / "raw" / "repairwiki" / "tradotte"


def file_tradotto(percorso: str, cartella: Path = CARTELLA) -> Path:
    return cartella / Path(percorso).name


def tradotta(percorso: str, cartella: Path = CARTELLA, root: Path = ROOT) -> str | None:
    """Il testo tradotto, se esiste già (senza front-matter), altrimenti None."""
    f = file_tradotto(percorso, cartella)
    if not f.exists():
        return None
    return leggi_guida(str(f.relative_to(root)).replace("\\", "/"), root=root)


def traduci(percorso: str, client=None, cartella: Path = CARTELLA, root: Path = ROOT) -> tuple[str, int, int]:
    """Traduce la guida e la salva. Restituisce (testo, token_in, token_out)."""
    originale = leggi_guida(percorso, root=root)
    righe_fonte = [r for r in originale.splitlines() if r.startswith("> Fonte:")]
    corpo = "\n".join(r for r in originale.splitlines() if not r.startswith("> Fonte:"))
    if client is None:
        from diagnosi.llm import crea_client
        client = crea_client()
    r = client.invoke(corpo, system_prompt=leggi_prompt("traduttore"), max_tokens=8000)
    attribuzione = (righe_fonte[0] if righe_fonte else "> Fonte: repair.wiki, CC BY-SA 3.0.") + \
        f"\n> Traduzione automatica in italiano ({date.today().isoformat()}): opera modificata, stessa licenza CC BY-SA 3.0."
    testo = r.text.strip()
    # L'attribuzione va in testa, subito dopo il titolo (come nell'originale).
    m = re.match(r"(# [^\n]*\n)", testo)
    testo = (m.group(1) + "\n" + attribuzione + "\n" + testo[m.end():]) if m else (attribuzione + "\n\n" + testo)
    fm = {"originale": percorso, "lingua": "it", "tradotto": date.today().isoformat(),
          "licenza": "CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)"}
    cartella.mkdir(parents=True, exist_ok=True)
    file_tradotto(percorso, cartella).write_text("---\n" + yaml.safe_dump(fm, allow_unicode=True) + "---\n\n" + testo + "\n",
                                                 encoding="utf-8")
    return testo, r.usage.prompt_tokens, r.usage.completion_tokens
