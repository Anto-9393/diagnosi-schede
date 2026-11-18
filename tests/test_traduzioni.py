"""Traduzione salvata una volta, con l'attribuzione CC BY-SA in testa (client finto: niente chiave)."""
from types import SimpleNamespace

from diagnosi.traduzioni import traduci, tradotta


class ClientFinto:
    def __init__(self):
        self.chiamate = 0

    def invoke(self, testo, system_prompt="", max_tokens=0):
        self.chiamate += 1
        assert "> Fonte:" not in testo                      # l'attribuzione non passa dal modello
        return SimpleNamespace(text="# Niente retroilluminazione\n\nMisura il pin 11 in diode mode.",
                               usage=SimpleNamespace(prompt_tokens=100, completion_tokens=50))


def test_traduzione_salvata_con_attribuzione(tmp_path):
    pagine = tmp_path / "raw" / "repairwiki" / "pagine"; pagine.mkdir(parents=True)
    (pagine / "g.md").write_text("---\nurl: x\n---\n# No Backlight\n\n> Fonte: [G — repair.wiki](https://repair.wiki/w/G), "
                                 "CC BY-SA 3.0.\n\nMeasure pin 11 in diode mode.\n", encoding="utf-8")
    cartella = tmp_path / "raw" / "repairwiki" / "tradotte"
    assert tradotta("raw/repairwiki/pagine/g.md", cartella, tmp_path) is None
    client = ClientFinto()
    testo, tin, tout = traduci("raw/repairwiki/pagine/g.md", client, cartella, tmp_path)
    assert (tin, tout) == (100, 50) and client.chiamate == 1
    assert testo.startswith("# Niente retroilluminazione\n\n> Fonte: [G — repair.wiki](https://repair.wiki/w/G)")
    assert "Traduzione automatica in italiano" in testo
    letta = tradotta("raw/repairwiki/pagine/g.md", cartella, tmp_path)      # la seconda volta: dal file, 0 token
    assert "Misura il pin 11" in letta and "originale:" not in letta
