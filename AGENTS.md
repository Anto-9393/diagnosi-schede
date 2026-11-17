# AGENTS.md — istruzioni di progetto

Vale per GitHub Copilot, per Claude e per l'agente *wiki builder* del progetto (S12: "vale l'AGENTS.md più
vicino al file su cui si lavora"). È anche lo **schema** della LLM Wiki (Karpathy; S08).

## Il progetto
Assistente diagnostico per riparatori di schede iPhone/iPad. Framework **datapizza-ai 0.1.0**, LLM scelto nel `.env`
(`PROVIDER=openai` con gpt-4o-mini, oppure `anthropic` con Claude), creato solo da `diagnosi.llm.crea_client()`. Conoscenza documentale: **LLM Wiki** al posto del RAG (concordato con il docente).

## Struttura
- `raw/` — fonti grezze. **Non si modificano mai.**
  - `raw/repairwiki/pagine/` pagine di repair.wiki convertite (CC BY-SA 3.0)
  - `raw/casi/` miei casi di riparazione, entrano nella wiki
  - `raw/banco/` i miei attrezzi (modelli esatti): l'agente propone misure fattibili con questi
  - `raw/casi_demo/` casi tenuti FUORI dalla wiki per la demo (A2316): si ingeriscono solo durante la demo 2
- `wiki/` — scritta e mantenuta dal wiki builder. `index.md` (catalogo) e `log.md` (registro).
  - `wiki/casi/` un caso reale per pagina · `wiki/componenti/` una pagina per componente
  - `wiki/sintomi/` una pagina per sintomo · `wiki/fonti/` riassunto di ogni pagina di repair.wiki
  - `wiki/tecniche/` una pagina per tecnica di misura o riparazione (diode mode, ricerca corti...), valida per tutti i modelli
  - `wiki/strumenti/` una pagina per strumento (alimentatore, aria calda, programmatori...), con quelli disponibili sul banco
  - `wiki/dispositivi/` una pagina per dispositivo (es. `ipad-air-4.md`): usata anche dal riquadro laterale della UI
- `src/diagnosi/` codice · `scripts/` punti di avvio · `tests/` pytest · `docs/diario.md` diario

## Schema delle pagine della wiki
Ogni pagina inizia con un front-matter YAML:
```yaml
---
titolo: CD3217 — controller USB-C/PD
tipo: componente            # caso | componente | sintomo | dispositivo | tecnica | strumento | fonte
modelli: [iPad Air 4, iPad Pro 11 2nd Gen]
fonti: [raw/repairwiki/pagine/how-to-program-rom-chip-for-ipads-with-cd3217.md]
aggiornato: 2026-11-15
licenza: CC BY-SA 3.0       # obbligatorio se il contenuto deriva da repair.wiki
---
```
Le pagine `tipo: dispositivo` hanno in più questi campi (li legge l'interfaccia):
```yaml
categoria: tablet                 # phone | tablet → decide l'icona
codici_modello: [A2316]           # solo codici trovati nelle fonti
componenti_chiave: [CD3217]       # sigle con una pagina in componenti/
casi: [casi/ipad-air-4-a2316-non-carica.md]
```
Niente immagini da repair.wiki o da Apple (licenze diverse dal testo, foto di prodotto protette): icona generica o foto proprie.

Regole:
- Link tra pagine in Markdown relativo: `[CD3217](../componenti/cd3217.md)`.
- Ogni affermazione tecnica deve avere una fonte (pagina raw o caso). Se manca, scrivere "da verificare".
- Nomi file: minuscolo, trattini, niente spazi (`non-carica-pc-non-rileva.md`).
- Valori di misura sempre con unità e condizioni (con/senza batteria, acceso/spento, cavo inserito o no).
- Componenti: sempre il CODICE DEL CHIP (universale, es. 343S00264, CD3217B12); la sigla sullo schema solo con
  lo schema da cui viene, es. "X3 (JC Drawing)", "U3100 (schema Apple)": schemi diversi numerano diversamente.
- Ogni ingest aggiunge una riga a `log.md`: `## [AAAA-MM-GG] ingest | <fonte> | pagine toccate: ...`.
- `index.md`: una riga per pagina, raggruppate per tipo: `- [titolo](percorso) — riassunto di una riga`.

## Regole per il codice
- `datapizza-ai==0.1.0`; client sempre con `model=` esplicito (default del client obsoleto).
- Chiavi solo in `.env`, mai nel codice, nei log o nel repo.
- Prompt in `src/diagnosi/prompts/*.md`, non nel codice.
- Codice e commenti in italiano.

## Come verificare
- `pytest` deve passare (i test non chiamano l'LLM).
- `python scripts/passo_strutturato.py` deve stampare un PassoDiagnosi completo.
