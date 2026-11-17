"""La sessione registra le pagine lette dall'agente (servono ai guardrail). Nessuna chiamata all'LLM."""
from diagnosi import wiki_tools


def test_i_tool_registrano_le_pagine_lette(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "x")
    monkeypatch.setenv("ANTHROPIC_API_KEY", "x")
    from diagnosi.agent import SessioneDiagnosi
    monkeypatch.setattr(wiki_tools, "pagina", lambda p, max_caratteri=0: f"FONTE: wiki/{p}\n\ntesto di {p}")
    monkeypatch.setattr(wiki_tools, "cerca", lambda q: "- wiki/componenti/cd3217.md")
    s = SessioneDiagnosi()
    leggi_indice, leggi_pagina, cerca_wiki = s._crea_tool()
    leggi_pagina("componenti/cd3217.md")
    cerca_wiki("CD3217")
    assert list(s.pagine_lette) == ["wiki/componenti/cd3217.md"]
    assert s.chiamate_tool == ["leggi_pagina(componenti/cd3217.md)", "cerca_wiki(CD3217)"]



def test_modalita_rapida_e_breve(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "x")
    from diagnosi.agent import SessioneDiagnosi
    from diagnosi.schemas import PassoBreve
    s = SessioneDiagnosi(dettaglio="breve", lettura="rapida")
    assert s.max_caratteri == 4_000 and s.agente._output_cls is PassoBreve
    assert "Lettura RAPIDA" in s.agente.system_prompt and "SOLO la prossima misura" in s.agente.system_prompt


def test_memoria_compatta_tra_i_turni(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "x")
    from diagnosi.agent import SessioneDiagnosi
    from diagnosi.schemas import Ipotesi, Misura, PassoDiagnosi
    s = SessioneDiagnosi()
    assert s._input_con_storia("primo") == "primo"
    passo = PassoDiagnosi(dispositivo="iPad Air 4", riepilogo="r",
                          ipotesi=[Ipotesi(componente="CD3217", motivo="m", probabilita="alta")],
                          prossima_misura=Misura(dove="X1548", modalita="tensione", condizioni="con batteria",
                                                 valore_atteso="~5 V", se_diverso="x"),
                          avvertenze_sicurezza=[], fonti=[], domande_al_tecnico=[])
    s.pagine_lette["wiki/componenti/cd3217.md"] = "testo lungo " * 1000
    s._ricorda("non carica", passo)
    secondo = s._input_con_storia("X1548 = 0,1 V")
    assert "Tecnico: non carica" in secondo and "misura X1548" in secondo and "X1548 = 0,1 V" in secondo
    assert "testo lungo" not in secondo                       # il testo delle pagine NON viene ripetuto
    assert "wiki/componenti/cd3217.md" in secondo             # solo il nome delle pagine già lette
