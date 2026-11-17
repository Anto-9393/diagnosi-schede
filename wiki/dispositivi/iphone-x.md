---
titolo: iPhone X
tipo: dispositivo
riassunto: 'iPhone X: no power/non charging—sequenza diagnostica e riparazione focalizzata
  su Tigris U3300, poi Tigris coils L3340/L3341, infine Hydra (raro).'
modelli:
- iPhone X
fonti:
- raw/repairwiki/pagine/iphone-x.md
- raw/repairwiki/pagine/how-to-fix-iphone-x-that-does-not-charge.md
aggiornato: '2026-11-17'
categoria: phone
codici_modello: []
componenti_chiave:
- Tigris (U3300)
- Tigris coils L3340/L3341
- Hydra
casi: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# iPhone X

- Uscita: 2017-11-03
- Codici modello: da verificare (non indicati nella fonte)

## Guasti tipici e casi

### Non carica / carica anomala (focus Tigris)
**Sintomi (da fonte):**
- Il telefono si accende ma **non carica**.
- USB Meter mostra **0.000 A**.
- USB Meter mostra **0.006 A** o **0.007 A**.
- Il livello batteria **non sale**.
- **Fake charging**.
- Inserendo il cavo: compare il simbolo **Lightning**, ma **non carica**.

**Causa più probabile (da fonte):**
1. **Tigris (U3300)**
   - La fonte indica che nella maggior parte dei casi la sostituzione di **Tigris (U3300)** risolve i problemi di ricarica.
   - Tigris “dà i problemi Tristar” tipici dei modelli iPhone 7 e precedenti.

2. **Tigris coils L3340 e L3341** (seconda causa più probabile)
   - Se dopo la sostituzione di Tigris non si risolve, la fonte indica come prossima causa più probabile le **Tigris Coils L3340 e L3341**.

3. **Hydra** (raro)
   - In casi rari la fonte indica **Hydra** come causa del no charging.

> Nota: la fonte include anche un possibile problema legato a liquidi/corrosione su flex dell’ear speaker (Face ID/ALS), con effetti tipo bootlooping e problemi di ricarica. Per i dettagli operativi vedi la sezione “Sequenza di riparazione” qui sotto.

## Sequenza di riparazione (da fonte)

1. **Isolamento componenti (setup minimo di test)**
   - Scollegare tutto: ear speaker flex, power button flex, camere, antenne, ecc.
   - Lasciare collegati solo: **schermo**, **charging port** e **batteria**.
   - Testare di nuovo la ricarica.

2. **Verifica con misure USB Meter (criteri dalla fonte)**
   - Se **USB Meter = 0.000 A**: procedere con diagnosi su Tigris.
   - Se **USB Meter = 0.006 A / 0.007 A**: la fonte suggerisce di **provare a sostituire Tigris (U3300)**.

3. **Sostituzione Tigris (U3300)**
   - La fonte indica che nella maggior parte dei casi la sostituzione di **Tigris (U3300)** risolve i problemi di ricarica.

4. **Se non risolve: Tigris coils L3340 / L3341**
   - Se ancora non carica, la fonte indica come prossima causa più probabile le **Tigris Coils L3340 e L3341**.
   - Sostituirle e testare se la ricarica torna con **top board** (la fonte raccomanda di testare con la parte superiore).

5. **Caso raro: Hydra**
   - Se dopo Tigris e coils non si risolve, la fonte indica **Hydra** come causa rara.
   - Sostituire Hydra e verificare.

6. **Controllo liquidi su ear speaker flex (Face ID/ALS) — da considerare**
   - La fonte segnala che il flex dell’ear speaker (con flood illuminator Face ID e sensore ALS) è un punto in cui può entrare liquido.
   - La corrosione può causare **short data lines** e portare a **bootlooping, non charging e altri problemi random**.
   - Opzioni riportate dalla fonte:
     - sostituire il flex (perdita Face ID), oppure
     - rimuovere in modo sicuro il flood illuminator dal flex, pulire la corrosione e riposizionarlo, oppure
     - se il flex è danneggiato, sostituire/swap dei sensori su un flex nuovo.

## Collegamenti utili
- Componenti:
  - [Tigris/Tristar (pagina componente)](../componenti/tristar.md)
  - [Hydra (pagina componente)](../componenti/hydra-ic.md)
- Sintomi correlati (generici):
  - [non carica o alimentazione instabile](../sintomi/non-carica-o-alimentazione-instabile.md)

## Casi reali
Da completare con casi reali e misure del banco (wiki builder).
