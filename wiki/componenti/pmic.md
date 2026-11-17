---
titolo: PMIC — power management IC (diagnosi e sostituzione)
tipo: componente
riassunto: 'PMIC “fries” da danno da acqua: non carica (anche a 9V), batteria bloccata
  a 1%/0% e panic log 0xA1; diagnosi via diode mode e tensioni ai pin battery connector.'
modelli:
- iPhone 11
- iPhone 15 Pro
fonti:
- raw/repairwiki/pagine/how-to-fix-an-ipad-that-will-charge-when-powered-off-but-not-when-powered-on.md
- raw/repairwiki/pagine/how-to-fix-an-iphone-8-plus-boot-looping-on-apple-logo-and-random-charging.md
- raw/repairwiki/pagine/how-to-fix-iphone-8-not-charging-after-screen-repair-stuck-at-0-battery-level.md
- raw/repairwiki/pagine/how-to-repair-ipad-6-no-power.md
- raw/repairwiki/pagine/ipad-10-2in-8th-gen-not-turning-on-drawing-between-0-0-2a-tristar-is-functional-repair.md
- raw/repairwiki/pagine/ipad-pro-9-7-not-powering-on-2a-or-higher-power-draw-before-prompt-to-boot.md
- raw/repairwiki/pagine/iphone-11-not-powering-on-2a-or-higher-power-draw-after-prompt-to-boot.md
- raw/repairwiki/pagine/iphone-11-not-powering-on-after-prompt-to-boot-current-jumps-back-and-forth-from-0-a-to-320-ma-then-0-a-to-1-4-a-then-0-a-to-500-ma-and-so-on.md
- raw/repairwiki/pagine/iphone-15-pro-stuck-at-1-percent-charging-and-no-battery-data-0xa1-panic-log-code.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Funzione
Il **PMIC (Power Management IC)** gestisce le alimentazioni e le fasi di power-up/charging. Quando il PMIC è difettoso può interrompere la carica e/o impedire la corretta comunicazione dati batteria.

> Nota differenziale (da fonte esistente): in più casi il “short su rail” viene attribuito soprattutto a **condensatori in corto**; il PMIC entra in gioco come sospetto solo in pattern specifici (da verificare).

## Dove si trova
**da verificare** (la fonte non indica posizione/part number del PMIC).

## Sintomi tipici quando si guasta
### iPhone 15 Pro — acqua → PMIC danneggiato (panic log 0xA1)
**Fonte:** repair.wiki (IPhone 15 Pro Stuck at 1 Percent Charging and No Battery Data 0xa1 Panic Log Code).

**Sintomi riportati:]
- Non carica (anche a **9V**)
- USB meter fluttuante
- Batteria sempre a **1%** e non sale
- Collegando il caricatore compare **0% remaining**
- Riavvii ogni **3 minuti** per mancanza dati batteria
- Panic log **0xA1**
- Anche con **batteria nuova** e **charging port nuovo** i sintomi restano

**Causa indicata dalla fonte:** danno da acqua che “**fries PMIC**”.

### Pattern “PMIC difettoso” (iPad 10.2in 8th Gen)
**Fonte:** pagina PMIC esistente.

- Condizione: **Tristar funzionale**
- Sintomi: **schermo lampeggia**; ciclo assorbimento **0 A → fino a ~0,300 A →** poi ripete
- Diagnosi (fonte): PMIC difettoso che **non abilita GPIO_PMU_TO_LCD_PWREN**

### Pattern “short/assorbimento alto prima del prompt to boot” (iPhone 11)
**Fonte:** pagina PMIC esistente.

- Condizione: iPhone 11 su **DCPSU**, assorbe **2 A o più** prima del prompt to boot
- Fonte (più probabile): **condensatore in corto** su linee (es. **PP_VDD_MAIN**, **PP_VDD_BOOST**, ecc.)
- PMIC: citato come sospetto in contesti diversi, ma qui la fonte spinge prima verso localizzazione corto su rail (da seguire la diagnosi della fonte)

## Misure utili (con valori attesi)
> Le misure sotto sono quelle riportate dalla fonte. Se non è specificato, non è indicata la strumentazione/condizione esatta oltre a quanto scritto.

### iPhone 15 Pro — diode mode su battery connector (valori attesi)
**Fonte:** repair.wiki.

**Diode Mode Values (ZXW / I2C2 / ANALOG_BATT):**
- **ZXW Pin 1:** **0.439V**
- **I2C2_SMC_CHARGER_BI_GG_SDA_1V8:** (associato a ZXW Pin 1)
- **ZXW Pin 2:** **0.548V**
- **I2C2_SMC_CHARGER_TO_GG_SCL_1V8_CONN:** (associato a ZXW Pin 2)
- **ZXW Pin 5:** **OL**
- **ANALOG_BATT_VCELL_NEG_CONN:** (associato a ZXW Pin 5)
- **ZXW Pin 6:** **0.505V**
- **ANALOG_BATT_VCELL_POS_CONN:** (associato a ZXW Pin 6)

