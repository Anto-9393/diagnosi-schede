"""Converte l'export XML di repair.wiki (Special:Export) in un file Markdown per pagina.

Livello "raw" della LLM Wiki: questi file non si modificano più, il wiki builder li legge.
Ogni file ha in cima l'attribuzione richiesta dalla licenza CC BY-SA 3.0.

Avvio:  python -m diagnosi.import_repairwiki raw/repairwiki/*.xml
"""
from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import quote

import yaml

from diagnosi.config import RAW_DIR

OUT_DIR = RAW_DIR / "repairwiki" / "pagine"
BASE_URL = "https://repair.wiki/w/"


# ----------------------------------------------------------------------------- XML
def _tag(el: ET.Element) -> str:
    """'{http://www.mediawiki.org/xml/export-0.11/}page' -> 'page' (ignora il namespace XML)."""
    return el.tag.rsplit("}", 1)[-1]


def _figlio(el: ET.Element, nome: str) -> ET.Element | None:
    return next((c for c in el if _tag(c) == nome), None)


def leggi_export(xml_path: Path) -> list[dict]:
    """Estrae dalle <page> dell'export: titolo, testo wikitext, data di revisione."""
    pagine = []
    for page in ET.parse(xml_path).getroot().iter():
        if _tag(page) != "page":
            continue
        ns = _figlio(page, "ns")
        if ns is not None and ns.text != "0":          # solo articoli, non categorie/template
            continue
        if _figlio(page, "redirect") is not None:       # i redirect non hanno contenuto
            continue
        rev = _figlio(page, "revision")
        testo_el = _figlio(rev, "text") if rev is not None else None
        ts_el = _figlio(rev, "timestamp") if rev is not None else None
        pagine.append({
            "titolo": _figlio(page, "title").text,
            "wikitext": (testo_el.text or "") if testo_el is not None else "",
            "revisione": ts_el.text if ts_el is not None else "",
        })
    return pagine


# ----------------------------------------------------------------------------- dati del dispositivo
def dati_dispositivo(t: str) -> dict:
    """Legge il riquadro {{Device page |Has code name=... |Device type=... }} delle pagine di modello.

    Va letto PRIMA di togliere i template: sono i dati che servono al riquadro laterale della UI.
    """
    m = re.search(r"\{\{\s*Device page(.*?)\}\}", t, flags=re.S | re.I)
    if not m:
        return {}
    campi = dict(re.findall(r"\|\s*([^=|]+?)\s*=\s*([^|}]*)", m.group(1)))
    dati = {}
    if campi.get("Device type"):
        dati["categoria_dispositivo"] = {"tablet": "tablet", "phone": "phone"}.get(campi["Device type"].strip().lower(), "altro")
    if campi.get("Has code name"):
        dati["codici_modello"] = sorted(set(re.findall(r"A\d{4}", campi["Has code name"])))
    if campi.get("Device release date"):
        dati["data_uscita"] = campi["Device release date"].strip()
    return dati


# ----------------------------------------------------------------------------- wikitext -> markdown
def _togli_template(t: str) -> str:
    """Rimuove {{...}} anche annidati, partendo dai più interni."""
    precedente = None
    while precedente != t:
        precedente = t
        t = re.sub(r"\{\{[^{}]*\}\}", "", t)
    return t


def _tabella(blocco: str) -> str:
    """Conversione grezza delle tabelle MediaWiki: una riga di testo per riga di tabella."""
    righe, corrente = [], []
    for linea in blocco.splitlines():
        linea = linea.strip()
        if linea.startswith("{|") or linea.startswith("|+"):
            continue
        if linea.startswith("|-") or linea.startswith("|}"):
            if corrente:
                righe.append("| " + " | ".join(corrente) + " |")
            corrente = []
            continue
        if linea[:1] in ("|", "!"):
            celle = re.split(r"\s*(?:\|\||!!)\s*", linea[1:])
            # 'style="..." | testo' -> 'testo'
            corrente += [c.split("|", 1)[-1].strip() for c in celle]
    if corrente:
        righe.append("| " + " | ".join(corrente) + " |")
    return "\n".join(righe)


