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
Apri `.env` e incolla la chiave dopo `OPENAI_API_KEY=` (o `ANTHROPIC_API_KEY=` con `PROVIDER=anthropic`), senza spazi né
virgolette. Se l'app dice "OPENAI_API_KEY mancante", la riga è vuota: salva il file e riavvia Streamlit.

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
Due agenti datapizza (`Agent`, `src/diagnosi/agent.py`) con **gli stessi tool e la stessa memoria**, schema diverso:

| Agente | Quando | Risponde con |
|---|---|---|
| **diagnosta** | sintomi e misure ("non carica, 0,002 A con batteria") | `PassoDiagnosi`: riepilogo, ipotesi ordinate, UNA prossima misura con valore su scheda sana, fonti (`PassoBreve` se il tecnico sceglie "solo prossima misura") |
| **istruttore** | "come sostituisco / come programmo / procedura…" | `Procedura`: passi in ordine con attrezzo e controllo, verifica finale, fonti |

Chi risponde lo decide il **codice** (`tipo_richiesta()`, regole testate, zero token), non un LLM: dopo una procedura
la risposta a una domanda dell'agente ("sto usando A2316") resta procedura; misure e sintomi tornano alla diagnosi.
Gli agenti leggono da soli indice e pagine della wiki e ricordano la sessione con una **memoria compatta**
(cosa si è detto, non il testo delle pagine: da 74.752 a ~14.000 token al secondo turno).

**Nomi precisi** (`src/diagnosi/sigle.py`): nelle risposte una sigla di schema da sola ("X3") diventa
"343S00264-A0 (X3 su JC Drawing)", con le corrispondenze lette dalle pagine consultate (es. "X3 = 343S00264-A0").

### Guardrail (`src/diagnosi/guardrails.py`, deterministici)
1. **Sicurezza elettrica**: blocca istruzioni pericolose (cortocircuitare la batteria, alimentare senza limite di
   corrente, scaldare vicino alla batteria); aggiunge l'avvertenza sul limite di corrente; segnala tensioni oltre la cella Li-ion.
2. **Valori impossibili**: tensioni oltre i 20 V (USB-PD).
3. **Sigle non verificate**: sigle di componenti che non compaiono nelle pagine lette.
4. **Fonti**: solo pagine lette davvero; senza fonti la risposta è marcata "da verificare".
Per le **procedure** (`controlla_procedura`): gli stessi controlli su tutti i passi, più "aria calda o saldatura senza
batteria scollegata" → avviso in testa.
Inoltre: lettura solo dentro `wiki/`, scrittura del builder solo nelle cartelle della wiki, niente contaminazione tra modelli.

### Osservabilità
Ogni passo stampa il riepilogo di `ContextTracing` (token, durata) e aggiunge una riga JSON a `docs/log/sessioni.jsonl`
(agente usato, tool chiamati, pagine usate, token, latenza, avvisi dei guardrail, testo della risposta).

## Interfaccia (Streamlit)
```powershell
streamlit run app/streamlit_app.py
```
Chat con gli agenti; a sinistra la scheda del dispositivo (scelto dal menu o riconosciuto dal testo, es. "A2316"):
foto, codici modello, componenti, casi, pagine della wiki consultate. Scelte del tecnico: risposta completa o solo
prossima misura, lettura della wiki approfondita o rapida (meno token). Timer dal vivo; sotto ogni risposta durata,
token e letture. Le risposte di diagnosi seguono il ragionamento: riepilogo → ipotesi → prossima misura.

**Solo il modello = elenco delle guide, senza LLM (0 token):** se il primo messaggio è solo "iPad Air 4" o "A2316"
(o se chiedi "guide …"), l'app elenca le pagine della wiki e le guide di repair.wiki di quel modello.

