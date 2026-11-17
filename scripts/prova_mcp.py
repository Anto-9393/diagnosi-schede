"""Consuma il server MCP del progetto come farebbe un host (Claude Desktop, VS Code…). Come mcp_consume_demo.py (S13).

Avvia il server come sottoprocesso (stdio), elenca le primitive e chiama i tool di sola lettura (niente chiave).
Avvio:  python scripts/prova_mcp.py
        python scripts/prova_mcp.py --agente     # chiama anche suggerisci_misura (usa l'LLM)
"""
import asyncio
import os
import sys
from pathlib import Path

from mcp import Client
from mcp.client.stdio import StdioServerParameters, stdio_client

# Il client MCP avvia il server con un ambiente RIDOTTO: passiamo le variabili e la cartella del progetto in modo esplicito.
ROOT = Path(__file__).resolve().parents[1]
SERVER = StdioServerParameters(command=sys.executable, args=["-m", "diagnosi.mcp_server"], cwd=str(ROOT),
                               env={**os.environ, "PYTHONPATH": str(ROOT / "src")})


async def main():
    async with Client(stdio_client(SERVER)) as c:
        print("TOOL:     ", [t.name for t in (await c.list_tools()).tools])
        print("RESOURCE: ", [str(r.uri_template) for r in (await c.list_resource_templates()).resource_templates])
        print("PROMPT:   ", [p.name for p in (await c.list_prompts()).prompts])

        print("\n--- cerca_caso('non carica, PC non lo rileva', 'iPad Air 4')")
        r = await c.call_tool("cerca_caso", {"sintomo": "non carica, PC non lo rileva", "modello": "iPad Air 4"})
        print(r.content[0].text[:700])

        print("\n--- componente_info('CD3217')")
        r = await c.call_tool("componente_info", {"sigla": "CD3217"})
        print(r.content[0].text[:500])

        print("\n--- resource wiki://dispositivi/ipad-air-4")
        r = await c.read_resource("wiki://dispositivi/ipad-air-4")
        print(r.contents[0].text[:400])

        if "--agente" in sys.argv:
            print("\n--- suggerisci_misura (agente + guardrail, usa l'LLM)")
            r = await c.call_tool("suggerisci_misura", {"contesto": "iPad Air 4 A2316, non carica, PC non lo rileva, "
                                                                   "0.002 A con batteria e cavo, 5.2 V senza batteria"})
            print(r.content[0].text)


asyncio.run(main())
