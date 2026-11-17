---
titolo: 'Alimentatore da banco (DC power supply) — sul banco: AiXun P2408S'
tipo: strumento
riassunto: 'DCPS AiXun P2408S: lettura corrente in “prompt to boot” e, se serve, localizzazione
  corto con iniezione a bassa tensione + termica/freeze spray.'
modelli:
- AiXun P2408S
fonti:
- raw/repairwiki/pagine/how-to-diagnose-fix-an-iphone-7-that-does-not-charge-takes-0-006a-via-usb.md
- raw/banco/miei-attrezzi.md
- raw/repairwiki/pagine/how-to-fix-an-iphone-8-that-has-no-power-does-not-boot.md
- raw/repairwiki/pagine/how-to-fix-iphone-x-that-does-not-power-on.md
- raw/repairwiki/pagine/iphone-11-pro-and-iphone-11-pro-max-not-powering-on-2a-or-higher-power-draw-after-prompt-to-boot.md
- raw/repairwiki/pagine/short-circuits-repair-basics.md
- raw/repairwiki/pagine/how-to-fix-an-iphone-12-pro-that-is-not-charging-and-touch-not-working.md
- raw/repairwiki/pagine/how-to-fix-iphone-7-that-does-not-turn-on-hangs-at-0-020-0-030-a-after-you-prompt-to-boot-on-dc-power-supply.md
- raw/repairwiki/pagine/how-to-fix-iphone-x-that-does-not-charge.md
- raw/repairwiki/pagine/how-to-repair-ipad-6-no-power.md
- raw/repairwiki/pagine/how-to-repair-ipad-pro-10-5-not-charging-or-not-detected-by-pc.md
- raw/repairwiki/pagine/ipad-7-not-charging.md
- raw/casi_demo/ipad-air-4-a2316-non-carica.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Scopo
- **Diagnosi “non power / non boot”** tramite lettura della **corrente assorbita** durante la sequenza di avvio (“**prompt to boot**”).
- **Localizzazione di un corto** (se la fonte lo indica): iniettare tensione a bassa tensione sulla rail/linea sospetta e usare **termocamera** o **freeze spray** per individuare il componente che scalda prima.

> Cautela (da fonte “Short Circuits - Repair Basics”): **non superare i rating V/I della rail** e **partire da 1 V**.

## Dove si usa in diagnosi (workflow)
1. Collegare il dispositivo all’**alimentatore da banco** (DCPS).
2. Eseguire il **prompt to boot**.
3. Confrontare **corrente prima** e **corrente dopo** il prompt:
   - **Short prima del prompt** → interpretazione come **short sul board** (pattern da fonte).
   - **Short dopo il prompt** → pattern compatibile con **bad Tristar** (pattern da fonte).

## Lettura corrente: comportamento atteso (da fonte)
### 1) Short **prima** del prompt to boot
Se la fonte osserva assorbimento **prima** del prompt to boot, allora (da fonte) è interpretato come **short sul board**.

Linee “più probabili” da controllare (da fonte):
- **PP_VDD_MAIN**
- **PP_VDD_BOOST** (di solito shortata quando non è VDD MAIN)
- **PP_SPKRAMP_TOP_VBOOST** (più rara)

### 2) Short **dopo** il prompt to boot (pattern “Tristar”)
Se **non** c’è assorbimento prima del prompt, ma **dopo** il prompt la prima lettura è **≈ 0.150–0.250 A**, allora (da fonte) indica **bad Tristar**.

Inoltre la fonte riporta un comportamento a salti (da fonte):
- **0 A > 320 mA > 0 A > 1.4 A > 0 A > 500 mA**

### 3) Dopo sostituzione Tristar (verifica)
La fonte indica che dopo la sostituzione la **prima lettura** dopo il prompt to boot dovrebbe essere **≈ 0.045 A**.

## Modello sul banco e nota operativa (da fonte banco)
- Sul banco viene usato un **AiXun P2408S** come DCPS.
- **“I-Range Show”**: cambia **solo la scala della lancetta**, **non il limite di corrente**.
- I **numeri rossi in alto** sono le **misure reali**.

> Valori “tensione/corrente max” dell’unità: **da verificare** (placeholder presenti nella pagina già esistente).

