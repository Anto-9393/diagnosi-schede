---
titolo: Test CD3217 e ricerca corti — probing in diode mode e iniezione a bassa tensione
tipo: tecnica
riassunto: 'Tecnica per localizzare corto su rail charging/USB-C/PD attorno a CD3217:
  diode mode su condensatori + iniezione 1V/1A con DCPS e localizzazione con termocamera/freeze.'
modelli: []
fonti:
- raw/repairwiki/pagine/how-to-fix-an-ipad-pro-11in-4th-gen-that-does-not-charge-cd3217-solution.md
- raw/repairwiki/pagine/how-to-program-rom-chip-for-ipads-with-cd3217.md
- raw/repairwiki/pagine/how-to-reprogram-the-cd32-rom-with-wylie-spi-programmer.md
- raw/repairwiki/pagine/ipad-pro-11in-1st-gen-not-recognized-by-pc-in-recovery-mode-or-charging-issues.md
- raw/casi_demo/ipad-air-4-a2316-non-carica.md
- revisione del tecnico (18 nov 2026)
aggiornato: '2026-11-18'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Scopo
Localizzare un **corto** su rail di alimentazione/charging attorno a un **controller USB-C/PD (famiglia CD321x, es. CD3217)** e distinguere se il corto è causato da:
- **condensatore/i** sulla stessa linea (in corto)
- oppure dall’**IC** (CD3217) che va in guasto e “tira” la linea

La fonte descrive la procedura in contesto **CD3215**; qui viene resa **generica** per CD3217, con nota che **rail e punti di probing vanno mappati sul tuo boardview/schemi** (da verificare).

## Quando usarla
- Sintomi compatibili con corto su rail charging/PD attorno all’IC (es. negoziazione assente/errata, carica che non parte, comportamento incoerente tra 5V e PD).
- Hai già escluso problemi “a monte” della porta (da verificare sul tuo caso).

## Condizioni di misura (fondamentali)
La fonte caso A2316 (liquido) evidenzia che i controller tipo CD3217 possono avere modalità **dead battery**:
- **Senza batteria**: può passare VBUS “da solo” (nessuna negoziazione PD).
- **Con batteria**: l’IC può bloccare il passaggio finché non ha firmware/comunicazione.

Quindi, per ogni misura/diagnosi ripeti sempre:
- **con batteria** e **senza batteria**
- **iPad acceso** e (se possibile) **spento**
- stesso cavo e stessa sorgente USB (da verificare)

## Strumenti
- [multimetro](../strumenti/multimetro.md) in **diode mode**
- [alimentatore da banco](../strumenti/alimentatore-da-banco.md) / DCPS impostabile a **1V / 1A**
- [termocamera](../strumenti/termocamera.md) **oppure** freeze spray (da verificare disponibilità)

## Procedura
### 1) Ispezione e pre-check
1. Ispeziona visivamente area IC e componenti adiacenti (segni di liquido/corrosione/surriscaldamenti).
2. Se il caso è da liquido (es. caffè), considera che i passivi/connessioni attorno al controller possono essere corrosi: prima di concludere su CD3217, verifica/bonifica (da verificare).

### 2) Diode mode: ricerca corto su rail/condensatori
1. Imposta il multimetro in **diode mode**.
2. Probing sui **condensatori attorno all’IC** (target: condensatori sulla linea che sospetti in corto).
3. Logica di misura (come da fonte):
   - **sonda nera** su un riferimento **GND**
   - **sonda rossa** su ciascun lato del condensatore (lato non-GND)
4. Obiettivo: identificare condensatori che risultano **in corto** (la fonte parla di “shorted to ground on both sides”).

**Nota operativa (da verificare per CD3217):** i “rail esatti” e quali condensatori sono i target vanno mappati su boardview/schemi del tuo modello.

### 3) Iniezione a bassa tensione (1V/1A) per localizzare il componente che scalda
Questa parte serve a distinguere **corto su condensatore** vs **corto sull’IC**.

1. Imposta l’[alimentatore da banco](../strumenti/alimentatore-da-banco.md) a **1V / 1A**.
2. Collega:
   - **black probe** su **GND**
   - **red probe** sul **lato del condensatore** che **non** è connesso a GND (come da fonte)
3. Applica alimentazione e usa:
   - [termocamera](../strumenti/termocamera.md) **oppure** freeze spray
4. Osserva quale componente **si scalda per primo**:
   - se scalda prima un **condensatore** sulla linea → probabile colpevole il condensatore
   - se scalda prima l’**IC** → probabile guasto dell’IC

#### Priorità diagnostica (nota da caso A2316)
*Corretto dal tecnico (18 nov 2026): l'ingest aveva scritto che il CD3217 era già stato sostituito. Non è così.*

Nel caso iPad Air 4 A2316 (caffè) sono stati sostituiti l’**IC di carica 343S00264-A0 (X3 su JC Drawing)** e il
**flat/connettore USB-C**, senza risolvere. Il **CD3217B12 (X5 su JC Drawing) NON è ancora stato sostituito** ed è il
sospettato n. 1. La fonte caso riporta anche che:
- con batteria + cavo la corrente misurata era **~0,002 A** (quindi non “corto duro” che manda subito in protezione)
- l’IC di carica **343S00264-A0 (X3)** scaldava subito con cavo inserito, ma cambiarlo non ha risolto: il calore era
  un effetto, non la causa
- con batteria + cavo le linee X1548–X1550 (uscita del CD3217 verso X3) restavano a ~0,026–0,186 V: il CD3217 non
  chiude il passaggio di VBUS verso l’IC di carica

Quindi, quando applichi questa tecnica su CD3217, non fermarti al “corto duro”: verifica sempre **condizioni con/senza batteria** e controlla anche alimentazioni/passivi attorno al controller.

### 4) Decisione e riparazione
#### Caso A — scalda per primo un condensatore
1. Rimuovi il condensatore in corto (la fonte indica che spesso è “loose and easy to break off”).
2. Dopo rimozione, verifica con multimetro in **diode mode** che il corto non sia più presente.
3. La fonte segnala che spesso i condensatori sono **smoothing caps** con più componenti sulla stessa linea: se restano altri condensatori sulla linea, **non è sempre necessario** sostituire tutti quelli in corto (da verificare sul tuo rail).

#### Caso B — scalda per primo l’IC
1. Procedi con **sostituzione dell’IC** (CD3217).
2. Dopo sostituzione, verifica che:
   - il corto sia rimosso
   - la negoziazione/charging torni coerente con il tuo caso (es. PD 15V dove applicabile; da adattare).

#### Caso C — non trovi corto ma sospetti l’IC
Se i condensatori non risultano in corto ma il comportamento resta coerente con guasto IC, la fonte indica che puoi procedere con **sostituzione dell’IC** (da adattare al tuo IC specifico).

## Verifiche finali (post-riparazione)
La fonte conclude con test funzionali:
- verifica che la carica/negoziazione torni corretta (es. **15V** con USB-C PD dove applicabile; da adattare)
- verifica riconoscimento in **recovery/DFU** (la fonte cita strumenti tipo iTunes/3utools; da adattare al flusso)

## Collegamenti utili
- [CD3217](../componenti/cd3217.md)
- [Tristar](../componenti/tristar.md)
- [Diode](../componenti/diode.md)
- [Condensatori MLCC/elettrolitici/tantalio](../componenti/condensatori-mlcc-elettrolitici-tantalio.md)
- [multimetro](../strumenti/multimetro.md)
- [alimentatore da banco](../strumenti/alimentatore-da-banco.md)
- [termocamera](../strumenti/termocamera.md)
