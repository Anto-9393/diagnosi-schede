# Diagnosi schede — assistente per riparatori

Assistente che guida la diagnosi a livello scheda di iPhone e iPad
(sintomo → misura → valore atteso → passo successivo), citando le fonti.
Progetto personale AITHO GenAI Academy · framework **datapizza-ai v0.1.0** · LLM a scelta: **OpenAI** (gpt-4o-mini, come nel corso) o **Claude**.

## Conoscenza documentale
Al posto di una pipeline RAG il sistema usa una **LLM Wiki** (schema di Karpathy, S08),
come concordato con il docente: un LLM scrive e mantiene pagine Markdown in `wiki/`
(casi, componenti, sintomi, fonti) e l'agente le consulta con indice, link e ricerca testuale.
Regole della wiki: [AGENTS.md](AGENTS.md).

## Installazione (Windows, Python 3.11+)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -e .
copy .env.example .env      # poi scegli PROVIDER (openai/anthropic) e inserisci la chiave relativa
```

## Avvio
```powershell
python scripts/primo_prompt.py        # baseline: domanda secca, niente prompt né wiki
python scripts/passo_strutturato.py   # prompt da tecnico + risposta strutturata PassoDiagnosi
pytest                                # test (non usano l'LLM né la chiave)
```

### Importare le pagine di repair.wiki
1. Da https://repair.wiki/w/Special:Export esporta le categorie *Apple Phones*, *Apple Tablets*, *Repair Basics* e *Repair guide* (tenendo solo le guide iPhone/iPad)
   (solo revisione attuale) e salva i file `.xml` in `raw/repairwiki/`.
2. `python -m diagnosi.import_repairwiki raw/repairwiki/*.xml`

### Costruire la wiki (ingest)
```powershell
python -m diagnosi.crea_dispositivi                          # pagine dispositivi/ dalle schede di modello (senza LLM)
python -m diagnosi.wiki_builder raw/repairwiki/pagine --max 3   # prova su 3 pagine
python -m diagnosi.wiki_builder raw/repairwiki/pagine --filtro "charg|power|cd32|tristar"  # solo guide sulla carica
python -m diagnosi.wiki_builder raw/repairwiki/pagine           # tutte
python -m diagnosi.wiki_builder raw/casi                        # i miei casi
```
Il builder crea/aggiorna le pagine in `wiki/`, rigenera `wiki/index.md` e aggiunge una riga a `wiki/log.md`.
`raw/casi_demo/` (A2316) si ingerisce **solo durante la demo**, per non contaminare la diagnosi guidata.

## Diagnosi guidata (agente)
```powershell
python scripts/chat_diagnosi.py           # sessione interattiva: scrivi sintomi e misure, 'esci' per finire
python scripts/chat_diagnosi.py --demo    # stessa cosa con il modello per la demo
python scripts/passo_con_wiki.py     # A2316, passo 1, con wiki: si salva in docs/confronto/ accanto a "senza-wiki"
```
L'agente (datapizza `Agent`, `src/diagnosi/agent.py`) legge da solo indice e pagine della wiki, ricorda le misure
della sessione e risponde con un `PassoDiagnosi` strutturato con le fonti.

### Guardrail (`src/diagnosi/guardrails.py`, deterministici)
1. **Sicurezza elettrica**: blocca istruzioni pericolose (cortocircuitare la batteria, alimentare senza limite di
   corrente, scaldare vicino alla batteria); aggiunge l'avvertenza sul limite di corrente; segnala tensioni oltre la cella Li-ion.
2. **Valori impossibili**: tensioni oltre i 20 V (USB-PD).
3. **Sigle non verificate**: sigle di componenti che non compaiono nelle pagine lette.
4. **Fonti**: solo pagine lette davvero; senza fonti la risposta è marcata "da verificare".
Inoltre: lettura solo dentro `wiki/`, scrittura del builder solo nelle cartelle della wiki, niente contaminazione tra modelli.

### Osservabilità
Ogni passo stampa il riepilogo di `ContextTracing` (token, durata) e aggiunge una riga JSON a `docs/log/sessioni.jsonl`
(tool chiamati, pagine usate, token, latenza, avvisi dei guardrail).

## Interfaccia (Streamlit)
```powershell
streamlit run app/streamlit_app.py
```
Chat con l'agente; a sinistra la scheda del dispositivo riconosciuto (da `wiki/dispositivi/`: icona, codici modello,
componenti, casi) e le pagine della wiki consultate. Sotto ogni risposta: durata, token e numero di tool usati.

## Server MCP (anche per Claude Desktop)
```powershell
python -m diagnosi.mcp_server                 # stdio
$env:MCP_HTTP=1; python -m diagnosi.mcp_server  # HTTP stateless su http://localhost:8000/mcp
```
Tool: `cerca_caso(sintomo, modello)`, `componente_info(sigla)`, `suggerisci_misura(contesto)` (agente + guardrail).
Resource: `wiki://indice`, `wiki://{tipo}/{nome}`. Prompt: `diagnosi_guidata`.
Per Claude Desktop: `materiali/claude_desktop_config.example.json`.

### Salute della wiki
```powershell
python -m diagnosi.lint_wiki            # link rotti, pagine senza fonti, orfane
python -m diagnosi.lint_wiki --ripara   # corregge i link rotti
```

## Struttura
| Cartella | Contenuto |
|---|---|
| `raw/` | fonti grezze, non modificate (repair.wiki, miei casi; `casi_demo/` fuori dalla wiki) |
| `wiki/` | la LLM Wiki: `index.md`, `log.md`, `casi/`, `componenti/`, `sintomi/`, `fonti/` |
| `src/diagnosi/` | codice: config, client, schemi, prompt, importatore, tool della wiki |
| `scripts/` | punti di avvio |
| `app/` | interfaccia Streamlit |
| `materiali/` | configurazione d'esempio per Claude Desktop |
| `docs/` | diario, confronti salvati, log delle sessioni |
| `tests/` | pytest |

## Fonti e licenze
Contenuti da repair.wiki: CC BY-SA 3.0, attribuzione in ogni file (vedi `raw/repairwiki/LICENSE-CC-BY-SA-3.0.md`).
