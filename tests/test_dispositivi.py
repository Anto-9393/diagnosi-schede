from diagnosi.dispositivi import casi_del_dispositivo, trova_dispositivo


def _wiki(tmp_path):
    d = tmp_path / "dispositivi"; d.mkdir()
    (d / "ipad-air.md").write_text("---\ntitolo: iPad Air\ncodici_modello: [A1474]\n---\n", encoding="utf-8")
    (d / "ipad-air-4.md").write_text("---\ntitolo: iPad Air 4\ncodici_modello: [A2316, A2324]\n---\n", encoding="utf-8")
    return tmp_path


def test_codice_modello_vince(tmp_path):
    assert trova_dispositivo("scheda A2316 dopo caffè", _wiki(tmp_path))["titolo"] == "iPad Air 4"


def test_nome_piu_lungo_vince(tmp_path):
    w = _wiki(tmp_path)
    assert trova_dispositivo("ho un iPad Air 4 che non carica", w)["titolo"] == "iPad Air 4"
    assert trova_dispositivo("ho un iPad Air che non carica", w)["titolo"] == "iPad Air"
    assert trova_dispositivo("ho un Galaxy", w) is None


def test_casi_del_dispositivo(tmp_path):
    w = _wiki(tmp_path); (w / "casi").mkdir()
    (w / "casi" / "a2316.md").write_text("---\ntitolo: caso\nmodelli: [iPad Air 4 (A2316)]\n---\n", encoding="utf-8")
    assert casi_del_dispositivo("iPad Air 4", w) == ["casi/a2316.md"]
    assert casi_del_dispositivo("iPad Air 5", w) == []
    assert casi_del_dispositivo("iPad Air", w) == []          # niente contaminazione tra modelli
