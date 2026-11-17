---
titolo: 'Sintomo — non si accende: ciclo assorbimento 0–0.3 A e schermo lampeggia'
tipo: sintomo
riassunto: 'Pattern assorbimento ciclico 0–~0,3 A con schermo lampeggia; possibile
  corto su rail o guasto PMIC/linea GPIO_PMU_TO_LCD_PWREN (da verificare sovrapposizione
  con caso iPhone XR: heat sopra CPU + corto su PP_SPKAMP_TOP_VBOOST).'
modelli:
- iPad 10.2 8th gen
- iPad Pro 9.7
fonti:
- raw/repairwiki/pagine/ipad-10-2in-8th-gen-not-turning-on-drawing-between-0-0-2a-tristar-is-functional-repair.md
- raw/repairwiki/pagine/ipad-pro-12-9-5th-gen-not-powering-on-due-to-long-screw-damage.md
- raw/repairwiki/pagine/ipad-pro-9-7-not-powering-on-2a-or-higher-power-draw-before-prompt-to-boot.md
- raw/repairwiki/pagine/iphone-xr-not-powering-on-with-heat-above-the-cpu.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Sintomi
- **Schermo lampeggia**
- **Assorbimento che cicla** tra **0 A e ~0,3 A** (tipicamente con alimentazione da banco)

## Cause probabili (in ordine)
1. **PMIC difettoso** che **non emette** il segnale **GPIO_PMU_TO_LCD_PWREN** verso la sezione display.
2. **Danno meccanico da vite lunga** con **trace/via rotta** sotto lo standoff: in particolare la linea **PP3V3_BSB** e/o la via che porta la linea più in profondità.
3. **Corto su rail** (da fonte esterna): se l’iPad Pro 9.7 assorbe **2 A o più** da **DCPS** **prima del prompt di boot**, la fonte interpreta la condizione come **short on the motherboard**.

> **Integrazione da fonte esterna (iPhone XR)**: esiste un caso iPhone XR con **heat sopra la CPU** e **corrente ≥1 A prima del prompt di boot**. La soluzione della fonte attribuisce la causa a:
> - **Speaker Amp** **cracked** (U5002)
> - oppure **corto su un condensatore** su **PP_SPKAMP_TOP_VBOOST**
>
> **Nota di compatibilità**: il tuo sintomo specifico è “ciclo 0–0,3 A + schermo lampeggia”. La fonte iPhone XR descrive un **pattern diverso** (heat sopra CPU + corrente ≥1 A). Quindi **non è direttamente sovrapponibile**: da verificare se creare/aggiornare un sintomo dedicato a **“heat sopra CPU + corto PP_SPKAMP_TOP_VBOOST”**.

## Pattern di assorbimento (da fonte)
### Su iPad Pro 9.7 (da verificare su altri modelli)
- Se l’iPad Pro 9.7 **disegna qualsiasi corrente prima del prompt di boot**, la fonte indica **short on the motherboard**.
- Linee sospette per short (da fonte):
  - **PP_VCC_MAIN**
  - **PP_BATT_VCC**
  - **PPSTROBE_LX**
  - **PPVCC_HIGH**
- La fonte indica che la linea più comune con short è **VCC_MAIN**.

### Su iPad Pro 12.9 5th gen (da verificare su altri modelli)
- Con iPad collegato a **USB amp meter**: assorbimento **~0,02 A**, poi **salita rapida a ~0,5 A**, poi ritorno a **~0 A**.
- Con iPad collegato a **DCPSU**:
  - **~0,00 A** prima del prompt di boot
  - dopo prompt: **~0,014–0,025 A**

### Su iPad 10.2 8th gen (pagina esistente)
- Assorbimento **cicla 0–0,3 A** e schermo lampeggia.

## Misure utili (da verificare)
- Con **alimentazione da banco**: osservare il **ciclo di assorbimento** e la **lampeggiatura schermo**.
- Verificare (da verificare) la presenza dell’uscita **GPIO_PMU_TO_LCD_PWREN** dal **PMIC**.
- Se sospetto **danno da vite lunga**:
  - ispezionare **visivamente** la zona sotto lo standoff (sopra le schermature/schermo FPC, vicino al connettore batteria) per trace/via lesionate.
  - verificare continuità/connessione della linea **PP3V3_BSB** e della **via** che porta la linea più in profondità.
