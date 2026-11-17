---
titolo: Sandwich board separation e reball BB_PMU (post backglass)
tipo: tecnica
riassunto: 'Estensione della tecnica: split sandwich e reball BB_PMU con avvertenze
  su affidabilità post-reball (fonte iPhone 11: rischio cold solder/assenza underfill)
  e controlli per corti/IMEI.'
modelli:
- iPhone 13 Pro
- iPhone 14 Pro
- iPhone 14 Pro Max
- iPhone 11 (note di rischio/affidabilità, da verificare per BB_PMU)
fonti:
- raw/repairwiki/pagine/how-to-fix-iphone-13-pro-no-power-or-no-imei-after-backglass-repair.md
- raw/repairwiki/pagine/how-to-repair-iphone-11-dead-not-charging.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Scopo
Ripristinare alimentazione/modem dopo riparazione back-glass quando la zona **BB_PMU** della *sandwich logic board* risulta danneggiata (es. **hairline cracks** su BB_PMU e/o **dent**/impronta da tool di cracking), con sintomi tipici: **no IMEI**, **Modem Firmware: N/A**, **salto corrente elevato su DCPS** e/o **device completamente morto**.

> La fonte originale della tecnica è specifica per **iPhone 13 Pro / 14 Pro / 14 Pro Max** (BB_PMU molto vicina al back glass). 
> 
> Integrazione: la fonte esterna su **iPhone 11** descrive un rischio generale legato alla rimozione/sostituzione del reball sotto CPU (assenza dell’underfill di fabbrica dopo reball → maggiore vulnerabilità a danni da drop/flex). Applicare queste avvertenze come **rischio affidabilità post-reball** anche quando si esegue reball su IC in area sandwich. (Per BB_PMU su iPhone 11: **da verificare**.)

## Avvertenze critiche (affidabilità post-reball)
- La fonte esterna (iPhone 11) specifica che questa tipologia di intervento è **estremamente delicata** e **non raccomandata per uso long-term**.
- Dopo reball e reinstallazione, **l’underfill (glue) di fabbrica sotto la CPU non sarà più presente**, rendendo il dispositivo **molto più vulnerabile** a ulteriori danni: anche **un drop o flex minore** può causare ulteriori guasti o perdita completa di funzionalità.
- La fonte esterna raccomanda: procedere con cautela e **non garantire affidabilità** oltre l’estrazione dati riuscita.

> Nota operativa: la tecnica qui descrive BB_PMU (non CPU). Tuttavia, la parte “underfill di fabbrica non presente dopo reball” è un rischio strutturale della procedura di reball su IC BGA in generale: trattare il cliente/il caso come **data recovery-first** quando l’intervento rimuove/compromette l’underfill.

## Attrezzatura/strumenti (da banco)
- Stazione ad aria calda (per preheat e reflow)
- Pinzette e lame sottili per separazione sandwich
- Microscopio
- Flux, wick (treccia dissaldante) e saldatura compatibile
- Stencil **corretto per il modello** (fondamentale per reball)
- DC power supply (DCPS) per test corrente/boot

## Parametri e controlli chiave (dalla fonte tecnica)
- **Preheat**: ~**160–180°C** prima della separazione.
- **Seam/contatti**: dopo la ricongiunzione upper/lower board, ispezionare sotto microscopio che la **seam** sia in contatto corretto.
- **BB_PMU**:
  - ispezione per **hairline cracks** su BB_PMU
  - ispezione per **dent** sul PCB causato dal tool di backglass
  - controllo per **danni pad** dopo rimozione
  - reflow fino a **self-centering** dell’IC

## Diagnosi rapida (prima di aprire)
1. **Ispezione visiva (microscopio)**
   - Controllare lower board sotto microscopio.
   - Cercare:
     - **hairline cracks su BB_PMU**
     - **dent in the board** (impronta) da backglass punch/cracking tool

2. **Se il telefono si accende**
   - Verificare:
     - *#06# → **No IMEI***
     - Settings → **Modem Firmware = N/A**

3. **Test DCPS (se possibile)**
   - Collegare **lower board only**.
   - Premere power:
     - **High Boot Current jump → Short** (indicazione di corto)

4. **Short check**
   - Controllare attorno a **BB_PMU** per corti.

## Procedura riparazione (sandwich separation + rimozione + reball + reinstall)
### 1) Split della logica sandwich (separazione upper/lower)
1. **Preheat** a ~**160–180°C**.
2. Inserire **lame sottili** per separare **upper & lower board**.

### 2) Rimozione BB_PMU danneggiato
1. Pulire **underfill attorno a BB_PMU**.
   - Attenzione: la fonte specifica di fare attenzione ai componenti attorno a BB_PMU.
2. Applicare **flux**.
3. Sollevare **BB_PMU** con cautela.
4. Ispezionare:
   - **pad danneggiati**
5. Pulire con **wick + solder fresco**.

### 3) Preparazione e reball del BB_PMU nuovo
1. Usare lo **stencil corretto per il modello**.
2. Ispezionare l’allineamento delle **ball** sotto microscopio.

### 4) Installazione BB_PMU
1. Allineare correttamente l’orientamento (la fonte cita **orientation markers**).
2. Eseguire reflow fino a quando l’IC va in **self-centering**.
3. Lasciare **cooldown**.
4. Pulire la board e ispezionare i giunti.

### 5) Ricongiungere upper & lower boards
1. Allineare i contatti.
2. Ispezionare sotto microscopio la **seam contact** (contatto corretto lungo la giunzione).

## Test finale
1. Collegare a **DCPS** e verificare **normal boot current**.
2. Avviare il device:
   - l’**IMEI** deve comparire
   - la voce **Modem Firmware** deve mostrare la versione corretta
3. Test funzionali:
   - **cellular**
   - **Wi-Fi calling**
   - **SIM detection**

## Integrazione da fonte iPhone 11 (rischio cold solder/underfill)
La fonte esterna su **iPhone 11** descrive un caso in cui:
- il telefono **non si accende**
- su DCPS, dopo prompt to boot, la corrente sale e si **stabilizza** a **0.140–0.150 A**
- il device **boota se si splitta la logica** (lower/upper), indicando problema di contatto sotto CPU
- il problema **si ripresenta** se si rimonta senza reball

Riparazione descritta dalla fonte esterna:
- rimozione logica e split layers
- ispezione delle **saldature balls sotto CPU**
- **reball CPU** con stencil corretto e profilo controllato
- reinstall e test su DCPS (boot normale)

**Lezione applicabile alla tecnica BB_PMU**: se dopo reball/reinstall il comportamento torna a “stuck” o a boot anomalo, la causa può essere **contatto freddo**/saldature non affidabili; inoltre, la fonte evidenzia che l’assenza dell’underfill di fabbrica dopo reball aumenta la probabilità di recidiva con vibrazioni/flex.

## Collegamenti utili
- Componente: [BB_PMU](../componenti/bb-pmu.md)
- Tecnica correlata (diagnosi corti/rail): [diagnosi-e-rimozione-corto-su-rail-con-capacitore-in-corto](../tecniche/diagnosi-e-rimozione-corto-su-rail-con-capacitore-in-corto.md)
- Tecnica correlata (test/diagnosi): [test-dcps-e-diagnosi-kraken-ic](../tecniche/test-dcps-e-diagnosi-kraken-ic.md)
