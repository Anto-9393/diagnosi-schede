"""Nomi precisi: prima il codice del chip, la sigla JC solo tra parentesi (regola del tecnico, 17 nov)."""
from diagnosi.schemas import PassoProcedura, Procedura
from diagnosi.sigle import con_nomi_precisi, mappa_sigle, nomi_precisi

CASO = ("- **NET205** (VBUS dal flat) arriva a **X5 = CD3217B12** (controller USB‑C/PD TI).\n"
        "- **X3 = 343S00264‑A0** (IC di ricarica):\n"
        "- **ROM CD3217**: marcatura **8N040** (chip piccolo accanto a X5, su JC Drawing siglato **X7**).")


def test_mappa_dalle_pagine_lette():
    assert mappa_sigle([CASO]) == {"X5": "CD3217B12", "X3": "343S00264-A0", "X7": "8N040"}


def test_sigla_da_sola_diventa_codice():
    m = mappa_sigle([CASO])
    assert con_nomi_precisi("Il CD3217 non chiude il passaggio verso X3; X3 scalda.", m) == \
        "Il CD3217 non chiude il passaggio verso 343S00264-A0 (X3 su JC Drawing); 343S00264-A0 scalda."
    assert con_nomi_precisi("Dissalda la ROM X7", m) == "Dissalda la ROM 8N040 (X7 su JC Drawing)"


def test_se_il_codice_ce_gia_non_tocca_e_sigle_sconosciute_restano():
    m = mappa_sigle([CASO])
    assert con_nomi_precisi("CD3217B12 (X5) da sostituire", m) == "CD3217B12 (X5) da sostituire"
    assert con_nomi_precisi("misura X1548", m) == "misura X1548"


def test_su_tutta_la_procedura_fonti_escluse():
    p = Procedura(dispositivo="iPad Air 4 (A2316)", obiettivo="Sostituire X5",
                  passi=[PassoProcedura(titolo="Dissalda X7", azione="aria calda su X7")], fonti=["wiki/casi/x3.md"])
    q = nomi_precisi(p, [CASO])
    assert q.obiettivo == "Sostituire CD3217B12 (X5 su JC Drawing)"
    assert q.passi[0].titolo == "Dissalda 8N040 (X7 su JC Drawing)" and q.fonti == ["wiki/casi/x3.md"]
