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


def test_aria_calda_con_batteria_scollegata_non_blocca():
    _, esito = controlla(_passo(condizioni="scollega la batteria, poi aria calda 350 °C sul CD3217 lontano dalla batteria"), LETTE)
    assert not esito.bloccato
    _, esito = controlla(_passo(condizioni="aria calda sul CD3217 vicino alla batteria"), LETTE)
    assert esito.bloccato


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


def test_iniezione_con_batteria_collegata():
    passo, esito = controlla(_passo(condizioni="iPad con batteria collegata; iniezione 1 V / 1 A con limite di corrente"), LETTE)
    assert any("SCOLLEGA la batteria" in a for a in esito.avvisi)
    _, esito = controlla(_passo(condizioni="batteria scollegata; iniezione 1 V con limite di corrente"), LETTE)
    assert not any("SCOLLEGA" in a for a in esito.avvisi)


def test_guardrail_funzionano_con_risposta_breve():
    from diagnosi.schemas import PassoBreve
    breve = PassoBreve(dispositivo="iPad Air 4", prossima_misura=_passo(condizioni="cortocircuita la batteria").prossima_misura,
                       avvertenze_sicurezza=[], fonti=["wiki/componenti/cd3217.md"], domande_al_tecnico=[])
    passo, esito = controlla(breve, LETTE)
    assert esito.bloccato and passo.fonti == ["wiki/componenti/cd3217.md"]


# ── Procedura ("come si fa") ──
from diagnosi.guardrails import controlla_procedura
from diagnosi.schemas import PassoProcedura, Procedura


def _proc(avvertenze=("protezione ESD",), azione="aria calda sul CD3217, poi pulisci le piazzole", fonti=("wiki/componenti/cd3217.md",)):
    return Procedura(dispositivo="iPad Air 4 (A2316)", obiettivo="Sostituire il CD3217",
                     avvertenze_sicurezza=list(avvertenze),
                     passi=[PassoProcedura(titolo="Rimuovi il CD3217", azione=azione, attrezzo="aria calda", controllo="piazzole pulite")],
                     fonti=list(fonti))


def test_procedura_con_calore_senza_batteria_scollegata_aggiunge_avviso():
    proc, esito = controlla_procedura(_proc(), LETTE)
    assert not esito.bloccato
    assert proc.avvertenze_sicurezza[0].startswith("Prima di aria calda o saldatura: SCOLLEGA")


def test_procedura_con_batteria_scollegata_passa():
    proc, esito = controlla_procedura(_proc(avvertenze=("Scollega la batteria e allontanala", "protezione ESD")), LETTE)
    assert esito.avvisi == [] and proc.fonti == ["wiki/componenti/cd3217.md"]
    assert not any(a.startswith("Prima di aria calda") for a in proc.avvertenze_sicurezza)


def test_procedura_pericolosa_blocca_e_fonti_non_lette():
    _, esito = controlla_procedura(_proc(azione="cortocircuita la batteria per scaricarla"), LETTE)
    assert esito.bloccato
    proc, esito = controlla_procedura(_proc(fonti=("wiki/tecniche/inventata.md",)), LETTE)
    assert proc.fonti == [] and any("Nessuna fonte" in a for a in esito.avvisi)


def test_valore_atteso_copiato_dal_caso_guasto():
    lette = {**LETTE, "wiki/casi/a2316.md": "Con batteria e cavo X1548 a 0,026–0,186 V: il CD3217 non chiude il passaggio."}
    _, esito = controlla(_passo(dove="X1548", valore="0,026–0,186 V"), lette)
    assert any("scheda guasta" in a for a in esito.avvisi)
    _, esito = controlla(_passo(dove="X1548", valore="livello VBUS, circa 5 V"), lette)     # valore sano: nessun avviso
    assert not any("scheda guasta" in a for a in esito.avvisi)
    lette["wiki/casi/a2316.md"] += " Senza batteria ~4,7 V."                                # un solo numero citato
    _, esito = controlla(_passo(dove="X1548", valore="Su scheda sana: livello di carica (nel caso senza batteria ~4,7 V)"), lette)
    assert not any("scheda guasta" in a for a in esito.avvisi)


def test_avvertenze_di_repertorio_tolte():
    passo, _ = controlla(_passo(avvertenze=("Usare ESD per proteggere i componenti sensibili.",
                                            "Batteria scollegata prima di iniettare.")), LETTE)
    assert passo.avvertenze_sicurezza == ["Batteria scollegata prima di iniettare."]


def test_scalda_come_sintomo_non_blocca():
    _, esito = controlla(_passo(condizioni="iniezione 1 V: con la termocamera guarda cosa scalda per primo, con batteria scollegata"), LETTE)
    assert not esito.bloccato
    _, esito = controlla(_passo(condizioni="usa aria calda a 350 gradi vicino alla batteria"), LETTE)
    assert esito.bloccato


def test_pericolo_nella_domanda():
    from diagnosi.guardrails import pericolo_nella_domanda
    for m in ("butto acqua con la presa attaccata", "lo lavo con acqua mentre è in carica",
              "posso spruzzare alcol con la batteria collegata?", "pulisco con IPA col caricatore attaccato"):
        assert pericolo_nella_domanda(m), m
    for m in ("è caduto in acqua e non carica", "non carica e non viene rilevato dopo caduta nel caffè",
              "mi hanno detto di pulirlo con l'acqua pensi che sia una buona idea?",
              "pulisco con IPA a batteria scollegata e cavo staccato", "0,002 A con batteria e cavo"):
        assert not pericolo_nella_domanda(m), m
