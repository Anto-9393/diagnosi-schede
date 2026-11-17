---
titolo: Multimetro — test transistor in diode mode (SUNSHINE DT-17N)
tipo: strumento
riassunto: 'Note operative per usare il multimetro SUNSHINE DT-17N in diode mode su
  transistor: autoscale/OL e interpretazione drop (BJT/FET/IGBT).'
modelli:
- SUNSHINE DT-17N
fonti:
- raw/banco/miei-attrezzi.md
- raw/repairwiki/pagine/how-to-repair-iphone-12-pro-max-that-does-not-detect-battery-and-does-not-charge.md
- raw/repairwiki/pagine/iphone-15-pro-stuck-at-1-percent-charging-and-no-battery-data-0xa1-panic-log-code.md
- raw/repairwiki/pagine/resistors-repair-basics.md
- raw/repairwiki/pagine/transistors-repair-basics.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Scopo (quando serve il multimetro)
In riparazione schede iPhone/iPad il multimetro in **diode mode** serve per verificare rapidamente che le giunzioni interne di un transistor (BJT/FET/IGBT) non siano **interrotte** o **in corto**, e per distinguere configurazioni (NPN/PNP, N/FET, presenza di “freewheeling diode” su IGBT).

> Riferimento test transistor: [Transistors - Repair Basics](../fonti/transistors-repair-basics.md).

## Impostazioni consigliate (diode mode)
- Usa **diode mode**.
- Se il multimetro ha **autoscale**, lascialo lavorare: in caso di transistor non in conduzione/giunzioni aperte la lettura può risultare “fuori scala” (tipicamente **OL**).
- Se stai cercando un corto/leakage prima del diode mode, imposta **resistenza alla scala più alta o autoscale** (vedi sezione “Corto/leakage prima di diode mode”).

## Prima regola: controlla corto/leakage (resistenza alta)
Prima di passare a diode mode:
1. Metti il multimetro su **resistenza (Ω)** con **scala più alta** o **autoscale**.
2. Misura tra i terminali principali del dispositivo (dipende dal tipo: BJT C–E, FET D–S).

Interpretazione (da fonte):
- **BJT:** se misuri **< 100 Ω tra C ed E** → BJT **in corto**.
- **FET:** se misuri **< 100 Ω tra D ed S** → FET **in corto**.
- Valori “alti” (decine di kΩ fino a megaΩ) indicano **leakage** ma **non** implicano automaticamente che sia inutilizzabile (dipende dal circuito).

## BJT in diode mode (NPN/PNP)
### 1) Identifica i pin (se non hai pinout)
Se il pinout non è noto:
- puoi cercare la configurazione “a due diodi con terminale comune” provando combinazioni in diode mode.
- questo può anche aiutare a capire se è **NPN o PNP**.

Nota fonte: se il transistor è guasto, potrebbe non essere possibile ricostruire il pinout con questo metodo.

### 2) Test giunzioni interne
**NPN** (da fonte):
- **rosso su base (B)**
- **nero su emettitore (E)** e poi su **collettore (C)**
- in entrambi i casi il multimetro dovrebbe leggere un **drop da diodo**.

**Valori tipici (da fonte):**
- **0,6–0,7 V** (tipico)
- **0,2–0,5 V** per **Germanium** (transistor vecchi)

**PNP** (da fonte):
- ripeti ma inverti le sonde: **nero su base (B)** e misura E/C.
- i valori di drop attesi devono risultare coerenti.

### 3) Interpretazione OL / drop anomalo
Da fonte:
- Se misuri una caduta **sostanzialmente più alta o più bassa** del previsto **oppure “OL”** → transistor **difettoso**.

## FET in diode mode (N-channel / P-channel)
### 1) Prima verifica: non deve essere in corto D–S
In resistenza (Ω) scala alta/autoscale: se **< 100 Ω tra D ed S** → FET **in corto**.

### 2) Test gate–source tramite conduzione controllata
Se non è in corto:
- metti in **diode mode**.

**N-Channel FET** (da fonte):
1. **rosso su gate (G)**
2. **nero su source (S)**
3. poi **sposta rapidamente il rosso su drain (D)**
4. dovresti misurare una caduta **molto molto bassa** (vicina a **0 V**) → conferma funzionamento.

**P-Channel FET** (da fonte):
- stesso concetto ma con sonde invertite: **nero su gate (G)**.

### 3) Interpretazione OL / drop alto
Da fonte:
- se leggi **drop alto** o **“OL”** → FET **difettoso**.

## IGBT in diode mode
Da fonte: spesso gli IGBT includono una **“freewheeling diode”** in reverse parallel.

### Test rapido
1. Metti in **diode mode**.
2. **rosso su emettitore (E)**
3. **nero su collettore (C)**
4. dovresti leggere una caduta da diodo **tipicamente 0,4–0,7 V**.

### Interpretazione
Da fonte:
- se leggi caduta **alta o bassa** o **“OL”** → IGBT **difettoso**.

## Su SUNSHINE DT-17N (nota banco)
- Il multimetro presente sul banco è **SUNSHINE DT-17N**.
- Uso: **diode mode** per test transistor (BJT/FET/IGBT) e lettura **OL** come indicatore di giunzione interrotta/fuori scala, confrontando la caduta con i valori tipici riportati sopra.

> Nota: la fonte di banco non specifica ulteriori dettagli su range/risoluzione del DT-17N in diode mode (da verificare).

## Collegamenti utili (per contesto)
- [Transistors - Repair Basics](../fonti/transistors-repair-basics.md)
- Per procedure specifiche su transistor in diode mode nella diagnostica schede: [tecniche/test-transistor-in-diode-mode.md](../tecniche/test-transistor-in-diode-mode.md)
- Per componenti transistor: [transistor-mosfet-bjt-igbt-fet](../componenti/transistor-mosfet-bjt-igbt-fet.md)

## Note pratiche (da verificare dove la fonte non entra nel dettaglio)
- La fonte non specifica **range/risoluzione** del multimetro in diode mode né come gestire esattamente l’**autoscale** in termini di soglie: usare “OL” come indicatore di fuori scala/interruzione e confrontare sempre con i valori tipici sopra.
- Per interpretare “OL” su linee di circuito (non solo sul transistor) servono misure di contesto (da verificare).
