---
titolo: Test I²C batteria — SDA/SCL ~1.8 V (U2470)
tipo: tecnica
riassunto: 'Aggiunge criteri di misura I²C batteria: su iPhone 15 Pro (panic 0xA1)
  SDA/SCL attesi ~1.8 V; letture basse (es. ~1.5 V/1.8 V) aiutano a distinguere bus
  tirato low/PMIC danneggiato.'
modelli:
- iPhone 12 Pro Max
- iPhone 15 Pro
fonti:
- raw/repairwiki/pagine/how-to-repair-iphone-12-pro-max-that-does-not-detect-battery-and-does-not-charge.md
- raw/repairwiki/pagine/iphone-15-pro-stuck-at-1-percent-charging-and-no-battery-data-0xa1-panic-log-code.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Scopo
Verificare la presenza della corretta tensione I²C sul connettore batteria (linee **SDA/SCL**) quando il telefono **non rileva la batteria** e **non carica**.

Questa tecnica integra due casi:
- caso iPhone 12 Pro Max: **BATT_VCC ok (3.7–4.0 V)** ma **SDA/SCL ~0.2 V** → tracciato fino a **U2470**.
- caso iPhone 15 Pro: con **panic log 0xA1** e sintomi “stuck at 1% / no battery data”, la fonte riporta letture su **I2C2_SMC_CHARGER_BI_GG_SDA_1V8** e **I2C2_SMC_CHARGER_TO_GG_SCL_1V8_CONN** (valori misurati su connettore batteria). 

## Attrezzatura
- [Multimetro](../strumenti/multimetro.md)
- Stazione ad aria calda (per eventuale rimozione/sostituzione U2470) (da verificare se necessaria anche per iPhone 15 Pro nel caso specifico)

## Procedura (diagnosi)
### 1) Verifica alimentazione batteria: BATT_VCC
1. Con telefono spento e scheda accessibile, misura **BATT_VCC** sul connettore batteria.
2. **Valore atteso (caso iPhone 12 Pro Max):** **3.7–4.0 V**.
3. Se **manca**: la fonte consiglia di diagnosticare prima il **power path** (non procedere con I²C come causa principale).

### 2) Controllo FPC batteria in diode mode (se disponibile)
1. Metti il multimetro in **diode mode**.
2. Controlla le letture sulle linee del **battery FPC**.
3. **Esito atteso (caso iPhone 12 Pro Max):** “tutte le linee” entro range normale.

### 3) Misura tensione I²C su SDA/SCL (al connettore batteria)
1. Misura la tensione sulle linee **SDA** e **SCL** al connettore batteria.
2. **Valore atteso (caso iPhone 12 Pro Max):** **~1.8 V**.
3. **Valore osservato (caso iPhone 12 Pro Max):** **~0.2 V**.
   - La fonte interpreta la lettura bassa come **linea tirata a massa (pulled low)**.

### 4) Traccia SDA/SCL fino a U2470 (solo se SDA/SCL risultano ~0.2 V)
1. Segui il routing delle linee **SDA/SCL** fino a **U2470**.
2. Verifica visivamente **danni/corrosione** su U2470.
3. Se la zona è pulita: la fonte indica di sospettare **short interno** o guasto che trascina il bus **low**.

## Riparazione (da fonte)
### Caso iPhone 12 Pro Max (U2470)
1. Rimuovi **U2470** con **hot air**.
2. Pulisci le piazzole e ispeziona per eventuali **corti**.
3. Sostituisci **U2470**.
4. Dopo la sostituzione, ricontrolla la tensione I²C su **SDA/SCL** al connettore batteria:
   - **atteso:** **~1.8 V**.
5. Test finale: collega batteria, avvia telefono, verifica che la batteria venga rilevata e che **carichi**.

## Su iPhone 15 Pro (panic log 0xA1) — letture SDA/SCL ~1.8 V
Nel caso descritto dalla fonte esterna (iPhone 15 Pro stuck at 1% / no battery data, panic log **0xA1**), la diagnosi include:
- controllo con parti note (batteria e charging port)
- controllo con **diode mode** sul connettore batteria
- misura tensioni sui pin del connettore **con board alimentata** e **charging port flex collegato**, poi inserimento del caricatore.

### Diode mode values (fonte)
- **ZXW Pin 1:** **0.439 V**
- **I2C2_SMC_CHARGER_BI_GG_SDA_1V8**
- **ZXW Pin 2:** **0.548 V**
- **I2C2_SMC_CHARGER_TO_GG_SCL_1V8_CONN**
- **ZXW Pin 5:** **OL**
- **ANALOG_BATT_VCELL_NEG_CONN**
- **ZXW Pin 6:** **0.505 V**
- **ANALOG_BATT_VCELL_POS_CONN**

### Tensioni sui pin (fonte)
Condizione indicata dalla fonte: **board only** con **charging port flex** collegato, poi **plug in the charger** e misura ogni pin.
- **ZXW Pin 1:** **1.5 V**
- **I2C2_SMC_CHARGER_BI_GG_SDA_1V8**
- **ZXW Pin 2:** **1.8 V**
- **I2C2_SMC_CHARGER_TO_GG_SCL_1V8_CONN**
- **ZXW Pin 5:** **0.6 V**
- **ANALOG_BATT_VCELL_NEG_CONN**
- **ZXW Pin 6:** **0.6 V**
- **eANALOG_BATT_VCELL_POS_CONN**

### Interpretazione (da fonte)
La fonte conclude che, se **diode mode reading è cattiva** o **bassa tensione** sul connettore batteria, è “likely PMIC that has failed”.

> Nota: la fonte esterna non descrive qui un valore “~0.2 V” come nel caso iPhone 12 Pro Max; riporta invece valori di tensione su SDA/SCL (1.5 V e 1.8 V) in una specifica condizione di misura. Per criteri di “SDA/SCL pulled low” su iPhone 15 Pro: da verificare.

## Criteri di decisione (riassunto)
- Se **BATT_VCC = 3.7–4.0 V** e **diode mode FPC è normale**, ma **SDA/SCL ~0.2 V** → la fonte indirizza verso **U2470**.
- Se nel caso iPhone 15 Pro (panic 0xA1) le letture su connettore batteria (diode mode e/o tensioni) risultano anomale → la fonte indica **PMIC** come probabile causa.

## Collegamenti utili
- [U2470](../componenti/u2470.md)
- [I²C battery connector](../componenti/i2c-line-battery-connector.md)
- [Test I²C battery connector — OL/diodes mode](../tecniche/test-i2c-battery-connector-ol-diodes-mode.md)
- [Test I²C battery connector — SDA/SCL ~1.8 V (questa pagina)](../tecniche/test-i2c-battery-connector-sda-scl-1-8v.md)