> La fonte riporta anche una seconda lettura “con board only” (tensione ai pin) e poi “plug in charger”. I valori sono sotto.

### iPhone 15 Pro — tensioni ai pin battery connector (board only vs con caricatore)
**Fonte:** repair.wiki.

**Condizione A: board only** (board collegata, con charging port flex collegato; poi si misura ogni pin):
- **ZXW Pin 1:** **1.5V**
- **I2C2_SMC_CHARGER_BI_GG_SDA_1V8:** **1.5V** (associato)
- **ZXW Pin 2:** **1.8V**
- **I2C2_SMC_CHARGER_TO_GG_SCL_1V8_CONN:** **1.8V** (associato)
- **ZXW Pin 5:** **0.6V**
- **ANALOG_BATT_VCELL_NEG_CONN:** **0.6V** (associato)
- **ZXW Pin 6:** **0.6V**
- **eANALOG_BATT_VCELL_POS_CONN:** **0.6V** (associato)

**Condizione B: poi plug in charger** (la fonte indica di misurare “each pin” dopo aver inserito il caricatore; i valori riportati sono quelli sopra, quindi da verificare se coincidono o se la fonte intende un set diverso):
- **da verificare** (la fonte nel testo fornito non separa chiaramente i valori “board only” vs “con caricatore” oltre alla frase)

## Diagnosi: quando sospettare PMIC
### iPhone 15 Pro — sospetto PMIC se diode mode o tensioni battery connector sono anomale
**Fonte:** repair.wiki.

- Se hai **bad diode mode reading** oppure **low voltage** sul battery connector → “**it’s likely PMIC that has failed**”.

### iPad 10.2in 8th Gen — PMIC se Tristar funzionale ma non abilita GPIO_PMU_TO_LCD_PWREN
**Fonte:** pagina PMIC esistente.

- Tristar funzionale + schermo lampeggia + assorbimento 0–~0,300 A → PMIC difettoso che non abilita **GPIO_PMU_TO_LCD_PWREN**.

### iPhone 11 — attenzione a non confondere PMIC con corto su rail
**Fonte:** pagina PMIC esistente.

- In alcuni pattern (es. “PMIC caldo” durante test via battery connector) la fonte indica che il PMIC può scaldare **senza** essere la causa dello short; lo short è su **condensatore vicino a NAND**.
- Linee citate per condensatore vicino a NAND (fonte): **PP2V63_NAND / PP1V8_NAND / PP0V9_NAND**.

## Soluzione / riparazione
### iPhone 15 Pro — sostituzione PMIC (implicita) dopo diagnosi su diode mode
**Fonte:** repair.wiki.

- La fonte conclude che letture diode mode/tensioni anomale sul battery connector indicano **PMIC fallito**.
- **da verificare**: nella fonte fornita non è riportato esplicitamente “sostituire PMIC” come step, ma la diagnosi è formulata come “likely PMIC failed”.

### iPad 10.2in 8th Gen — sostituzione PMIC (fonte esistente)
**Fonte:** pagina PMIC esistente.

- La fonte riporta che **sostituendo il PMIC** il problema si risolve.

### iPhone 11 — spesso risoluzione tramite rimozione corto su rail (fonte esistente)
**Fonte:** pagina PMIC esistente.

- In pattern con assorbimento alto prima del prompt to boot, la fonte indica come più probabile un **condensatore in corto** e riporta che spesso basta **rimuovere** il condensatore in corto.

## Collegamenti diagnostici correlati
- [i2c-line-battery-connector](../componenti/i2c-line-battery-connector.md)
- [batteria](../componenti/batteria.md)
- [diode](../componenti/diode.md)
- [tecniche/test-i2c-battery-connector-ol-diodes-mode](../tecniche/test-i2c-battery-connector-ol-diodes-mode.md)
- [tecniche/test-i2c-battery-connector-sda-scl-1-8v](../tecniche/test-i2c-battery-connector-sda-scl-1-8v.md)
- [non-carica-o-alimentazione-instabile](../sintomi/non-carica-o-alimentazione-instabile.md)

## Modelli su cui compare
### iPhone 11
- PMIC citato in contesti di diagnosi/heat e come sospetto in pattern specifici; la fonte spinge spesso verso **condensatore in corto**.

### iPhone 15 Pro
- Danno da acqua → PMIC “fries” con: non carica (anche a 9V), batteria bloccata a 1%, USB meter fluttuante, riavvii ogni 3 minuti, panic log **0xA1**.
- Diagnosi via **diode mode** e **tensioni** sul **battery connector**.
