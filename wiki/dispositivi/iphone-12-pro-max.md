---
titolo: iPhone 12 Pro Max
tipo: dispositivo
riassunto: 'iPhone 12 Pro Max: mancata rilevazione batteria e mancata carica legate
  a I²C low (SDA/SCL ~0,2 V) e guasto/sospetto su U2470.'
modelli:
- iPhone 12 Pro Max
fonti:
- raw/repairwiki/pagine/iphone-12-pro-max.md
- raw/repairwiki/pagine/how-to-repair-iphone-12-pro-max-that-does-not-detect-battery-and-does-not-charge.md
aggiornato: '2026-11-17'
categoria: phone
codici_modello: []
componenti_chiave:
- U2470
casi: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# iPhone 12 Pro Max

- Uscita: 2020-10-23
- Codici modello: da verificare (non indicati nella fonte)

## Guasti tipici e casi

### Mancata rilevazione batteria + mancata carica (I²C SDA/SCL low) — caso U2470

**Sintomi (da fonte):**
- iPhone non carica e non si alimenta dalla batteria.
- Percentuale batteria non visualizzata; il dispositivo può funzionare solo da [DCPS](../strumenti/alimentatore-da-banco.md).
- Nessuna corrosione o danno visibile nell’area del connettore batteria.

**Misure chiave (da fonte):**
- **BATT_VCC** (tensione al connettore batteria): **3,7–4,0 V** → ✅ normale.
- **Battery FPC diode mode**: letture **entro range normale** → ✅.
- **I²C lines (SCL/SDA)**: atteso **~1,8 V**, osservato **~0,2 V** → indica che la linea viene **tirata a massa (pulled low)**.

**Diagnosi (da fonte):**
- Tracciando le linee I²C (SDA/SCL) si arriva a **U2470** (battery data level translator IC, vicino alla batteria).
- Se l’area è pulita, la causa viene attribuita a **guasto interno** o a un problema che porta a **pull-down anomalo** del bus I²C.

**Riparazione (da fonte):**
1. Rimozione di **U2470** (hot air).
2. Pulizia pad e ispezione per eventuali **corti**.
3. Sostituzione (o reball) di **U2470**.
4. Verifica: dopo la sostituzione, la tensione I²C al connettore batteria deve tornare a **~1,8 V**.
5. Test finale: con batteria collegata, verifica che **la batteria venga rilevata**, che la **percentuale** compaia e che il dispositivo **carichi**.

**Link utili (pagine wiki):**
- [U2470](../componenti/u2470.md)
- [i2c-line-battery-connector](../componenti/i2c-line-battery-connector.md)
- [non-carica-batteria-non-rilevata-iphone-12-pro-max-i2c-0-2v](../sintomi/non-carica-batteria-non-rilevata-iphone-12-pro-max-i2c-0-2v.md)
- [test-i2c-battery-connector-sda-scl-1-8v](../tecniche/test-i2c-battery-connector-sda-scl-1-8v.md)

## Note
- La fonte non riporta codici modello specifici per iPhone 12 Pro Max: **da verificare**.

Fonte: [How to Repair iPhone 12 Pro Max that does not detect battery and does not charge — repair.wiki](https://repair.wiki/w/How_to_Repair_iPhone_12_Pro_Max_that_does_not_detect_battery_and_does_not_charge), CC BY-SA 3.0.
