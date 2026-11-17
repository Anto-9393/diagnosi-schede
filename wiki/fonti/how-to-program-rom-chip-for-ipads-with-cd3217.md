---
titolo: Fonte — How To Program ROM Chip for iPads with CD3217
tipo: fonte
riassunto: 'Guida (repair.wiki) per ripristinare iPad con CD3217: spesso serve sostituire
  anche la ROM e programmarla con JC V1S Pro (o dump da donor).'
modelli:
- iPad (modelli non specificati nella fonte; file dipende dal modello)
fonti:
- raw/repairwiki/pagine/how-to-program-rom-chip-for-ipads-with-cd3217.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# How To Program ROM Chip for iPads with CD3217 (repair.wiki)

Fonte esterna: [How To Program ROM Chip for iPads with CD3217 — repair.wiki](https://repair.wiki/w/How_To_Program_ROM_Chip_for_iPads_with_CD3217) (CC BY-SA 3.0).

## Problema
Alcuni iPad che usano l’IC controller USB‑C **CD3217** possono andare in **no charge / no boot** o avere problemi di **negoziazione bassa tensione**. La fonte collega l’evento tipicamente a **liquid damage** o **power surge**.

La fonte specifica che:
- **Sostituire solo il CD3217 spesso non basta**, perché l’**IC ROM collegato** risulta spesso **corrotto/danneggiato**.
- **CD3217 e ROM non sono “paired”**: la ROM contiene firmware/dati necessari al funzionamento del CD3217.
- Se il **CD3217 fallisce**, spesso **danneggia anche la ROM**; quindi un nuovo CD3217 **non funzionerà** senza **sostituire o riprogrammare** la ROM.

## Sintomi riportati
1. Con **USB‑C power meter**: si vede solo **5V** e **nessuna negoziazione** (la fonte indica che dovrebbe essere **15V**).
2. Anche dopo aver installato un **nuovo CD3217**, il problema **rimane** (ancora **no charge**).

## Soluzione proposta (high level)
- **Sostituire entrambi**: **CD3217** e **ROM IC**.
- **Programmare la ROM** con **JC V1S Pro**.
- Installare i due chip programmati/sostituiti.
- La fonte riporta che così **la carica viene ripristinata**.

## Passi diagnostici (dalla fonte)
1. **Ispezione visiva**
   - Cercare **corrosione** e **corti** attorno all’area CD3217/ROM.
   - Verificare presenza di **ROM chip bruciato** o **CD3217 bruciato**.
2. **Test tensioni**
   - Usare **USB‑C power meter** o **bench power supply**.
   - Inserire USB‑C e controllare se l’iPad **negozia la tensione corretta**.
   - La fonte considera **5V** come indicatore di errore (CD3217/ROM o problema di negoziazione).

## Passi di riparazione (dalla fonte)
### Step 1 — Rimozione CD3217 e ROM danneggiati
- Dissaldare **sia CD3217** sia l’**IC ROM adiacente**.
- Pulire bene l’area e verificare che le **piazzole/pad** siano integre e utilizzabili.

### Step 2 — Preparazione nuovi chip
- Procurarsi un **nuovo CD3217** da fornitore affidabile.
- Procurarsi una **blank ACE SPI Flash** compatibile per **dimensione** con la board.

### Step 3 — Programmazione ROM (JC V1S Pro)
**Opzione A: JC V1S Pro Server**
- Usare **JC V1S Pro** con il loro **ROM Read/Write Module**.
- Allineare il chip ROM alla **triangolazione** sul programmatore.
- Procedura (come da fonte):
  1. Premere **check** per rilevare lo **SPI chip**.
  2. Selezionare **Open** poi **ServerFile**.
     - Nota: la fonte dice che il **V1S Pro deve essere connesso al WiFi**.
  3. Scegliere il file corrispondente al **modello** dell’iPad.
  4. **Write** e **Confirm write**.

**Opzione B: dump da donor board**
- Prelevare una ROM funzionante da una **donor board** dello **stesso modello**.
- Usare JC V1S Pro per **leggere** e salvare il dump localmente.
- Scrivere sul chip ROM blank selezionando il file del dump.
- La fonte suggerisce di archiviare i dump in una cartella etichettata (esempio: **iPad Pro 11 2nd Gen CD3217 ROM.bin**).

### Step 4 — Reball e installazione CD3217
- **Reball** e saldare il nuovo **CD3217**.
- Verificare che i **passivi** attorno siano integri.

### Step 5 — Installazione ROM programmata
- Saldare la ROM programmata nella posizione originale.
- Pulire con **IPA** e ispezionare i giunti al microscopio.
- Verificare la carica collegando un caricatore che supporti **15V charging**.

## Nota alternativa (solo menzionata)
La fonte cita un metodo alternativo/meno costoso per riprogrammare la ROM CD32 con **Wylie SPI Programmer**, ma i dettagli non sono inclusi nel testo fornito.

## Collegamenti wiki (da usare in diagnostica/riparazione)
- [JC V1S Pro](../strumenti/jc-v1s-pro.md)
- [Wylie SPI Programmer](../strumenti/wylie-spi-programmer.md)
- [CD3217](../componenti/cd3217.md)
- [tecnica: test CD3217 e ricerca corti](../tecniche/test-cd3217-e-ricerca-corti.md)
