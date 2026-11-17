from pathlib import Path

"""Test del wiki builder con un client FINTO: nessuna chiave, nessuna chiamata reale.

Il client finto risponde a structured_response con oggetti preparati: così si verifica tutto ciò che
fa il NOSTRO codice (guardrail sui percorsi, front-matter, index, log) indipendentemente dall'LLM.
"""
from types import SimpleNamespace

from diagnosi.wiki_builder import (PaginaDaToccare, PaginaWiki, PianoIngest, dispositivo_pertinente, ingest,
                                   leggi_front_matter, percorso_valido, ripara_link)


class ClientFinto:
    def __init__(self, piano, pagine):
        self.risposte = [piano, *pagine]
        self.chiamate = []

    def structured_response(self, **kw):
        self.chiamate.append(kw)
        return SimpleNamespace(structured_data=[self.risposte.pop(0)])


def _pagina(titolo, **extra):
    base = dict(titolo=titolo, riassunto=f"riassunto {titolo}", modelli=["iPad Air 4"],
                contenuto=f"Corpo di {titolo}.", categoria="nessuna", codici_modello=[], componenti_chiave=[])
    return PaginaWiki(**(base | extra))


def _progetto(tmp_path):
    (tmp_path / "AGENTS.md").write_text("schema", encoding="utf-8")
    (tmp_path / "wiki").mkdir()
    fonte = tmp_path / "raw" / "repairwiki" / "pagine" / "rom-cd3217.md"
    fonte.parent.mkdir(parents=True)
    fonte.write_text("---\ntitolo: ROM CD3217 iPad Air 4\nlicenza: CC BY-SA 3.0\n---\nTesto della fonte.", encoding="utf-8")
    disp = tmp_path / "wiki" / "dispositivi"
    disp.mkdir()
    (disp / "ipad-air-4.md").write_text("---\ntitolo: iPad Air 4\ntipo: dispositivo\n---\nScheda.", encoding="utf-8")
    (disp / "ipad-air.md").write_text("---\ntitolo: iPad Air\ntipo: dispositivo\n---\nScheda.", encoding="utf-8")
    return tmp_path, fonte


def test_percorso_valido_corregge_e_vincola_la_cartella():
    assert percorso_valido("wiki/componenti/cd3217.md", "componente").as_posix() == "componenti/cd3217.md"
    assert percorso_valido("../../.env", "componente").as_posix() == "componenti/env.md"     # niente fuga
    assert percorso_valido("sintomi/Non Carica.md", "sintomo").as_posix() == "sintomi/non-carica.md"
    assert percorso_valido("casi/x.md", "componente").as_posix() == "componenti/x.md"          # cartella dal tipo


def test_ingest_scrive_pagine_indice_e_log(tmp_path):
    root, fonte = _progetto(tmp_path)
    piano = PianoIngest(pagine=[
        PaginaDaToccare(percorso="componenti/cd3217.md", tipo="componente", motivo="ROM e firmware"),
        PaginaDaToccare(percorso="dispositivi/ipad-air-4.md", tipo="dispositivo", motivo="modello interessato"),
    ])
    client = ClientFinto(piano, [
        _pagina("CD3217"),
        _pagina("iPad Air 4", categoria="tablet", codici_modello=["A2316"], componenti_chiave=["CD3217"]),
    ])
    toccate = ingest(client, fonte, wiki_dir=root / "wiki", root=root, verbose=False)

    assert toccate == ["componenti/cd3217.md", "dispositivi/ipad-air-4.md"]
    fm, corpo = leggi_front_matter((root / "wiki/componenti/cd3217.md").read_text(encoding="utf-8"))
    assert fm["fonti"] == ["raw/repairwiki/pagine/rom-cd3217.md"] and fm["licenza"] == "CC BY-SA 3.0"
    assert corpo.startswith("Corpo di CD3217")
    fm_d, _ = leggi_front_matter((root / "wiki/dispositivi/ipad-air-4.md").read_text(encoding="utf-8"))
    assert fm_d["categoria"] == "tablet" and fm_d["codici_modello"] == ["A2316"]
    indice = (root / "wiki/index.md").read_text(encoding="utf-8")
    assert "[CD3217](componenti/cd3217.md)" in indice and "## Dispositivi" in indice
    assert "ingest | raw/repairwiki/pagine/rom-cd3217.md" in (root / "wiki/log.md").read_text(encoding="utf-8")
    assert len(client.chiamate) == 3                       # 1 piano + 2 pagine


