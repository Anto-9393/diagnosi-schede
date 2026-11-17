---
titolo: How to reprogram the CD32 ROM with Wylie SPI Programmer — riassunto fonte
tipo: fonte
riassunto: Guida esterna (repair.wiki) per leggere/scrivere la ROM collegata al CD3217
  usando un programmatore SPI Wylie, con attenzione a Pin 1 e sequenza Detect/Write.
modelli: []
fonti:
- raw/repairwiki/pagine/how-to-reprogram-the-cd32-rom-with-wylie-spi-programmer.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Scopo della fonte
La fonte descrive una procedura alternativa per **flashare la ROM** associata al controller **CD3217** (iPad/iPhone con problemi tipo: **no charge**, **no boot** o **negoziazione bassa tensione**), quando la sostituzione del solo CD3217 non risolve perché la **ROM collegata risulta corrotta/danneggiata**.

> Nota della fonte: non è una guida di riparazione generale per un iPad/iPhone USB‑C che non carica.

## Strumento/approccio
- Uso di un **programmatore SPI Wylie** (la fonte lo indica come alternativa più economica rispetto al metodo JCID).
- Il programmatore viene collegato al PC e gestito tramite software dedicato.

## Procedura (sequenza operativa)
1. **Scaricare** il file/programma indicato dalla fonte, **estrarre** l’archivio RAR ed eseguire il programma.
2. Per leggere la ROM:
   - **Dissaldare** la ROM dall’iPad/iPhone.
   - **Saldare** la ROM sul programmatore.
3. **Attenzione Pin 1**:
   - La fonte sottolinea che va **matchato correttamente Pin 1**.
   - Se l’IC viene saldato **al contrario**, si può **danneggiare permanentemente** l’IC.
4. Collegare il programmatore al PC.
5. Nel software:
   - Clic su **Detect**.
   - Se non compare nulla: la fonte suggerisce **connessione di saldatura difettosa** o **ROM IC dead**.
6. Clic su **Select**.
   - La fonte indica che devono comparire molte informazioni sull’IC: è un **buon segno**.
7. Scaricare la **ROM corretta** per il dispositivo (tramite il link indicato nella fonte).
8. Caricare il file nel programma:
   - **Open File** → selezionare il file.
   - La fonte riporta che il software mostra un messaggio di caricamento (testo “simile a questo”, da verificare in base allo screenshot originale).
9. Scrittura:
   - Clic su **Write**.
   - La fonte indica che la scrittura richiede **pochi secondi** e che al termine compare **100%**.
10. Fine:
   - Scollegare il programmatore dal PC.
   - **Dissaldare** l’IC dal programmatore e **risaldarlo** sulla motherboard.
11. Risultato atteso (condizionale):
   - La fonte afferma che “**l’iPad dovrebbe (sperabilmente) caricare normalmente di nuovo**”.

## Collegamenti utili (wiki)
- Pagina componente CD3217: [CD3217](../componenti/cd3217.md)
- Tecnica correlata (test/ricerca corti): [test-cd3217-e-ricerca-corti](../tecniche/test-cd3217-e-ricerca-corti.md)
- Pagina strumento programmatore Wylie: [wylie-spi-programmer](../strumenti/wylie-spi-programmer.md)
- Fonte interna collegata (metodo alternativo): How To Program ROM Chip for iPads with CD3217 (presente in wiki come fonte: da verificare il link esatto nella sezione fonti)

## Note di qualità / dati mancanti
- La fonte non specifica qui **sigla esatta della ROM**, **pinout**, **tensioni**, né **valori di lettura/verifica**: da verificare.
- La fonte non fornisce criteri di successo/fallimento oltre a “Detect/Select ok” e “Write 100%”: da verificare.
