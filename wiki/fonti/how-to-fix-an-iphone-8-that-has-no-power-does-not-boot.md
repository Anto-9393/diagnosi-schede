---
titolo: How To Fix an iPhone 8 That Has No Power. Does Not Boot — fonte esterna (repair.wiki)
tipo: fonte
riassunto: 'iPhone 8/8 Plus senza segni di vita: ispezione liquidi e ricerca corto
  su rail (PP_VDD_MAIN/PP_VDD_BOOST/PP_DISPLAY_BL*_ANODE/PP_SPKRAMP_TOP_VBOOST) con
  iniezione 4 V/2 A e localizzazione del condensatore in corto.'
modelli:
- iPhone 8
- iPhone 8 Plus
fonti:
- raw/repairwiki/pagine/how-to-fix-an-iphone-8-that-has-no-power-does-not-boot.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Fonte
- Repair.wiki: [How To Fix an iPhone 8 That Has No Power. Does Not Boot](https://repair.wiki/w/How_To_Fix_an_iPhone_8_That_Has_No_Power._Does_Not_Boot)
- Licenza: CC BY-SA 3.0
- Revisione fonte: 2024-01-30T06:36:58Z

## Cosa descrive (sintomi)
- **No Power / Does not turn on / No signs of life**
- **Does not boot**
- **Does not charge**
- Comportamento corrente (quando si arriva al “prompt to boot”):
  - “Pulls 2A or more”
  - prima del prompt: **0 A**
  - dopo il prompt: salto rapido tra **0 A** e valori come **320 mA**, **1.4 A**, **500 mA** (valori riportati dalla fonte)

## Soluzione proposta (diagnosi e riparazione)
### 1) Ispezione visiva e danni da liquidi
- Ispezione completa della scheda.
- Controllo di **danni da acqua** sotto gli adesivi sul retro.
- Rimozione della **schiuma attorno ai connettori** per migliorare la visibilità.
- Ricerca di **corrosione** su componenti e IC.

### 2) Se NON c’è danno da liquidi → “shorted capacitor” più probabile
- La fonte indica che, in assenza di danni da liquidi, la causa più probabile è un **condensatore in corto**.

### 3) Ricerca del corto “prima del prompt to boot”
La fonte suggerisce di controllare queste linee (rail) come più probabili:
- **PP_VDD_MAIN** (più probabile)
- **PP_VDD_BOOST** (di solito corto quando non è VDD MAIN)
- **PP_DISPLAY_BL_ANODE** oppure **PP_DISPLAY_BL34_ANODE** (a volte corto sul circuito backlight)
- **PP_SPKRAMP_TOP_VBOOST** (più raro)

**Localizzazione del condensatore**:
- Iniezione di tensione **4 V / 2 A** direttamente sulla linea misurata come in corto.
- Uso di **freeze spray** o **termocamera** per individuare il condensatore che scalda.

**Riparazione**:
- In questi casi la fonte indica che si può **rimuovere il condensatore in corto senza sostituirlo** e il dispositivo funzionerà normalmente.
- Motivo riportato: sostituire significherebbe aggiungere calore e aumentare il rischio.

### 4) Se c’è danno da liquidi
- La fonte consiglia di prestare attenzione alle aree con segni di liquido.
- Esempi di aree/IC dove la fonte riporta corrosione e possibile corto su **VDD MAIN**:
  - Sotto **BBPMU** e attorno (es. condensatori **C303_E**)
  - Parte alta posteriore (“back top arm”): **C4190, C4191, C4195, C4196**
  - Sopra e vicino al WiFi (WLAN_W): **C7608_W, C7609_W**
  - Parte alta front sopra CPU: **C3790**
  - A volte: vite allentata che mette in corto **TP0526** a massa (TP0526 è un test point vicino allo slot SIM, lato opposto alla CPU shield, sotto l’adesivo)

### 5) Nota su iniezione tramite connettore batteria (DCPS)
- Se si inietta tramite connettore batteria con alimentatore DC (es. iPower Pro / DT880), la fonte avverte che il **Tigris Mosfet Q3350** scalda **istantaneamente**.
- Motivazione riportata: la linea **PP_BATT_VCC** del connettore batteria collega **PP_VDD_MAIN** tramite **Q3350**, creando molta dissipazione.
- La fonte specifica che **Q3350 non ha connessione a GND**, quindi “non è shortabile” (secondo la fonte).

### 6) Ricerca del corto “dopo il prompt to boot”
- Controllare corti attorno a **NAND**.
- La fonte riporta spesso condensatori in corto associati a:
  - **PP3V0_NAND**
  - **PP0V9_NAND**
  - **PP1v8_IO**
- Anche qui: localizzazione con iniezione e termica.

### 7) Nota su PMIC (U2700) e calore durante test con DCPS
- La fonte indica che il **PMIC (U2700)** può mostrare molto calore quando si testa con DCPS collegato tramite connettore batteria.
- Interpretazione della fonte: il corto vero è nel condensatore vicino a NAND, ma la corrente deve passare dal PMIC per arrivare al condensatore, quindi il PMIC scalda.

### 8) Caso alternativo: corto su PP1V8_S2 o PP1V1_S2 → RAM short
- La fonte riporta che lo stesso comportamento può comparire se è corto **PP1V8_S2** o **PP1V1_S2**.
- Procedura indicata:
  - controllare **calore sopra la CPU**
  - se **PP1V8_S2** o **PP1V1_S2** è corto e si trova calore sopra la CPU → **RAM short**
- Riparazione indicata: **sostituire RAM**.
- Avvertenza: riparazione “molto avanzata”; rischio di danneggiare la CPU.

## Collegamenti alle pagine wiki (per componenti/tecniche)
- Tecniche di ricerca corto e diagnosi su rail: [tecniche/diagnosi-e-rimozione-corto-su-rail-con-capacitore-in-corto.md](../tecniche/diagnosi-e-rimozione-corto-su-rail-con-capacitore-in-corto.md)
- Test DCPS/diagnosi Kraken IC: [tecniche/test-dcps-e-diagnosi-kraken-ic.md](../tecniche/test-dcps-e-diagnosi-kraken-ic.md)
- Componenti rilevanti citati dalla fonte (sigle/IC):
  - [componenti/pmic.md](../componenti/pmic.md) (PMIC U2700 citato dalla fonte)
  - [componenti/condensatori-mlcc-elettrolitici-tantalio.md](../componenti/condensatori-mlcc-elettrolitici-tantalio.md) (condensatore in corto)
  - [componenti/hydra-ic.md](../componenti/hydra-ic.md) (da verificare: non citato esplicitamente nella fonte)
  - [componenti/tristar.md](../componenti/tristar.md) (da verificare: non citato esplicitamente nella fonte)
  - [componenti/kraken-ic-usb.md](../componenti/kraken-ic-usb.md) (da verificare: non citato esplicitamente nella fonte)
  - [componenti/cd3217.md](../componenti/cd3217.md) (da verificare: non citato esplicitamente nella fonte)

> Nota: la fonte esterna non fornisce sigle “wiki” per tutti i componenti citati (es. Q3350, U2700, TP0526, BBPMU, RAM). Dove non esiste una pagina componente con la stessa sigla, lasciare “da verificare”.
