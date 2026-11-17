---
titolo: Fonte — iPhone 15 Pro stuck at 1% charging e panic log 0xa1 (no battery data)
tipo: fonte
riassunto: 'Caso esterno: iPhone 15 Pro non carica, batteria bloccata a 1%, USB meter
  fluttuante e restart ogni ~3 min; panic log 0xa1; spesso PMIC danneggiato da liquidi.'
modelli:
- iPhone 15 Pro
fonti:
- raw/repairwiki/pagine/iphone-15-pro-stuck-at-1-percent-charging-and-no-battery-data-0xa1-panic-log-code.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# iPhone 15 Pro stuck at 1% charging and no battery data — panic log 0xa1

> Fonte: [IPhone 15 Pro Stuck at 1 Percent Charging and No Battery Data 0xa1 Panic Log Code — repair.wiki](https://repair.wiki/w/IPhone_15_Pro_Stuck_at_1_Percent_Charging_and_No_Battery_Data_0xa1_Panic_Log_Code), CC BY-SA 3.0. Autori: vedi cronologia.

## Descrizione problema (da fonte)
- iPhone 15 Pro **non carica**.
- Mostra **batteria sempre al 1%** e non aumenta.
- Il **USB meter** (indicatore su USB) **fluttua continuamente**.
- Collegando il cavo di ricarica compare **0% rimanente**.
- Il telefono **si riavvia ogni ~3 minuti** per **mancanza di battery data**.
- Il **panic log** riporta **codice 0xa1**.
- Anche sostituendo **batteria** e **charging port**, i sintomi **rimangono**.
- La fonte collega il problema a **danno da liquidi** che “fries” (danneggia) il **PMIC**.

## Sintomi (da fonte)
- Non carica a **9V**.
- USB meter fluttuante.
- Batteria sempre letta come **1%**.
- Collegando il caricatore: **0% remaining**.
- Restart ogni **3 minuti**.
- Panic log: **0xa1**.

## Diagnosi (da fonte)
1. Test con **parti note buone**, in particolare **batteria** e **charging port**.
2. Controllo **connettore batteria**: pin **dritti**, non piegati/warped/mancanti.
3. Controllo **Diode Mode Values** sui pin indicati (ZXW):
   - **ZXW Pin 1**: **0.439V**
     - **I2C2_SMC_CHARGER_BI_GG_SDA_1V8**
   - **ZXW Pin 2**: **0.548V**
     - **I2C2_SMC_CHARGER_TO_GG_SCL_1V8_CONN**
   - **ZXW Pin 5**: **OL**
     - **ANALOG_BATT_VCELL_NEG_CONN**
   - **ZXW Pin 6**: **0.505V**
     - **ANALOG_BATT_VCELL_POS_CONN**
4. Misura **tensione** sui pin del connettore batteria:
   - Condizione: **board alimentata solo con board**, con **charging port flex collegato**; poi inserire il caricatore e misurare ogni pin.
   - Valori riportati dalla fonte:
     - **ZXW Pin 1**: **1.5V**
       - **I2C2_SMC_CHARGER_BI_GG_SDA_1V8**
     - **ZXW Pin 2**: **1.8V**
       - **I2C2_SMC_CHARGER_TO_GG_SCL_1V8_CONN**
     - **ZXW Pin 5**: **0.6V**
       - **ANALOG_BATT_VCELL_NEG_CONN**
     - **ZXW Pin 6**: **0.6V**
       - **eANALOG_BATT_VCELL_POS_CONN**

## Riparazione / conclusione (da fonte)
- Se le letture in **diode mode** sono “bad” o la tensione sul connettore batteria è **bassa**, la fonte indica come causa probabile un **PMIC guasto**.

## Collegamenti utili (wiki)
- [PMIC](../componenti/pmic.md)
- [i2c-line-battery-connector](../componenti/i2c-line-battery-connector.md)
- [Batteria](../componenti/batteria.md)
