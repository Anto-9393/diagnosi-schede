---
titolo: Low battery su schermo ma non carica — batteria bloccata a 0%/1% con riavvii
tipo: sintomo
riassunto: Schermo “low battery” con batteria bloccata a 0%/1% (spesso sempre 1%),
  USB meter fluttuante e riavvii ~3 minuti; spesso PMIC/connessione batteria danneggiati
  (panic log 0xa1).
modelli: []
fonti:
- raw/repairwiki/pagine/how-to-fix-an-ipad-air-that-shows-the-low-battery-screen-but-will-not-charge.md
- raw/repairwiki/pagine/how-to-fix-an-ipad-air-that-will-not-charge-or-power-on.md
- raw/repairwiki/pagine/how-to-fix-iphone-8-not-charging-after-screen-repair-stuck-at-0-battery-level.md
- raw/repairwiki/pagine/ipad-not-charging-battery-always-reporting-1-percent-charge.md
- raw/repairwiki/pagine/iphone-15-pro-stuck-at-1-percent-charging-and-no-battery-data-0xa1-panic-log-code.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Sintomo
- Dispositivo che mostra lo **schermo “low battery”**.
- La batteria risulta **bloccata a 0% o 1%** (in alcuni casi **sempre 1%**).
- **Mancata carica**.
- **USB meter fluttuante** (valori che oscillano).
- **Riavvii spontanei**: in una fonte circa **ogni ~3 minuti**; in altre fonti “every few minutes”.
- **Quando si collega il caricatore**: in una fonte compare **0% remaining**.
- **Panic log**: in una fonte compare **panic log error code 0xa1**.

> Fonti: 
> - raw/repairwiki/pagine/how-to-fix-an-ipad-air-that-shows-the-low-battery-screen-but-will-not-charge.md
> - raw/repairwiki/pagine/how-to-fix-an-ipad-air-that-will-not-charge-or-power-on.md
> - raw/repairwiki/pagine/how-to-fix-iphone-8-not-charging-after-screen-repair-stuck-at-0-battery-level.md
> - raw/repairwiki/pagine/ipad-not-charging-battery-always-reporting-1-percent-charge.md
> - raw/repairwiki/pagine/iphone-15-pro-stuck-at-1-percent-charging-and-no-battery-data-0xa1-panic-log-code.md

## Cause possibili (ordine di probabilità)
1. **Batteria guasta o lettura batteria non affidabile**
   - La fonte indica che il problema è “usually caused by a faulty battery”.
   - Per iPad: percentuale **sempre 1%**.
   - Fonti: 
     - raw/repairwiki/pagine/ipad-not-charging-battery-always-reporting-1-percent-charge.md

2. **Problema di connessione tra motherboard e batteria (connettore / FPC / contatto)**
   - La fonte suggerisce di controllare **panic logs** per sensori batteria (TG0B/TG0V) e quindi una possibile **communication issue** tra batteria e motherboard.
   - Controlli fisici: vite sul connettore batteria, ispezione Battery FPC, verifica connessione “solida”.
   - Fonti:
     - raw/repairwiki/pagine/ipad-not-charging-battery-always-reporting-1-percent-charge.md

3. **Vite mancante o serraggio errato (troppo lunga / troppo stretta)**
   - Se la vite è mancante o serrata in modo errato può causare i sintomi.
   - Fonti:
     - raw/repairwiki/pagine/ipad-not-charging-battery-always-reporting-1-percent-charge.md

4. **Da verificare: guasto su linee/sensori sotto Tigris (panic log TG0B/TG0V)**
   - Se nei panic logs compaiono riferimenti ai sensori **TG0B** e **TG0V**, la fonte collega il problema a batteria o comunicazione batteria↔motherboard.
   - Fonti:
     - raw/repairwiki/pagine/ipad-not-charging-battery-always-reporting-1-percent-charge.md
     - raw/repairwiki/pagine/how-to-fix-iphone-8-not-charging-after-screen-repair-stuck-at-0-battery-level.md

5. **PMIC danneggiato (caso iPhone 15 Pro con panic 0xa1)**
   - In una fonte specifica (iPhone 15 Pro): anche con **batteria nuova** e **charging port nuovo** i sintomi restano.
   - La fonte attribuisce il caso a **water damage** che “fries the PMIC”.
   - Fonti:
     - raw/repairwiki/pagine/iphone-15-pro-stuck-at-1-percent-charging-and-no-battery-data-0xa1-panic-log-code.md

## Misure utili / prove per distinguere
### 1) Panic log
- Condizione: dispositivo che riavvia / accesso ai panic logs.
- Atteso:
  - **0xa1** (caso iPhone 15 Pro) → orienta verso guasto PMIC nel caso descritto.
  - **TG0B/TG0V** (caso iPad) → orienta verso batteria o comunicazione batteria↔motherboard.
