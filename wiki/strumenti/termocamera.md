---
titolo: Termocamera — verifica calore su rail in corto durante iniezione a bassa tensione
tipo: strumento
riassunto: Usata per confermare quale componente scalda durante test di corto (qualitativo)
  e per controllare punti caldi su IC di charging/rail (es. CD3217).
modelli:
- iPhone 7
- iPhone XR
- iPad Pro 12.9 3rd Gen
- iPad Pro 12.9 4th Gen
fonti:
- raw/repairwiki/pagine/how-to-diagnose-fix-an-iphone-7-that-does-not-charge-takes-0-006a-via-usb.md
- raw/banco/miei-attrezzi.md
- raw/repairwiki/pagine/how-to-fix-an-iphone-8-that-has-no-power-does-not-boot.md
- raw/repairwiki/pagine/ipad-pro-11in-1st-gen-not-recognized-by-pc-in-recovery-mode-or-charging-issues.md
- raw/repairwiki/pagine/ipad-pro-12-9-3rd-gen-not-charging-repair.md
- raw/repairwiki/pagine/ipad-pro-12-9-4th-gen-not-charging-repair.md
- raw/repairwiki/pagine/iphone-xr-not-charging.md
- raw/repairwiki/pagine/iphone-xr-not-powering-on-with-heat-above-the-cpu.md
- raw/repairwiki/pagine/visual-inspection-repair-basics.md
- raw/casi_demo/ipad-air-4-a2316-non-carica.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Scopo
- Verificare se un componente della **charging/rail** (in particolare area **Tristar** o componenti attorno a **CD3215C00**) **scalda** durante eventi di diagnosi.
- In caso di **corto su una rail**, usare la termocamera per capire **quale componente scalda per primo** durante l’**iniezione di una tensione bassa** (metodo **qualitativo**).

## Limite importante
- La termocamera **non sostituisce** l’ispezione visiva.
- La fonte “Visual Inspection - Repair Basics” indica che spesso il problema è visibile (corrosione/ossido, tracce bruciate, polvere verde/“green dust”, probe point danneggiati). Dopo pulizia/ultrasonica questi segni possono diventare più difficili da notare: quindi conviene **ispezionare prima** e poi usare la termocamera per confermare la zona sospetta.

## Dove si usa (logic board)
- Area **Tristar** (controller/charging path).
- Area **CD3215C00** e componenti attorno alla rail in corto.
- Area **CD3217B12** (se sospetto corto attorno al controller di charging; alcuni condensatori possono essere **nascosti sotto lo shield metallico**).
- Area **Yangtze (U3300)** su iPhone XR (se si sospetta il charging IC).

## Strumento (banco)
- **Termocamera MEGA-IDEA Super IR CAM MINI S**.

## Procedura (operativa)
### A) Tristar: controllo calore durante prompt to boot (iPhone 7)
1. Preparare la diagnosi per il caso “**non carica**” con **corrente USB anomala** (la fonte riporta ~0.006–0.007 A su iPhone 7).
2. Eseguire il **prompt to boot**.
3. Usare la termocamera per controllare se **Tristar** “si scalda” durante l’evento.

**Atteso / interpretazione (iPhone 7)**
- **Di solito**: Tristar diventa caldo quando è guasto.
- **Non sempre**: la fonte specifica che può **non scaldare** anche se è guasto.

### B) Corto su rail: quale componente scalda per primo (iPad Pro 12.9 3rd Gen)
1. Identificare che il problema è compatibile con un **corto su rail** attorno a:
   - **CD3215C00**
   - **Tristar 610A3C**
   - **Charging IC 343S00235**
2. Eseguire un test di corto **iniettando una tensione bassa** nella linea cortocircuitata.
3. Durante l’iniezione, usare la termocamera (o **freeze spray** come affiancamento/alternativa secondo la fonte) per vedere **quale componente scalda per primo**.
4. Interpretazione e azione (da fonte):
   - Se scalda per primo un **condensatore** (zona rail): rimuoverlo e poi verificare con **multimetro in diode mode** che il corto non sia più presente.
   - Se il corto è attribuito all’**IC** (es. **CD3215C00** o **Tristar 610A3C**): sostituire l’IC e poi ricontrollare che il corto non sia più presente e che la negoziazione/carica tornino corrette (secondo il caso).

**Atteso / interpretazione (corto su rail)**
- Metodo **qualitativo** per distinguere se scalda prima un **condensatore** o l’**IC**.

### C) Corto attorno a CD3217B12 (iPad Pro 12.9 4th Gen)
1. Verificare che il problema sia compatibile con un caso “**not charging**” con assorbimento molto basso (la fonte riporta **0.01–0.14 A** dal caricatore; il dispositivo può o meno bootare).
2. Se la porta/connettore non è danneggiato, controllare la presenza di **shorts attorno a CD3217B12**.
3. Usare la termocamera per individuare componenti che **scaldano** durante la diagnosi.

**Atteso / interpretazione (iPad Pro 12.9 4th Gen)**
- La fonte non fornisce dettagli operativi (impostazioni/soglie): uso da considerare **qualitativo**.

### D) iPhone XR: heat sopra CPU prima del prompt to boot (pin-point corto)
1. Caso: iPhone XR **non si accende**.
2. Prima del **prompt to boot**: la fonte riporta **calore sopra la CPU**.
3. Sintomi elettrici associati (da fonte):
   - assorbimento **1 A o superiore** prima del prompt to boot su **DC Power Supply**
   - sensazione di **calore sopra la CPU**
4. Diagnosi: usare **Thermal Cam** o **Freeze Spray** per **pin-pointare** la causa del corto.
5. Azione (da fonte):
   - se la causa è un **cracked Speaker Amp (U5002)** → **sostituire**
   - se la causa è un **cap shorted** su **PP_SPKAMP_TOP_VBOOST** → **rimuovere il condensatore corto** e poi verificare **PP_SPKAMP_TOP_VBOOST** con **multimetro in diode mode** per confermare che il corto non sia più presente
   - la fonte indica che **non serve** sostituire il condensatore corto se il corto non è più presente dopo la rimozione

## Nota da caso reale (iPad Air 4 A2316)
Nel caso “iPad Air 4 Wi‑Fi (A2316) — non carica dopo caffè” la termocamera è stata usata per controllare punti caldi durante prove su area CD3217:
- **CPU ~60 °C** da accesa e aperta = considerato **normale**.
- **Nessun punto caldo sul CD3217**.

Questo caso è utile per ricordare che “caldo” non è automaticamente sinonimo di guasto sul singolo IC: serve correlare con misure (VBUS passante, corrente, negoziazione) e con l’area effettivamente sospetta.

## Collegamenti utili
- [Tristar](../componenti/tristar.md)
- [CD3215C00](../componenti/cd3215c00.md)
- [CD3217](../componenti/cd3217.md)
- [343S00235](../componenti/343s00235.md)
- [Yangtze (U3300)](../componenti/yangtze-u3300.md)
- [Tecnica: ricerca corto iniezione bassa tensione e termocamera](../tecniche/ricerca-corto-iniezione-bassa-tensione-e-termocamera.md)

## Note operative / limiti (da verificare)
- La fonte non fornisce **impostazioni specifiche** della termocamera (emissività, distanza, range °C): **da verificare**.
- La fonte non fornisce una **soglia numerica**: l’uso è **qualitativo** (caldo vs non caldo).
- La fonte indica l’uso di **termocamera o freeze spray** per pin-pointare la causa del corto; tempi/modalità sono **da verificare**.
