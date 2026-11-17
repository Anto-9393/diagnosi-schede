---
titolo: Wylie SPI Programmer — riprogrammazione ROM per CD3217
tipo: strumento
riassunto: Strumento Wylie V2.0 per leggere/scrivere la ROM SPI (CD32 ROM) quando
  CD3217 non negozia o non carica; flusso Detect → Select → Open File → Write e precauzioni
  su Pin 1.
modelli:
- iPad Pro 11 2nd Gen
- da verificare
fonti:
- raw/repairwiki/pagine/how-to-program-rom-chip-for-ipads-with-cd3217.md
- raw/repairwiki/pagine/how-to-reprogram-the-cd32-rom-with-wylie-spi-programmer.md
- raw/banco/miei-attrezzi.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## A cosa serve
Quando un iPad con [CD3217](../componenti/cd3217.md) va in **no charge / no boot / low voltage negotiation**, la fonte indica che spesso il problema è sulla **ROM SPI collegata** (CD32 ROM): il CD3217 e la ROM non sono “paired” e la ROM può risultare **corrotta/danneggiata** (es. dopo liquid damage o power surge). In questi casi sostituire solo il CD3217 può non risolvere.

Questa pagina descrive l’uso del **Wylie SPI Programmer** come alternativa (più economica) per **leggere/scrivere** la ROM SPI.

> La fonte è una guida di riprogrammazione ROM, **non** una guida generale per riparare un iPad USB-C che non carica.

## Modello esatto (da banco)
- **Programmatore Wylie: V2.0** (disponibile sul banco del tecnico).
- Nota d’uso/limiti: **da verificare** (la fonte non riporta settaggi/pinout specifici del Wylie; eventuali dettagli su SPI mode e pin mapping sono da verificare).

## Dove si usa nella riparazione
- Dopo aver rimosso **CD3217** e la **ROM SPI** (ROM IC) dalla scheda.
- Prima di reinstallare la ROM riprogrammata e poi il CD3217.

## Cosa controllare prima di programmare
Dalla fonte:
- Ispezione e verifica che la ROM non sia danneggiata (se in Detect non succede nulla può essere **bad solder connection** oppure **Dead ROM IC**).
- Verifica che la ROM sia saldata correttamente sul programmatore, con attenzione a **Pin 1**.

Inoltre (da pagina esistente):
- Valore indicativo di negoziazione: **15 V** attesi; errore tipico: **solo 5 V** su USB-C power meter (da usare come contesto diagnostico, non come settaggio Wylie).

## Flusso operativo (software) — Detect → Select → Open File → Write
Dalla fonte:
1. **Desolder** la ROM SPI dall’iPad/iPhone e **solder** la ROM sul programmatore.
2. Collegare il programmatore al PC.
3. Nel software cliccare **Detect**.
   - Deve comparire una piccola finestra.
   - Se **Nothing happens**: possibile **bad solder connection** o **Dead ROM IC**.
4. Cliccare **Select**.
5. Dopo la selezione, il software deve mostrare **molte informazioni** sul chip (è un buon segno).
6. Scaricare la **ROM corretta** per il dispositivo (la fonte rimanda al link “ROM file” della guida).
7. Caricare il file nel programma:
   - cliccare **Open File**
   - selezionare il file ROM
   - verificare che il programma mostri un messaggio di caricamento (la fonte cita un messaggio “similar to this”, ma senza dettagli testuali).
8. Cliccare **Write**.
9. Attendere il completamento:
   - la scrittura dovrebbe richiedere **solo pochi secondi**
   - al termine deve comparire **100%**.
10. A scrittura completata:
   - scollegare il programmatore dal PC
   - **desolder** la ROM dal programmatore e **solder it back** sulla motherboard.
11. Riprova la ricarica (la fonte indica che “hopefully” l’iPad tornerà a caricare normalmente).

## Tempi indicativi
- **Write**: “only take a few seconds” (pochi secondi).

## Precauzioni (critiche)
Dalla fonte:
- **Match Pin 1 correttamente**.
- Se si salda l’IC **al contrario**, si può **danneggiare permanentemente** la ROM.

Precauzioni aggiuntive (da verificare nella fonte specifica Wylie):
- La fonte non riporta settaggi/pinout specifici del Wylie; quindi eventuali dettagli su tensioni, modalità SPI e pin mapping sono **da verificare**.

## Collegamenti utili
- [CD3217](../componenti/cd3217.md)
- [JC V1S Pro](../strumenti/jc-v1s-pro.md) (procedura completa presente nella fonte collegata in pagina esistente)
