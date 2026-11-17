---
titolo: U9500 — test 5V pad e distinzione da Tigris (wireless charger)
tipo: tecnica
riassunto: 'Integra la tecnica: cavo genuino + ispezione porta, heat/short vicino
  a U9500, controllo U9500/U9720 e verifica 5V sul pad sotto per distinguere U9500
  vs Tigris.'
modelli: []
fonti:
- raw/repairwiki/pagine/iphone-15-pro-max-not-charging-and-no-touch.md
- raw/repairwiki/pagine/iphone-15-series-no-touch-no-charging.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Scopo
Diagnostica rapida del circuito USB‑C/riconoscimento accessori quando **non carica** e/o **non funziona il touch**: distinguere se il problema è dovuto a **U9500** (chip che rileva cosa è connesso alla porta USB‑C) oppure a **Tigris**.

> Nota: la fonte collega questo scenario a iPhone 15 Pro Max, ma la procedura qui sotto è scritta come tecnica generale.

## Attrezzatura
- [multimetro](../strumenti/multimetro.md)
- Alimentatore/charger da banco (o caricatore USB‑C) per alimentare la linea di ricarica
- Amp meter (misura corrente in ricarica)
- (Consigliato) Wireless charger per test funzionale
- (Per rework) Stazione ad aria calda + flussante/strumenti di pulizia
- (Per ispezione) Termocamera (o rosin + IPA per evidenziare heat/short)

## 1) Prima regola: escludere componenti “ovvi”
1. Testare display e batteria con componenti noti buoni.
2. Se **non carica**, non concludere automaticamente che sia U9500: la fonte indica che può essere anche **Tigris**.

## 2) Distinguere U9500 vs Tigris con wireless charger
1. Prova a caricare il dispositivo con un **wireless charger**.
2. Interpretazione (da fonte):
   - Se **carica via wireless**, allora **Tigris IC è probabilmente funzionante**.
   - Se **non carica via wireless**, la diagnosi su U9500/Tigris va comunque confermata con misure (passi successivi).

## 3) Verifiche “a monte” (cavo/porta/touch-combo)
Questa sezione integra il flusso diagnostico della fonte:
1. **Test con cavo genuino + adapter**: confermare che il problema persiste anche con accessori originali.
2. **Ispezione porta USB‑C**: controllare corrosione o detriti dentro la porta; pulire se necessario.
3. **Touch + Charge combo fault**: se **sia touch che charge** non funzionano, la fonte indica di sospettare **U9500 immediatamente**.

## 4) Heat/short vicino a U9500 + ispezione visiva U9500/U9720
Dopo apertura:
1. Usare **termocamera** (o rosin + IPA) per rilevare **heat/short** vicino all’area di **U9500**.
2. Ispezione visiva di **U9500** e **U9720** per danni.

> La fonte non fornisce valori/criteri numerici: la valutazione è “da verificare” in base a boardview e condizioni operative.

## 5) Verifica fondamentale: U9500 deve avere 5V sul pad sotto
La fonte specifica che **per funzionare U9500 deve avere 5V sul pad sotto**.

### Procedura di misura (da fonte)
1. **Separare la motherboard** (necessario per accedere al pad sotto U9500).
2. **Connettere la charging port**.
3. Collegare la scheda a un **charger**.
4. Misurare la tensione sul **pad sotto U9500**.

### Interpretazione (da fonte)
- Se misuri **5V all’ingresso**, significa che **U9500 sta ricevendo alimentazione** e “dovrebbe” funzionare.
- Se **non trovi 5V**, il problema è a monte (da verificare: alimentazioni/rail/connessioni), e U9500 potrebbe non essere alimentato correttamente.

**Valori attesi (da fonte):** **5V** sul pad sotto U9500 (condizione: motherboard separata, charging port connessa, dispositivo collegato a charger).

## 6) Verifica corrente in ricarica con amp meter (funzionalità)
Dopo aver confermato/risolto (o durante test di funzionalità), la fonte propone di misurare la corrente assorbita dal telefono.

### Setup di test (da fonte)
- Collegare **charging port**, **screen** e **battery** alla parte superiore (top board).
- La fonte indica che l’iPhone 15 Pro Max può **power on con solo top board**.

### Misura (da fonte)
1. Collegare il telefono a un **charger**.
2. Usare un **amp meter** per misurare la corrente che il telefono sta ricevendo.

### Interpretazione (da fonte)
- Per “fast charge” (quando applicabile):
  - dovrebbe **draw 9V**
  - e **circa 2+ A**, “a seconda della capacità batteria”.

**Valori da fonte:** **9V** e **~2+ A** in fast charge (condizione: test con fast charger, misurazione con amp meter).

## 7) Collegamento con ROM IC (U9720) — implicazione diagnostica
La fonte evidenzia che **U9500 non lavora da solo**: funziona in congiunzione con **ROM/EEPROM IC U9720**.

- Se **U9500 o U9720** falliscono o risultano **mismatched**, il telefono può perdere **charging** e potenzialmente anche **touchscreen**.
- Per la sostituzione: la fonte indica che i due chip sono **encrypted e paired**, quindi per sostituire U9500 serve anche **U9720**.
- La fonte indica anche un vincolo di sourcing: componenti da **donor board same-model** (non da iPhone 15 o 15 Pro).

Vedi componenti:
- [U9500](../componenti/u9500.md)
- [U9720](../componenti/u9720.md)

## Rischi / note operative
- La misura “5V sul pad sotto” richiede **separazione motherboard**: rischio di danneggiare connettori/flat e di introdurre ossidazioni se non si lavora pulito.
- La fonte non fornisce valori “attesi” per correnti in ricarica non-fast: per i valori intermedi **da verificare**.

## Collegamenti utili
- [U9500](../componenti/u9500.md)
- [U9720](../componenti/u9720.md)
- [Tigris IC](../componenti/rigel-u4400.md) (da verificare: la sigla/IC esatta dipende dalla boardview)
- [Amp meter / strumenti di misura](../strumenti/multimetro.md)
