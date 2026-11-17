---
titolo: Test CD3217 e ricerca corti — probing in diode mode e iniezione a bassa tensione
tipo: tecnica
riassunto: 'Tecnica generale per distinguere corto su condensatori vs IC di charging/PD:
  diode mode sulle linee PP, iniezione 1V/1A con DCPS e localizzazione con freeze
  spray o termocamera.'
modelli: []
fonti:
- raw/repairwiki/pagine/how-to-fix-an-ipad-pro-11in-4th-gen-that-does-not-charge-cd3217-solution.md
- raw/repairwiki/pagine/how-to-program-rom-chip-for-ipads-with-cd3217.md
- raw/repairwiki/pagine/how-to-reprogram-the-cd32-rom-with-wylie-spi-programmer.md
- raw/repairwiki/pagine/ipad-pro-11in-1st-gen-not-recognized-by-pc-in-recovery-mode-or-charging-issues.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Scopo
Questa tecnica serve a **localizzare un corto** su rail di alimentazione/charging attorno a un **IC di carica USB-C/PD** (es. famiglia CD321x) e a distinguere se il corto è causato da:
- **condensatore/i in corto** sulla stessa linea
- oppure dall’**IC** (charging/PD) stesso

La fonte descrive la procedura in contesto **CD3215**; qui viene integrata come tecnica **generale** per IC di charging/PD. Verificare se i rail e i punti di probing coincidono con il tuo IC specifico (da verificare).

## Quando usarla
- Sintomi di **negoziazione assente o errata** (es. carica solo a 5V o solo su PD 15V) e sospetto corto su rail attorno all’IC.
- Hai già escluso (o stai escludendo) problemi di **porta di ricarica**.

## Strumenti
- [multimetro](../strumenti/multimetro.md) (modalità **diode mode**)
- [alimentatore da banco](../strumenti/alimentatore-da-banco.md) / DC power supply (impostabile a **1V/1A**)
- [termocamera](../strumenti/termocamera.md) **oppure** freeze spray (da verificare disponibilità)

## Procedura
### 1) Ispezione e pre-check
1. Ispeziona visivamente area IC e componenti adiacenti (segni di liquido, surriscaldamenti, corrosione).
2. Se possibile, verifica che la **porta di ricarica** sia nota/compatibile (la fonte indica che su quel modello la porta può essere sostituita per test; per altri modelli da verificare).

### 2) Diode mode: ricerca corto su rail/condensatori
1. Imposta il multimetro in **diode mode**.
2. Probing sui **condensatori attorno all’IC**.
3. Imposta la logica di misura come da fonte:
   - **sonda nera** su un riferimento **GND**
   - **sonda rossa** su ciascun lato del condensatore (lato non-GND)
4. Obiettivo: verificare che **nessun condensatore risulti in corto** (la fonte parla di “shorted to ground on both sides”).

**Criterio dalla fonte (CD3215, ma tecnica applicabile):**
- Se trovi un **condensatore in corto** su una delle linee, prima di sostituire l’IC conviene localizzare quale componente sta scaldando per primo.

> Nota: per CD3217/altro IC, i **rail esatti** e i condensatori “target” vanno mappati sullo schema/boardview (da verificare).

### 3) Iniezione a bassa tensione (1V/1A) per localizzare il componente che scalda
Questa parte è il cuore della tecnica per distinguere **corto su condensatore** vs **corto sull’IC**.

1. Imposta l’[alimentatore da banco](../strumenti/alimentatore-da-banco.md) a **1V / 1A**.
2. Collega:
   - **black probe** su **GND**
   - **red probe** sul **lato del condensatore** che **non** è connesso a GND (come da fonte).
3. Applica l’alimentazione e usa:
   - **termocamera** oppure
   - **freeze spray**
4. Osserva quale componente **si scalda per primo**:
   - se scalda prima un **condensatore** sulla linea in corto → il condensatore è il probabile colpevole
   - se scalda prima l’**IC** → probabile guasto dell’IC

### 4) Decisione e riparazione
#### Caso A — scalda per primo un condensatore
1. Rimuovi il condensatore in corto (la fonte indica che spesso è “loose and easy to break off”, con lama o leva).
2. Dopo la rimozione, verifica con multimetro in **diode mode** che il **corto non sia più presente**.
3. La fonte specifica che spesso i condensatori sono **smoothing caps** con più condensatori sulla stessa linea: se restano altri condensatori sulla linea, **non è sempre necessario** sostituire tutti quelli in corto.

#### Caso B — scalda per primo l’IC
1. Se il corto è attribuito all’IC, procedi con **sostituzione** dell’IC.
2. Dopo sostituzione, verifica:
   - che il **corto** sia rimosso
   - che la **negoziazione/charging** torni corretta (es. la fonte parla di test su negoziazione 15V e riconoscimento in recovery/DFU, da adattare al tuo caso).

#### Caso C — non trovi corto ma sospetti l’IC
La fonte indica che, se non trovi condensatori in corto ma il comportamento resta coerente con guasto IC, puoi procedere direttamente con **sostituzione** dell’IC (da adattare al tuo IC specifico).

## Verifiche finali (post-riparazione)
La fonte conclude con test funzionali:
- verifica che la carica/negoziazione torni corretta (es. **15V** con USB-C PD dove applicabile)
- verifica che il dispositivo venga riconosciuto anche in **recovery/DFU** (la fonte cita iTunes/3utools; da adattare al tuo flusso di lavoro)

## Collegamenti utili
- [CD3217](../componenti/cd3217.md)
- [Tristar](../componenti/tristar.md)
- [Diode](../componenti/diode.md)
- [Condensatori MLCC/elettrolitici/tantalio](../componenti/condensatori-mlcc-elettrolitici-tantalio.md)
- [multimetro](../strumenti/multimetro.md)
- [alimentatore da banco](../strumenti/alimentatore-da-banco.md)
- [termocamera](../strumenti/termocamera.md)
