---
titolo: Test DCPS e diagnosi Kraken IC (catena 5V / Tristar)
tipo: tecnica
riassunto: Usa DCPS per osservare il comportamento in prompt-to-boot e, in parallelo,
  verifica la catena 5V (5V in → MOSFET → Tristar) con misure su diode scale e test
  termico per localizzare corto/guasto.
modelli: []
fonti:
- raw/repairwiki/pagine/how-to-fix-an-iphone-12-pro-that-is-not-charging-and-touch-not-working.md
- raw/repairwiki/pagine/how-to-fix-an-iphone-8-plus-boot-looping-on-apple-logo-and-random-charging.md
- raw/repairwiki/pagine/how-to-fix-an-iphone-8-that-has-no-power-does-not-boot.md
- raw/repairwiki/pagine/how-to-fix-iphone-7-that-does-not-turn-on-hangs-at-0-020-0-030-a-after-you-prompt-to-boot-on-dc-power-supply.md
- raw/repairwiki/pagine/how-to-repair-ipad-6-no-power.md
- raw/repairwiki/pagine/how-to-repair-ipad-pro-10-5-not-charging-or-not-detected-by-pc.md
- raw/repairwiki/pagine/ipad-7-not-charging.md
- raw/repairwiki/pagine/ipad-pro-11in-1st-gen-not-recognized-by-pc-in-recovery-mode-or-charging-issues.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Scopo
Questa tecnica integra due aspetti diagnostici:
1) **osservazione con [DC power supply (DCPS)](../strumenti/alimentatore-da-banco.md)** del comportamento di assorbimento quando il dispositivo entra in **prompt to boot**;
2) **verifica della catena di alimentazione 5V di carica** (5V in arrivo → MOSFET → **Tristar**), per distinguere guasti su **charge port / filtri / MOSFET** da guasti su **Tristar**.

> Nota: la parte “DCPS/prompt-to-boot” è presente nella pagina tecnica esistente; la parte “catena 5V” e i dettagli su CD3215/Tristar derivano dalla fonte esterna fornita (da verificare l’estensione esatta a “Kraken IC” su tutti i modelli).

## Quando usarla
- Sintomi di **non carica** (anche se il dispositivo si accende ma non carica).
- Si sospetta guasto su **charge port / circuito di carica** o su **Tristar**.
- In presenza di comportamento anomalo su DCPS in prompt-to-boot.

## Attrezzatura
- [DC power supply (DCPS)](../strumenti/alimentatore-da-banco.md) (disponibile sul banco).
- Multimetro con modalità **diode scale**.
- **Termocamera** o **freeze spray** (per distinguere quale componente scalda per primo su una linea in corto).
- Microscopio (consigliato) per ispezione e controllo pad/saldature.

## Procedura

### 1) Diagnosi rapida con DCPS (prompt-to-boot)
1. Collegare il dispositivo al **DCPS**.
2. Osservare la **corrente** durante la fase di **prompt to boot**.
3. Criteri riportati dalla pagina tecnica esistente:
   - **Ramping atteso**: **0.050 A → 0.060 A → 0.100 A → … → 1.00 A**.
   - **Spike istantaneo > 1.00 A**: indicativo di **dead short**.
   - **Spike istantaneo a ~0.150 A con reset/cycling**: indicativo di **Tristar failure**.
   - **Salto diretto a 0.200 A** durante prompt to boot: probabile fault nella path **Hydra/Tristar/PMIC**.
   - Integrazioni presenti nella pagina esistente:
     - iPad Pro 10.5: criterio pratico **< 100 mA al click iniziale**.
     - iPhone 8: pattern “salto rapido” tra **0 A** e valori diversi.
     - iPhone 7: **0 A prima del prompt**, poi **20–40 mA stabile** durante prompt-to-boot (indirizza a controlli meccanici/underfill su L1801/L1804/L3302).

### 2) Verifica catena 5V di carica (approccio “linea in corto” + test termico)
Questa parte segue la logica della fonte esterna: prima si identifica il punto di guasto tra **charge port** e IC di gestione/commutazione, poi si usa un test “a bassa tensione” per localizzare il componente che scalda per primo.

#### 2.1 Ispezione visiva (prima di alimentare)
- Controllare **charge port** e zona circostante per **detriti**, **danni fisici** o **liquido/ossidazione**.

#### 2.2 Verifica “charge port” come punto di fallimento
- La fonte esterna indica che su quel caso il **charge port non è saldato alla board** e può essere **swap** con un **port noto buono**.
- Se non si dispone di un port noto buono, provare **più porte**.

