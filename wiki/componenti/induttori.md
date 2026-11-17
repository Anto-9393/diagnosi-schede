---
titolo: Induttori (Lxxx) — componenti DC-DC
tipo: componente
riassunto: 'Induttori Lxxx nei DC-DC: funzione di filtraggio/smoothing e storage,
  tipico guasto “blown open” (OL) e test base con multimetro (~1 Ω).'
modelli: []
fonti:
- raw/repairwiki/pagine/inductors-repair-basics.md
- raw/repairwiki/pagine/ipad-pro-9-7-not-powering-on-2a-or-higher-power-draw-before-prompt-to-boot.md
- raw/repairwiki/pagine/resistors-repair-basics.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Funzione
Gli induttori (sigla **Lxxx**) sono componenti passivi che **immagazzinano energia in un campo magnetico** quando attraversati da corrente. Nei dispositivi con **DC-DC** sono usati soprattutto per:
- **smoothing/filtraggio** dell’uscita del convertitore (riduzione del ripple),
- **storage di energia** per buck/boost,
- **filtraggio LC** insieme ai condensatori (da soli: bloccano AC e lasciano passare DC),
- altre applicazioni (risonanza, sensing induttivo).

> In pratica: **in quasi ogni dispositivo con convertitori DC-DC trovi un induttore all’uscita**. (da fonte)

## Dove si trovano tipicamente
- **All’uscita dei DC-DC** (rail di alimentazione) dove fanno da filtro/smoothing insieme ai condensatori. (da fonte)
- In generale, sono presenti nelle sezioni di conversione di potenza (buck/boost) della scheda. (da fonte)

## Tipi (per riconoscimento)
La fonte descrive:
- **Air core** (bobina su supporto non magnetico),
- **Iron core** (nucleo in materiale magnetico),
- **Ferrite core** (nucleo in ferrite, comune in alta frequenza/EMI),
- **Toroidal** (nucleo toroidale). (da fonte)

## Sintomi tipici quando si guasta
- L’induttore tende a guastarsi in modo **“blown open”** (aperto) per **surriscaldamento** dovuto a **corrente eccessiva**. (da fonte)
- Se l’induttore risulta **aperto (OL)**, il sintomo è tipicamente legato a **mancata/instabile alimentazione del rail** a valle del DC-DC (da verificare sul singolo caso, perché la fonte non collega direttamente ogni sintomo a un modello specifico).
- Nota importante: la fonte afferma che l’induttore è il componente **più affidabile**; se è danneggiato, **spesso è un sintomo** e **non la causa**, e di solito c’è **un corto da qualche parte** nel circuito/rail. (da fonte)

## Misure base (multimetro)
### Controllo visivo
1. **Verifica prima eventuali danni fisici** (rotture, bruciature, deformazioni). È il modo più rapido per identificare un induttore guasto. (da fonte)

### Continuità / resistenza
1. Imposta il multimetro in **modalità resistenza (Ω)**.
2. Collega le sonde **ai capi dell’induttore**.
3. Atteso: il multimetro dovrebbe mostrare **~1 Ω** (la fonte lo motiva col fatto che “l’induttore è solo un filo”). (da fonte)
4. Se misuri **resistenza alta** o **OL**, significa che l’induttore è **aperto** (“blown open”). (da fonte)

### LCR meter (opzionale)
- La fonte indica che si può misurare anche l’**induttanza** con un **LCR meter**, ma di solito **non è necessario** per la diagnosi di base. (da fonte)

## Considerazioni per la sostituzione
Quando sostituisci un induttore, la fonte consiglia di rispettare:
1. **Valore di induttanza**: uguale o molto vicino.
2. **Current rating**: uguale o superiore rispetto all’originale.
3. **Tipo di nucleo** (air/iron/ferrite/toroidal): deve essere compatibile perché influenza le prestazioni.
4. **Dimensioni fisiche**: simili/compatibili. (da fonte)

## Collegamenti utili
- Sintomo correlato (pagina piano): [induttore danneggiato o aperto](../sintomi/induttore-danneggiato-o-aperto.md)
- Tecnica (pagina piano): [test induttori](../tecniche/test-induttori.md)