def wikitext_a_markdown(t: str) -> tuple[str, list[str]]:
    """Ritorna (markdown, categorie). Conversione volutamente semplice: il lettore è un LLM."""
    categorie = re.findall(r"\[\[\s*Category\s*:\s*([^\]|]+)", t, flags=re.I)
    t = re.sub(r"<!--.*?-->", "", t, flags=re.S)
    t = re.sub(r"<ref[^>]*/>|<ref[^>]*>.*?</ref>", "", t, flags=re.S | re.I)
    t = re.sub(r"<gallery.*?</gallery>", "", t, flags=re.S | re.I)
    t = _togli_template(t)
    t = re.sub(r"\[\[\s*(File|Image|Category)\s*:[^\]]*\]\]", "", t, flags=re.I)
    t = re.sub(r"\{\|.*?\|\}", lambda m: _tabella(m.group(0)), t, flags=re.S)
    t = re.sub(r"\[\[[^\]|]*\|([^\]]*)\]\]", r"\1", t)                 # [[Pagina|testo]] -> testo
    t = re.sub(r"\[\[([^\]]*)\]\]", r"\1", t)                          # [[Pagina]] -> Pagina
    t = re.sub(r"\[(https?://\S+)\s+([^\]]+)\]", r"[\2](\1)", t)       # [url testo] -> [testo](url)
    # Schemi e dump ROM su siti di file-sharing: provenienza e licenza incerte -> fuori dalla wiki.
    t = re.sub(r"^.*https?://(www\.)?(sendspace|mega|mediafire|drive\.google)\S*.*$", "", t, flags=re.M | re.I)
    # Gli elenchi PRIMA di titoli e grassetto: altrimenti "##" e "**" generati qui sotto
    # verrebbero riletti come elenchi (bug trovato dal test).
    t = re.sub(r"^(\*+)\s*", lambda m: "  " * (len(m.group(1)) - 1) + "- ", t, flags=re.M)
    t = re.sub(r"^(#+)\s*", lambda m: "  " * (len(m.group(1)) - 1) + "1. ", t, flags=re.M)
    t = re.sub(r"^(=+)\s*(.*?)\s*\1\s*$",
               lambda m: "#" * min(len(m.group(1)), 6) + " " + m.group(2), t, flags=re.M)
    t = re.sub(r"'''(.*?)'''", r"**\1**", t)
    t = re.sub(r"''(.*?)''", r"*\1*", t)
    t = re.sub(r"<br\s*/?>", "\n", t, flags=re.I)
    t = re.sub(r"</?(div|span|center|small|big|u|s|sup|sub)[^>]*>", "", t, flags=re.I)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip(), [c.strip() for c in categorie]


# ----------------------------------------------------------------------------- scrittura
def slug(titolo: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", titolo.lower()).strip("-")


def front_matter(p: dict, categorie: list[str], dispositivo: dict | None = None) -> str:
    """Intestazione YAML scritta da yaml.safe_dump: gestisce da sola virgolette e caratteri speciali
    (bug trovato su un titolo con 12.9" — mai costruire YAML a mano con le f-string)."""
    url = BASE_URL + quote(p["titolo"].replace(" ", "_"))
    meta = {
        "titolo": p["titolo"],
        "tipo": "fonte_esterna",
        "url": url,
        "cronologia": f"{url}?action=history",
        "revisione": p["revisione"],
        "categorie": categorie,
        **(dispositivo or {}),
        "licenza": "CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)",
    }
    return (
        "---\n" + yaml.safe_dump(meta, allow_unicode=True, sort_keys=False) + "---\n\n"
        f"# {p['titolo']}\n\n"
        f"> Fonte: [{p['titolo']} — repair.wiki]({url}), CC BY-SA 3.0. Autori: vedi cronologia.\n\n"
    )


def importa(xml_path: Path, out_dir: Path = OUT_DIR) -> list[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    scritti = []
    for p in leggi_export(xml_path):
        if re.search(r"[\u0400-\u04FF\u4e00-\u9fff]", p["titolo"]):   # copie in russo/cinese: doppioni
            print(f"  saltata (altra lingua): {p['titolo']}")
            continue
        dispositivo = dati_dispositivo(p["wikitext"])
        md, categorie = wikitext_a_markdown(p["wikitext"])
        # Le pagine di modello sono quasi vuote ma i loro dati (codici modello) servono: si tengono.
        if len(md) < 200 and not dispositivo:
            print(f"  saltata (troppo corta, {len(md)} caratteri): {p['titolo']}")
            continue
        f = out_dir / f"{slug(p['titolo'])}.md"
        f.write_text(front_matter(p, categorie, dispositivo) + md + "\n", encoding="utf-8")
        scritti.append(f)
    return scritti


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Uso: python -m diagnosi.import_repairwiki raw/repairwiki/*.xml  (uno o più file)")
    xml_files = [f for a in sys.argv[1:] for f in (sorted(Path().glob(a)) if "*" in a else [Path(a)])]
    totale = 0
    for x in xml_files:
        print(f"== {x}")
        totale += len(importa(x))
    print(f"\n{totale} pagine scritte in {OUT_DIR}")
