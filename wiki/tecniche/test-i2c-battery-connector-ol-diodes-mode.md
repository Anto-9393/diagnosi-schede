---
titolo: Test I2C2_SMC_CHARGER_BI_GG_SDA_1V8 in diode mode (battery connector) — ricerca
  OL e jumper fine
tipo: tecnica
riassunto: 'Procedura diode mode sul connettore batteria per I2C2_SMC_CHARGER_BI_GG_SDA_1V8:
  criteri OL/valori attesi e ripristino continuità con jumper fine.'
modelli:
- iPhone 14
- iPhone 15 Pro
fonti:
- raw/repairwiki/pagine/how-to-fix-iphone-14-not-charging-due-to-open-i2c-line-at-battery-connector.md
- raw/repairwiki/pagine/how-to-fix-iphone-8-not-charging-after-screen-repair-stuck-at-0-battery-level.md
- raw/repairwiki/pagine/iphone-15-pro-stuck-at-1-percent-charging-and-no-battery-data-0xa1-panic-log-code.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Scopo
Verificare se la linea **I2C2_SMC_CHARGER_BI_GG_SDA_1V8** al **battery connector** è **aperta (OL)** e, se lo è, ripristinare la continuità con **jumper fine**.

- Per **iPhone 14** la fonte riporta che in **diode mode** la linea deve dare un valore ~**0.350** (non OL).
- Per **iPhone 15 Pro** la fonte esterna riporta valori specifici su più pin ZXW e sulle linee I2C2/analog battery.

## Sintomi associati (da fonti)
- **Non carica**.
- **Nessuna icona di ricarica**.
- Percentuale batteria **bloccata/inaccurata** (es. **1% fisso** su iPhone 15 Pro).
- Il device può **accendersi**, ma **rifiuta di aumentare la % batteria**.
- Su iPhone 15 Pro: **USB meter fluttuante**, lettura **0%** quando si collega il charger, **restart ogni 3 minuti** e panic log **0xa1**.

## Strumenti
- [Multimetro](../strumenti/multimetro.md) con modalità **diode mode**.
- (Per la riparazione) filo per **jumper fine** e attrezzi di microsaldatura: da verificare in base al banco.

## Procedura diagnostica
### 1) Conferma che il problema è di ricarica/comunicazione batteria (da fonti)
1. Testare con **cavo e brick noti buoni**.
2. Verificare che non ci sia **aumento della carica** (da fonte iPhone 14: “no charging current increase”).
3. Verificare che il **dock flex** non sia la causa (da fonte iPhone 14).

### 2) Diode mode sul battery connector (da fonti)
1. Impostare il multimetro in **diode mode**.
2. Puntare la sonda sulla linea **I2C2_SMC_CHARGER_BI_GG_SDA_1V8** al **battery connector**.
3. Leggere il valore.

#### Criteri di interpretazione
- **iPhone 14 (da fonte iPhone 14)**
  - **Atteso:** circa **0.350** (non OL).
  - **Guasto:** lettura **OL** (open line).

- **iPhone 15 Pro (da fonte esterna)**
  - **ZXW Pin 1:** **0.439V**
  - **I2C2_SMC_CHARGER_BI_GG_SDA_1V8:** (riportata insieme a ZXW Pin 1 come valore in diode mode)
  - **ZXW Pin 5:** **OL**
  - **ZXW Pin 2:** **0.548V**
  - **I2C2_SMC_CHARGER_TO_GG_SCL_1V8_CONN:** (riportata insieme a ZXW Pin 2)
  - **ZXW Pin 6:** **0.505V**
  - **ANALOG_BATT_VCELL_NEG_CONN:** (riportata insieme a ZXW Pin 5)
  - **ANALOG_BATT_VCELL_POS_CONN:** (riportata insieme a ZXW Pin 6)

> Nota: la fonte esterna non esplicita “atteso” per I2C2_SMC_CHARGER_BI_GG_SDA_1V8 come singolo valore target, ma fornisce i valori diode mode associati ai pin ZXW e alle linee I2C2/analog battery.

### 3) Verifica continuità / ricerca punto di rottura (da fonte iPhone 14)
1. Identificare un **test point** o una **pad/via** corrispondente sull’altro lato della board.
2. Misurare **continuità** tra:
   - **battery connector pin**
   - **altro lato board / test pad**
3. Interpretazione (da fonte iPhone 14):
   - **nessuna continuità** → traccia **interrotta**.

## Riparazione (jumper fine) — quando trovi OL/linea aperta (da fonte iPhone 14)
1. **Scollegare la batteria**.
2. Localizzare il **pin del battery connector** interessato.
3. Identificare un **punto alternativo** (test point/via) sull’altro lato della board.
4. Verificare che il **donor point** sulla parte funzionante dia la lettura corretta in **diode mode**.
5. Eseguire un **jumper wire** tra:
   - **working side della linea**
   - **battery connector pin**
6. **Fissare** correttamente il jumper.
7. **Ispezionare per eventuali short**.
8. Rimontare e riprovare.

## Note operative / rischi (da fonti)
- La fonte iPhone 14 non specifica valori di corrente/tensione per questa procedura: attenersi a **diode mode** e a **continuità**.
- Dopo il jumper, la fonte raccomanda esplicitamente **ispezione per corti**.
- La fonte esterna (iPhone 15 Pro) collega spesso questo scenario a **water damage** e a **PMIC fritto** (diagnosi “likely PMIC that has failed” se diode mode è cattivo o tensioni basse sul battery connector).

## Collegamenti utili
- Contesto linea: [i2c-line-battery-connector](../componenti/i2c-line-battery-connector.md)
- Sintomo correlato: [non-carica-icona-assente-i2c-ol](../sintomi/non-carica-icona-assente-i2c-ol.md)
- Tecnica generale: [test-diodi](../tecniche/test-diodi.md)
