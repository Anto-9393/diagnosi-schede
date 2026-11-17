---
titolo: Sintomo — iPhone non carica e touch non risponde
tipo: sintomo
riassunto: 'iPhone 15 series: dopo cavi/accessori USB-C terzi (specie non Apple) può
  comparire “no charge + touch morto”; sospetto immediato U9500 con paired EEPROM
  U9720, con verifica anche di porta e corti vicino all’area.'
modelli:
- iPhone 15 Pro Max
fonti:
- raw/repairwiki/pagine/how-to-fix-an-iphone-12-pro-that-is-not-charging-and-touch-not-working.md
- raw/repairwiki/pagine/iphone-15-pro-max-not-charging-and-no-touch.md
- raw/repairwiki/pagine/iphone-15-series-no-touch-no-charging.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Sintomi (pattern)
- L’iPhone **si accende**, ma **non carica**.
- **Touchscreen non funziona** (nessuna risposta).
- La porta **USB-C può apparire fisicamente ok**.
- Pattern tipico: dopo aver collegato il device a **accessori USB-C di terze parti**, soprattutto con **cavi di bassa qualità / non Apple**.

## Cause probabili (ordine di probabilità — da fonte)
1. **U9500 guasto** (USB-C control circuit).
2. **Mancata corrispondenza / guasto del paired EEPROM U9720**: la fonte specifica che **U9500 e U9720 sono criptati e “paired”**; se uno dei due fallisce o risulta **mismatched**, il telefono perde **charging** e può perdere anche **touch**.
3. **Danni/contaminazione nella porta USB-C** (corrosione/debris): la fonte include ispezione e pulizia.
4. **Corto/condizione termica anomala vicino all’area U9500**: la fonte indica thermal camera o rosin + IPA per individuare heat/shorts.
5. **Problemi da flex/batteria/display**: la fonte include un **board swap test** per escludere flex/batteria.

## Diagnosi pratica (passi)
### 1) Conferma con cavo/adattatore genuino
- Testare con **cavo + adapter Apple/genuini**.
- Se il problema **persiste anche** con accessori originali, la fonte indirizza verso guasto del circuito USB-C (U9500/U9720).

### 2) Ispezione porta USB-C
- Aprire e/o ispezionare la **porta USB-C**.
- Controllare **corrosione o detriti** all’interno della porta.
- Se presente, **pulire**.

### 3) Correlazione “touch + charge combo fault”
- Se **sia touch che charging** non funzionano insieme, la fonte indica di **sospettare U9500 immediatamente**.

### 4) Ispezione/ricerca corti vicino a U9500
Dopo apertura del device:
- Usare **termocamera** oppure **rosin + IPA** per individuare **heat/shorts** nella zona attorno a U9500.
- Ispezionare visivamente **U9500 e U9720** per danni.

### 5) Board swap test (esclusione flex/batteria)
- La fonte propone un test di esclusione: installare **battery, screen e dock flex** su una **known good board**.
- Serve a verificare che il problema non sia dovuto a **flex/batteria**.

## Riparazione (logica dalla fonte)
### Nota critica: U9500 non è “standalone”
- La fonte afferma che **U9500 e U9720 sono paired** e che sono **encrypted**.
- Se **uno dei due fallisce** o se sono **mismatched**, il telefono perde **charging** e può perdere anche **touch**.

### Sostituzione corretta (da fonte)
1. Rimuovere la logica: **scollegare batteria** e rimuovere la **logic board**.
2. Localizzare **U9500 & U9720** (la fonte: placement varia tra i modelli iPhone 15 series).
3. Preparare area: **flux**, protezione componenti vicini, **preheat** se possibile.
4. Rimuovere chip: desaldare con hot air **U9500 e U9720**.
5. Donor: prelevare **entrambi** i chip da **donor board della stessa famiglia/modello**.
   - La fonte specifica che devono essere **matched pair**.
6. Reball e reinstall:
   - **Reball di U9720 (EEPROM) prima**, poi **U9500**.
7. Ispezione finale: pulizia con **IPA**, controllare **bridges sotto microscopio**.
8. Rimontaggio e test: riconnettere, power on, verificare **charging e touch**.

## Test post-riparazione (da fonte)
- Dopo rework: verificare **charging** e **touch**.
- La fonte non fornisce in questo estratto valori numerici di corrente/tensione; per i dettagli di test (es. fast charge) fare riferimento alla pagina del sintomo esistente.

## Su quali modelli compare
- **iPhone 15 series** (pattern generale della fonte).
- Caso specifico già documentato nella wiki: **iPhone 15 Pro Max**.

## Link componenti
- [U9500](../componenti/u9500.md)
- [U9720](../componenti/u9720.md)
