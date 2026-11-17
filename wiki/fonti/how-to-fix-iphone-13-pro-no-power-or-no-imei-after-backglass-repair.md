---
titolo: Fonte — How To Fix iPhone 13 Pro No Power or No IMEI After Backglass Repair
tipo: fonte
riassunto: 'Dopo sostituzione back-glass su iPhone 13 Pro, possono comparire “No IMEI”,
  “Modem Firmware: N/A” o dispositivo morto: spesso per danni/crepe o corto nell’area
  BB_PMU; procedura con ispezione, test DCPS e reball/sostituzione BB_PMU.'
modelli:
- iPhone 13 Pro
- iPhone 14 Pro
- iPhone 14 Pro Max
fonti:
- raw/repairwiki/pagine/how-to-fix-iphone-13-pro-no-power-or-no-imei-after-backglass-repair.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Scopo della fonte
La fonte descrive un guasto che diventa sempre più comune dopo la sostituzione del back-glass: il dispositivo può risultare:
- **No IMEI**
- **No modem firmware** (es. “Modem Firmware: N/A”)
- **Nessun servizio cellulare**
- **Completamente morto (no power)**

La causa indicata è l’uso di un **back-glass cracking tool** nella zona del **baseband/sandwich logic board**, dove la **PMU (BB_PMU)** è molto vicina al back-glass.

## Sintomi riportati
- In **Impostazioni > Generale > Info**: **“No IMEI”**
- In **Modem Firmware**: **“N/A”**
- **Salto di corrente elevato** su **DCPS**
- Se il telefono è stato **ripristinato** con problemi baseband: dopo aver risolto il baseband potrebbe essere necessario **ripristinare di nuovo**
- Se il telefono **non è stato cancellato (non wiped)**: la fonte dice di **non fare Restore**, ma solo **Update** (il Restore può portare a blocco su schermata Hello/attivazione)
- **Full dead device** (nessun avvio)

## Diagnosi (passi)
### 1) Ispezione visiva (microscopio)
Ispezionare la **lower board** sotto microscopio e cercare:
- **Hairline cracks** su **BB_PMU**
- **Dent** sulla scheda causato dal punch/tool del back-glass

> La fonte sottolinea che questo è **molto comune** su **iPhone 13 Pro / 14 Pro / Pro Max** perché la PMU è vicina al back-glass.

### 2) Diagnosi software (se il telefono si accende)
- Comando **`*#06#`** → **No IMEI**
- **Impostazioni → Modem Firmware** → **N/A**

### 3) Test alimentazione DC (DCPS)
- Collegare **solo la lower board**
- Premere power
- Se si osserva **high boot current jump** → la fonte interpreta come **short**

### 4) Ricerca corto
- Controllare **intorno a BB_PMU** per **short**

## Riparazione (passi)
### 1) Separazione sandwich board
- **Preheat ~160–180°C**
- Inserire **thin blades** per separare **upper & lower board**

### 2) Rimozione BB_PMU crepata
- Pulire l’**underfill** attorno a **BB_PMU** (attenzione ai componenti vicini)
- Applicare **flux**
- Sollevare con cura **BB_PMU**
- Ispezionare **pad danneggiati**
- Pulire con **wick + fresh solder**

### 3) Preparazione e reball BB_PMU nuova
- Usare lo **stencil corretto** per il modello
- Verificare l’allineamento delle **ball** sotto microscopio

### 4) Installazione BB_PMU
- Allineare correttamente gli **orientation markers**
- Reflow finché l’IC **si self-centra**
- Lasciare raffreddare
- Pulire la scheda e ispezionare le **giunzioni**

### 5) Riconnessione upper/lower board
- Allineare i contatti
- Ispezionare sotto microscopio la corretta **seam contact**

### 6) Test finale
- Collegare a **DCPS** e verificare **normal boot current**
- Avviare il dispositivo:
  - deve comparire **IMEI**
  - **Modem Firmware** deve mostrare la versione corretta
- Testare: **cellular**, **Wi‑Fi calling**, **SIM detection**

## Collegamenti interni utili (da wiki)
- [BB_PMU](../componenti/bb-pmu.md)
- [DCPS](../strumenti/alimentatore-da-banco.md)
- [Test CD3217 e ricerca corti](../tecniche/test-cd3217-e-ricerca-corti.md) (utile come riferimento generale per ricerca corti/diagnosi, da verificare rispetto al caso specifico)

## Note di tracciabilità
- Fonte esterna: repair.wiki (CC BY-SA 3.0)
- URL: https://repair.wiki/w/How_To_Fix_iPhone_13_Pro_No_Power_or_No_IMEI_After_Backglass_Repair
