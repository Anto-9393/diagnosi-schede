---
titolo: Fonti — iPhone 15 series no touch / no charging (U9500/U9720)
tipo: fonte
riassunto: 'Riassunto della fonte esterna: su iPhone 15, dopo accessori USB-C scadenti,
  perdita di carica e spesso touch dovuta a circuito USB-C con coppia U9500 + U9720
  (pairing/encryption).'
modelli:
- iPhone 15
- iPhone 15 Plus
- iPhone 15 Pro
- iPhone 15 Pro Max
fonti:
- raw/repairwiki/pagine/iphone-15-series-no-touch-no-charging.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# iPhone 15 Series - No Touch/No Charging (U9500/U9720)

> Fonte: [IPhone 15 Series - No Touch/No Charging — repair.wiki](https://repair.wiki/w/IPhone_15_Series_-_No_Touch/No_Charging) (CC BY-SA 3.0)

## Cosa descrive la fonte
Su iPhone 15 series, la carica può interrompersi improvvisamente dopo il collegamento a accessori USB‑C di terze parti (in particolare cavi/adattatori di bassa qualità o non Apple). La fonte attribuisce il problema principalmente a danni del circuito di controllo USB‑C, con coinvolgimento di:
- **U9500 (IC)**
- **U9720 (EEPROM)**

La fonte specifica che **U9500 e U9720 sono “encrypted and paired”**: se uno dei due fallisce o risulta **non abbinato/mismatched**, il telefono perde **carica** e può perdere anche la **funzione touch**.

## Sintomi tipici riportati
- Il telefono **si accende** ma **non carica**
- **Touchscreen non funziona**
- La **porta USB‑C** appare **fisicamente integra**

## Diagnosi (passi indicati)
1. **Test con cavo + adattatore originali**: verificare se il problema persiste anche con accessori Apple.
2. **Ispezione porta USB‑C**: controllare corrosione o detriti; pulire se necessario.
3. **Valutazione “touch + charge combo fault”**: se **sia touch che carica** non funzionano, la fonte indica di **sospettare U9500 immediatamente**.
4. **Apertura e ispezione area U9500/U9720**:
   - usare **termocamera** oppure **rosin + IPA** per evidenziare calore/corti nell’area attorno a U9500
   - ispezionare visivamente **U9500 e U9720** per danni
5. **Board swap test**: installare su una board “buona” (nota) **batteria, display e dock flex** per escludere problemi di flex/batteria.

## Riparazione (passi indicati)
1. **Disassemblare**: scollegare batteria e rimuovere logic board.
2. **Localizzare U9500 & U9720**: la fonte segnala che la **posizione varia** tra i modelli iPhone 15 series; usare i diagrammi/board view del guide.
3. **Preparazione area**: flux, protezione componenti vicini, preheat se possibile.
4. **Rimozione chip difettosi**: rimuovere con hot air **U9500 e U9720**, poi pulire i pad con wick e flux.
5. **Donor chips**: prelevare da **donor board della stessa famiglia/modello** e installare **entrambi** come **matched pair**.
6. **Reball & reinstall**:
   - la fonte indica di **reballare e saldare U9720 (EEPROM) prima**, poi **U9500**.
7. **Ispezione finale**: pulizia con IPA e controllo al microscopio di eventuali bridge.
8. **Riassemblaggio e test**: accendere e verificare **carica** e **touch**.

## Collegamenti alle pagine della wiki (piano)
- Componenti coinvolti:
  - [U9500](../componenti/u9500.md)
  - [U9720](../componenti/u9720.md)
- Sintomo correlato (combo touch + no charge):
  - [non-carica-e-touch-non-funziona](../sintomi/non-carica-e-touch-non-funziona.md)
- Dispositivo:
  - [iPhone 15 Pro Max](../dispositivi/iphone-15-pro-max.md)
- Tecniche/diagnosi collegate:
  - [test-u9500-5v-e-diagnosi-tigris](../tecniche/test-u9500-5v-e-diagnosi-tigris.md)
  - [ricerca-corto-iniezione-bassa-tensione-e-termocamera](../tecniche/ricerca-corto-iniezione-bassa-tensione-e-termocamera.md)

## Note di integrazione per la wiki
- La fonte non fornisce valori numerici di misura (da verificare) ma collega chiaramente la fault condition a **U9500 + U9720** e al concetto di **pairing/encryption**.
- La fonte non specifica soglie/voltaggi per test elettrici: eventuali valori presenti nelle pagine [U9500](../componenti/u9500.md) e [U9720](../componenti/u9720.md) vanno mantenuti come da wiki/piano.