- Fonti:
  - raw/repairwiki/pagine/iphone-15-pro-stuck-at-1-percent-charging-and-no-battery-data-0xa1-panic-log-code.md
  - raw/repairwiki/pagine/ipad-not-charging-battery-always-reporting-1-percent-charge.md

### 2) Controllo fisico connettore batteria
- Condizione: device aperto.
- Atteso:
  - pin **dritti**, non **bent/warped/missing**.
- Fonti:
  - raw/repairwiki/pagine/iphone-15-pro-stuck-at-1-percent-charging-and-no-battery-data-0xa1-panic-log-code.md

### 3) Diode Mode sul connettore batteria (valori attesi — caso iPhone 15 Pro)
- Condizione: misurazioni in **Diode Mode** sul connettore batteria (come da fonte).
- Atteso (valori indicati dalla fonte):
  - **ZXW Pin 1**: **0.439V**
  - **I2C2_SMC_CHARGER_BI_GG_SDA_1V8**: (associato a ZXW Pin 1) **0.439V**
  - **ZXW Pin 2**: **0.548V**
  - **I2C2_SMC_CHARGER_TO_GG_SCL_1V8_CONN**: (associato a ZXW Pin 2) **0.548V**
  - **ZXW Pin 5**: **OL**
  - **ANALOG_BATT_VCELL_NEG_CONN**: (associato a ZXW Pin 5) **OL**
  - **ZXW Pin 6**: **0.505V**
  - **ANALOG_BATT_VCELL_POS_CONN**: (associato a ZXW Pin 6) **0.505V**
- Fonti:
  - raw/repairwiki/pagine/iphone-15-pro-stuck-at-1-percent-charging-and-no-battery-data-0xa1-panic-log-code.md

### 4) Tensione sui pin con board alimentata (valori attesi — caso iPhone 15 Pro)
- Condizione: **board only** (senza batteria collegata), con **charging port flex** collegato; poi misurare i pin e quindi **inserire il caricatore**.
- Atteso (valori indicati dalla fonte):
  - Con board only:
    - **ZXW Pin 1**: **1.5V**
    - **I2C2_SMC_CHARGER_BI_GG_SDA_1V8**: **1.5V**
    - **ZXW Pin 2**: **1.8V**
    - **I2C2_SMC_CHARGER_TO_GG_SCL_1V8_CONN**: **1.8V**
    - **ZXW Pin 5**: **0.6V**
    - **ANALOG_BATT_VCELL_NEG_CONN**: **0.6V**
    - **ZXW Pin 6**: **0.6V**
    - **eANALOG_BATT_VCELL_POS_CONN**: **0.6V**
- Nota: la fonte riporta anche valori “Diode Mode” (0.439/0.548/OL/0.505V) e valori di tensione (1.5/1.8/0.6V); non sono direttamente sovrapponibili.
- Fonti:
  - raw/repairwiki/pagine/iphone-15-pro-stuck-at-1-percent-charging-and-no-battery-data-0xa1-panic-log-code.md

## Azione correttiva (da fonte)
- Se **Diode Mode** sul connettore batteria è **bad** o le **tensioni** risultano **basse**: la fonte conclude che è “likely PMIC that has failed”.
- Fonti:
  - raw/repairwiki/pagine/iphone-15-pro-stuck-at-1-percent-charging-and-no-battery-data-0xa1-panic-log-code.md

> Per iPad, in parallelo, la fonte orienta anche a: vite/connettore/FPC batteria e, se necessario, sostituzione batteria o connettore.
> Fonti:
> - raw/repairwiki/pagine/ipad-not-charging-battery-always-reporting-1-percent-charge.md

## Final test (conferma)
- Verificare che il dispositivo **non riavvii** (stabilità oltre i minuti indicati dalla fonte).
- Verificare che il dispositivo **carichi normalmente**.
- Verificare che la percentuale batteria riporti **valori corretti** (non bloccata a 0%/1%).
- Fonti:
  - raw/repairwiki/pagine/ipad-not-charging-battery-always-reporting-1-percent-charge.md
  - raw/repairwiki/pagine/how-to-fix-iphone-8-not-charging-after-screen-repair-stuck-at-0-battery-level.md

## Link componenti / pagine correlate
- [Batteria](../componenti/batteria.md)
- [I2C line battery connector](../componenti/i2c-line-battery-connector.md)
- [PMIC](../componenti/pmic.md)
- [Diode](../componenti/diode.md)
- [Hydra/IC](../componenti/hydra-ic.md)
- [Tristar](../componenti/tristar.md) (da verificare: la fonte parla di Tigris come chip che sostituisce Tristar su iPhone 8/8P e newer)
