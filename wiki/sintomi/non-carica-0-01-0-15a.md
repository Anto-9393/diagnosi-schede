---
titolo: Non carica — assorbimento 0.01–0.15 A (o 0 A) con/ senza boot
tipo: sintomo
riassunto: 'Sintomo: assorbimento ~0.01–0.14 A (o 0 A) dal caricatore; possibile boot.
  Spesso legato a corto/rail di ricarica o a guasti su IC di charging/PMIC (water
  damage).'
modelli:
- iPhone 15 Pro Max
- iPhone 15 Pro
fonti:
- raw/repairwiki/pagine/ipad-pro-12-9-3rd-gen-not-charging-repair.md
- raw/repairwiki/pagine/ipad-pro-12-9-4th-gen-not-charging-repair.md
- raw/repairwiki/pagine/iphone-15-pro-max-dead-and-not-charging.md
- raw/repairwiki/pagine/iphone-15-pro-stuck-at-1-percent-charging-and-no-battery-data-0xa1-panic-log-code.md
- raw/repairwiki/pagine/iphone-xs-not-charging.md
- raw/repairwiki/pagine/resistors-repair-basics.md
- raw/repairwiki/pagine/short-circuits-repair-basics.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Pattern di assorbimento (sintomo)
- Il dispositivo **assorbe ~0.01–0.14 A** dal caricatore (oppure **0 A**).
- L’iPhone **può o non può fare boot**.

> Fonte: raw/repairwiki/pagine/ipad-pro-12-9-3rd-gen-not-charging-repair.md

### Integrazione da fonte aggiuntiva (iPhone 15 Pro Max)
Su **iPhone 15 Pro Max** (non carica / dead):
- con **DC Power Supply (DCPS)** il dispositivo consuma **0.105–0.130 A** **prima del prompt di boot**;
- dopo il prompt, il telefono **boota normalmente**;
- **thermal imaging**: il **charging IC** scalda in modo anomalo.

> Fonte: raw/repairwiki/pagine/iphone-15-pro-max-dead-and-not-charging.md

### Variante “PMIC panic 0xa1” (iPhone 15 Pro)
Su **iPhone 15 Pro** con **water damage**:
- **non carica a 9V**;
- USB meter **fluttua**;
- batteria sempre letta **1%** e non sale;
- quando si collega il caricatore compare **0% remaining**;
- **restart ogni ~3 minuti** per mancanza di “battery data”;
- panic log error code: **0xa1**;
- anche sostituendo **batteria** e **charging port**, i sintomi **rimangono**.

> Fonte: raw/repairwiki/pagine/iphone-15-pro-stuck-at-1-percent-charging-and-no-battery-data-0xa1-panic-log-code.md

**Interpretazione dalla fonte:** la situazione “tende a succedere” quando il telefono ha subito danni da liquidi e **“fries the PMIC”**.

> Fonte: raw/repairwiki/pagine/iphone-15-pro-stuck-at-1-percent-charging-and-no-battery-data-0xa1-panic-log-code.md

---

## Cause probabili (in ordine)
1. **Corto/guasto su linee di ricarica attorno ai controller**
   - La fonte esistente indica di **controllare corti attorno ai controller** e componenti di ricarica comuni.
   - Componenti citati nella pagina esistente: **CD3215C00**, **Tristar 610A3C**, **Charging IC 343S00235**.
   - 
   > Fonte: raw/repairwiki/pagine/ipad-pro-12-9-3rd-gen-not-charging-repair.md

2. **Porta USB-C danneggiata / pin danneggiati (meccanicamente o da liquidi)**
   - La fonte esistente collega spesso il mancato charging a **danni fisici** sulla porta.
   - 
   > Fonte: raw/repairwiki/pagine/ipad-pro-12-9-3rd-gen-not-charging-repair.md

3. **Guasto del controller di ricarica (chip specifici del modello)**
   - La fonte esistente indica **CD3215C00** come chip comune da fallire su quel modello.
   - 
   > Fonte: raw/repairwiki/pagine/ipad-pro-12-9-3rd-gen-not-charging-repair.md

4. **PMIC danneggiato da liquidi (variante iPhone 15 Pro panic 0xa1)**
   - La fonte esterna indica che la situazione “tende a succedere” quando il telefono è stato **water damaged** e il **PMIC** viene danneggiato.
   - 
   > Fonte: raw/repairwiki/pagine/iphone-15-pro-stuck-at-1-percent-charging-and-no-battery-data-0xa1-panic-log-code.md

5. **Yangtze (U3300) — criterio di corrente molto bassa**
   - Fonte esterna: se si misura **0.006 A** (o “qualcosa di molto basso”), provare a **sostituire Yangtze (U3300)**.
   - 
   > Fonte: raw/repairwiki/pagine/iphone-xs-not-charging.md

6. **Hydra — causa rara**
   - Fonte esterna: in casi rari, **Hydra** può essere la causa del no charging; provare a **sostituire Hydra**.
   - 
   > Fonte: raw/repairwiki/pagine/iphone-xs-not-charging.md

