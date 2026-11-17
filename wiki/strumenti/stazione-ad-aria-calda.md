---
titolo: Stazione ad aria calda — strumento per rework BGA/IC
tipo: strumento
riassunto: Aggiornata con modello banco QUICK 861DW e note d’uso/limiti per rework
  di shield e IC su schede iPhone/iPad.
modelli: []
fonti:
- raw/banco/miei-attrezzi.md
- raw/repairwiki/pagine/iphone-xr-not-powering-on-not-charging.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Modello (da banco)
- **QUICK 861DW** (stazione ad aria calda)

## A cosa serve
- Rework/dissaldatura e risaldatura di componenti **SMD** e **IC** su schede iPhone/iPad.
- In particolare, per la **rimozione di shield** sotto cui sono presenti IC di ricarica e altri circuiti (es. su iPhone XR: shield “bottom back shield”).

## Impostazioni/approccio (da fonte)
- Per rimuovere lo shield: usare **max heat** e **max air**.
- Usare **largest nozzle** (**ugello grande**).
- Se lo shield non si stacca facilmente: può essere necessario **molto calore** oppure **tagliare lo shield** (es. con tin snips).

## Precauzioni operative (da fonte)
- **Estrema attenzione** a non “flottare” componenti o a non urtarli durante la rimozione dello shield.
- Attenzione alla **forza meccanica**: troppa forza può **flettere la scheda** e danneggiare **tracce interne**.

## Nota d’uso (da banco)
- **Da verificare**: la fonte di banco non riporta settaggi numerici (°C/flusso/tempi) o limiti specifici della QUICK 861DW.
- La stazione viene usata nel flusso di rework per rimozione shield e successiva risaldatura IC; per i dettagli operativi (ugello/temperatura/tempo) fare riferimento alle indicazioni “max heat/max air” della fonte.

## Limiti / rischi
- La fonte non specifica valori numerici (°C, flusso, tempi) né limiti di precisione/controllo della stazione: **da verificare**.
- Non sono riportate indicazioni su gestione di plastiche/connettori o uso di preriscaldatore: **da verificare**.

## Note d’uso collegate (per contesto diagnostico)
- Su iPhone XR, la fonte collega il problema “not powering on & not charging” al guasto dell’IC di ricarica **Yangtze (U3300)** sotto lo shield; dopo rimozione dello shield, la sostituzione dell’IC è descritta come relativamente semplice.

## Link utili
- [Yangtze U3300](../componenti/yangtze-u3300.md)
- [Stazione ad aria calda — pagina tecnica generale (da verificare)](../tecniche/diagnosi-e-rimozione-corto-su-rail-con-capacitore-in-corto.md)
