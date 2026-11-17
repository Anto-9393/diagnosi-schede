"""Salva ogni risposta in docs/confronto/: input, modello, token e output completo (JSON).

Perché: per confrontare "senza wiki" e "con wiki" servono risultati salvati, non ricordi.
È lo stesso principio delle gold run di S08/S11: stessa domanda, varianti diverse, risultati registrati.
"""
from datetime import datetime

from pydantic import BaseModel

from diagnosi.config import MODEL_DEV, PROVIDER, ROOT

CONFRONTO_DIR = ROOT / "docs" / "confronto"


def salva(variante: str, situazione: str, passo: BaseModel, usage, model: str = MODEL_DEV) -> str:
    CONFRONTO_DIR.mkdir(parents=True, exist_ok=True)
    ora = datetime.now()
    f = CONFRONTO_DIR / f"{ora:%Y-%m-%d_%H%M}_{variante}.md"
    f.write_text(
        "---\n"
        f"variante: {variante}\n"
        f"data: {ora:%Y-%m-%d %H:%M}\n"
        f"provider: {PROVIDER}\n"
        f"modello: {model}\n"
        f"token: {usage.prompt_tokens} in / {usage.completion_tokens} out\n"
        "---\n\n"
        f"## Input\n\n```\n{situazione}\n```\n\n"
        f"## Output\n\n```json\n{passo.model_dump_json(indent=2)}\n```\n\n"
        "## Valutazione del tecnico\n- \n",
        encoding="utf-8",
    )
    return str(f.relative_to(ROOT))
