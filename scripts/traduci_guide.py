"""Traduce in anticipo le guide di repair.wiki di un dispositivo (es. prima della demo).

Avvio:  python scripts/traduci_guide.py ipad-air-4       # solo quelle non ancora tradotte
"""
import sys

from diagnosi.dispositivi import guide_del_dispositivo, schede
from diagnosi.traduzioni import file_tradotto, traduci

nome = sys.argv[1] if len(sys.argv) > 1 else "ipad-air-4"
scheda = next((s for s in schede() if s["percorso"] == f"dispositivi/{nome}.md"), None)
if not scheda:
    sys.exit(f"Dispositivo '{nome}' non trovato in wiki/dispositivi/")
for g in guide_del_dispositivo(scheda)["repairwiki"]:
    if file_tradotto(g["percorso"]).exists():
        print(f"= già tradotta: {g['titolo']}")
        continue
    _, tin, tout = traduci(g["percorso"])
    print(f"+ {g['titolo']}  ({tin} token in, {tout} out)")
