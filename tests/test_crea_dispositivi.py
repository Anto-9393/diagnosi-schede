from diagnosi.crea_dispositivi import crea, nome_italiano
from diagnosi.wiki_builder import leggi_front_matter

RAW = """---
titolo: "IPad Air 4"
tipo: fonte_esterna
url: https://repair.wiki/w/IPad_Air_4
categoria_dispositivo: tablet
codici_modello: ['A2072', 'A2316']
data_uscita: 2020-10-23
licenza: CC BY-SA 3.0
---
# IPad Air 4
"""


def test_nome_italiano():
    assert nome_italiano("IPhone 11 Pro") == "iPhone 11 Pro"


def test_crea_pagina_dispositivo_e_non_sovrascrive(tmp_path):
    raw = tmp_path / "raw" / "repairwiki" / "pagine"
    raw.mkdir(parents=True)
    (raw / "ipad-air-4.md").write_text(RAW, encoding="utf-8")
    (raw / "short-circuits.md").write_text("---\ntitolo: Short\n---\ntesto", encoding="utf-8")
    wiki = tmp_path / "wiki"
    creati = crea(raw, wiki, tmp_path)
    assert [c.name for c in creati] == ["ipad-air-4.md"]           # solo le schede di modello
    fm, corpo = leggi_front_matter(creati[0].read_text(encoding="utf-8"))
    assert fm["titolo"] == "iPad Air 4" and fm["categoria"] == "tablet" and fm["codici_modello"] == ["A2072", "A2316"]
    assert "[iPad Air 4](dispositivi/ipad-air-4.md)" in (wiki / "index.md").read_text(encoding="utf-8")
    creati[0].write_text(creati[0].read_text(encoding="utf-8") + "\nArricchita dal builder.", encoding="utf-8")
    assert crea(raw, wiki, tmp_path) == []                         # seconda volta: non tocca nulla
    assert "Arricchita dal builder." in creati[0].read_text(encoding="utf-8")
