---
titolo: Induttore danneggiato o aperto — sintomo
tipo: sintomo
riassunto: 'Induttore con resistenza alta/OL (aperto): spesso indica che c’è un corto
  sul rail/power path a monte; l’induttore è più spesso “sintomo” che causa.'
modelli: []
fonti:
- raw/repairwiki/pagine/inductors-repair-basics.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Cosa significa
Un induttore guasto in genere si presenta come **aperto**: misura **resistenza alta** o **OL** in continuità/resistenza. La fonte ricorda che “un induttore è solo un filo” e quindi, a banco, ci si aspetta una lettura bassa.

> Nota di diagnosi: la fonte specifica che l’induttore è spesso **il componente più affidabile** e, se risulta danneggiato, è **più probabile che sia un sintomo**; tipicamente “c’è un corto da cercare da qualche parte”.

## Dove si trova (contesto)
La fonte non indica posizioni per singolo modello, ma descrive che gli induttori sono comunemente presenti **all’uscita dei DC-DC** (power converter) per **smoothing/stabilizzazione** e in generale nei **power path** dove filtrano e stabilizzano la tensione.

## Sintomi tipici correlati
- **Induttore con resistenza alta o OL** (aperto).
- Possibile **surriscaldamento** dell’induttore dovuto a **eccesso di corrente** (causa tipica: corto a monte).
- In diagnosi, l’induttore danneggiato porta a sospettare un **corto sul rail/power path**.

## Misure utili (multimetro)
1. **Ispezione fisica**: prima controllare che non ci sia **danno visibile**.
2. **Misura resistenza/continuità** con multimetro in modalità **resistenza**:
   - Misurare **ai capi dell’induttore**.
   - Valore atteso (da fonte): circa **~1 Ω**.
   - Se misuri **resistenza alta** o **OL** → induttore **aperto/blown open**.

Condizioni: misura con multimetro (scheda da verificare; da verificare se la fonte richiede alimentazione scollegata/non alimentata).

## Interpretazione (ordine di probabilità)
1. **Corto da cercare sul rail/power path** a monte dell’induttore (la fonte afferma che un induttore danneggiato è spesso “sintomo” e che probabilmente c’è un corto).
2. **Induttore realmente guasto** (blown open) come conseguenza del corto/sovracorrente.

## Collegamenti utili
- [Induttori](../componenti/induttori.md)
- [Test induttori](../tecniche/test-induttori.md)
- [Diode](../componenti/diode.md) (da verificare se nel tuo caso il corto coinvolge diodi di power)
- [Tecniche: ricerca corti su rail](../tecniche/diagnosi-e-rimozione-corto-su-rail-con-capacitore-in-corto.md) (da verificare: la fonte qui non lo cita, ma è coerente con l’ipotesi “corto sul rail”)
