---
titolo: iPhone XS — non carica (fonte esterna)
tipo: fonte
riassunto: 'Per iPhone XS che si accende ma non carica: isolamento componenti (flex/Face
  ID/ALS), sospetto su Yangtze (U3300) come causa principale e raramente Hydra.'
modelli:
- iPhone XS
fonti:
- raw/repairwiki/pagine/iphone-xs-not-charging.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# iPhone XS Not Charging — riassunto fonte

## Sintomo
- iPhone XS si accende, ma **non carica**.

## Isolamento rapido (prima di cambiare componenti)
1. **Scollegare tutto**: ear speaker flex, power button flex, camere, antenne, ecc.
2. Lasciare collegati **solo**: schermo, **charging port** e batteria.
3. Se continua a non caricare, testare con **charging port**, **batteria** e **schermo** sicuramente funzionanti.

## Cause principali e sospetti
### 1) Ear speaker flex con danno da liquidi (Face ID + ALS)
- Il flex dell’ear speaker (con **flood illuminator** per Face ID e sensore **ALS** per auto brightness/True Tone) è **molto vicino alla zona della griglia ear mesh**.
- È facile che eventuali liquidi entrino e vadano a corrodere/contaminare i sensori.
- La corrosione può **cortocircuitare le linee dati sotto i sensori**, causando **bootlooping, non carica e altri problemi random**.

**Opzioni riportate dalla fonte (da verificare sul caso):**
- Sostituire il flex **perdere Face ID**.
- Rimuovere in modo sicuro il flood illuminator dal flex, **pulire la corrosione** e riposizionarlo.
- Se il flex è danneggiato oltre riparazione, **trasferire i sensori** su un flex nuovo.

### 2) Yangtze (U3300) — causa più frequente
- Nella maggior parte dei casi, la fonte indica che **sostituire Yangtze (U3300)** risolve i problemi di carica.
- Yangtze viene associato a problemi “tipo Tristar” (come su iPhone 7 e modelli più vecchi).

**Test consigliato dalla fonte:**
- Consiglia di **separare la sandwich board** e testare la carica con **solo**: top board, batteria, charging port e schermo.
- Se si misura **0.006 A** (o “molto basso” secondo la fonte), provare a **sostituire Yangtze**.

### 3) Hydra — raro
- In casi rari, la fonte indica **Hydra** come causa del “no charging”.
- Procedura: **sostituire Hydra** e verificare se risolve.

## Collegamenti wiki (componenti)
- [Yangtze (U3300)](../componenti/yangtze-u3300.md)
- [Hydra](../componenti/hydra-ic.md)

## Note
- Valori e procedure di misura dettagliate (es. quali rail/condizioni esatte per la corrente “0.006 A”) non sono ulteriormente specificati nella fonte: **da verificare** sul banco con la tua configurazione di test.
