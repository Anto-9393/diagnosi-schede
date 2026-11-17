---
titolo: How To Fix iPhone 14 Not Charging due to open i2c line at battery connector
  — repair.wiki (riassunto)
tipo: fonte
riassunto: 'iPhone 14 non carica: linea I2C2_SMC_CHARGER_BI_GG_SDA_1V8 al connettore
  batteria in OL (open). Diagnosi in diode mode e riparazione con jumper tra lato
  buono e pin del connettore.'
modelli:
- iPhone 14
fonti:
- raw/repairwiki/pagine/how-to-fix-iphone-14-not-charging-due-to-open-i2c-line-at-battery-connector.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Link alla fonte
- Fonte esterna: [How To Fix iPhone 14 Not Charging due to open i2c line at battery connector](https://repair.wiki/w/How_To_Fix_iPhone_14_Not_Charging_due_to_open_i2c_line_at_battery_connector) (CC BY-SA 3.0)

## Problema
- iPhone 14 arriva con **nessuna carica**: può anche **accendersi**, ma **non accetta carica** da cavo e alimentatore noti buoni.
- In diagnostica board-level, la linea al connettore batteria:
  - **I2C2_SMC_CHARGER_BI_GG_SDA_1V8**
  risulta **OL (open line)** invece di una lettura attesa in modalità diode/valore di tensione.
- Conseguenza: la linea dati impedisce la comunicazione tra **battery gas gauge** e **charging subsystem**, quindi la carica non parte.

## Sintomi tipici (da fonte)
- Non carica
- Nessuna icona di ricarica
- Percentuale batteria può essere **bloccata** o **inaccurata**
- Cavo e brick noti buoni non risolvono
- Nessun danno visibile alla porta di ricarica
- Il device può accendersi ma **rifiuta** di aumentare la % batteria

## Diagnosi (da fonte)
### 1) Conferma che è un guasto di carica
- Testare con **cavo e brick noti buoni**
- Verificare che **non aumenti la corrente di carica**
- Verificare che il **dock flex** non sia la causa

### 2) Misura della linea I2C al connettore batteria
- Impostare il multimetro in **diode mode**
- Puntare su **I2C2_SMC_CHARGER_BI_GG_SDA_1V8** al connettore batteria
- **Atteso:** lettura **~0.350** (non OL)
- **Guasto:** lettura **OL** (linea aperta)

### 3) Traccia della linea
- Trovare un **test point** o un **pad** corrispondente (lato opposto)
- Misurare continuità tra:
  - pin del connettore batteria
  - lato opposto / test pad
- Se **manca continuità** → la traccia è **interrotta**

## Riparazione (da fonte)
1. **Scollegare la batteria**
2. Identificare il **pin** del connettore batteria interessato
3. Trovare un **test point/punto donatore** sul lato opposto dove la linea risulta corretta
4. Verificare che il punto donatore abbia **lettura corretta in diode mode**
5. Eseguire un **jumper** con filo fine tra:
   - lato funzionante della linea
   - **pin** del connettore batteria
6. Fissare bene il jumper
7. Ispezionare per **assenza di corti**
8. Rimontare il dispositivo

## Componenti/aree correlate (link utili)
- [I2C line battery connector](../componenti/i2c-line-battery-connector.md)
- [Test i2c battery connector OL (diode mode)](../tecniche/test-i2c-battery-connector-ol-diodes-mode.md)
- [Sintomo: non carica / icona assente i2c-OL](../sintomi/non-carica-icona-assente-i2c-ol.md)
