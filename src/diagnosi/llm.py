"""Un'unica funzione che crea il client LLM.

datapizza-ai dà la stessa interfaccia a tutti i provider (Lab 01, cella 13): invoke, structured_response,
Agent... funzionano uguali. Per questo il resto del progetto non sa (e non deve sapere) chi c'è dietro:
il provider si sceglie nel .env con PROVIDER=openai oppure PROVIDER=anthropic.
"""
from diagnosi.config import MODEL_DEV, PROVIDER, api_key


def crea_client(model: str = MODEL_DEV, temperature: float | None = 0.2):
    # Temperatura bassa: in diagnosi vogliamo risposte stabili, non creative.
    # Il modello si passa SEMPRE in modo esplicito (i default dei client cambiano o sono vecchi).
    if PROVIDER == "openai":
        from datapizza.clients.openai import OpenAIClient
        return OpenAIClient(api_key=api_key(), model=model, temperature=temperature)
    from datapizza.clients.anthropic import AnthropicClient       # PROVIDER=anthropic (prima creava OpenAI: bug)
    return AnthropicClient(api_key=api_key(), model=model, temperature=temperature)
