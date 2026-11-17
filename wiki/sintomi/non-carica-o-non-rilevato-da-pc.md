---
titolo: Sintomo — non carica e non rilevato da PC (nessun suono USB)
tipo: sintomo
riassunto: 'Pattern: iPad non carica + PC non lo rileva (iTunes/3uTools) anche in
  recovery/DFU; spesso coinvolge Tristar o controller USB-C/PD (CD3217/CD3215) prima
  dell’IC di carica.'
modelli:
- iPad Pro 10.5
- iPad Air 4 (A2316)
fonti:
- raw/repairwiki/pagine/how-to-repair-ipad-pro-10-5-not-charging-or-not-detected-by-pc.md
- raw/repairwiki/pagine/ipad-7-not-charging.md
- raw/repairwiki/pagine/ipad-pro-11in-1st-gen-not-recognized-by-pc-in-recovery-mode-or-charging-issues.md
- raw/casi_demo/ipad-air-4-a2316-non-carica.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Pattern riconosciuto
- iPad **non carica**
- nessuna icona di carica / nessun fulmine
- il **PC non rileva** il dispositivo (nessun suono USB; iTunes/3uTools non lo vedono)
- spesso **non c’è comunicazione/dati**
- sostituire cavo e alimentatore **non risolve**
- il dispositivo può comunque **accendersi** se la batteria ha carica

Fonti: pagina sintomo esistente (iPad Pro 10.5) + caso demo iPad Air 4 A2316 (caffè).

## Cause possibili (ordine di probabilità)
1. **Controller USB/charging (CD3217 su alcuni iPad, o Tristar su altri)**
   - La pagina esistente per iPad Pro 10.5 indica “in most cases” Tristar come causa.
   - Il caso iPad Air 4 A2316 mostra che, dopo pulizia e sostituzione flat USB-C, il problema resta e la diagnosi porta a sospettare **CD3217B12 (X5)** e/o alimentazioni/passivi attorno al CD3217.
   - Link: [Tristar](../componenti/tristar.md), [CD3217](../componenti/cd3217.md).

2. **Corrosione attiva nel connettore/porta USB-C**
   - Nel caso A2316 la corrosione attiva è stata evidenziata con misure in **diode mode** sulla porta (VBUS lato A instabile; segnali D+/D− instabili; ponte verso GND che va e viene).
   - Anche se il flat è stato sostituito, la corrosione/contaminazione può aver danneggiato alimentazioni/passivi a valle.

3. **Dock/porta di ricarica (dock flex) difettosa**
   - La pagina esistente prevede un dock test sostituendo il dock flex con uno noto-good.
   - Nel caso A2316 la sostituzione del flat/connettore USB-C **non ha risolto**.

4. **ROM/firmware abbinata al controller USB-C/PD (CD3217)**
   - Nel caso A2316 viene indicato che la ROM del CD3217 va in coppia con il CD3217 e che, se si sostituisce il chip da donor, va trasferita la ROM dello stesso donor oppure riprogrammata con Wylie.
   - Da verificare: impatto reale su questo specifico caso (la diagnosi aggiornata sospetta CD3217 più che la ROM, ma la ROM resta tra le ipotesi).

## Integrazione diagnostica: “non carica + PC non rileva”
### Logica di priorità
Quando il PC non rileva e non carica, la fonte esistente (iPad Pro 10.5) e il caso A2316 indicano di dare priorità a ciò che gestisce **sia alimentazione sia comunicazione** (porta/USB-C + controller USB/PD), prima di arrivare all’IC di carica.

### Punti di fallimento (da fonte esterna, compatibilità da verificare)
La pagina esistente integra un riferimento esterno (iPad Pro 11in 1st Gen) che cita tre punti principali:
1. **Charge port**
2. **CD3215**
3. **Tristar 610A3C**

> Nota: la compatibilità tra modelli va verificata. Nel caso iPad Air 4 A2316 il controller coinvolto è **CD3217B12** (non CD3215) e l’IC di ricarica indicato è **343S00264**.

## Misure utili (dal caso A2316 e dalla pagina esistente)
### 1) Porta USB-C — diode mode (corrosione/short intermittenti)
Dal caso iPad Air 4 A2316 (Mech T-824 SE, diode mode):
- **VBUS (pin 4/9/16/21)**: lettura bassa anche da sana; lato A **instabile** (es. 0.00 → lato A 0.69/0.38 → di nuovo tutti 0.00).
- **D+/D− lato A (6/7)**: **instabile** (es. 0.71 → 1.00 → 0.70).
- **RX1+ (23)**: **OL → 0.00 → OL → 0.00** con ponte verso **GND (pin 24)** che va e viene.

Conclusione del caso: **corrosione attiva nel connettore vecchio**.

### 2) Alimentazione/negoziazione USB — comportamento con/senza batteria
Dal caso A2316:
- Senza batteria, USB dall’AiXun: **5,2 V, 0,11–0,20 A**, resta a **5 V** (nessuna negoziazione PD).
- Con batteria e iPad acceso, cavo inserito: **0,002 A** (non prende corrente dall’USB).
- Batteria: **3,66 V** → scesa a ~**2,9–3,1 V**; ricaricata dal banco a **4,2 V** fino a **3,8 V / 45%**.

Interpretazione operativa (da caso): se con batteria il controller non “chiude” il passaggio verso il power path, il sintomo “non carica + PC non rileva” è coerente.

### 3) Verifica passaggio VBUS verso l’IC di ricarica (CD3217 → X3)
Dal caso A2316 (JC Drawing):
- **NET205 (VBUS dal connettore flat)**: 5 V fino a **X5 = CD3217B12**.
- Uscita CD3217 verso **X3** (X1548/X1549/X1550):
  - prima misura: **4,7 V** (probabilmente in condizioni senza batteria / modalità “dead battery”)
  - con batteria + cavo: **0,026–0,186 V** (CD3217 non chiude il passaggio verso X3).

### 4) IC di ricarica (343S00264) — calore indicativo
Dal caso A2316:
- **X3 = 343S00264-A0**: “scalda subito col cavo inserito”; senza cavo si asciuga lentamente.

## Dove si trova (indicazioni dal caso)
- Nel caso A2316 il controller coinvolto è **CD3217B12 (X5)**.
- La posizione fisica di Tristar è descritta nella fonte esterna citata dalla pagina esistente (hidden underneath shield sopra i connettori FPC, al centro della board), ma per questo sintomo la pagina esistente non conferma Tristar per A2316: **da verificare**.

## Collegamenti utili
- [Tristar](../componenti/tristar.md)
- [CD3217](../componenti/cd3217.md)
- [Tecnica — test Tristar e diagnosi non carica iPhone](../tecniche/test-tristar-e-diagnosi-non-carica-iphone.md)
- [Tecnica — test CD3217 e ricerca corti](../tecniche/test-cd3217-e-ricerca-corti.md)
- [iPad Air 4 (A2316) — non carica (caso)](../casi/ipad-air-4-a2316-non-carica.md)
- [iPad Pro 10.5 — non carica (caso)](../casi/ipad-air-4-a2316-non-carica.md) 

> Nota: il link “iPad Pro 10.5 — non carica” non è presente tra le pagine del piano fornite; da verificare.
