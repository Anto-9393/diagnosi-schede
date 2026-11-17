---
titolo: No IMEI / Modem Firmware N/A — assenza servizio cellulare (post backglass)
tipo: sintomo
riassunto: 'No IMEI e/o “Modem Firmware: N/A” dopo riparazione backglass: spesso corto/danno
  BB_PMU e/o mancata alimentazione modem; test *#06# e DCPS, poi verifica corti su
  BB_PMU e ripristino BB-PMU.'
modelli:
- iPhone 13 Pro
- iPhone 14 Pro
- iPhone 14 Pro Max
fonti:
- raw/repairwiki/pagine/how-to-fix-iphone-13-pro-no-power-or-no-imei-after-backglass-repair.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Sintomo
Dopo sostituzione back-glass (o lavorazioni con tool di cracking sulla zona baseband/sandwich logic board), il dispositivo può presentare:

- **“No IMEI”** in **Settings > General > About**
- **“Modem Firmware: N/A”**
- **Nessun servizio cellulare**
- In alcuni casi: **device completamente morto** (nessun power)

La fonte collega questo guasto all’uso del **back-glass cracking tool** in prossimità della **baseband zone** e in particolare alla posizione del **BB_PMU** (molto vicina al back glass).

## Cause probabili (in ordine)
1. **Danno fisico / microcrack o dent da tool** nella zona **BB_PMU** (hairline cracks o deformazione della board)
   - La fonte indica come segni tipici: **hairline cracks su BB_PMU** e **dent** sulla board causato dal punch/tool.
2. **Corto elettrico attorno a BB_PMU**
   - La fonte indica: su **DCPS** si osserva **high current jump** quando si prova ad avviare con **lower board only** → interpretazione: **Short**.
3. **Problema baseband persistente** dopo restore
   - La fonte: se il telefono viene ripristinato con problemi baseband, potrebbe essere necessario **restore di nuovo dopo la riparazione baseband**.

## Test / verifiche
### 1) Ispezione visiva (microscopio)
- Ispeziona la **lower board** sotto microscopio.
- Cerca:
  - **hairline cracks su BB_PMU**
  - **dent** della board dovuto al backglass punch tool

### 2) Diagnostica software (se il telefono si accende)
- **Codice *#06#** → verifica **assenza IMEI**
- **Settings → Modem Firmware** → deve risultare **“N/A”**

### 3) DC Power Supply Test (se sospetti corto / device non stabile)
- **Connetti lower board only**.
- Premi power.
- Osserva su **DCPS**:
  - **High Boot Current jump** → la fonte lo associa a **Short**.

### 4) Short check
- Controlla **intorno a BB_PMU** per corti.

## Note su restore/aggiornamento (da fonte)
- Se il device **non è wiped**: **non restore**.
- Eseguire **solo update**.
- La fonte segnala che il **restore** può portare il device a bloccarsi sulla schermata **Hello/activation**.

## Riparazione (alto livello, collegamenti)
Per la parte hardware la fonte descrive:
1. **Split logic board (sandwich board separation)**
2. **Rimozione BB_PMU** danneggiato (pulizia underfill, flux, lift, ispezione pad, wick + solder)
3. **Reball e installazione BB_PMU** (stencil corretto, allineamento ball, reflow fino ad auto-centraggio)
4. **Riconnessione upper/lower board** e verifica contatti
5. **Test finale** su **DCPS** e verifica IMEI + “Modem Firmware” + test SIM/cellular

Vedi:
- [BB-PMU](../componenti/bb-pmu.md)
- [Sandwich board separation e reball BB_PMU](../tecniche/sandwich-board-separation-e-reball-bb-pmu.md)

## Collegamenti utili
- [BB-PMU](../componenti/bb-pmu.md)
- [Sandwich board separation e reball BB_PMU](../tecniche/sandwich-board-separation-e-reball-bb-pmu.md)
- iPhone 13 Pro — caso correlato