def test_secondo_ingest_conserva_le_fonti(tmp_path):
    root, fonte = _progetto(tmp_path)
    altra = root / "raw" / "casi" / "caso.md"
    altra.parent.mkdir(parents=True)
    altra.write_text("Appunti di un caso.", encoding="utf-8")
    voce = PaginaDaToccare(percorso="componenti/cd3217.md", tipo="componente", motivo="x")
    ingest(ClientFinto(PianoIngest(pagine=[voce]), [_pagina("CD3217")]), fonte, root / "wiki", root, False)
    ingest(ClientFinto(PianoIngest(pagine=[voce]), [_pagina("CD3217")]), altra, root / "wiki", root, False)
    fm, _ = leggi_front_matter((root / "wiki/componenti/cd3217.md").read_text(encoding="utf-8"))
    assert fm["fonti"] == ["raw/repairwiki/pagine/rom-cd3217.md", "raw/casi/caso.md"]
    assert fm["licenza"] == "CC BY-SA 3.0"                 # la licenza resta anche se la 2a fonte non l'ha


def test_dispositivo_pertinente_evita_la_contaminazione():
    assert dispositivo_pertinente("iPad Air", "How to fix an iPad Air that will not charge")
    assert not dispositivo_pertinente("iPad Air 4", "How to fix an iPad Air that will not charge")
    assert not dispositivo_pertinente("iPad Air", "IPad Air 4 No Backlight")
    assert not dispositivo_pertinente("iPhone 7", "How To Fix iPhone 7 Plus boot loop")
    assert dispositivo_pertinente("iPhone 7", "How To Fix an iPhone 7 That Does Not Charge")
    assert not dispositivo_pertinente("iPhone X", "How To Fix iPhone XS That Randomly Restarts")


def test_ingest_scarta_caso_da_guida_e_dispositivo_non_pertinente(tmp_path):
    root, fonte = _progetto(tmp_path)
    piano = PianoIngest(pagine=[
        PaginaDaToccare(percorso="casi/finto.md", tipo="caso", motivo="x"),
        PaginaDaToccare(percorso="dispositivi/ipad-air.md", tipo="dispositivo", motivo="x"),
        PaginaDaToccare(percorso="dispositivi/ipad-pro.md", tipo="dispositivo", motivo="x"),
    ])
    client = ClientFinto(piano, [])
    assert ingest(client, fonte, root / "wiki", root, False) == []   # tutte scartate, nessuna chiamata di pagina
    assert len(client.chiamate) == 1


def test_ripara_link(tmp_path):
    (tmp_path / "fonti").mkdir(); (tmp_path / "tecniche").mkdir()
    (tmp_path / "fonti" / "a.md").write_text("x", encoding="utf-8")
    testo = "[A](../../fonti/a.md) e [B](../componenti/inesistente.md) e [C](../fonti/a.md)"
    nuovo, corretti, rimossi = ripara_link(testo, Path("tecniche/t.md"), tmp_path)
    assert nuovo == "[A](../fonti/a.md) e B e [C](../fonti/a.md)"
    assert (corretti, rimossi) == (1, 1)


class ClientCheFallisce(ClientFinto):
    def structured_response(self, **kw):
        if self.chiamate:                                   # il piano va, la prima pagina fallisce
            self.chiamate.append(kw)
            if len(self.chiamate) == 2:
                raise ValueError("JSON troncato")
        return super().structured_response(**kw)


def test_errore_su_una_pagina_non_ferma_l_ingest(tmp_path):
    root, fonte = _progetto(tmp_path)
    piano = PianoIngest(pagine=[PaginaDaToccare(percorso="componenti/a.md", tipo="componente", motivo="x"),
                                PaginaDaToccare(percorso="componenti/b.md", tipo="componente", motivo="x")])
    client = ClientCheFallisce(piano, [_pagina("B")])
    assert ingest(client, fonte, root / "wiki", root, False) == ["componenti/b.md"]


def test_identita_del_dispositivo_non_cambia(tmp_path):
    root, fonte = _progetto(tmp_path)
    f = root / "wiki/dispositivi/ipad-air-4.md"
    f.write_text("---\ntitolo: iPad Air 4\ntipo: dispositivo\ncategoria: tablet\ncodici_modello: [A2316]\n"
                 "componenti_chiave: [CD3217]\n---\nScheda.", encoding="utf-8")
    piano = PianoIngest(pagine=[PaginaDaToccare(percorso="dispositivi/ipad-air-4.md", tipo="dispositivo", motivo="x")])
    rinominata = _pagina("iPad Air 4 — non carica (CD3217)", categoria="phone", codici_modello=["A9999"],
                         componenti_chiave=["343S00264"])
    ingest(ClientFinto(piano, [rinominata]), fonte, root / "wiki", root, False)
    fm, _ = leggi_front_matter(f.read_text(encoding="utf-8"))
    assert fm["titolo"] == "iPad Air 4" and fm["categoria"] == "tablet" and fm["codici_modello"] == ["A2316"]
    assert fm["componenti_chiave"] == ["CD3217", "343S00264"]          # i componenti invece si sommano
