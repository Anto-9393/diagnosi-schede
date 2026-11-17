"""Test dei guardrail sulle risposte (deterministici, S15): nessuna chiave, nessun LLM."""
from diagnosi.guardrails import controlla
from diagnosi.schemas import Ipotesi, Misura, PassoDiagnosi


def _passo(dove="NET205", condizioni="con batteria, cavo inserito", valore="5 V", ipotesi="CD3217",
           fonti=("wiki/componenti/cd3217.md",), avvertenze=()):
    return PassoDiagnosi(
        dispositivo="iPad Air 4 (A2316)", riepilogo="non carica",
        ipotesi=[Ipotesi(componente=ipotesi, motivo="sospetto", probabilita="alta")],
        prossima_misura=Misura(dove=dove, modalita="tensione", condizioni=condizioni,
                               valore_atteso=valore, se_diverso="guasto"),
        avvertenze_sicurezza=list(avvertenze), fonti=list(fonti), domande_al_tecnico=[])


LETTE = {"wiki/componenti/cd3217.md": "FONTE: wiki/componenti/cd3217.md\nCD3217 controller USB-C, NET205"}


def test_risposta_pulita_passa():
    passo, esito = controlla(_passo(), LETTE)
    assert esito.avvisi == [] and not esito.bloccato and passo.fonti == ["wiki/componenti/cd3217.md"]


def test_alimentatore_senza_limite_di_corrente_aggiunge_avvertenza():
    passo, esito = controlla(_passo(condizioni="alimenta dal banco a 4 V sul connettore batteria"), LETTE)
    assert any("LIMITE DI CORRENTE" in a for a in esito.avvisi)
    assert passo.avvertenze_sicurezza[0].startswith("Usa l'alimentatore")


def test_istruzione_pericolosa_blocca():
    _, esito = controlla(_passo(condizioni="cortocircuita la batteria per scaricarla"), LETTE)
    assert esito.bloccato


def test_negazione_non_blocca():
    _, esito = controlla(_passo(condizioni="non cortocircuitare la batteria durante la misura"), LETTE)
    assert not esito.bloccato


def test_tensione_impossibile_e_batteria_oltre_cella():
    _, esito = controlla(_passo(valore="28 V"), LETTE)
    assert any("fuori dal plausibile" in a for a in esito.avvisi)
    _, esito = controlla(_passo(dove="connettore batteria", valore="5 V"), LETTE)
    assert any("cella Li-ion" in a for a in esito.avvisi)


def test_sigla_inventata_viene_segnalata():
    _, esito = controlla(_passo(ipotesi="U4001 Tristar"), LETTE)
    assert esito.sigle_non_verificate == ["U4001"]


def test_fonti_non_lette_rimosse_e_nessuna_fonte_segnalata():
    passo, esito = controlla(_passo(fonti=("wiki/componenti/inventata.md",)), LETTE)
    assert passo.fonti == []
    assert any("Nessuna fonte" in a for a in esito.avvisi)
