"""PASSO 1 — la baseline: una domanda secca, nessun prompt di sistema, nessuna wiki. (Lab 01)

Tieni l'output: è il "prima" da mostrare nello speech, da confrontare con le versioni successive.
Avvio:  python scripts/primo_prompt.py
"""
from diagnosi.llm import crea_client

client = crea_client()

result = client.invoke(
    "iPad Air 4 A2316, dopo un versamento di caffè non carica e il PC non lo rileva. "
    "Quali sono le prime 3 misure da fare sulla scheda?"
)

print(result.text)
print("\n--- token in/out:", result.usage.prompt_tokens, "/", result.usage.completion_tokens)
