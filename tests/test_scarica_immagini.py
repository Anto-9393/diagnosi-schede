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


def test_nomi_wikipedia_speciali():
    assert scarica.titoli_candidati("iPad Pro 11in 1st Gen") == ["iPad Pro (3rd generation)"]
    assert scarica.titoli_candidati("iPad Pro 12.9 3rd Gen") == ["iPad Pro (3rd generation)"]
    assert scarica.titoli_candidati("iPhone SE 2020") == ["iPhone SE (2nd generation)"]
    assert scarica.titoli_candidati("iPhone 11 Pro Max") == ["iPhone 11 Pro Max", "iPhone 11 Pro"]
    assert scarica.titoli_candidati("iPhone 17 Air") == ["iPhone Air"]


def test_foto_adatta():
    assert scarica.foto_adatta("iPad Air 4", "iPad Air (4th generation)", "IPad_Air_(4th_generation,_logo).svg")[0] is False
    assert scarica.foto_adatta("iPad Air", "IPad Air", "IPad_Air_2020_(51012790753).jpg")[0] is False
    assert scarica.foto_adatta("iPad 4", "IPad (4th generation)", "IPad_3.png") == (True, "foto di un modello simile")
    assert scarica.foto_adatta("iPad 7", "IPad (7th generation)", "IPad_10.2\u2011inch.png") == (True, "")
    assert scarica.foto_adatta("iPad Air 4", "IPad Air (4th generation)", "IPad_Air_4.png") == (True, "")
    assert scarica.foto_adatta("iPhone 12 Mini", "IPhone 12", "IPhone_12_Blue.svg")[1] == "foto del modello base (stesso design)"
