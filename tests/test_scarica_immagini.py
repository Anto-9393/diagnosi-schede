"""Il controllo della licenza delle immagini, senza rete."""
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("scarica", Path(__file__).parents[1] / "scripts" / "scarica_immagini.py")
scarica = importlib.util.module_from_spec(spec); spec.loader.exec_module(scarica)


def _info(licenza, autore="<a href='x'>Mario</a>"):
    return {"descriptionurl": "https://commons.wikimedia.org/wiki/File:X.jpg",
            "extmetadata": {"LicenseShortName": {"value": licenza}, "Artist": {"value": autore}}}


def test_licenze_libere_accettate():
    assert scarica.credito(_info("CC BY-SA 4.0"), "X.jpg") == ("https://commons.wikimedia.org/wiki/File:X.jpg", "Mario", "CC BY-SA 4.0")
    assert scarica.credito(_info("Public domain"), "X.jpg")[2] == "Public domain"


def test_licenze_non_libere_rifiutate():
    assert scarica.credito(_info("Fair use"), "X.jpg") is None
    assert scarica.credito(_info("All rights reserved"), "X.jpg") is None


def test_titoli_secondo_le_convenzioni_di_wikipedia():
    assert scarica.titoli_candidati("iPad Air 4")[0] == "iPad Air (4th generation)"
    assert scarica.titoli_candidati("iPad 10")[0] == "iPad (10th generation)"
    assert scarica.titoli_candidati("iPad Mini 6")[0] == "iPad Mini (6th generation)"
    assert scarica.titoli_candidati("iPad 2")[0] == "iPad (2nd generation)"
    assert scarica.titoli_candidati("iPhone 11 Pro") == ["iPhone 11 Pro"]


def test_coerenza_del_modello():
    assert scarica.coerente("iPad Air 4", "iPad Air (4th generation)")
    assert not scarica.coerente("iPad 2", "iPad Air 2")                 # il bug visto il 17 nov
    assert not scarica.coerente("iPad 4", "iPad Mini 4")
    assert not scarica.coerente("iPad 10", "List of iPad models")
    assert not scarica.coerente("iPhone 11", "iPhone 11 Pro")
