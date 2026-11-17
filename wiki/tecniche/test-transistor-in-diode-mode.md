---
titolo: Test transistor in diode mode (BJT/FET/IGBT)
tipo: tecnica
riassunto: 'Tecnica generale per verificare transistor con multimetro in diode mode:
  criteri OL/valori attesi e precauzioni su pinout e corti.'
modelli: []
fonti:
- raw/repairwiki/pagine/transistors-repair-basics.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Scopo
Verificare rapidamente se un transistor (BJT, FET/MOSFET, IGBT) è **in corto** o **aperto/fuori specifica** usando il multimetro in **diode mode**, interpretando i risultati come “due diodi” (BJT) o come giunzioni gate/DS (FET) e presenza della **freewheeling diode** (IGBT).

> Valori attesi e criteri: dalla fonte (da usare come riferimento, non come garanzia assoluta su ogni circuito).

- **BJT (giunzioni PN):** tipicamente **0.6–0.7 V**; per **Germanium** **0.2–0.5 V**.
- **IGBT (E–C con diode freewheeling):** tipicamente **0.4–0.7 V**.
- **FET (G–S e verifica D–S dopo “carica/scarica” gate):** in diode mode ci si aspetta **OL** se guasto; in funzionamento D–S deve dare **caduta molto bassa (vicina a 0)** dopo aver “attivato” il gate.

## Attrezzatura
- **Multimetro** con modalità **diode mode**.
- (Opzionale) **LCR meter** per misurare capacità gate (G–S o G–E) e confrontare con datasheet/simili (da verificare su disponibilità e compatibilità).

Strumenti collegati:
- [Multimetro](../strumenti/multimetro.md)

## Precauzioni (obbligatorie)
1. **Pinout prima di tutto:** la fonte insiste che, se il pinout non coincide, si rischia di danneggiare tutto il circuito. Se non sei sicuro del pinout, fermati e identifica i pin corretti.
2. **Controllo corto prima del diode mode:** per FET, prima di passare al diode mode, misura **resistenza D–S**; se è **< 100 Ω** il componente è in corto.
3. **Transistor può avere guasti “non visibili” solo con diode mode:** anche se le giunzioni “diodo” sembrano ok, possono esistere **leakage** o guasti tra altri terminali (da verificare sul caso).
4. **Power BJTs/IGBT:** alcuni modelli possono avere **flyback/freewheeling diodi interni**; questo può influenzare le letture (da verificare su specifico componente).

## Procedura generale
### 1) Ispezione visiva
- Corrosione pin/metal shell (se presente)
- Pin rotti
- Surriscaldamento: discolorazione, burn marks, crepe

(da fonte: elenco segni di deterioramento)

### 2) Se possibile, identifica pinout
- Se il pinout non è noto, la fonte suggerisce di trovare la configurazione “BJT come due diodi con terminale comune” provando combinazioni in diode mode.
- Per FET/IGBT: identificare G/D/S (o G/E/C) in base a documentazione o schema (da verificare).

### 3) Test in diode mode (per tipo)
Vai alla sezione corretta.

---

## BJT (NPN/PNP) — “due diodi con terminale comune”
### Cosa aspettarsi
- Un BJT sano in diode mode si comporta come **due giunzioni PN**: due letture “diodo” con **un terminale comune**.
- Per **NPN:**
  - **rosso su B (base)**, **nero su E (emitter)** e poi su C (collector): in entrambi i casi lettura **~0.6–0.7 V** (oppure **0.2–0.5 V** per Germanium).
- Per **PNP:**
  - ripeti ma **inverti i puntali** (nero su base) e devi ottenere valori equivalenti.

### Criteri guasto
- Se misuri **OL** o una caduta **sostanzialmente più alta o più bassa** rispetto ai valori attesi → **transistor guasto**.

### Test aggiuntivo: corto/leakage C–E
- Imposta multimetro su **resistenza massima** (o autoscale).
- Misura **R tra C ed E**:
  - **< 100 Ω** → BJT **in corto**.
  - Valori in **decine di kΩ fino a MΩ** → possibile **leakage** (non necessariamente inutilizzabile: dipende dal circuito).
- Prova anche con polarità invertita: se trovi **valore basso in una direzione** e **alto nell’altra**, può esserci un **flyback diode** interno.

---

## FET / MOSFET — gate attiva D–S
### Cosa aspettarsi
La fonte descrive che il FET conduce tra **drain (D)** e **source (S)** quando il **gate (G)** viene “caricato” rispetto a S.

### 1) Controllo corto D–S
- Misura **resistenza tra D e S**.
- Se **< 100 Ω** → FET **in corto**.

### 2) Test in diode mode (G–S e poi D–S)
- Metti multimetro in **diode mode**.
- **N-Channel:**
  1. **rosso su G**, **nero su S**.
  2. **poi** sposta rapidamente il puntale rosso su **D**.
  3. D–S deve risultare con **caduta molto bassa (vicina a 0)** → conferma funzionamento.
- **P-Channel:**
  - stessa logica ma **inverti i puntali** (nero su G).

### Criteri guasto
- Se leggi **caduta alta** o **OL** → FET **difettoso**.

### (Opzionale) Capacità gate
- Se hai **LCR meter**, misura la **capacitá G–S** e confronta con datasheet/simili.

---

## IGBT — verifica freewheeling diode e E–C
### Cosa aspettarsi
La fonte indica che spesso l’IGBT include una **freewheeling diode** in reverse parallel.

### Procedura
1. Identifica i pin: **G (gate), E (emitter), C (collector)**.
2. Metti multimetro in **diode mode**.
3. Misura tra **E (rosso)** e **C (nero)**:
   - atteso **~0.4–0.7 V**.

### Criteri guasto
- Se leggi **caduta alta o bassa** o **OL** → IGBT **guasto**.

### (Opzionale) Capacità gate
- Con LCR meter: misura **capacitá G–E** e confronta con datasheet/simili.

---

## Note operative / interpretazione rapida
- **OL** in diode mode, quando ti aspetti una caduta “diodo”, è un forte indicatore di guasto (BJT/FET/IGBT secondo la logica della fonte).
- **Valori molto bassi** (es. <100 Ω in resistenza tra terminali principali) indicano **corto**.
- Se le letture “diodo” sembrano corrette ma il circuito resta anomalo, considera **leakage** o guasti non coperti da questo test (da verificare sul caso).

## Collegamenti utili
- [Transistors - Repair Basics (fonte)](../fonti/transistors-repair-basics.md)
- [Test diodi](test-diodi.md)
- [Test i2c battery connector ol diodes mode](../tecniche/test-i2c-battery-connector-ol-diodes-mode.md)
- [Transistor MOSFET/BJT/IGBT — pagina componente](../componenti/transistor-mosfet-bjt-igbt-fet.md)
