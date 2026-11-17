"""PASSO 2 — prompt da tecnico + risposta strutturata PassoDiagnosi. (Lab 02, cella 22)

Differenze rispetto a primo_prompt.py:
  1. system_prompt: il ruolo e le regole di lavoro stanno in prompts/tecnico.md
  2. structured_response(output_cls=PassoDiagnosi): il modello compila uno schema validato
  3. in input diamo sintomi E misure già fatte, come al banco
Avvio:  python scripts/passo_strutturato.py
Ogni esecuzione viene salvata in docs/confronto/ (variante "senza-wiki").
"""
from diagnosi import registro
from diagnosi.config import leggi_prompt
from diagnosi.llm import crea_client
from diagnosi.scenari import A2316_PASSO1
from diagnosi.schemas import PassoDiagnosi

SITUAZIONE = A2316_PASSO1

client = crea_client()
result = client.structured_response(
    input=SITUAZIONE,
    output_cls=PassoDiagnosi,
    system_prompt=leggi_prompt("tecnico"),
    max_tokens=4096,            # il default di datapizza (2048) può troncare uno schema ricco
)

passo: PassoDiagnosi = result.structured_data[0]   # come ticket = result_struct.structured_data[0]

print("DISPOSITIVO:", passo.dispositivo)
print("RIEPILOGO:", passo.riepilogo, "\n")
print("IPOTESI:")
for i, ip in enumerate(passo.ipotesi, 1):
    print(f"  {i}. [{ip.probabilita}] {ip.componente} — {ip.motivo}")
m = passo.prossima_misura
print(f"\nPROSSIMA MISURA: {m.dove} ({m.modalita})")
print(f"  condizioni:    {m.condizioni}")
print(f"  valore atteso: {m.valore_atteso}")
print(f"  se diverso:    {m.se_diverso}")
if passo.avvertenze_sicurezza:
    print("\nSICUREZZA:", *passo.avvertenze_sicurezza, sep="\n  - ")
if passo.domande_al_tecnico:
    print("\nDOMANDE:", *passo.domande_al_tecnico, sep="\n  - ")
print("\nFONTI:", passo.fonti or "nessuna (ancora niente wiki: la risposta viene solo dal modello)")
print("\n--- token in/out:", result.usage.prompt_tokens, "/", result.usage.completion_tokens)
print("salvato in:", registro.salva("senza-wiki", SITUAZIONE, passo, result.usage))
