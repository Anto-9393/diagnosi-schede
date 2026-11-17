---
titolo: Test induttori con multimetro (resistenza/continuità)
tipo: tecnica
riassunto: Procedura generale per verificare induttori con multimetro (resistenza/continuità)
  e interpretare OL/alta R come possibile induttore aperto.
modelli: []
fonti:
- raw/repairwiki/pagine/inductors-repair-basics.md
- raw/repairwiki/pagine/resistors-repair-basics.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Scopo
Verificare rapidamente se un induttore (L) è guasto usando un multimetro in modalità **resistenza/continuità** e interpretare correttamente i risultati.

## 1) Controllo visivo (prima di misurare)
1. Ispeziona l’induttore: cerca **danni fisici** (rotture, bruciature, deformazioni).
2. Se è danneggiato, quello è il primo indicatore di guasto.

> Fonte: [inductors-repair-basics.md](../../raw/repairwiki/pagine/inductors-repair-basics.md) dice di fare prima il controllo fisico perché è il modo più rapido per identificare un induttore difettoso.

## 2) Misura con multimetro (resistenza/continuità)
1. Imposta il multimetro in **modalità resistenza**.
2. Collega le sonde **ai due terminali dell’induttore**.
3. Leggi il valore.

### Valore atteso (indicazione generale)
- Il multimetro dovrebbe mostrare **~1 Ω** (l’induttore è “di fatto” una bobina di filo).

> Fonte: [inductors-repair-basics.md](../../raw/repairwiki/pagine/inductors-repair-basics.md) riporta “around 1 Ohm since the inductor is just a wire”.

## 3) Interpretazione risultati
### Caso A — OL / alta resistenza
- Se misuri **OL** o **alta resistenza**, l’induttore è **aperto** (“blown open”).

> Fonte: [inductors-repair-basics.md](../../raw/repairwiki/pagine/inductors-repair-basics.md) dice: “If you measure high resistance or OL that means the inductor is blown open.”

### Caso B — resistenza bassa (vicina a ~1 Ω)
- Se la lettura è bassa e coerente con l’ordine di grandezza atteso, l’induttore **non risulta aperto** con questo test.

> Fonte: [inductors-repair-basics.md](../../raw/repairwiki/pagine/inductors-repair-basics.md) fornisce il riferimento “around 1 Ohm”.

## 4) Nota diagnostica importante (non confondere causa e sintomo)
- L’induttore è descritto come il **componente elettrico più affidabile**.
- Se trovi un induttore danneggiato (tipicamente aperto), **è spesso un sintomo**, non la causa.
- In particolare, la fonte collega il guasto “blown open” a **sovracorrente/riscaldamento** e quindi suggerisce che probabilmente c’è **un corto da qualche parte a valle**.

> Fonte: [inductors-repair-basics.md](../../raw/repairwiki/pagine/inductors-repair-basics.md): “If you find a damaged inductor, that means it is a symptom and not the cause and you most likely have a short circuit somewhere.”

## 5) Alternative di misura (opzionale)
- È possibile usare un **LCR meter** per misurare l’induttanza, ma la fonte dice che di solito **non è necessario**.

> Fonte: [inductors-repair-basics.md](../../raw/repairwiki/pagine/inductors-repair-basics.md).

## Collegamenti utili
- Pagina componente: [Induttori](../componenti/induttori.md)
- Sintomo correlato: [Induttore danneggiato o aperto](../sintomi/induttore-danneggiato-o-aperto.md)