Foto dei dispositivi (facoltative) in `app/immagini/<nome-pagina>.jpg`, con i crediti in `app/immagini/CREDITI.md`.
Per scaricarle da Wikipedia/Wikimedia Commons **solo con licenza libera** (CC BY, CC BY-SA, CC0, pubblico dominio):
```powershell
python scripts/scarica_immagini.py --prova          # mostra cosa troverebbe (+ giusta, ~ modello simile, x scartata)
python scripts/scarica_immagini.py --anche-simili   # scarica (anche le foto del modello base) e scrive i crediti
```
Consigliato un **token personale Wikimedia** (OAuth 2.0 owner-only, gratuito: da ~500 a ~5.000 richieste/ora,
istruzioni in testa allo script): `WIKIMEDIA_TOKEN` e `WIKIMEDIA_CONTATTO` nel `.env`. Lo script scarta loghi e foto
di altri modelli; oggi 76 dispositivi su 79 hanno un'immagine.

## Server MCP (anche per Claude Desktop)
```powershell
python -m diagnosi.mcp_server                 # stdio
$env:MCP_HTTP=1; python -m diagnosi.mcp_server  # HTTP stateless su http://localhost:8000/mcp
```
Tool: `cerca_caso(sintomo, modello)`, `componente_info(sigla)`, `suggerisci_misura(contesto)` (agente + guardrail).
Resource: `wiki://indice`, `wiki://{tipo}/{nome}`. Prompt: `diagnosi_guidata`.
Prova come farebbe un host (stdio): `python scripts/prova_mcp.py` (`--agente` per chiamare anche l'agente).
Per Claude Desktop: `materiali/claude_desktop_config.example.json`.

### Dashboard Grafana (stack "ops" di S11: Prometheus + Grafana)
Serve Docker Desktop acceso. Il modo più semplice: doppio clic su **`avvia_osservabilita.bat`**. A mano, due terminali:
```powershell
python -m diagnosi.metriche                      # 1) exporter: http://localhost:8001/metrics (legge docs/log/sessioni.jsonl)
cd observability ; docker compose up -d          # 2) Prometheus (:9090) + Grafana (:3000)
```
Grafana: http://localhost:3000 → dashboard **"Diagnosi schede — agente e guardrail"** (senza login).
Numeri (risposte, costo totale e medio in €, token medi, tempo mediano, risposte bloccate), grafici a gradini
"ogni risposta" (token, secondi, euro), spesa e token cumulati, torte "chi ha risposto" (diagnosi/procedura),
"cosa legge l'agente" e "lettura della wiki", avvisi dei guardrail per tipo. Prezzi veri del modello nel `.env`:
`PREZZO_INPUT_USD_1M`, `PREZZO_CACHE_USD_1M`, `PREZZO_OUTPUT_USD_1M` (default: listino gpt-4o-mini del corso) e il cambio `CAMBIO_USD_EUR` (euro per 1 dollaro): la dashboard mostra i costi in euro.
Per fermare: `docker compose down`.

### Salute della wiki
```powershell
python -m diagnosi.lint_wiki            # link rotti, pagine senza fonti, orfane
python -m diagnosi.lint_wiki --ripara   # corregge i link rotti
```

## Struttura
| Cartella | Contenuto |
|---|---|
| `raw/` | fonti grezze, non modificate (repair.wiki, miei casi; `casi_demo/` fuori dalla wiki) |
| `wiki/` | la LLM Wiki: `index.md`, `log.md`, `dispositivi/`, `casi/`, `componenti/`, `sintomi/`, `tecniche/`, `strumenti/`, `fonti/` |
| `src/diagnosi/` | codice: config, client, schemi, prompt, agenti, guardrail, nomi precisi, tool della wiki, server MCP, metriche |
| `observability/` | Prometheus + Grafana (docker compose, dashboard già pronta) |
| `scripts/` | punti di avvio |
| `app/` | interfaccia Streamlit |
| `materiali/` | configurazione d'esempio per Claude Desktop |
| `docs/` | diario, confronti salvati, log delle sessioni |
| `tests/` | pytest |

## Fonti e licenze
Contenuti da repair.wiki: CC BY-SA 3.0, attribuzione in ogni file (vedi `raw/repairwiki/LICENSE-CC-BY-SA-3.0.md`).
Immagini dei dispositivi: Wikimedia Commons, solo licenze libere, autore e licenza in `app/immagini/CREDITI.md`.
