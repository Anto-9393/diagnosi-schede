"""Percorsi e impostazioni in un posto solo.

Perché un file di config: se un percorso o un modello cambia, lo cambi qui e non in dieci script.
"""
import os
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[2]      # .../diagnosi-schede
load_dotenv(ROOT / ".env")                       # legge ANTHROPIC_API_KEY dal .env (Lab 01)

RAW_DIR = ROOT / "raw"
WIKI_DIR = ROOT / "wiki"
PROMPTS_DIR = Path(__file__).parent / "prompts"

# Provider scelto nel .env: "openai" (chiave del corso, gpt-4o-mini come nelle lezioni) o "anthropic" (Claude).
PROVIDER = os.getenv("PROVIDER", "openai").lower()

_DEFAULT = {
    "openai": ("OPENAI_API_KEY", "gpt-4o-mini", "gpt-4o"),
    "anthropic": ("ANTHROPIC_API_KEY", "claude-haiku-5-5", "claude-sonnet-5-5"),
}
if PROVIDER not in _DEFAULT:
    raise RuntimeError(f"PROVIDER non valido: {PROVIDER!r}. Usa 'openai' o 'anthropic' nel .env.")

_ENV_CHIAVE, _DEV, _DEMO = _DEFAULT[PROVIDER]
MODEL_DEV = os.getenv("MODEL_DEV", _DEV)      # economico: sviluppo
MODEL_DEMO = os.getenv("MODEL_DEMO", _DEMO)   # più capace: demo e valutazione


def api_key() -> str:
    key = os.getenv(_ENV_CHIAVE)
    if not key:
        raise RuntimeError(
            f"{_ENV_CHIAVE} mancante (PROVIDER={PROVIDER}): copia .env.example in .env e inserisci la chiave."
        )
    return key


def leggi_prompt(nome: str) -> str:
    """I prompt stanno in file .md: si leggono e si modificano senza toccare il codice."""
    return (PROMPTS_DIR / f"{nome}.md").read_text(encoding="utf-8")
