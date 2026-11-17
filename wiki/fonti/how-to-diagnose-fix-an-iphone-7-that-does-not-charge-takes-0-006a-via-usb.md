---
titolo: Fonte — How To Diagnose & Fix an iPhone 7 That Does Not Charge, Takes 0.006A
  via USB
tipo: fonte
riassunto: 'Diagnosi iPhone 7 non carica con assorbimento ~0.006–0.007 A via USB:
  focus su Tristar 610A3B (U4001), misure corrente/boot e tensione su J2201, verifica
  post-sostituzione e possibile corto C4005.'
modelli:
- iPhone 7
- iPhone 7 Plus
fonti:
- raw/repairwiki/pagine/how-to-diagnose-fix-an-iphone-7-that-does-not-charge-takes-0-006a-via-usb.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# Fonte: How To Diagnose & Fix an iPhone 7 That Does Not Charge, Takes 0.006A via USB

> Link: [How To Diagnose & Fix an iPhone 7 That Does Not Charge, Takes 0.006A via USB](../fonti/how-to-diagnose-fix-an-iphone-7-that-does-not-charge-takes-0-006a-via-usb.md)

## Sintomi chiave (scenario della fonte)
- iPhone 7/7 Plus **si accende ma non carica**.
- Con misuratore di corrente USB: assorbimento circa **0.006 A** (anche **0.007 A**).
- Inserendo il cavo: il telefono può accendersi, ma **non compare il simbolo di ricarica** in alto a destra.
- A volte il telefono **non si accende**.

## Criteri/diagnosi per misure

### 1) Escludere problemi di parti (board-level)
- La fonte consiglia di testare la logic board con **parti note buone** (es. **charging port flex** e **batteria** già verificate).
- Idealmente: rimuovere la board e collegare **solo**:
  - display (solo per power/boot),
  - batteria,
  - charging port flex,
  - poi collegare a carica e controllare il **USB meter**.
- Se la corrente resta ~**0.006 A** e il telefono si accende ma **non mostra il simbolo di carica**, la fonte indica come scenario tipico:
  - **Tristar — U4001 — Part# 610A3B**.

### 2) Tristar Tester (opzionale)
- Strumento “Tristar Tester” (non infallibile) per distinguere issue su charging port/Tristar.
- Tester citati:
  - Smartmod Pro Tristar Tester
  - ICC Pro Tristar Tester
  - JC programmer Tri-Star Tester
- Interpretazione (come riportato):
  - Se dice **“Tristar Fail”** → alta probabilità Tristar.
  - Se dice **“Tristar Pass”** → **può comunque** essere Tristar difettoso.

### 3) Corrente prima/dopo “prompt to boot” (DC supply / DT880)
- Con alimentatore DC o DT880, misurare la corrente:
  - **prima** del prompt to boot
  - **dopo** il prompt to boot
- Regole riportate:
  - Se c’è **corrente prima** del prompt to boot → **non** Tristar (scenario indicato come possibile short sulla board).
  - Se **non** c’è corrente prima del prompt, ma **dopo** il prompt la prima lettura è circa **0.150–0.250 A** → “definitely points towards a bad Tristar”.

### 4) Controllo calore su Tristar (opzionale)
- Thermal camera o freeze spray per vedere se **Tristar scalda** quando si fa il prompt to boot.
- La fonte dice che di solito scalda quando è guasto, ma **non sempre**.

### 5) Tensione ai pin batteria su J2201
- Collegare il **charging port flex** alla logic board e lasciare **solo** quello (nessun display, nessuna batteria, ecc.).
- Collegare il cavo al charging port.
- Multimetro in **DC volts**.
- Misurare la tensione ai pin batteria su **J2201**:
  - sono i **2 pin grandi su ciascun lato**.
  - la polarità “non importa”: ignorare il simbolo negativo se si sonda invertendo.
- Interpretazione riportata:
  - se la tensione è **< ~2 V** → Tristar bad.
  - valori tipici riportati: **~0.300–0.600 V**.
  - circuito di carica funzionante: circa **3.7 V**.

## Procedura di riparazione (come da fonte)
1. Eseguire i test sopra per confermare scenario Tristar.
2. **Sostituire Tristar**.
   - Per iPhone 7/7 Plus serve **610A3B** (versione corretta).
3. Nota meccanica (importante):
   - Tristar su iPhone 7/7 Plus è **parzialmente coperto da uno shield**.
   - Raccomandazione: **non toccare lo shield**.
   - La fonte suggerisce: “pull off the chip at an angle” e posizionare il nuovo Tristar “at angle”.
   - Tagliare lo shield è sconsigliato per rischio di:
     - danneggiare componenti vicini
     - creare punti taglienti che possono interferire con il charging port → “No Charging again”.

## Verifiche post-sostituzione (criteri riportati)
- Ripetere gli stessi controlli.
- Con screen, batteria e port “known good”:
  - verificare USB charging: la fonte indica **~1 A o più** come riferimento.
- Se disponibile: rilanciare il **Tristar Tester** e verificare se passa.
- Dopo “prompt to boot”:
  - la prima lettura corrente dovrebbe essere circa **~0.045 A**.
- Controllare se Tristar scalda ancora con freeze spray / thermal camera.
- Controllare tensione su **J2201**:
  - dovrebbe essere **~3.7 V**.
- Confrontare risultati precedenti vs nuovi per capire se il problema è risolto.

## Note su variabilità (brick/cavo/batteria)
- Ogni charging brick è leggermente diverso: letture corrente USB possono variare.
- Anche cavi e brick diversi danno letture diverse.
- Batterie quasi cariche caricano a corrente più bassa.
- Batterie vecchie/usurate caricano a correnti più basse (degradate).

## Altri guasti possibili se non risolve dopo Tristar
- Se non carica dopo sostituzione Tristar:
  - controllare corti attorno a Tristar.
  - “probe both sides of each capacitor directly surrounding Tristar” e verificare continuità a massa.
- Possibile corto indicato:
  - **TRISTAR_BYPASS capacitor C4005** shorted to ground → raccomandata sostituzione.
  - Valore C4005 riportato: **1.0 μF, 6.3 V, 0201 package**.
- Ulteriore verifica:
  - rimuovere Tristar e fare **diode mode** su tutte le pad Tristar.
  - confrontare con boardview (es. ZXW) e/o con una board nota buona.
- Se si trovano corti: iniettare tensione per individuare il capacitor in corto.

## Pagine wiki collegate (da usare come hub)
- [Tristar](../componenti/tristar.md)
- [C4005](../componenti/c4005.md)
- [Batteria](../componenti/batteria.md)
- [Tecnica: test Tristar e diagnosi non carica iPhone](../tecniche/test-tristar-e-diagnosi-non-carica-iphone.md)
- [Sintomo: non carica o alimentazione instabile](../sintomi/non-carica-o-alimentazione-instabile.md)
- [Strumento: alimentatore da banco](../strumenti/alimentatore-da-banco.md)
- [Strumento: termocamera](../strumenti/termocamera.md)
