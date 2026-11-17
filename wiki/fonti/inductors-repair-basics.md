---
titolo: Induttori — basi di riparazione (fonte)
tipo: fonte
riassunto: Funzione, tipi, test base con multimetro e criteri di sostituzione degli
  induttori in ottica riparazione schede.
modelli: []
fonti:
- raw/repairwiki/pagine/inductors-repair-basics.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# Induttori — basi di riparazione

> Fonte: [Inductors - Repair Basics — repair.wiki](https://repair.wiki/w/Inductors_-_Repair_Basics), CC BY-SA 3.0.

## Cos’è un induttore
Un **induttore** è un componente passivo che **immagazzina energia in un campo magnetico** quando attraversato da corrente. Resiste alle variazioni di corrente.

- È costituito da **un filo avvolto a spirale** attorno a un **nucleo** (core).
- La **scelta del core** e il **numero di spire** determinano l’induttanza e la forza del campo magnetico.

### Unità di misura
L’induttanza si misura in **Henry (H)**, ma in pratica si trova spesso in:
- **mH** (millihenry)
- **nH** (nanohenry)
- **µH** (microhenry)

## Funzioni principali
Secondo la fonte, gli induttori sono usati per:

1. **Smoothing / stabilizzazione della tensione**
   - Negli stadi di uscita dei **DC-DC**, filtrano il DC pulsante riducendo il ripple.
   - La fonte afferma che **quasi in ogni dispositivo con DC-DC** si trova un induttore all’uscita.

2. **Stoccaggio di energia**
   - Fondamentale in **boost** e **buck**.

3. **Elettromagnete**
   - Il campo magnetico generato dalla corrente è usato anche in applicazioni tipo relè.

4. **Filtraggio**
   - In combinazione con condensatori formano filtri **LC**.
   - Da soli: **bloccano l’AC** e lasciano passare il **DC**.

5. **Circuiti di risonanza**
   - Interazione con condensatori per risonanza a una frequenza specifica.

6. **Sensing induttivo**
   - Sensori di prossimità e metal detector (variazioni di induttanza).

## Tipi di induttori
La fonte elenca:
- **Air core**: bobina su supporto non magnetico (plastica/ceramica), tipico RF.
- **Iron core**: nucleo magnetico in ferro, tipico potenza/trasformatori.
- **Ferrite core**: nucleo in ferrite (alta permeabilità), comune in alta frequenza e EMI.
- **Toroidal**: nucleo a toroide, compatto e con interferenza magnetica ridotta.

## Test di base (multimetro)
### Controllo visivo
Prima di misurare:
- verificare **danni fisici** (è indicato come il modo più rapido per identificare un induttore guasto).

### Misura resistenza/continuità
La fonte indica che, elettricamente, l’induttore è **“solo un filo”**.

Procedura (da fonte):
- usare un **multimetro digitale**
- impostare su **resistenza**
- collegare i puntali **ai capi dell’induttore**
- atteso: lettura **~1 Ω**

Interpretazione (da fonte):
- se leggi **alta resistenza** o **OL** → induttore **aperto** (“blown open”).

### LCR meter
La fonte dice che si può usare un **LCR meter** per misurare l’induttanza, ma **di solito non è necessario**.

## Considerazioni sulla sostituzione
Quando si sostituisce un induttore, la fonte raccomanda di considerare:
1. **Valore di induttanza**: uguale o molto vicino.
2. **Corrente nominale (current rating)**: uguale o superiore.
3. **Tipo di core**: deve combaciare (air/iron/ferrite/toroidal), perché influenza le prestazioni.
4. **Dimensioni fisiche**: simili o compatibili.

La fonte avverte che usare specifiche sbagliate può portare a **rottura ripetuta**.

## Nota importante: induttore guasto come sintomo
La fonte afferma che l’induttore è il componente elettrico più affidabile e che, se risulta danneggiato, **probabilmente è un sintomo** e non la causa.
- In particolare, un guasto tipico è in modalità **“blown open”** dovuta a **sovracorrente**, surriscaldamento e successiva rottura.
- Se l’induttore è danneggiato, la fonte suggerisce che ci sia **probabilmente un corto da qualche parte**.

Per trovare il corto: da verificare (la fonte rimanda alla ricerca del corto, ma non fornisce qui la procedura operativa).
