---
titolo: How To Fix an iPhone 12 Pro that is not charging and touch not working — Kraken
  IC (fonte)
tipo: fonte
riassunto: 'Fonte esterna: su iPhone 12 Pro non carica + touch non funziona; sospetto
  Kraken IC e procedura diagnostica con DCPS e sostituzione IC.'
modelli:
- iPhone 12 Pro
fonti:
- raw/repairwiki/pagine/how-to-fix-an-iphone-12-pro-that-is-not-charging-and-touch-not-working.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# How To Fix an iPhone 12 Pro that is not charging and touch not working — Kraken IC (fonte)

> Fonte: [How To Fix an iPhone 12 Pro that is not charging and touch not working — repair.wiki](https://repair.wiki/w/How_To_Fix_an_iPhone_12_Pro_that_is_not_charging_and_touch_not_working), CC BY-SA 3.0.

## Problem description
L’iPhone 12 Pro può presentare problemi di ricarica e/o perdita della funzionalità touch. La fonte collega spesso il guasto al fallimento dell’USB IC, chiamato **Kraken IC**.

La fonte indica che il guasto può essere innescato dall’uso di **caricatori aftermarket o di scarsa qualità**, ma che l’IC può anche guastarsi **spontaneamente**.

## Sintomi (come riportati)
- L’iPhone **non carica**.
- **Nessuna risposta** quando si collega il caricatore.
- **Touchscreen non funzionante**.
- Il dispositivo **si accende** mentre è alimentato tramite **DCPS**, ma **non rileva la connessione USB**.
- Possibile **corrente anomala** su DCPS quando si tenta di avviare/boot.

## Diagnosi (passi riportati)
1. **Test con parti note funzionanti**
   - Provare una **charging port flex** funzionante (known good).
   - Provare anche una **batteria** funzionante (known good).
   - Se il problema persiste, la fonte suggerisce un **fault a livello di scheda**.

2. **Ispezione visiva**
   - Controllare danni a livello di board, **corrosione** o segni di **liquido/ingresso liquidi** nell’area USB/IC di ricarica.

3. **Test con alimentatore DC (DC Power Supply Test)**
   - Collegare il dispositivo a **DCPS**.
   - Se il **consumo di corrente è anomalo** (la fonte cita un **picco irregolare** quando si prova a fare il boot) → indicazione di possibile problema **Kraken IC**.

## Riparazione (passi riportati)
1. **Accesso alla board**
   - Rimuovere la **logic board** con attenzione.
   - **Separare lo “sandwich layer”**.
   - Isolare l’area dell’IC di ricarica (**Kraken**).

2. **Preparazione**
   - Applicare **flux** attorno al Kraken IC.
   - Usare una **hot air station** con flusso d’aria e temperatura **controllati**.

3. **Sostituzione IC**
   - Rimuovere il **Kraken IC** guasto.
   - Pulire i pad con **solder wick** e flux.
   - Eseguire **reball** o usare un **nuovo IC**.
   - Allineare e fare **reflow** del Kraken IC sostitutivo.

4. **Testing**
   - Rimontare il dispositivo.
   - Collegare a un caricatore e verificare la **funzione di ricarica**.
   - Verificare che la risposta **touch** sia ripristinata completamente.

## Note di collegamento alla wiki (componenti/tecniche)
- La fonte parla esplicitamente di **Kraken IC** (da collegare alla pagina piano: [kraken-ic-usb](../componenti/kraken-ic-usb.md)).
- La diagnosi con **DCPS** e la logica “corrente anomala/picco irregolare” è da collegare alla pagina tecnica: [test-dcps-e-diagnosi-kraken-ic](../tecniche/test-dcps-e-diagnosi-kraken-ic.md).
- La sostituzione/gestione IC e test correlati sono da collegare alle pagine tecniche disponibili (da verificare se la fonte specifica ulteriori dettagli oltre a quelli sopra).
