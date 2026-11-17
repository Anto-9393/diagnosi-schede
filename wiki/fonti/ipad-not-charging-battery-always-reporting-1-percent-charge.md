---
titolo: IPad non carica — batteria sempre al 1% (possibili restart)
tipo: fonte
riassunto: 'iPad che non carica e mostra batteria bloccata al 1%: spesso batteria
  difettosa o problema connessione batteria (screw mancante/errato, FPC battery danneggiato);
  verifica panic log TG0B/TG0V e ripara/risalda con low melt.'
modelli:
- iPad Air 1
- iPad Air 2
- iPad 5
- iPad 6
- iPad 7
- iPad 8
- iPad 9
- iPad Air 3
- iPad Pro 11" 1st Gen (2018)
- iPad Pro 11" 2nd Gen (2020)
- iPad Pro 11" 3rd Gen (2021)
- iPad Pro 10.5
- iPad Pro 12.9" 1st Gen (2015)
- iPad Pro 12.9" 3rd Gen (2018)
- iPad Pro 12.9" 4th Gen (2020)
- iPad Pro 12.9" 5th Gen (2021)
- iPad Pro 12.9" 6th Gen (2022)
- iPad Air 4 (5 Pin)
- iPad Pro 9.7"
- iPad Pro 12.9" 2nd Gen (2017)
fonti:
- raw/repairwiki/pagine/ipad-not-charging-battery-always-reporting-1-percent-charge.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Descrizione problema
iPad non carica, la percentuale batteria resta sempre a **1%** e può anche **riavviarsi casualmente** ogni pochi minuti.

## Sintomi tipici
- Percentuale batteria **sempre bloccata a 1%**
- iPad **non carica**
- **Restart casuali** ogni pochi minuti

## Diagnosi (da fonte)
Questa condizione è “di solito” dovuta a:
- **batteria difettosa**
- **problema di connessione** tra motherboard e batteria

### Verifica panic log (restart)
Se l’iPad si riavvia, controllare i **panic logs**: se compare un riferimento ai sensori **TG0B** e **TG0V**, il problema è da ricondurre a:
- batteria, oppure
- **problema di comunicazione** tra batteria e motherboard.

### Controllo meccanico del connettore batteria
Aprire il dispositivo e verificare che la **vite sul connettore batteria** sia presente e avvitata correttamente.
- Se la vite **manca**, può causare i sintomi sopra.

### Ispezione FPC batteria
Rimuovere la motherboard dall’alloggiamento e ispezionare la **Battery FPC**:
- è comune trovare il connettore **danneggiato** se l’iPad era già stato aperto e qualcosa è stato inserito per scollegare la batteria.

### Verifica “al tatto” del contatto
Con un paio di **tweezers**, toccare la connessione per verificare che sia **solida** e non **crepata**.

### Se tutto sembra ok
Se meccanica e connettori sembrano a posto, la fonte indica come step successivo:
- **test con una batteria nuova**.

## Riparazione (da fonte)
### Caso 1 — vite mancante o errata
- Se la vite manca: installare una **nuova vite**.
- Assicurarsi che la vite non sia **troppo lunga**, altrimenti il connettore non viene spinto correttamente nella batteria.
- Non stringere eccessivamente: una vite troppo stretta può **danneggiare l’FPC**.
- La fonte segnala che una vite troppo stretta può anche **piegare l’FPC** e far sollevare i pin laterali.

**Vite (dimensione indicata dalla fonte):**
- “Most iPads use a screw between **1.8–2.3mm Phillips**”.

### Caso 2 — connettore danneggiato (sostituzione/risaldatura)
Se il connettore è danneggiato:
1. La fonte consiglia di aggiungere **low melt** sulle connessioni della motherboard per facilitare la riparazione.
2. Usare la **stazione ad aria calda** per **desaldare l’FPC**.
3. Mentre la scheda è ancora calda, usare il saldatore con punta “a bit tip” per **pulire i fori**.
   - La fonte specifica che serve “un po’ di calore” per pulire i fori.
   - Se il solo saldatore non basta, aiutarsi con hot air “allo stesso tempo”.
4. Posizionare il **nuovo connettore**.
5. Aggiungere **saldatura fresca**.

> Nota fonte: i connettori sono “facili da trovare” e “molti dispositivi usano la stessa parte”.

## Verifiche post-riparazione (da fonte)
- Assicurarsi che l’iPad riporti la **percentuale batteria corretta**.
- Assicurarsi che il dispositivo **non si riavvii**.
- Assicurarsi che l’iPad **carichi normalmente**.

## Parti/compatibilità (da fonte)
La fonte raggruppa i dispositivi che usano “la stessa parte” del connettore batteria:

### Gruppo A — stessa parte
- iPad Air 1 / Air 2
- iPad 5 / 6 / 7 / 8 / 9

### Gruppo B — stessa parte
- iPad Air 3
- iPad Pro 11" 1st Gen (2018)
- iPad Pro 11" 2nd Gen (2020)
- iPad Pro 11" 3rd Gen (2021)
- iPad Pro 10.5
- iPad Pro 12.9" 1st Gen (2015)
- iPad Pro 12.9" 3rd Gen (2018)
- iPad Pro 12.9" 4th Gen (2020)
- iPad Pro 12.9" 5th Gen (2021)
- iPad Pro 12.9" 6th Gen (2022)
- iPad Air 4 (5 Pin)

### Gruppo C — stessa parte
- iPad Pro 9.7"
- iPad Pro 12.9" 2nd Gen (2017) (5 Pin)

## Link utili (componenti/tecniche)
- [Battery connector I2C line](../componenti/i2c-line-battery-connector.md)
- [Analisi panic log / restart casuali](../tecniche/analisi-panic-log-restart-casuali.md)
- [Capacitori: test e sostituzione](../tecniche/capacitori-test-e-sostituzione.md)
- [Batteria](../componenti/batteria.md)
- [PMIC](../componenti/pmic.md)
- [Tristar](../componenti/tristar.md)
- [CD3217](../componenti/cd3217.md)
