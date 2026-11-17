---
titolo: Sintomo — non carica, icona assente, lettura OL I2C (diode mode)
tipo: sintomo
riassunto: 'Non carica con icona assente: in diode mode la linea I2C2_SMC_CHARGER_BI_GG_SDA_1V8
  al connettore batteria risulta OL (open line), bloccando comunicazione gas gauge/charging.'
modelli:
- iPhone 14
fonti:
- raw/repairwiki/pagine/how-to-fix-iphone-14-not-charging-due-to-open-i2c-line-at-battery-connector.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Descrizione del sintomo
- Il dispositivo **non carica** (anche con **cavo e alimentatore/brick noti buoni**).
- **Nessuna icona di ricarica**.
- La percentuale batteria può risultare **bloccata o inaccurata**.
- Il dispositivo può **accendersi**, ma **rifiuta di aumentare la % batteria**.

La fonte collega il problema a una **linea I2C aperta** al connettore batteria.

## Causa più probabile (in ordine)
1. **Linea I2C2_SMC_CHARGER_BI_GG_SDA_1V8 aperta (open line) al connettore batteria**
   - In **diode mode** la linea misura **OL** invece di un valore atteso.
   - Questo impedisce la comunicazione tra **battery gas gauge** e **sottosistema di ricarica**, causando **nessuna carica**.

## Misure utili (multimetro in diode mode)
### 1) Conferma del guasto di ricarica
- Testare con **cavo e brick noti buoni**.
- Verificare che **non aumenti la % batteria**.
- Verificare che il **dock flex** non sia la causa (da fonte).

### 2) Misura della linea I2C al connettore batteria
- Impostare il multimetro in **diode mode**.
- Puntare la sonda sulla linea:
  - **I2C2_SMC_CHARGER_BI_GG_SDA_1V8** (al connettore batteria)

**Atteso (da fonte):**
- **0.350** (valore non-OL)

**Difettoso (da fonte):**
- **OL** (open line)

### 3) Verifica continuità / tracciamento della linea
- Trovare il **test point** o la **pad/via** corrispondente dall’altro lato.
- Misurare **continuità** tra:
  - **pin del connettore batteria**
  - **lato opposto della board / test pad**

Se **manca continuità**, la fonte indica che la linea è **interrotta/rottta** (trace rotto).

## Riparazione (high level, da fonte)
1. **Scollegare la batteria**.
2. Identificare il **pin del connettore batteria** interessato.
3. Trovare un **test point / via alternativo** dall’altro lato.
4. Verificare che il **donor point** abbia la **lettura corretta in diode mode** (da fonte).
5. Eseguire un **fine jumper wire** tra:
   - lato funzionante della linea
   - **pin del connettore batteria**
6. Controllare che non ci siano **corti**.
7. Rimontare.

## Collegamenti utili
- [i2c-line-battery-connector](../componenti/i2c-line-battery-connector.md)
- [diode](../componenti/diode.md)
- [batteria](../componenti/batteria.md)
- [tecniche/test-i2c-battery-connector-ol-diodes-mode](../tecniche/test-i2c-battery-connector-ol-diodes-mode.md)
