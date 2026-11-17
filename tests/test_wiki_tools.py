"""Test dei tool di lettura della wiki su una wiki finta in una cartella temporanea."""
from diagnosi.wiki_tools import cerca, indice, pagina


def _wiki(tmp_path):
    (tmp_path / "componenti").mkdir()
    (tmp_path / "index.md").write_text("# Indice\n- [CD3217](componenti/cd3217.md)\n", encoding="utf-8")
    (tmp_path / "componenti" / "cd3217.md").write_text(
        "---\ntitolo: CD3217\n---\nController USB-C. Modalità dead battery senza batteria.\n", encoding="utf-8")
    (tmp_path / "componenti" / "tristar.md").write_text(
        "---\ntitolo: Tristar\n---\nIC Lightning degli iPhone.\n", encoding="utf-8")
    return tmp_path


def test_indice(tmp_path):
    assert "CD3217" in indice(_wiki(tmp_path))


def test_pagina_ha_la_fonte(tmp_path):
    testo = pagina("componenti/cd3217.md", _wiki(tmp_path))
    assert testo.startswith("FONTE: wiki/componenti/cd3217.md")


def test_pagina_fuori_dalla_wiki_e_vietata(tmp_path):
    w = _wiki(tmp_path)
    (tmp_path.parent / "segreto.md").write_text("chiave", encoding="utf-8")
    assert "non consentito" in pagina("../segreto.md", w)


def test_cerca_ordina_per_pertinenza(tmp_path):
    risultato = cerca("cd3217 dead battery", wiki_dir=_wiki(tmp_path))
    assert risultato.splitlines()[0].startswith("- wiki/componenti/cd3217.md")
    assert "tristar" not in risultato