## Integrazione: misure AiXun (da caso reale iPad Air 4 A2316)
Dal caso reale (iPad Air 4 Wi‑Fi **A2316**) la fonte riporta come comportamento tipico dell’alimentazione da banco:
- **Senza batteria**, alimentando via USB dall’AiXun: **5,2 V, 0,11–0,20 A** (nessuna negoziazione PD; resta a 5 V).
- **Con batteria e iPad acceso**, con cavo inserito: **0,002 A** (non prende corrente dall’USB).
- **Ricarica batteria** dal banco: **4,2 V, ~2–3 A** fino a **3,8 V / 45%**.

Questi valori sono utili come **criteri di lettura** per capire se il problema è “manca passaggio VBUS/charging” o se c’è un comportamento compatibile con corto (da verificare sul singolo caso).

## Iniezione tensione per localizzare il corto (da fonte + precauzioni)
### Quando usarla
Se la diagnosi porta a sospetto di corto su una rail/linea e non si riesce a identificarlo solo con ispezione/termica.

### Come farla (da fonte)
1. Identificare la **linea/rail** misurata come corto.
2. **Iniettare 4 V / 2 A** direttamente sulla linea/rail sospetta.
3. Usare **freeze spray** o **termocamera** per individuare il **condensatore in corto**.

> Dalla fonte: in questi casi puoi **rimuovere** il condensatore in corto e il dispositivo può funzionare normalmente senza sostituirlo.

### Precauzioni (integrazione dalla fonte “Short Circuits - Repair Basics”)
- **Non superare mai i rating V/I** della rail.
- **Partire da 1 V**: la fonte indica che è “di solito sicuro per quasi tutte le rail”.
- Se possibile, preferire approcci a basso rischio (ispezione visiva, controllo componenti caldi, termica) prima dell’iniezione.

## Termica / freeze spray per trovare il componente
- Durante l’iniezione o l’alimentazione controllata della linea sospetta, l’area del corto tende ad avere **maggiore flusso di corrente** e quindi **maggiore dissipazione**.
- Tecniche riportate:
  - **termocamera** per vedere quale componente scalda prima/di più
  - **freeze spray** (o aria compressa spruzzata “al contrario”) per evidenziare il componente che cambia temperatura per primo

## Rischio specifico: DCPS via connettore batteria (da fonte)
Se usi un **DC power supply** per iniettare tensione attraverso il **connettore batteria**:
- **Yangtze può scaldare istantaneamente**.

Motivo (da fonte):
- la linea del connettore batteria **PP_BATT_VCC** collega **PP_VDD_MAIN** tramite **Q3350**, creando molta dissipazione.
- in base alla fonte, **Q3350 non ha connessione a ground**, quindi (secondo la fonte) non è “shortabile” in quel contesto.

## Calore del PMIC durante il test (da fonte)
- La fonte segnala che il **PMIC (U2700)** può mostrare **molto calore** quando il DCPS è connesso tramite il connettore batteria.
- La fonte precisa che **non significa necessariamente** che il PMIC sia la causa: il corto è spesso sul condensatore vicino a NAND, ma la corrente deve passare dal PMIC per arrivare al corto.

## Collegamenti utili
- [Tristar](../componenti/tristar.md)
- [Tecnica: test Tristar e diagnosi non carica iPhone](../tecniche/test-tristar-e-diagnosi-non-carica-iphone.md)
- [Sintomo: non carica o alimentazione instabile](../sintomi/non-carica-o-alimentazione-instabile.md)
- [Tecnica: test DCPS e diagnosi Kraken IC](../tecniche/test-dcps-e-diagnosi-kraken-ic.md)

## Limiti / note operative (da verificare)
- **Tensione/corrente max** dell’**AiXun P2408S**: **da verificare**.
- La fonte non fornisce settaggi numerici del DCPS (limiti/corrente impostata): **da verificare**.

## Rischi pratici
- Evitare prove ripetute “a caso”: la fonte descrive pattern legati a tentativi di boot.
- Se il pattern indica **dead short** (es. spike >1 A su iPad 6), procedere con diagnosi su corti/rail prima di insistere con avvii ripetuti (da verificare la procedura esatta nella fonte).
- Se osservi **power cycling**/tensione instabile, considera che potrebbe essere dovuto a **OCP/active current limiting** dell’alimentatore (fonte esterna): interpreta la misura come “fault presente” finché non viene rimosso il corto/guasto.
