"""PASSO 3 — lo stesso input di passo_strutturato.py, ma con l'AGENTE che consulta la wiki.

Salva due file in docs/confronto/:
  - <data>_con-wiki.md   output strutturato (JSON) accanto a quello "senza-wiki"
  - <data>_con-wiki.txt  tutto quello che compare nel terminale (da inviare per la revisione)

Avvio:  python scripts/passo_con_wiki.py
"""
import sys
from datetime import datetime

from diagnosi import registro
from diagnosi.agent import SessioneDiagnosi, stampa
from diagnosi.config import ROOT
from diagnosi.scenari import A2316_PASSO1


class Copia:
    """Scrive sia nel terminale sia in un file (come il comando `tee`)."""
    def __init__(self, *flussi):
        self.flussi = flussi

    def write(self, testo):
        for f in self.flussi:
            f.write(testo)

    def flush(self):
        for f in self.flussi:
            f.flush()


file_txt = ROOT / "docs" / "confronto" / f"{datetime.now():%Y-%m-%d_%H%M}_con-wiki.txt"
file_txt.parent.mkdir(parents=True, exist_ok=True)
with file_txt.open("w", encoding="utf-8") as out:
    terminale = sys.stdout
    sys.stdout = Copia(terminale, out)
    try:
        print("INPUT:\n" + A2316_PASSO1 + "\n")
        sessione = SessioneDiagnosi()
        passo, esito, info = sessione.chiedi(A2316_PASSO1)
        stampa(passo, esito, info)
        print("\nTool usati:", *info["tool"], sep="\n  - ")

        class _Usage:  # registro.salva vuole un oggetto con prompt_tokens / completion_tokens
            prompt_tokens, completion_tokens = info["token_in"], info["token_out"]

        print("\nsalvato in:", registro.salva("con-wiki", A2316_PASSO1, passo, _Usage()))
    except Exception as e:                      # anche l'errore finisce nel file, così si può inviare
        import traceback
        traceback.print_exc(file=sys.stdout)
        raise
    finally:
        sys.stdout = terminale

print(f"\nOutput completo in: {file_txt.relative_to(ROOT)}")
