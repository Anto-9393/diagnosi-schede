---
titolo: Sintomo — non carica e non rilevato da PC (nessun suono USB)
tipo: sintomo
riassunto: 'Pattern: iPad non carica + PC non rileva (iTunes/3uTools) anche in recovery/DFU;
  spesso riconducibile a Tristar (es. 610A3C) o a charge port/CD3215 (su modelli specifici).'
modelli:
- iPad Pro 10.5
fonti:
- raw/repairwiki/pagine/how-to-repair-ipad-pro-10-5-not-charging-or-not-detected-by-pc.md
- raw/repairwiki/pagine/ipad-7-not-charging.md
- raw/repairwiki/pagine/ipad-pro-11in-1st-gen-not-recognized-by-pc-in-recovery-mode-or-charging-issues.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Pattern riconosciuto
- iPad non carica
- nessuna icona di carica
- il PC non rileva il dispositivo
- nessun suono di riconoscimento USB sul PC
- nessuna comunicazione/dati
- sostituire cavo e alimentatore non risolve
- il dispositivo può comunque accendersi se la batteria ha carica

Fonte: How to Repair iPad Pro 10.5 not charging or not detected by pc — repair.wiki

## Cause possibili (ordine di probabilità)
1. **Tristar — controller USB/charging (U3500 su iPad Pro 10.5, secondo la fonte esistente)**
   - La pagina esistente indica che “in most cases” il guasto è legato a Tristar (U3500).
   - Indizi: consumo anomalo, dock test che non risolve, assenza di rilevazione PC e assenza di negoziazione.
   - Riferimento componente: [Tristar](../componenti/tristar.md)

2. **Dock/porta di ricarica (dock flex) difettosa**
   - La pagina esistente prevede un dock test sostituendo il dock flex con uno noto-good.
   - Se dock test fallisce (continua a non caricare e non essere rilevato) allora la dock non è la causa.
   - (Sigle/part number del dock: da verificare)

3. **Cablaggio/brick non risolutivi**
   - La pagina esistente specifica che sostituire cavo e charging brick non risolve.
   - Quindi, se il pattern è completo, la probabilità di sola causa “accessorio” diminuisce.

## Integrazione diagnostica (recovery/DFU + PC non rileva)
Questa sezione integra la catena diagnostica “non carica” con il pattern aggiuntivo: **iPad non si collega al PC (iTunes/3uTools) anche in recovery/DFU**.

### Punti di fallimento (3 punti principali)
La fonte esterna (iPad Pro 11in 1st Gen) indica che, per questo problema, ci sono **di solito tre punti di fallimento**:
1. **Charge port**
2. **CD3215** (gestione charging da USB-PD)
3. **Tristar 610A3C** (gestione principalmente 5V USB-A)

> Nota compatibilità: la fonte esterna parla di **iPad Pro 11in 1st Gen** e cita **CD3215** e **Tristar 610A3C**. Per iPad Pro 10.5 la pagina esistente cita **Tristar U3500** e non menziona CD3215: da verificare la corrispondenza dei componenti tra modelli.

### Sintomi che aiutano a distinguere Tristar vs CD3215 (da fonte esterna)
- Se l’iPad **può caricare solo con USB-C PD a 15V** ma **non** con USB-A 5V (o viceversa), la fonte esterna indica che:
  - **CD3215** gestisce principalmente la negoziazione/charging da **USB-PD** (15V) e se fallisce potresti riuscire a caricare via **5V USB-A** ma non negoziare/ottenere **15V**.
  - **Tristar 610A3C** gestisce principalmente **5V USB-A** e se fallisce potresti non riuscire a caricare via **5V USB-A**.

### Test rapidi indicati dalla fonte esterna (multimetro in diode mode)
- **CD3215**: “probe the capacitors around the chip” in **diode mode** con:
  - sonda rossa su **ground**
  - sonda nera su ciascun lato del **capacitore** per verificare che **nessun condensatore sia shorted to ground su entrambi i lati**.
- **Tristar 610A3C**: stessa logica di controllo corti sui condensatori attorno al chip.

> Dove si trova Tristar (da fonte esterna): “hidden underneath a part of the shield above the screen FPC connectors in the middle of the board”; serve rimuovere abbastanza shield per accesso.

## Collegamenti utili
- [Tristar](../componenti/tristar.md)
- [CD3217](../componenti/cd3217.md)
- [Tecnica — test Tristar e diagnosi non carica iPhone](../tecniche/test-tristar-e-diagnosi-non-carica-iphone.md)
- [Tecnica — test DCPS e diagnosi Kraken IC](../tecniche/test-dcps-e-diagnosi-kraken-ic.md)
- [alimentatore da banco](../strumenti/alimentatore-da-banco.md)
- [DC power supply (DCPS)](../strumenti/alimentatore-da-banco.md)
