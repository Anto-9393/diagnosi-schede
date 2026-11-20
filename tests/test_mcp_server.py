"""Il server MCP espone tool, resource e prompt; i tool di sola lettura funzionano senza chiave (come S13)."""
import asyncio

from diagnosi import mcp_server, wiki_tools


def test_primitive_esposte():
    tools = asyncio.run(mcp_server.mcp.list_tools())
    assert {t.name for t in tools} == {"cerca_caso", "componente_info", "suggerisci_misura"}
    prompts = asyncio.run(mcp_server.mcp.list_prompts())
    assert [p.name for p in prompts] == ["diagnosi_guidata"]
    templates = asyncio.run(mcp_server.mcp.list_resource_templates())
    assert "wiki://{tipo}/{nome}" in [str(t.uri_template) for t in templates]


def test_resource_rifiuta_uri_strani(monkeypatch):
    monkeypatch.setattr(wiki_tools, "pagina", lambda p: f"FONTE: wiki/{p}")
    assert mcp_server.pagina_wiki("componenti", "cd3217") == "FONTE: wiki/componenti/cd3217.md"
    assert mcp_server.pagina_wiki("..", "env") == "URI non valido."


def test_componente_info_preferisce_il_nome_esatto():
    from diagnosi.mcp_server import componente_info
    assert componente_info("Tristar").startswith("FONTE: wiki/componenti/tristar.md")   # non c4005.md, che lo cita
