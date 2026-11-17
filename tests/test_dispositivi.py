from diagnosi.dispositivi import casi_del_dispositivo, guide_del_dispositivo, solo_dispositivo, trova_dispositivo


def _wiki(tmp_path):
    d = tmp_path / "dispositivi"; d.mkdir()
    (d / "ipad-air.md").write_text("---\ntitolo: iPad Air\ncodici_modello: [A1474]\n---\n", encoding="utf-8")
    (d / "ipad-air-4.md").write_text("---\ntitolo: iPad Air 4\ncodici_modello: [A2316, A2324]\n---\n", encoding="utf-8")
    return tmp_path


def test_codice_modello_vince(tmp_path):
    w = _wiki(tmp_path)
    assert trova_dispositivo("scheda A2316 dopo caffè", w)["titolo"] == "iPad Air 4"
    assert trova_dispositivo("a2316", w)["titolo"] == "iPad Air 4"      # anche minuscolo


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


def test_solo_dispositivo(tmp_path):
    w = _wiki(tmp_path)
    d = trova_dispositivo("iPad Air 4", w)
    assert solo_dispositivo("iPad Air 4", d)
    assert solo_dispositivo("A2316", d)
    assert solo_dispositivo("dammi le guide per l'iPad Air 4", d)
    assert not solo_dispositivo("iPad Air 4 non carica", d)        # c'è un sintomo: va all'agente
    assert not solo_dispositivo("A2316, 0,002 A con batteria", d)


def _guida(raw, nome, titolo):
    (raw / f"{nome}.md").write_text(f"---\ntitolo: {titolo}\nurl: https://repair.wiki/w/{nome}\n---\n", encoding="utf-8")


def test_guide_del_dispositivo(tmp_path):
    (tmp_path / "wiki").mkdir(); w = _wiki(tmp_path / "wiki")
    raw = tmp_path / "raw"; pagine = raw / "repairwiki" / "pagine"; pagine.mkdir(parents=True)
    _guida(pagine, "air4-backlight", "IPad Air 4 No Backlight")
    _guida(pagine, "air-no-touch", "IPad Air No Touch")
    (pagine / "ipad-air-4.md").write_text("---\ntitolo: IPad Air 4\ncategoria_dispositivo: tablet\n---\n", encoding="utf-8")
    (w / "componenti").mkdir()
    (w / "componenti" / "cd3217.md").write_text("---\ntitolo: CD3217\ntipo: componente\nmodelli: [iPad Air 4 A2316]\n---\n",
                                                encoding="utf-8")
    (w / "componenti" / "backlight.md").write_text("---\ntitolo: Backlight\ntipo: componente\nmodelli: []\n"
                                                   "fonti: [raw/repairwiki/pagine/air4-backlight.md]\n---\n", encoding="utf-8")
    (w / "componenti" / "tristar.md").write_text("---\ntitolo: Tristar\ntipo: componente\nmodelli: [iPad Air]\n---\n",
                                                 encoding="utf-8")
    g = guide_del_dispositivo(trova_dispositivo("iPad Air 4", w), w, raw)
    assert [x["titolo"] for x in g["repairwiki"]] == ["IPad Air 4 No Backlight"]   # né "iPad Air", né la pagina dispositivo
    assert {x["percorso"] for x in g["wiki"]} == {"componenti/cd3217.md", "componenti/backlight.md"}
    g = guide_del_dispositivo(trova_dispositivo("iPad Air", w), w, raw)
    assert [x["titolo"] for x in g["repairwiki"]] == ["IPad Air No Touch"]
    assert [x["percorso"] for x in g["wiki"]] == ["componenti/tristar.md"]
