# Confronto: stesso input (A2316, passo 1), tre configurazioni

Input: `src/diagnosi/scenari.py` → `A2316_PASSO1`. Modello: gpt-5.4-nano (OpenAI). Diagnosi reale (15 nov): CD3217B12 (X5 su JC) n.1.

| | Senza wiki (16 nov) | Demo 1: wiki + revisione tecnico (17 nov 19:12) | Demo 2: + caso A2316 (17 nov 19:16) |
|---|---|---|---|
| Sospettato n.1 | generico "PMIC / Uxxxx" | CD3217 [alta] | **CD3217B12 (X5) [alta]** |
| Prossima misura | D+/D− in ohm (già misurate in diode mode) | iniezione bassa tensione + termocamera (cerca un corto) | **X1548–X1550 con e senza batteria** (misura decisiva) |
| ROM | — | — | 8N040, abbinata o da riprogrammare |
| Ipotesi "corto" | — | 2ª [media] | assente |
| Tristar (assente su Air 4) | — | assente (prima della revisione: 2ª ipotesi) | assente |
| Fonti citate | 0 | 5 | 3 (incluso il caso) |
| Tool chiamati | 0 | 9 | 6 |
| Token in / out | 1.164 / 985 | 46.213 / 1.381 | 43.706 / 1.147 |
| Tempo | pochi s | 15,9 s | 15,1 s |

## Cosa cambia tra le colonne
- **Senza → Demo 1:** la wiki porta il componente giusto e le fonti. Due correzioni a mano del tecnico (pagina CD3217 e pagina iPad Air 4) eliminano il Tristar e chiariscono il ruolo del CD3217.
- **Demo 1 → Demo 2:** il caso reale porta la regola "con/senza batteria" (modalità dead battery) e la misura su X1548, togliendo l'ipotesi del corto.

## Limiti osservati
- Demo 2: il "valore atteso" riporta i valori del GUASTO (0,026–0,186 V) invece di quelli di una scheda sana.
- Ingest del caso: i dati di X3 (343S00264) sono finiti nella pagina 343S00235 (iPad Pro 12.9), segnalati dal builder come "da verificare".
- Costo: con la wiki l'input passa da ~1k a ~45k token per diagnosi (l'agente legge 6–10 pagine).

## Guardrail
- Sulla risposta di Demo 1 il guardrail aggiunto il 17 nov segnala: "Iniezione di tensione con la batteria collegata: SCOLLEGA la batteria".

## Ottimizzazione dei token (17 nov, 19:47) — stessa domanda della Demo 2
| | Prima | Dopo |
|---|---|---|
| Token in ingresso | 43.706 | **28.199 (−35%)**, di cui 9.216 in cache (scontati) |
| Token in uscita | 1.147 | 1.224 |
| Tempo | 15,1 s | 13,8 s |
| Diagnosi | CD3217B12 [alta], X1548 con/senza batteria, ROM 8N040 | **uguale** |

Cosa è cambiato: indice compatto per l'agente (senza Dispositivi e Fonti: ~10.700 → ~4.900 token, ripagati a ogni passo),
memoria compatta tra i turni (non ripete il testo delle pagine), istruzione a leggere più pagine nello stesso passo.
Perché funziona: un agente rimanda all'LLM tutta la conversazione a OGNI passo → ciò che legge presto si paga più volte.
