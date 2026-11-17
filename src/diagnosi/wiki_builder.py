"""Wiki builder — l'operazione INGEST della LLM Wiki (Karpathy; S08).

Una fonte grezza entra, la wiki si aggiorna in due fasi:
  1. PIANO   — l'LLM legge la fonte e l'indice e decide quali pagine creare o aggiornare (structured_response).
  2. PAGINE  — per ogni pagina, l'LLM riceve la fonte e la pagina esistente e restituisce la versione aggiornata.
Poi, SENZA LLM: il programma scrive il front-matter, rigenera index.md dai front-matter e aggiunge una riga a log.md.

Perché index e log li fa il codice e non l'LLM: sono deterministici, quindi sempre coerenti con i file.
Guardrail: il builder scrive solo in wiki/casi|componenti|sintomi|dispositivi|fonti, con nomi file validi.

Avvio:
  python -m diagnosi.wiki_builder raw/repairwiki/pagine            # tutta la cartella
  python -m diagnosi.wiki_builder raw/repairwiki/pagine --max 3    # solo le prime 3 (per provare)
  python -m diagnosi.wiki_builder raw/casi/mio-caso.md             # un file
  python -m diagnosi.wiki_builder raw/repairwiki/pagine --filtro "charg|power|cd32|tristar"   # solo la carica
"""
from __future__ import annotations

import argparse
import re
from datetime import date
from pathlib import Path
from typing import Literal

import yaml
from pydantic import BaseModel, Field

from diagnosi.config import ROOT, WIKI_DIR, leggi_prompt

CARTELLE = {"caso": "casi", "componente": "componenti", "sintomo": "sintomi",
            "dispositivo": "dispositivi", "tecnica": "tecniche", "strumento": "strumenti", "fonte": "fonti"}
MAX_PAGINE_PER_FONTE = 8
MAX_CARATTERI_FONTE = 15_000
MAX_TOKEN_PAGINA = 8_000            # una pagina lunga può superare 4096 token (bug reale: JSON troncato)
MAX_PAROLE_PAGINA = 1_200


# ----------------------------------------------------------------------------- schemi per l'LLM
class PaginaDaToccare(BaseModel):
    percorso: str = Field(description="Percorso nella wiki, es. 'componenti/cd3217.md' (minuscolo, trattini)")
    tipo: Literal["caso", "componente", "sintomo", "dispositivo", "tecnica", "strumento", "fonte"]
    motivo: str = Field(description="Cosa aggiunge la fonte a questa pagina, in una frase")


class PianoIngest(BaseModel):
    pagine: list[PaginaDaToccare] = Field(description=f"Da 1 a {MAX_PAGINE_PER_FONTE} pagine, le più utili")


class PaginaWiki(BaseModel):
    titolo: str
    riassunto: str = Field(description="Una riga per index.md")
    modelli: list[str] = Field(description="Dispositivi a cui si riferisce, es. ['iPad Air 4']; vuoto se generale")
    contenuto: str = Field(description="Corpo della pagina in Markdown, senza front-matter, con link relativi")
    # campi usati solo dalle pagine 'dispositivo' (riquadro laterale della UI)
    categoria: Literal["phone", "tablet", "nessuna"] = Field(description="phone/tablet per i dispositivi, altrimenti 'nessuna'")
    codici_modello: list[str] = Field(description="Codici tipo A2316 trovati nelle fonti; vuoto se non dispositivo")
    componenti_chiave: list[str] = Field(description="Sigle dei componenti chiave; vuoto se non dispositivo")


# ----------------------------------------------------------------------------- utilità deterministiche
def percorso_valido(percorso: str, tipo: str) -> Path:
    """Guardrail di scrittura: cartella coerente col tipo, nome file pulito, niente '..'."""
    percorso = percorso.strip().removeprefix("wiki/")
    cartella = CARTELLE[tipo]
    nome = Path(percorso).name
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*\.md", nome):
        nome = re.sub(r"[^a-z0-9]+", "-", Path(nome).stem.lower()).strip("-") + ".md"
    if nome == ".md":
        raise ValueError(f"Nome pagina non valido: {percorso!r}")
    return Path(cartella) / nome


def leggi_front_matter(testo: str) -> tuple[dict, str]:
    if testo.startswith("---"):
        _, fm, corpo = testo.split("---", 2)
        return yaml.safe_load(fm) or {}, corpo.lstrip("\n")
    return {}, testo


