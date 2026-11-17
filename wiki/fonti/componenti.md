---
titolo: fonti/componenti.md
tipo: fonte
riassunto: 'Caso demo interno iPad Air 4 A2316: corrosione porta USB-C; X3=343S00264
  scalda col cavo ma non carica/PC non rileva; sospetto CD3217B12 (X5) e/o ROM CD3217
  (8N040).'
modelli:
- iPad Air 4 A2316
fonti:
- raw/repairwiki/pagine/iphone-15-pro-max-dead-and-not-charging.md
- raw/casi_demo/ipad-air-4-a2316-non-carica.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# Fonte → componenti/sintomi (iPad Air 4 Wi‑Fi A2316)

> Nota progetto: questa è una **fonte demo interna** (non repair.wiki esterna). **Non** crea pagine in `fonti/`; serve solo per aggiornare pagine esistenti di **componenti**, **sintomi** e **casi**.

## Contesto del caso (da fonte)
- Dispositivo: **iPad Air 4 Wi‑Fi (A2316)**.
- Evento: **caffè versato** → spento e **non caricava**.
- Dopo pulizia con IPA della porta: ha caricato per ore (fino a ~**58–67%**), **senza scaldare**.
- Poi: smette di caricare, **nessun fulmine**, **il PC non lo rileva**.
- Da spento: inserendo il cavo si accende, ma **non carica**.
- Con batteria all’1%: inserire il cavo lo faceva **riavviare**.

## Misure chiave (da fonte)
### Porta USB‑C (Mechanic T‑824, diode mode)
- **VBUS** (pin 4/9/16/21): letture **0.00 → lato A 0.69/0.38 → di nuovo tutti 0.00** (instabile; indicazione di problema/instabilità lato A).
- **CC1/CC2**: **0.53 / 0.63** (stabili).
- **D+/D− lato A** (6/7): **0.71 → 1.00 → 0.70** (instabile).
- **RX1+ (23)**: **OL → 0.00 → OL → 0.00** (ponte verso GND pin 24 che va e viene).

**Conclusione fonte:** corrosione attiva nel connettore USB‑C vecchio.

### Alimentazione / comportamento con batteria
- Senza batteria, USB da AiXun: **5.2 V, 0.11–0.20 A**, resta a 5 V (**nessuna negoziazione PD**).
- Con batteria e iPad acceso, cavo inserito: **0.002 A** → non prende corrente dall’USB.
- Batteria: **3.66 V** → scesa a ~**2.9–3.1 V**, poi ricaricata dal banco (4.2 V, ~2–3 A) fino a **3.8 V / 45%**.

### IC di ricarica / power path (JC Drawing)
- **NET205**: VBUS dal connettore flat → **X5 = CD3217B12** (controller USB‑C/PD TI).
- **X1548 / X1549 / X1550**: uscita CD3217 → ingresso **X3**.
  - Con batteria + cavo: **0.026–0.186 V** (il CD3217 non chiude il passaggio verso X3).
- **X3 = 343S00264‑A0** (IC di ricarica; *non* 343S00394):
  - **scalda subito** con cavo inserito (goccia di IPA evapora in fretta);
  - senza cavo si asciuga lentamente.
- Bobine **X2020 / X2021** collegate a X3 (non misurabili a puntale).
- **ROM del CD3217**: marcatura **8N040**.
  - Su JC Drawing è il chip piccolo accanto a X5, siglato **X7**.
  - Fonte: la ROM va in coppia col CD3217; se si sostituisce il CD3217 da donor va trasferita la ROM dello **stesso donor** oppure riprogrammata (Wylie).

### Termocamera
- CPU ~**60 °C** da accesa e aperta = normale.
- **Nessun punto caldo sul CD3217** (nota fonte).

## Diagnosi (da fonte)
1. **X5 CD3217B12** — sospetto n.1:
   - con batteria non fa passare VBUS verso X3;
   - spiega **nessun fulmine** e **PC non rileva** (carica + dati).
2. Alimentazioni/passivi intorno al CD3217 corrosi dal caffè — **da verificare prima di toccare il chip**.
3. **ROM 8N040 (X7 su JC)** — meno probabile (ha caricato dopo pulizia), ma da considerare:
   - sostituire insieme al CD3217 da scheda donatrice **A2316** oppure riprogrammare.

## Interventi fatti (da fonte)
- 25 ott: pulizia porta con IPA → carica per ore, poi smette.
- ~15 nov: **X3 sostituito** con **343S00264** nuovo → non carica.
- 15 nov: **flat/connettore USB‑C sostituito** → non carica.

## Aggiornamenti da applicare alle pagine esistenti

### 1) Pagina caso
- Aggiornare: [casi/ipad-air-4-a2316-non-carica.md](../casi/ipad-air-4-a2316-non-carica.md)
  - Inserire i dati: **X3=343S00264‑A0 scalda col cavo**, ma con batteria + cavo **X1548/X1549/X1550 = 0.026–0.186 V** e **corrente USB ~0.002 A**.
  - Inserire sospetto principale: **CD3217B12 (X5) + ROM 8N040 (X7)**.
  - Inserire evidenza porta: **RX1+ (23) che va/torna da 0.00** (ponte verso GND pin 24) e instabilità D+/D− lato A.

### 2) Pagina componente — CD3217
- Aggiornare: [componenti/cd3217.md](../componenti/cd3217.md)
  - Aggiungere sezione/caso: su **iPad Air 4 A2316** (X5 = **CD3217B12**) con batteria + cavo:
    - VBUS non passa verso X3 (misure **0.026–0.186 V** su X1548/1549/1550).
    - Sintomi correlati: **nessun fulmine**, **PC non rileva**, **0.002 A**.
  - Nota: fonte dice “nessun punto caldo sul CD3217” (quindi heating non è sempre indicativo).

### 3) Pagina componente — IC di ricarica 343S00264
- Aggiornare: [componenti/343s00235.md](../componenti/343s00235.md)
  - **Contraddizione/da verificare:** la fonte identifica **X3 = 343S00264‑A0**, ma la pagina componente esistente è per **343S00235**.
  - Azione: o si crea/si collega correttamente la pagina del componente **343S00264** (se esiste/da creare) oppure si segnala in [casi/ipad-air-4-a2316-non-carica.md](../casi/ipad-air-4-a2316-non-carica.md) che il caso riguarda 343S00264 e non 343S00235.

### 4) Pagina sintomo
- Valutare aggiornamento/creazione (da verificare compatibilità):
  - [sintomi/non-carica-o-non-rilevato-da-pc.md](../sintomi/non-carica-o-non-rilevato-da-pc.md)
  - La fonte mostra **PC non rileva** + **non carica** + **0.002 A** con batteria e cavo.
  - Se la pagina sintomo esistente copre già “non rilevato da PC”, aggiungere i dettagli specifici del caso (CD3217B12 non chiude passaggio verso X3).

## Dati utili per future misure (da fonte)
- Misurare sempre in condizioni ripetibili:
  - **con/senza batteria**
  - **iPad acceso/spento**
  - **cavo inserito**
- Nel caso:
  - senza batteria: USB resta a **5.2 V** e assorbe **0.11–0.20 A** (nessuna negoziazione PD).
  - con batteria: assorbimento USB quasi nullo (**0.002 A**) e passaggio verso X3 non avviene.

## Strumenti usati (da fonte)
- Mechanic T‑824 SE (diode mode)
- Alimentatore da banco AiXun
- Multimetro
- Termocamera MEGA‑IDEA
- Microscopio
- JC Drawing
