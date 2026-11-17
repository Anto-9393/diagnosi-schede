---
titolo: iPhone 7
tipo: dispositivo
riassunto: 'Aggiornata sezione iPhone 7 con caso dead/no-boot e assorbimento 0 A→20–40
  mA stabile (impossibile DFU): pulizia underfill e “poking” induttanze L1801/L1804/L3302
  con valori attesi; mantenuta la sezione iPhone 7/7 Plus “si accende ma non carica”
  (0.006–0.007 A USB) su Tristar 610A3B.'
modelli:
- iPhone 7
- iPhone 7 Plus
fonti:
- raw/repairwiki/pagine/iphone-7.md
- raw/repairwiki/pagine/how-to-diagnose-fix-an-iphone-7-that-does-not-charge-takes-0-006a-via-usb.md
- raw/repairwiki/pagine/how-to-fix-iphone-7-that-does-not-turn-on-hangs-at-0-020-0-030-a-after-you-prompt-to-boot-on-dc-power-supply.md
aggiornato: '2026-11-17'
categoria: phone
codici_modello: []
componenti_chiave:
- Tristar 610A3B
- J2201
- L1801
- L1804
- L3302
casi: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# iPhone 7

- Uscita: September 16, 2016
- Codici modello: da verificare (non indicati nella fonte)

## Guasti tipici e casi

### Caso: “si accende ma non carica”, assorbimento ~0.006–0.007A via USB

**Sintomi riportati (da fonte):**
- Il telefono **si accende** ma **non carica**.
- Con misuratore USB: lettura **0.006 A** o **0.007 A** via USB.
- Inserendo il cavo, il telefono può **accendersi**, ma **non compare il simbolo di ricarica** in alto a destra.
- A volte il telefono **non si accende affatto**.

**Diagnosi (da fonte):**
1. **Riduzione variabili / test parti note buone**
   - Testare la logica con **charging port flex** e **batteria** noti buoni.
   - Idealmente: rimuovere la board dall’alloggiamento e collegare **solo**: schermo, batteria e charging port alla logica; poi misurare l’assorbimento via USB.
   - Se la corrente resta intorno a **0.006 A** e il telefono si accende ma **non** mostra il simbolo di carica, la fonte indica **problema di board**.
   - La fonte collega questi casi a: **Tristar — U4001 — Part# 610A3B**.

2. **Tristar Tester (opzionale)**
   - Strumento: “Tristar Tester” (Smartmod Pro / ICC Pro / JC programmer Tri-Star Tester).
   - Se lo strumento dice **“Tristar Fail”**: alta probabilità di Tristar.
   - **“Tristar Pass” non esclude** Tristar difettoso.

3. **DC power supply / DT880: consumo prima/dopo prompt di boot**
   - Se c’è **draw prima del prompt di boot**: secondo la fonte **non è Tristar** (indica corto sulla board).
   - Se **non** c’è draw prima del prompt, ma **dopo** il prompt la prima lettura è **≈0.150–0.250 A**: la fonte indica “definitivamente” **Tristar difettoso**.

4. **Controllo calore su Tristar (opzionale)**
   - Termocamera o freeze spray.
   - La fonte riporta che di solito Tristar scalda quando è guasto, ma **non sempre**.

5. **Tensione al connettore batteria: J2201**
   - Procedura (da fonte): collegare il **charging port flex** alla logica e **niente altro** (no schermo, no batteria, ecc.).
   - Inserire il cavo di ricarica.
   - Multimetro in **DC volts** e misurare i pin batteria **positivi e negativi** del connettore **J2201**.
   - La fonte specifica che sono **le 2 pin grandi su ciascun lato**; la polarità per la lettura **non è critica**.
   - Interpretazione (da fonte):
     - Se la tensione è **< ~2 V** → Tristar cattivo (tipicamente **0.300–0.600 V**).
     - Un circuito di carica funzionante mostra **~3.7 V**.

**Riparazione (da fonte):**
- Sostituzione **Tristar**.
- Per **iPhone 7 e 7 Plus** serve la versione **610A3B** (la fonte avverte di usare la versione corretta).

**Nota meccanica (da fonte):**
- Su iPhone 7/7 Plus Tristar è **parzialmente coperto da uno shield**.
- Raccomandazione: **non toccare** lo shield.
- La fonte suggerisce: rimuovere il chip “**a angolo**” e posizionare il nuovo Tristar “**a angolo**”.
- Tagliare lo shield aumenta il rischio di danni:
  - possibile contatto/penetrazione dello shield nel charging port al rimontaggio → **No Charging**.

**Verifica dopo sostituzione (da fonte):**
- Test USB charging con **schermo, batteria e charging port** noti buoni: dovrebbe essere simile a un iPhone funzionante (in genere **1 A o più**).
- Eseguire di nuovo il **Tristar Tester** (se disponibile).
- Con DC power supply: controllare la **prima lettura dopo prompt di boot** → dovrebbe essere **≈0.045 A**.
- Controllare se Tristar scalda ancora con **freeze spray** o **termocamera**.
- Rimisurare tensione su **J2201** → dovrebbe tornare a **~3.7 V**.

**Altre note dalla fonte (da fonte):**
- Ogni brick/cavo può dare letture USB leggermente diverse.
- Batterie quasi cariche caricano a corrente più bassa; batterie vecchie/usurate caricano a corrente più bassa.

### Caso: dead/no boot, impossibile DFU; DCPS 0 A poi 20–40 mA stabile (hang)

**Sintomi riportati (da fonte):**
- **No Power / Doesn't boot**: completamente dead.
- **Cannot get into DFU mode**.
- Con board collegata a **DC power supply**:
  - **0 A draw** prima del **prompt di boot**.
  - Dopo il **prompt di boot**, la corrente **salta a 20–40 mA** e **rimane stabile** (nessuna fluttuazione), poi “hang”.

**Diagnosi / causa indicata (da fonte):**
- Problema associato a **underfill** e **distacco/rottura** di induttanze vicino alla CPU.

**Soluzione (da fonte):**
1. **Clean underfill sopra CPU**.
2. **Clear out all underfill** attorno alle induttanze **L1801, L1804 e L3302**.
3. **Poke** (poking) le tre induttanze per verificare se si “rompono/staccano”.
4. Se una o più induttanze **si rompono**: **sostituire** le induttanze che si sono staccate.

**Valori induttanze (da fonte):**
- **L1801** — **1 μH**, **2.1 A**, **0.12 Ω**
- **L1804** — **1 μH**, **2.1 A**, **0.12 Ω**
- **L3302** — **1.2 μH**, **3.0 A**, **0.080 Ω**

**Nota importante (da fonte):**
- Non è possibile verificare se le induttanze sono allentate “poking” **con l’underfill ancora presente**: bisogna prima **rimuovere tutto l’underfill** attorno a L1801/L1804/L3302 e poi fare il poke.

**Attenzione meccanica (da fonte):**
- Le induttanze sono **premute molto vicino alla CPU**: fare attenzione con l’aria calda, perché si può accidentalmente “**float**” la CPU e causare un guasto più grave.

## Collegamenti utili
- [Tristar](../componenti/tristar.md)
- [C4005](../componenti/c4005.md)
- [Non carica o alimentazione instabile](../sintomi/non-carica-o-alimentazione-instabile.md)
- [Batteria](../componenti/batteria.md)
- [BB-PMU](../componenti/bb-pmu.md)
- [PMIC](../componenti/pmic.md)
- [Kraken IC](../componenti/hydra-ic.md)
- [DC power supply / DCPS](../strumenti/alimentatore-da-banco.md)