- Se il comportamento include **assorbimento elevato prima del prompt di boot** (scenario fonte esterna, iPad Pro 9.7):
  - ispezionare la board per **componenti bruciati** e **danni da liquidi**.
  - se non c’è danno da liquidi: considerare **short** su una delle linee **PP_VCC_MAIN / PP_BATT_VCC / PPSTROBE_LX / PPVCC_HIGH**.

## Diagnosi/Conferma corto su rail (da fonte esterna, iPad Pro 9.7)
- La fonte propone di **iniettare tensione**: **4 V / 2 A** direttamente sulla linea misurata come in corto.
- Usare **freeze spray** o **termocamera** per individuare il **capacitore in corto**.
- Nota: se lo short è su un chip, la fonte riporta che **U8500** può scaldarsi; però consiglia di **non assumere subito** che U8500 sia la causa e di cercare altri hot spot sulla board.
- Se lo short è su un **chip**: sostituire il componente.
- Se lo short è su un **capacitore di disaccoppiamento**: rimuoverlo spesso risolve; la fonte indica che la capacitance potrebbe non scendere abbastanza da compromettere la funzione.
- Se c’è **danno da acqua/corrosione**: la fonte indica che la pulizia può risolvere; se la corrosione è sotto un IC, può essere necessario rimuovere/pulire e poi **reball** o sostituire il chip.

## Valutazione con diode reading (da fonte esterna)
- Dopo la rimozione del componente in corto, la fonte indica che una **VCC Main sana** dovrebbe avere una lettura con **vault tra 0,400 e 0,500**.

## Integrazione: caso iPhone XR con heat sopra CPU (pattern diverso)
- Sintomi della fonte:
  - **corrente 1 A o superiore** prima del prompt di boot su **DC Power Supply**
  - **heat sopra la CPU**
- Soluzione della fonte:
  - possibile **Speaker Amp** **cracked** (**U5002**)
  - oppure **corto su un condensatore** su **PP_SPKAMP_TOP_VBOOST**
  - usare **Thermal Cam** o **Freeze Spray** per localizzare il corto
  - se Speaker Amp è crepato: **sostituire**
  - se è corto un condensatore: **rimuoverlo** e poi verificare **PP_SPKAMP_TOP_VBOOST** in **diode mode** con multimetro per confermare che lo short non è più presente (la fonte dice che non serve sostituire il condensatore se lo short non è più presente)

## Modelli su cui compare
### Su iPad 10.2 8th gen (pagina esistente)
- **Assorbimento**: ciclo **0–0,3 A**
- **Schermo**: lampeggia e il ciclo si ripete
- Diagnosi dalla fonte: **PMIC** che non outputta **GPIO_PMU_TO_LCD_PWREN**
- Esito: sostituzione **PMIC** risolve

### Su iPad Pro 9.7 (da fonte esterna)
- Condizione chiave: assorbimento **2 A o più** da **DCPS** **prima del prompt di boot** → interpretazione fonte: **short on the motherboard**.
- Linee sospette: **PP_VCC_MAIN / PP_BATT_VCC / PPSTROBE_LX / PPVCC_HIGH** (più comune: **VCC_MAIN**).

### Su iPad Pro 12.9 5th gen (da fonte esterna già presente in pagina)
- **Assorbimento**: pattern **~0,02 A → ~0,5 A → ~0 A** (USB amp meter)
- Con **DCPSU**: **~0,00 A** prima del prompt, poi **~0,014–0,025 A** dopo prompt
- Causa più probabile (da pagina esistente): **trace/via rotta** sotto standoff con vite lunga, soprattutto **PP3V3_BSB**
- Possibile workaround (da pagina esistente): applicare **pressione** localizzata vicino allo standoff per far contatto temporaneo alla via

## Componenti correlati
- [PMIC](../componenti/pmic.md)
