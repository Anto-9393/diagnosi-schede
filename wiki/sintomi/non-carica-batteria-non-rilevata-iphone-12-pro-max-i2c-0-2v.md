---
titolo: Sintomo — iPhone 12 Pro Max non carica e non rileva batteria (I²C SDA/SCL
  ~0.2 V)
tipo: sintomo
riassunto: 'iPhone 12 Pro Max non carica e non rileva batteria: SDA/SCL I²C a ~0.2
  V invece di ~1.8 V; causa tipica U2470/linea I²C.'
modelli:
- iPhone 12 Pro Max
fonti:
- raw/repairwiki/pagine/how-to-repair-iphone-12-pro-max-that-does-not-detect-battery-and-does-not-charge.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Descrizione del sintomo
- iPhone 12 Pro Max **non carica** e **non rileva la batteria** (nessuna percentuale batteria; può funzionare solo su alimentazione esterna/DCPS).
- Misura su connettore batteria: **I²C SDA/SCL ~0.2 V** invece del valore atteso **~1.8 V**.

## Cause possibili (in ordine di probabilità)
1. **U2470 guasto o non funzionante** (translator/gestione livello batteria) → porta le linee I²C a livello basso (~0.2 V).
2. **Problema sulla linea I²C (SDA/SCL)**: corto interno o condizione che “pull-a-low” le linee (la fonte indica che ~0.2 V implica che la linea viene tirata a massa).
3. **Da verificare**: guasto/contaminazione sul percorso tra connettore batteria e U2470 (la fonte non descrive corrosione visibile, ma richiede comunque ispezione/danno/corrosione su U2470).

## Misure e verifiche per distinguere
### 1) Verifica alimentazione batteria (BATT_VCC)
- Misura **BATT_VCC** sul connettore batteria.
- **Atteso (fonte): 3.7–4.0 V**.
- Se **manca** BATT_VCC, la fonte indica di **diagnosticare prima il power path** (non è il caso descritto nella fonte, ma serve per distinguere).

### 2) Verifica FPC batteria (diode mode)
- Esegui test in **diode mode** sulle linee del connettore batteria (FPC).
- **Atteso (fonte): letture “within normal range”**.
- Se le letture sono normali, la fonte indirizza verso problema I²C (non verso corti sulle linee batteria).

### 3) Misura I²C SDA/SCL
- Misura la tensione su **SCL** e **SDA**.
- **Atteso (fonte): ~1.8 V**.
- **Osservato (fonte): ~0.2 V** → indica che la linea viene **tirata a massa**.

### 4) Traccia fino a U2470
- Segui/traccia le linee I²C fino a **U2470** (posizionato vicino al connettore batteria, secondo la fonte).
- **Controllo visivo**: verifica danni/corrosione.
- Se U2470 risulta pulito, la fonte suggerisce comunque **sospetto di corto interno o guasto che porta le linee a livello basso**.

## Riparazione (coerente con la fonte)
1. **Rimuovere U2470** (hot air), pulire i pad e ispezionare per corti.
2. **Sostituire U2470** (nuovo o reballato), allineamento accurato.
3. **Rimisurare I²C SDA/SCL al connettore batteria**:
   - **Atteso (fonte): ~1.8 V**.
4. Test finale:
   - collega batteria, avvia,
   - verifica **rilevamento batteria/percentuale** e **carica**.

## Su iPhone 12 Pro Max
- Caso specifico: iPhone 12 Pro Max con **non carica** e **non rileva batteria**.
- Condizione chiave misurata (fonte): **SDA/SCL ~0.2 V** invece di **~1.8 V**.
- Causa indicata (fonte): **U2470**.

## Link utili
- [U2470](../componenti/u2470.md)
- [i2c-line-battery-connector](../componenti/i2c-line-battery-connector.md)
- [test-i2c-battery-connector-sda-scl-1-8v](../tecniche/test-i2c-battery-connector-sda-scl-1-8v.md)