#### 2.3 Diagnosi CD3215 (USB-PD 15V) — solo se il sintomo è “carica solo a 15V”
- La fonte esterna indica che il **CD3215** gestisce la carica da **USB-PD**.
- Se l’iPad **carica via USB-A 5V** ma **non negozia 15V** con un caricatore USB-C PD (capace di 15V), la fonte indica **CD3215** come sospetto.
- Test consigliato dalla fonte:
  - con multimetro in **diode mode**: “probe” sui **capacitori attorno al CD3215**.
  - configurazione: **red probe su ground** e **black probe** su ciascun lato del **capacitore**, per verificare che **nessun condensatore sia in corto verso ground su entrambi i lati**.

#### 2.4 Diagnosi Tristar (5V USB-A) — accesso e test corto
- La fonte esterna indica che il **Tristar 610A3C** gestisce principalmente la carica **5V USB-A** (non 15V PD).
- Nota compatibilità: la fonte indica che il Tristar “A3C” **non è retro-compatibile** con altri Tristar.
- Accesso fisico: la fonte indica che il Tristar è **nascosto sotto una parte dello shield** sopra i connettori FPC al centro della board; per accedere può servire rimuovere parte dello shield (es. grinding tool o snips).
- Test corto attorno al Tristar:
  - come per CD3215, usare multimetro in **diode mode** per cercare **capacitori shortati** attorno all’IC.

### 3) Localizzazione del componente in corto con DCPS “a bassa tensione” + termica
Questa è la parte più “DCPS/diagnosi” della fonte esterna: si inietta una **piccola tensione** sulla linea e si osserva quale componente scalda per primo.

#### 3.1 Preparazione
- Impostare un **DC power supply** a **bassa tensione**: **1 V / 1 A** (come da fonte).
- Configurazione sonde (come da fonte):
  - **black probe su ground**
  - **red probe** sul **lato del condensatore** che **non** è connesso a ground.

#### 3.2 Osservazione termica
- Usare **termocamera** o **freeze spray** per capire se:
  - scalda per primo un **capacitore** sulla linea in corto, oppure
  - scalda per primo l’**IC** (CD3215 o Tristar).

#### 3.3 Azione correttiva
- Se scalda per primo un **capacitore**:
  - rimuoverlo con blade o pry tool (la fonte indica che dovrebbe essere “loose” e facile da rompere),
  - poi verificare con multimetro in **diode mode** che il corto **non** sia più presente.
- Se il corto è su **CD3215**:
  - sostituire l’IC.
  - dopo sostituzione: verificare che il corto sia sparito e che l’iPad torni a negoziare/caricare come previsto (15V su PD se applicabile) e che sia riconosciuto da iTunes/3uTools anche in recovery/DFU.
- Se il corto è su **Tristar 610A3C**:
  - stessa logica: se trovi corto su capacitore, rimuovi/risolvi il corto; se non trovi corto o resti sospettoso, sostituisci il Tristar.
  - dopo sostituzione: verificare che il corto sia sparito e che l’iPad carichi a **5V** con USB-A e che sia riconosciuto da iTunes/3uTools anche in recovery/DFU.

## Riparazione (da fonte)
- **Charge port**: la fonte indica che su quel caso il port è sostituibile (non saldato alla board) rimuovendo il vecchio e montando il nuovo.
- **CD3215**: sostituzione dell’IC se confermato corto/guasto.
- **Tristar 610A3C**:
  - rimozione con **hot air station**,
  - pulizia pad,
  - **reball** se non è pre-balled,
  - risaldatura.

## Test finale (da fonte)
- Se riparato **charge port**: verificare **carica** e **data transfer**; testare anche **speaker** (entrambi).
- Se riparato **CD3215/Tristar**: verificare che l’iPad **carichi** (secondo la modalità corretta: 5V USB-A e/o 15V USB-C PD) e che sia riconosciuto da **iTunes/3uTools** anche in recovery o DFU.

## Collegamenti utili
- [DC power supply (DCPS)](../strumenti/alimentatore-da-banco.md)
- [Tristar](../componenti/tristar.md)
- [Kraken IC — USB](../componenti/kraken-ic-usb.md)
- [CD3217](../componenti/cd3217.md)
- [CD3217 — test e ricerca corti](../tecniche/test-cd3217-e-ricerca-corti.md)
- [Test Tristar e diagnosi non carica iPhone](../tecniche/test-tristar-e-diagnosi-non-carica-iphone.md)
- [Test diodi](../tecniche/test-diodi.md)
- [Termocamera](../strumenti/termocamera.md)