def scrivi_pagina(wiki_dir: Path, rel: Path, tipo: str, pagina: PaginaWiki, fonte_rel: str, licenza: str | None):
    f = wiki_dir / rel
    vecchio, _ = leggi_front_matter(f.read_text(encoding="utf-8")) if f.exists() else ({}, "")
    fonti = list(dict.fromkeys([*vecchio.get("fonti", []), fonte_rel]))       # unione senza duplicati
    fm = {"titolo": pagina.titolo, "tipo": tipo, "riassunto": pagina.riassunto,
          "modelli": pagina.modelli, "fonti": fonti, "aggiornato": date.today().isoformat()}
    if tipo == "dispositivo":
        # Identità del dispositivo (nome, codici, categoria) dalla scheda esistente: l'LLM NON la può cambiare
        # (bug reale: "iPhone XR" rinominato in "iPhone XR — non carica / nessun boot (Yangtze U3300)").
        componenti = list(dict.fromkeys([*vecchio.get("componenti_chiave", []), *pagina.componenti_chiave]))
        fm |= {"titolo": vecchio.get("titolo", pagina.titolo),
               "modelli": vecchio.get("modelli", pagina.modelli),
               "categoria": vecchio.get("categoria", pagina.categoria),
               "codici_modello": vecchio.get("codici_modello") or pagina.codici_modello,
               "componenti_chiave": componenti, "casi": vecchio.get("casi", [])}
    if licenza or vecchio.get("licenza"):
        fm["licenza"] = licenza or vecchio["licenza"]
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text("---\n" + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False) + "---\n\n"
                 + pagina.contenuto.strip() + "\n", encoding="utf-8")


def rigenera_indice(wiki_dir: Path = WIKI_DIR) -> str:
    """index.md costruito dai front-matter: una riga per pagina, raggruppate per tipo."""
    gruppi: dict[str, list[str]] = {t: [] for t in CARTELLE}
    for f in sorted(wiki_dir.rglob("*.md")):
        if f.name in ("index.md", "log.md"):
            continue
        fm, _ = leggi_front_matter(f.read_text(encoding="utf-8"))
        tipo = fm.get("tipo", "fonte")
        rel = f.relative_to(wiki_dir).as_posix()
        modelli = f" ({', '.join(fm['modelli'])})" if fm.get("modelli") else ""
        gruppi.setdefault(tipo, []).append(f"- [{fm.get('titolo', f.stem)}]({rel}){modelli} — {fm.get('riassunto', '')}")
    righe = ["# Indice della wiki", "", "Generato dal wiki builder: non modificare a mano.", ""]
    for tipo, voci in gruppi.items():
        if voci:
            righe += [f"## {CARTELLE.get(tipo, tipo).capitalize()}", "", *voci, ""]
    testo = "\n".join(righe)
    (wiki_dir / "index.md").write_text(testo, encoding="utf-8")
    return testo


def aggiungi_log(wiki_dir: Path, fonte_rel: str, toccate: list[str]):
    f = wiki_dir / "log.md"
    if not f.exists():
        f.write_text("# Log della wiki\n\n", encoding="utf-8")
    with f.open("a", encoding="utf-8") as out:
        out.write(f"## [{date.today().isoformat()}] ingest | {fonte_rel} | pagine toccate: {', '.join(toccate)}\n")


_SUFFISSI_MODELLO = r"(?!\s*(\d|Plus|Pro|Max|Mini|mini|Air|S\b|e\b|XR|XS|SE))"


def dispositivo_pertinente(titolo_dispositivo: str, titolo_fonte: str) -> bool:
    """Guardrail contro la contaminazione tra modelli: una fonte aggiorna la pagina di un dispositivo
    solo se ne nomina ESATTAMENTE il modello. 'iPad Air' non vale per 'iPad Air 4', 'iPhone 7' non vale
    per una guida su 'iPhone 7 Plus' (bug reale: una guida sul primo iPad Air finita nella pagina dell'Air 4)."""
    patt = r"(?<!\w)" + re.escape(titolo_dispositivo) + _SUFFISSI_MODELLO
    return re.search(patt, titolo_fonte, flags=re.I) is not None


