"""Test dell'importatore su un export XML finto (formato Special:Export). Nessuna rete, nessun LLM."""
from diagnosi.import_repairwiki import importa, wikitext_a_markdown
from diagnosi.wiki_builder import leggi_front_matter

XML = """<mediawiki xmlns="http://www.mediawiki.org/xml/export-0.11/">
  <page><title>iPhone X</title><ns>0</ns><id>1</id>
    <revision><id>10</id><timestamp>2026-01-01T22:19:00Z</timestamp>
      <text xml:space="preserve">{{Infobox|name=iPhone X}}
== Common issues ==
'''No backlight''' is common, see [[Backlight circuit|backlight]].
* Check the [[Tristar]] chip
** Measure PP_VCC_MAIN in diode mode
[[File:board.jpg|thumb]]
[[Category:Apple Phones]]
Lorem ipsum per superare la soglia minima di lunghezza della pagina, ripetuto per sicurezza.
Lorem ipsum per superare la soglia minima di lunghezza della pagina, ripetuto per sicurezza.</text>
    </revision></page>
  <page><title>Category:Apple Phones</title><ns>14</ns><id>2</id>
    <revision><id>11</id><timestamp>2026-01-01T00:00:00Z</timestamp><text>x</text></revision></page>
  <page><title>Old name</title><ns>0</ns><id>3</id><redirect title="iPhone X"/>
    <revision><id>12</id><timestamp>2026-01-01T00:00:00Z</timestamp><text>#REDIRECT [[iPhone X]]</text></revision></page>
</mediawiki>"""


def test_conversione_wikitext():
    md, categorie = wikitext_a_markdown("== Titolo ==\n'''grassetto''' [[Pagina|testo]] {{tmpl}}\n[[Category:Apple Phones]]")
    assert "## Titolo" in md and "**grassetto**" in md and "testo" in md
    assert "{{" not in md and "Category" not in md
    assert categorie == ["Apple Phones"]


def test_importa_solo_articoli_con_attribuzione(tmp_path):
    xml = tmp_path / "export.xml"
    xml.write_text(XML, encoding="utf-8")
    scritti = importa(xml, tmp_path / "out")
    assert [f.name for f in scritti] == ["iphone-x.md"]          # niente categoria, niente redirect
    testo = scritti[0].read_text(encoding="utf-8")
    fm, _ = leggi_front_matter(testo)
    assert fm["licenza"].startswith("CC BY-SA 3.0")
    assert fm["url"] == "https://repair.wiki/w/iPhone_X"
    assert fm["revisione"] == "2026-01-01T22:19:00Z"
    assert "  - Measure PP_VCC_MAIN" in testo                    # lista annidata
    assert "File:" not in testo


STUB = """<mediawiki xmlns="http://www.mediawiki.org/xml/export-0.11/">
  <page><title>IPad Air 4</title><ns>0</ns><id>5</id>
    <revision><id>50</id><timestamp>2026-02-01T10:00:00Z</timestamp>
      <text xml:space="preserve">{{Device page
|Manufacturer=Apple
|Has code name=A2316, A2324, A2325, A2072
|Device release date=2020-10-23
|Device type=Tablet
}}
{{stub}}
== Guides ==
{{List Guides}}
== More Information/External Sources ==
CD3217 Know good ROM dump: https://www.sendspace.com/filegroup/abc</text>
    </revision></page>
  <page><title>Ru Как диагнозировать</title><ns>0</ns><id>6</id>
    <revision><id>60</id><timestamp>2026-02-01T10:00:00Z</timestamp><text>testo lungo</text></revision></page>
</mediawiki>"""


def test_pagina_modello_tiene_i_codici_e_toglie_sendspace(tmp_path):
    xml = tmp_path / "stub.xml"
    xml.write_text(STUB, encoding="utf-8")
    scritti = importa(xml, tmp_path / "out")
    assert [f.name for f in scritti] == ["ipad-air-4.md"]          # la copia in russo è saltata
    testo = scritti[0].read_text(encoding="utf-8")
    fm, _ = leggi_front_matter(testo)
    assert fm["categoria_dispositivo"] == "tablet"
    assert fm["codici_modello"] == ["A2072", "A2316", "A2324", "A2325"]
    assert str(fm["data_uscita"]) == "2020-10-23"
    assert "sendspace" not in testo


def test_titolo_con_virgolette_resta_yaml_valido(tmp_path):
    xml = tmp_path / "q.xml"
    xml.write_text(XML.replace("<title>iPhone X</title>", "<title>iPad Air 6 12.9\" Touch Not Working</title>"), encoding="utf-8")
    fm, _ = leggi_front_matter(importa(xml, tmp_path / "out")[0].read_text(encoding="utf-8"))
    assert fm["titolo"] == 'iPad Air 6 12.9" Touch Not Working'


def test_figure_della_guida():
    from diagnosi.import_repairwiki import figure_da_wikitext
    t = ("[[File:Screenshot A.png|center|thumb|876x876px|Figure 2.  LCD FPC readings]] testo "
         "<gallery>\nFile:Example pcb pictures.jpg\nFile:Diode Readings.jpg|Diode Mode Readings\n</gallery>")
    assert figure_da_wikitext(t) == [{"file": "Screenshot A.png", "didascalia": "Figure 2. LCD FPC readings"},
                                     {"file": "Diode Readings.jpg", "didascalia": "Diode Mode Readings"}]   # "Example" no


def test_indirizzo_figura_come_mediawiki(tmp_path):
    from diagnosi.dispositivi import figure_guida
    pagine = tmp_path / "raw" / "repairwiki" / "pagine"; pagine.mkdir(parents=True)
    (pagine / "g.md").write_text("---\nfigure:\n- file: example.jpg\n  didascalia: Figura\n---\n# G\n", encoding="utf-8")
    f = figure_guida("raw/repairwiki/pagine/g.md", tmp_path)[0]
    assert f["url"] == "https://repair.wiki/images/a/a9/Example.jpg"        # esempio della documentazione MediaWiki
    assert f["pagina"] == "https://repair.wiki/w/File:Example.jpg"
    assert figure_guida("casi/a.md", tmp_path) == []                          # le pagine della nostra wiki no