---

## Collegamento al concetto “OCP / power cycling” (contesto del sintomo)
Se il rail di alimentazione/charging è in **corto**, molte alimentazioni implementano **over-current protection (OCP)**: il generatore può **ridurre la tensione** o **spegnere/riaccendere ciclicamente**. Questo può manifestarsi come **“power cycling”** e come **tensione instabile** misurata al voltmetro.

> Fonte: raw/repairwiki/pagine/short-circuits-repair-basics.md

> Nota operativa: la pagina sintomo qui descrive un pattern di assorbimento molto basso (0.01–0.14 A / 0 A). La fonte OCP spiega il comportamento osservabile su alimentatori quando scatta la protezione; la mappatura esatta “0.01–0.14 A ↔ OCP” non è esplicitata nella fonte e va considerata **da verificare**.

---

## Misure/controlli per distinguere
### 1) Verifica assorbimento e presenza/assenza boot
- Misura l’assorbimento dal caricatore:
  - **~0.01–0.14 A** oppure **0 A**.
- Osserva se il dispositivo **fa boot** o resta spento.

Fonti:
- raw/repairwiki/pagine/ipad-pro-12-9-3rd-gen-not-charging-repair.md
- raw/repairwiki/pagine/iphone-15-pro-max-dead-and-not-charging.md

### 2) Criterio “corrente molto bassa” → Yangtze (U3300)
- Se ottieni **0.006 A** (o comunque **molto basso**) durante il test di charging, la fonte esterna suggerisce di **provare a sostituire Yangtze (U3300)**.

> Fonte: raw/repairwiki/pagine/iphone-xs-not-charging.md

### 3) Controllo battery/charging via diode mode (variante iPhone 15 Pro panic 0xa1)
Dalla fonte esterna:
- controllare il **battery connector** (pin dritti, non piegati/warped/mancanti);
- verificare i **Diode Mode Values** su specifici pin:
  - **ZXW Pin 1: 0.439V**
  - **I2C2_SMC_CHARGER_BI_GG_SDA_1V8**
  - **ZXW Pin 2: 0.548V**
  - **I2C2_SMC_CHARGER_TO_GG_SCL_1V8_CONN**
  - **ZXW Pin 5: OL**
  - **ANALOG_BATT_VCELL_NEG_CONN**
  - **ZXW Pin 6: 0.505V**
  - **ANALOG_BATT_VCELL_POS_CONN**

Poi, con board alimentata **solo con board** (charging port flex collegato) e misurando i pin dopo:
- **ZXW Pin 1: 1.5V**
- **I2C2_SMC_CHARGER_BI_GG_SDA_1V8**
- **ZXW Pin 2: 1.8V**
- **I2C2_SMC_CHARGER_TO_GG_SCL_1V8_CONN**
- **ZXW Pin 5: 0.6V**
- **ANALOG_BATT_VCELL_NEG_CONN**
- **ZXW Pin 6: 0.6V**
- **eANALOG_BATT_VCELL_POS_CONN**

> Fonte: raw/repairwiki/pagine/iphone-15-pro-stuck-at-1-percent-charging-and-no-battery-data-0xa1-panic-log-code.md

**Criterio dalla fonte:** se diode mode è “bad” o tensioni basse sul battery connector, è “likely PMIC that has failed”.

> Fonte: raw/repairwiki/pagine/iphone-15-pro-stuck-at-1-percent-charging-and-no-battery-data-0xa1-panic-log-code.md

---

## Componenti correlati
- [CD3215C00](../componenti/cd3215c00.md)
- [CD3217](../componenti/cd3217.md)
- [Tristar](../componenti/tristar.md)
- [343S00235](../componenti/343s00235.md)
- [PMIC](../componenti/pmic.md)
- [Yangtze (U3300)](../componenti/yangtze-u3300.md)
- [Hydra](../componenti/hydra-ic.md)

---

## Note operative
- La pagina esistente descrive un pattern di assorbimento **~0.01–0.14 A (o 0 A)** con/ senza boot su iPad Pro 12.9 3rd/4th Gen.
- La fonte esterna aggiunge un criterio specifico su **iPhone XS**: se la corrente è **0.006 A** (molto bassa), provare **sostituzione Yangtze (U3300)**; in rari casi **Hydra**.
- **Da verificare (armonizzazione criterio):** la fonte esterna usa un valore “molto basso” (**0.006 A**) per decidere Yangtze; la pagina esistente usa un range (**0.01–0.14 A / 0 A**). Non è esplicitato dalla fonte come mappare 0.006 A dentro il range 0.01–0.14 A.
- La fonte “Short Circuits - Repair Basics” spiega che in presenza di corto può scattare **OCP** con possibile **power cycling** e tensione instabile; la relazione diretta con il range di corrente qui riportato non è quantificata nella fonte e va considerata **da verificare**.
