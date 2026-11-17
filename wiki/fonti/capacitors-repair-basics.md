---
titolo: Capacitors — Repair Basics (fonte)
tipo: fonte
riassunto: 'Riassunto esterno: funzione dei condensatori, tipi (elettrolitici/ceramici/film/tantalio),
  test (scarica, short in ohmmetro, LCR fuori circuito) e criteri di sostituzione
  (C, tensione, tipo, dimensioni).'
modelli: []
fonti:
- raw/repairwiki/pagine/capacitors-repair-basics.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# Capacitors — Repair Basics (fonte)

> Fonte: [Capacitors - Repair Basics — repair.wiki](https://repair.wiki/w/Capacitors_-_Repair_Basics), CC BY-SA 3.0.

## Funzione del condensatore
- Un condensatore **immagazzina e rilascia energia elettrica** sotto forma di **campo elettrico**.
- È composto da **due piastre conduttive** separate da un **dielettrico**.
- In condizioni ideali tra le piastre c’è **quasi “resistenza infinita”**.
- È paragonabile a una **“batteria molto piccola”** in grado di **caricare e scaricare molto velocemente**.

### Usi tipici (da riparazione)
- **Energy storage**: accumulo di carica per fornire corrente per tempi brevi (es. flash).
- **Voltage smoothing / filtering**: condensatori vicini a **VCC** di IC per stabilizzare l’alimentazione.
- **Filtro passa-basso / passa-alto**: il condensatore **blocca DC** e con **AC** si carica/scarica ciclicamente.
- **Timing circuits (RC)**: costante di tempo RC per ritardi/intervalli (es. circuiti con 555 dove C influenza il periodo).

## Tipi di condensatori
### Elettrolitici (Electrolytic)
- **Alta capacità**; usati per energy storage in alimentazione.
- **Polarizzati**: negativo indicato con **strip/mark**.
- **Valore e tensione nominale** scritti sul componente.

### Ceramici (Ceramic / MLCC)
- Molto comuni, soprattutto **MLCC**.
- **Non polarizzati**.
- Usati per **decoupling**, filtering e timing.
- In genere **meno densità di energia** rispetto agli elettrolitici.
- Spesso in **SMD**; spesso **senza scritte** → valore/tensione da schema.

### Film (Film)
- Usati per filtering, coupling e signal processing.
- **Basso ESR** (Equivalent Series Resistance).
- In genere più grandi, ma con **migliore capacità di sopportare surge/pulse**.
- **Non polarizzati**.
- **Valore e tensione nominale** scritti sul componente.

### Tantalio (Tantalum)
- Variante “dry electrolytic”.
- **Polarizzati**: negativo indicato con **strip/mark**.
- Valore e tensione nominale scritti sul componente.

## Test dei condensatori (fuori circuito)
### Ispezione visiva
- Se presenti **discolorazione** o **rigonfiamento** (soprattutto elettrolitici) → **sostituzione**.

### Scarica prima del test
- Scaricare i terminali cortocircuitandoli con una resistenza **20–100 Ω** finché la tensione sul condensatore scende a **0 V**.

### Test “short” con multimetro in resistenza
- La fonte indica che i condensatori spesso falliscono **in corto**.
- Misurare **fuori circuito** in modalità **resistenza**.
- Lettura tipica: **bassa all’inizio** (il condensatore si carica), poi la resistenza dovrebbe **salire nel tempo**.
- Criterio indicato: idealmente entro **10 s** arrivare a **ordine di kilo-ohm**.

### Test con LCR meter (fuori circuito)
- Se non si trovano corti ma il comportamento del circuito resta anomalo, usare un **LCR meter fuori circuito**.
- LCR misura:
  - **capacitance** (valore reale a varie frequenze)
  - **ESR** (Equivalent Series Resistance)
- La fonte consiglia di confrontare con un condensatore **simile in circuito**, perché l’ESR varia per tipo.
- Criterio qualitativo: **ESR più alto** → prestazioni meno desiderabili.

### Criteri di accettabilità (da fonte)
- **Capacitance** entro **±5%** del valore nominale → accettabile.
- Per **elettrolitici**: fino a **±20%** può essere ancora accettabile.

## Sostituzione: criteri principali
1. **Capacitance (C)**
   - Scegliere **uguale capacità** al difettoso, **soprattutto** se usato in **timing circuits**.
   - Se usato per **voltage smoothing**, una **capacità maggiore** può funzionare.
2. **Voltage rating**
   - Scegliere tensione nominale **uguale o superiore**.
   - In genere una tensione più alta comporta **dimensioni maggiori**.
3. **Tipo**
   - Preferire lo **stesso tipo**.
   - Si può usare un tipo diverso se **la dimensione non è un vincolo**.
4. **Dimensioni fisiche**
   - Preferire **stesse dimensioni**.
   - Se non disponibili e non ci sono vincoli, si può usare un condensatore **più grande o più piccolo** purché rispetti la **tensione nominale**.

## Verifica del riassunto in wiki/fonti
- Il riassunto presente in `wiki/fonti/capacitors-repair-basics.md` rispecchia i contenuti della fonte: **funzione**, **tipi**, **test** (scarica, short in ohmmetro, LCR fuori circuito) e **criteri di sostituzione** (C, tensione, tipo, dimensioni).
- Nota: nella fonte esterna sono presenti anche dettagli su **misura ESR** e criteri numerici (**±5%**, **±20%**, **10 s** per kilo-ohm) che nel riassunto attuale non sono esplicitati (non è una contraddizione, solo dettaglio non riportato nel riassunto).