def ripara_link(contenuto: str, rel: Path, wiki_dir: Path) -> tuple[str, int, int]:
    """Controlla ogni link Markdown verso pagine .md: se il file esiste va bene, se esiste una pagina con
    lo stesso nome in un'altra cartella il link viene corretto, altrimenti si toglie il link e resta il testo.
    Ritorna (contenuto, link corretti, link rimossi)."""
    per_nome = {f.name: f for f in wiki_dir.rglob("*.md")}
    corretti = rimossi = 0
    cartella = (wiki_dir / rel).parent

    def sostituisci(m):
        nonlocal corretti, rimossi
        testo, dest = m.group(1), m.group(2)
        if (cartella / dest).resolve().exists():
            return m.group(0)
        trovato = per_nome.get(Path(dest).name)
        if trovato:
            corretti += 1
            nuovo = Path(trovato).resolve().relative_to(wiki_dir.resolve())
            return f"[{testo}]({'../' * (len(rel.parts) - 1)}{nuovo.as_posix()})"
        rimossi += 1
        return testo

    contenuto = re.sub(r"\[([^\]]+)\]\(([^)#\s]+\.md)\)", sostituisci, contenuto)
    return contenuto, corretti, rimossi


def elenco_pagine(wiki_dir: Path) -> str:
    return "\n".join(sorted(f.relative_to(wiki_dir).as_posix() for f in wiki_dir.rglob("*.md")
                            if f.name not in ("index.md", "log.md")))


# ----------------------------------------------------------------------------- ingest
def ingest(client, fonte: Path, wiki_dir: Path = WIKI_DIR, root: Path = ROOT, verbose: bool = True) -> list[str]:
    testo_fonte = fonte.read_text(encoding="utf-8")[:MAX_CARATTERI_FONTE]
    fm_fonte, _ = leggi_front_matter(testo_fonte)
    licenza = fm_fonte.get("licenza")                       # presente sulle pagine di repair.wiki
    titolo_fonte = str(fm_fonte.get("titolo", fonte.stem))
    fonte_rel = fonte.resolve().relative_to(root.resolve()).as_posix()
    sistema = leggi_prompt("wiki_builder") + "\n\nSchema della wiki (AGENTS.md):\n" + (root / "AGENTS.md").read_text(encoding="utf-8")
    indice = (wiki_dir / "index.md").read_text(encoding="utf-8") if (wiki_dir / "index.md").exists() else "(wiki vuota)"

    # FASE 1 — piano. Se fallisce, la fonte si salta e NON va nel log: al prossimo giro verrà ritentata.
    try:
        piano: PianoIngest = client.structured_response(
            input=f"INDICE ATTUALE:\n{indice}\n\nFONTE ({fonte_rel}):\n{testo_fonte}\n\n"
                  "Quali pagine della wiki vanno create o aggiornate con questa fonte?",
            output_cls=PianoIngest, system_prompt=sistema, max_tokens=2048,
        ).structured_data[0]
    except Exception as e:                            # noqa: BLE001
        print(f"  ERRORE nel piano per {fonte_rel}: {type(e).__name__} — fonte saltata")
        return []

    toccate = []
    for voce in piano.pagine[:MAX_PAGINE_PER_FONTE]:
        try:
            rel = percorso_valido(voce.percorso, voce.tipo)
        except (ValueError, KeyError) as e:
            print(f"  scartata: {voce.percorso} ({e})")
            continue
        f = wiki_dir / rel
        if voce.tipo == "caso" and not fonte_rel.startswith("raw/casi"):
            print(f"  scartata: {rel.as_posix()} (una guida non è un caso reale)")
            continue
        if voce.tipo == "dispositivo":
            if not f.exists():
                print(f"  scartata: {rel.as_posix()} (le pagine dispositivo le crea crea_dispositivi.py)")
                continue
            titolo_disp = leggi_front_matter(f.read_text(encoding="utf-8"))[0].get("titolo", "")
            if not fonte_rel.startswith("raw/casi") and not dispositivo_pertinente(titolo_disp, titolo_fonte):
                print(f"  scartata: {rel.as_posix()} (la fonte non parla di '{titolo_disp}')")
                continue
        esistente = f.read_text(encoding="utf-8") if f.exists() else "(pagina nuova)"
        # FASE 2 — una pagina alla volta. Un errore su UNA pagina (es. risposta troncata) non ferma l'ingest.
        try:
            pagina: PaginaWiki = client.structured_response(
                input=f"PAGINA DA SCRIVERE: {rel.as_posix()} (tipo: {voce.tipo})\nMOTIVO: {voce.motivo}\n\n"
                      f"PAGINE ESISTENTI (link solo verso queste o verso pagine del piano):\n{elenco_pagine(wiki_dir)}\n"
                      f"PAGINE DEL PIANO: {', '.join(v.percorso for v in piano.pagine)}\n\n"
                      f"PAGINA ESISTENTE:\n{esistente}\n\nFONTE ({fonte_rel}):\n{testo_fonte}",
                output_cls=PaginaWiki, system_prompt=sistema, max_tokens=MAX_TOKEN_PAGINA,
            ).structured_data[0]
        except Exception as e:                        # noqa: BLE001
            print(f"  ERRORE su {rel.as_posix()}: {type(e).__name__}: {str(e)[:120]} — pagina saltata")
            continue
        scrivi_pagina(wiki_dir, rel, voce.tipo, pagina, fonte_rel, licenza)
        toccate.append(rel.as_posix())
        if verbose:   # (bug di indentazione corretto: prima stampava sempre l'ultimo percorso)
            print(f"  {'aggiornata' if esistente != '(pagina nuova)' else 'creata   '}: {rel.as_posix()}")

    # Link riparati DOPO aver scritto tutte le pagine del piano: così i link tra pagine nuove sono validi.
    for r in toccate:
        f = wiki_dir / r
        fm, corpo = leggi_front_matter(f.read_text(encoding="utf-8"))
        corpo, corretti, rimossi = ripara_link(corpo, Path(r), wiki_dir)
        if corretti or rimossi:
            f.write_text("---\n" + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False) + "---\n\n" + corpo,
                         encoding="utf-8")
            if verbose:
                print(f"  link in {r}: {corretti} corretti, {rimossi} rimossi")

    rigenera_indice(wiki_dir)
    aggiungi_log(wiki_dir, fonte_rel, toccate)
    return toccate


