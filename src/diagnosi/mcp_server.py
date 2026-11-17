"""Server MCP della wiki di riparazione — stesso schema di aitho_devops_server.py (S13, SDK `mcp` >= 2).

Espone la wiki e l'agente a qualunque host MCP (Claude Desktop, VS Code, Cursor, Inspector):
    @mcp.tool()      cerca_caso · componente_info · suggerisci_misura   -> VERBI, li chiama il modello
    @mcp.resource()  wiki://{tipo}/{nome}                              -> SOSTANTIVI, pagine per URI
    @mcp.prompt()    diagnosi_guidata                                  -> RICETTA, template lato server

NB (come in S13): datapizza-ai 0.1.0 monta l'SDK MCP 1.x nel suo MCPClient, per il server usiamo l'SDK ufficiale.
I guardrail restano attivi anche quando l'agente è usato da un altro host (suggerisci_misura).

Avvio:  python -m diagnosi.mcp_server               # stdio (Claude Desktop, Inspector)
        MCP_HTTP=1 python -m diagnosi.mcp_server    # Streamable HTTP stateless su :8000/mcp
"""
from __future__ import annotations

import re

from mcp.server import MCPServer

from diagnosi import wiki_tools
from diagnosi.config import WIKI_DIR
from diagnosi.wiki_builder import leggi_front_matter

mcp = MCPServer("Diagnosi schede iPhone/iPad")


def _pagine(tipo: str) -> list:
    return sorted((WIKI_DIR / tipo).glob("*.md")) if (WIKI_DIR / tipo).exists() else []


# ============================== TOOL 1: cerca caso/sintomo ==================
@mcp.tool()
def cerca_caso(sintomo: str, modello: str = "") -> str:
    """Cerca nella wiki di riparazione casi reali, sintomi e guide per un sintomo, es. 'non carica'.

    Args:
        sintomo: descrizione breve, es. "non carica, PC non lo rileva".
        modello: opzionale, es. "iPad Air 4" o "A2316".
    """
    risultati = wiki_tools.cerca(f"{sintomo} {modello}".strip())
    return risultati + "\n\nApri una pagina con la resource wiki://<cartella>/<nome> (es. wiki://sintomi/non-carica-o-alimentazione-instabile)."


# ============================== TOOL 2: scheda componente ===================
@mcp.tool()
def componente_info(sigla: str) -> str:
    """Restituisce la pagina della wiki di un componente, es. 'CD3217', 'Tristar', 'U4001'."""
    s = sigla.lower().strip()
    candidati = [f for f in _pagine("componenti")
                 if s in f.stem or s in f.read_text(encoding="utf-8")[:600].lower()]
    if not candidati:
        return f"Nessuna pagina componente per '{sigla}'. Prova cerca_caso con la sigla."
    return wiki_tools.pagina(f"componenti/{candidati[0].name}")


# ============================== TOOL 3: prossima misura (agente) ============
@mcp.tool()
def suggerisci_misura(contesto: str) -> str:
    """Chiede all'agente diagnostico il prossimo passo: dispositivo, sintomi e misure già fatte -> ipotesi,
    prossima misura con valore atteso, avvertenze di sicurezza e fonti. Usa un LLM (chiave nel .env)."""
    from diagnosi.agent import SessioneDiagnosi            # import qui: gli altri tool non richiedono la chiave

    passo, esito, info = SessioneDiagnosi().chiedi(contesto)
    if esito.bloccato:
        return "Risposta bloccata dai guardrail di sicurezza:\n- " + "\n- ".join(esito.avvisi)
    m = passo.prossima_misura
    righe = [f"Dispositivo: {passo.dispositivo}", f"Riepilogo: {passo.riepilogo}", "Ipotesi:"]
    righe += [f"  {i}. [{ip.probabilita}] {ip.componente} — {ip.motivo}" for i, ip in enumerate(passo.ipotesi, 1)]
    righe += [f"Prossima misura: {m.dove} ({m.modalita})", f"  condizioni: {m.condizioni}",
              f"  valore atteso: {m.valore_atteso}", f"  se diverso: {m.se_diverso}"]
    if passo.avvertenze_sicurezza:
        righe += ["Avvertenze:"] + [f"  - {a}" for a in passo.avvertenze_sicurezza]
    righe += ["Fonti:"] + [f"  - {f}" for f in (passo.fonti or ["nessuna"])]
    return "\n".join(righe)


# ============================== RESOURCE: pagine della wiki =================
@mcp.resource("wiki://{tipo}/{nome}")
def pagina_wiki(tipo: str, nome: str) -> str:
    """Una pagina della wiki per URI, es. wiki://componenti/cd3217 o wiki://dispositivi/ipad-air-4."""
    if not re.fullmatch(r"[a-z]+", tipo) or not re.fullmatch(r"[a-z0-9-]+", nome):
        return "URI non valido."
    return wiki_tools.pagina(f"{tipo}/{nome}.md")


@mcp.resource("wiki://indice")
def indice_wiki() -> str:
    """L'indice della wiki: tutte le pagine con un riassunto di una riga."""
    return wiki_tools.indice()


# ============================== PROMPT: diagnosi guidata ====================
@mcp.prompt()
def diagnosi_guidata(dispositivo: str, sintomo: str) -> str:
    """Template per avviare una diagnosi a livello scheda con la wiki."""
    return (
        f"Sei un tecnico di terzo livello. Al banco c'è un {dispositivo} con questo sintomo: {sintomo}.\n"
        "1. Cerca casi e sintomi simili (cerca_caso).\n"
        "2. Leggi le pagine dei componenti sospetti (componente_info).\n"
        "3. Chiedi il prossimo passo all'agente (suggerisci_misura), riportando tutte le misure già fatte.\n"
        "Una misura alla volta, sempre con condizioni e valore atteso, citando le pagine della wiki."
    )


if __name__ == "__main__":
    import os
    if os.getenv("MCP_HTTP"):
        mcp.run(transport="streamable-http", stateless_http=True)
    else:
        mcp.run()
