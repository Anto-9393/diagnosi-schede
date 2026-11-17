---
titolo: Resistori — funzioni, codici valore e test (pull-up/pull-down, shunt, NTC/PTC,
  varistor)
tipo: fonte
riassunto: 'Riassunto “Resistors - Repair Basics”: funzioni dei resistori, codici
  valore SMD/through-hole, pull-up/pull-down, shunt per misura corrente e componenti
  correlati (varistor, NTC, PTC) con note di test da collegare alle pagine tecniche.'
modelli: []
fonti:
- raw/repairwiki/pagine/resistors-repair-basics.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# Resistori — funzioni, codici valore e test (pull-up/pull-down, shunt, NTC/PTC, varistor)

> Fonte: [Resistors - Repair Basics — repair.wiki](https://repair.wiki/w/Resistors_-_Repair_Basics) (CC BY-SA 3.0).

Questa pagina è un **riassunto operativo** per riparatori: cosa fanno i resistori, come leggere i **codici valore**, e come riconoscere/interpretare alcune famiglie usate spesso in diagnostica (pull-up/pull-down, shunt per misura corrente, NTC/PTC, varistor).

## Funzione base del resistore
Un resistore **limita il passaggio di corrente** quando applico una tensione ai suoi capi, dissipando potenza in calore.

- Valore in **Ohm (Ω)**.
- Relazione fondamentale: **Ohm’s Law: V = I * R**.

### Applicazioni tipiche (in ottica riparazione)
- **Voltage dropper / current limiter (limitazione corrente / caduta di tensione)**: resistore in serie al carico per “bruciare” una parte della tensione e/o limitare la corrente.
- **Voltage divider (partitore)**: due o più resistori in serie per ottenere una tensione proporzionale all’ingresso (utile per riferimenti/bias/monitoring).
- **Resistor sensors**: sensori resistivi (es. termistori, fotoresistenze).

## Pull-up / Pull-down (logica “non flottante”)
I resistori **pull-up** e **pull-down** servono a mantenere un ingresso digitale in uno stato noto quando non è pilotato.

- **Pull-up**: collega l’ingresso a **Vcc** → quando il segnale non “spinge”, l’ingresso risulta **HIGH**.
- **Pull-down**: collega l’ingresso a **GND** → quando il segnale non “spinge”, l’ingresso risulta **LOW**.

La fonte indica tipicamente valori **2.2 kΩ – 10 kΩ**.

> Collegamenti utili: per interpretare corti/OL su linee e rail, vedi anche le pagine tecniche di ricerca corti e test (da verificare dove applicare esattamente in base al caso).

## Shunt resistor (misura corrente)
La misura corrente tramite **shunt** usa un resistore a **bassissima resistenza** in serie al carico.

- Principio: **V = I * R**.
- Lo shunt è progettato con valore noto e calibrato, **molto vicino a 0 Ω**, spesso indicato come **~0.002 Ω**.
- Se la caduta è piccola, può servire amplificazione; in elettronica moderna spesso si usano IC dedicati per misurare la caduta.

Posizionamento tipico:
- spesso dove ci sarebbe un **fusibile** (tutta la corrente passa lì);
- in alcuni casi lo shunt può comportarsi da “fusibile” perché, in corto, diventa il punto a resistenza più alta.

> Collegamenti utili: per la logica di misura su rail e diagnosi “non carica/assorbimento anomalo”, vedi le pagine sintomo e tecniche già presenti (es. ricerca corto/iniezione bassa tensione, ecc.).

## Codici valore dei resistori (SMD e through-hole)
### Through-hole assiale (codice a bande)
- Storicamente comune.
- Valore spesso indicato con **4 o 5 bande** colorate.
- In alcuni casi il valore è stampato in numeri.

### SMD (codice numerico)
La fonte descrive due notazioni comuni:

1) **Codice numerico a 3 cifre**: le ultime cifre indicano il moltiplicatore/numero di zeri.
   - Esempio: **221 → 220 Ω**.

2) **Notazione con lettera (R/K/M)**: la lettera rappresenta il moltiplicatore.
   - Esempi: **4k7 → 4700 Ω**.
   - Esempi con lettera a inizio/fine: **K33 → 330 Ω**, **10R → 10 Ω**.

> Nota: la fonte rimanda a un calcolatore conversione codici SMD (link esterno in pagina fonte).

## Tipi “speciali” correlati (NTC/PTC, varistor)
### Termistori
La fonte li tratta come sensori resistivi con resistenza che varia con la temperatura.

- **NTC (Negative Temperature Coefficient)**: al crescere della temperatura, **la resistenza diminuisce**.
- **PTC (Positive Temperature Coefficient)**: al crescere della temperatura, **la resistenza aumenta**.

Funzione PTC in ottica protezione:
- la fonte indica che i **PTC possono funzionare come “self-resetting fuses” / current limiters**: quando scaldano per corrente eccessiva, la resistenza aumenta e riduce la corrente.

### Varistor (VDR)
La fonte specifica che un **varistor** è in realtà un dispositivo a comportamento simile a una coppia di zener in anti-serie.

- Non conduce fino a una **soglia di tensione** (positiva/negativa).
- Oltre la soglia inizia a condurre e **clampa** la tensione.
- Usato per protezione da **spike** e **sovratensioni transitorie**.

La fonte menziona anche la famiglia moderna:
- **Metal Oxide Varistors** (non polarizzati), con comportamento “a soglia” dovuto a catene di micro-diodi.

## Collegamenti alla wiki (pagine già presenti)
Per rendere questa pagina utile durante la diagnosi:
- Per **misure e interpretazione** su componenti e rail, usa le tecniche già presenti (es. ricerca corto/iniezione, test induttori, ecc.).
- Per componenti “correlati” (diodi/TVS/varistor spesso si confondono in test), vedi anche:
  - [diode](../componenti/diode.md)
  - [condensatori-mlcc-elettrolitici-tantalio](../componenti/condensatori-mlcc-elettrolitici-tantalio.md) (per contesti di corti/assorbimenti dove i resistori non sono l’unico sospetto)
  - [induttori](../componenti/induttori.md) e [tecniche/test-induttori](../tecniche/test-induttori.md)

> Dove applicare esattamente pull-up/pull-down e shunt dipende dal circuito: da verificare caso per caso con schema/boardview e misure.
