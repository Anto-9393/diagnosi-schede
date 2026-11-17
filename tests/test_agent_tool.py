"""La sessione registra le pagine lette dall'agente (servono ai guardrail). Nessuna chiamata all'LLM."""
from diagnosi import wiki_tools


def test_i_tool_registrano_le_pagine_lette(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "x")
    monkeypatch.setenv("ANTHROPIC_API_KEY", "x")
    from diagnosi.agent import SessioneDiagnosi
    monkeypatch.setattr(wiki_tools, "pagina", lambda p: f"FONTE: wiki/{p}\n\ntesto di {p}")
    monkeypatch.setattr(wiki_tools, "cerca", lambda q: "- wiki/componenti/cd3217.md")
    s = SessioneDiagnosi()
    leggi_indice, leggi_pagina, cerca_wiki = s._crea_tool()
    leggi_pagina("componenti/cd3217.md")
    cerca_wiki("CD3217")
    assert list(s.pagine_lette) == ["wiki/componenti/cd3217.md"]
    assert s.chiamate_tool == ["leggi_pagina(componenti/cd3217.md)", "cerca_wiki(CD3217)"]