def _fonti_da(percorsi: list[str]) -> list[Path]:
    fonti = []
    for p in map(Path, percorsi):
        fonti += sorted(p.glob("*.md")) if p.is_dir() else [p]
    fonti = [f for f in fonti if not f.name.startswith("LICENSE")]
    # Le schede di modello (solo codici, quasi niente testo) le gestisce crea_dispositivi.py senza LLM.
    schede = [f for f in fonti if "categoria_dispositivo:" in f.read_text(encoding="utf-8")[:800]]
    if schede:
        print(f"Salto {len(schede)} schede di modello (gestite da: python -m diagnosi.crea_dispositivi)")
    return [f for f in fonti if f not in schede]


if __name__ == "__main__":
    from diagnosi.llm import crea_client

    ap = argparse.ArgumentParser(description="Ingest di fonti grezze nella wiki")
    ap.add_argument("percorsi", nargs="+", help="file .md o cartelle in raw/")
    ap.add_argument("--max", type=int, default=None, help="numero massimo di fonti (per provare)")
    ap.add_argument("--rifai", action="store_true",
                    help="rielabora anche le fonti già presenti in wiki/log.md (di default si saltano)")
    ap.add_argument("--filtro", default=None,
                    help="espressione regolare sul nome del file, es. 'charg|power|cd32|tristar'")
    args = ap.parse_args()
    fonti = _fonti_da(args.percorsi)
    if args.filtro:
        fonti = [f for f in fonti if re.search(args.filtro, f.name, re.I)]
    if not args.rifai and (WIKI_DIR / "log.md").exists():
        log = (WIKI_DIR / "log.md").read_text(encoding="utf-8")
        gia_fatte = [f for f in fonti if f"ingest | {f.as_posix()} |" in log]
        if gia_fatte:
            print(f"Salto {len(gia_fatte)} fonti già ingerite (usa --rifai per rielaborarle)")
        fonti = [f for f in fonti if f not in gia_fatte]
    fonti = fonti[: args.max]
    if any("casi_demo" in f.as_posix() for f in fonti):
        print("ATTENZIONE: stai ingerendo un caso della demo (raw/casi_demo). Fallo solo durante la demo 2.")
    client = crea_client()
    for i, fonte in enumerate(fonti, 1):
        print(f"[{i}/{len(fonti)}] {fonte}")
        ingest(client, fonte)
    print(f"\nFatto. Indice: {WIKI_DIR / 'index.md'}")
