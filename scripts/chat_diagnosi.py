"""Diagnosi guidata da terminale (NB: lo script NON si chiama diagnosi.py, altrimenti "fa ombra" al pacchetto
`diagnosi` e `import diagnosi` troverebbe lo script: bug reale di shadowing).

Scrivi sintomi e misure, l'agente propone il passo successivo.
La sessione ricorda tutto quello che hai già detto. Scrivi 'esci' per terminare.

Avvio:  python scripts/chat_diagnosi.py            (modello di sviluppo)
        python scripts/chat_diagnosi.py --demo     (modello per la demo)
        Opzioni: --breve (solo la prossima misura)  --rapida (legge al massimo 3 pagine: meno token)
"""
import sys

from diagnosi.agent import SessioneDiagnosi, stampa
from diagnosi.config import MODEL_DEMO, MODEL_DEV

sessione = SessioneDiagnosi(model=MODEL_DEMO if "--demo" in sys.argv else MODEL_DEV,
                            dettaglio="breve" if "--breve" in sys.argv else "completa",
                            lettura="rapida" if "--rapida" in sys.argv else "approfondita")
print(f"Sessione {sessione.id} — modello {sessione.model}, risposta {sessione.dettaglio}, lettura {sessione.lettura}. Descrivi dispositivo, sintomi e misure ('esci' per finire).")
while True:
    try:
        msg = input("\ntu > ").strip()
    except (EOFError, KeyboardInterrupt):
        break
    if msg.lower() in ("esci", "exit", "quit"):
        break
    if msg:
        stampa(*sessione.chiedi(msg))
