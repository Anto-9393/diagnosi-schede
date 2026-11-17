---
titolo: Analisi visiva e ispezione della logic board
tipo: tecnica
riassunto: 'Procedura generale di ispezione: edge PCB, probe point, corrosione (anche
  sotto BGA), angolazione, saldature e componenti compromessi.'
modelli: []
fonti:
- raw/repairwiki/pagine/visual-inspection-repair-basics.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Scopo
Prima di passare a misure complesse, usa l’ispezione visiva per “leggere” la scheda: spesso il problema è evidente (o localizzabile) guardando bene bordi, probe point e zone interessate da liquidi/ossidazione.

Questa tecnica è valida per tutti i modelli.

## 1) Preparazione e condizioni di lavoro
1. **Illuminazione**: usa luce radente/forte e, se disponibile, lente/microscopio.
2. **Pulizia preliminare**: se la scheda è visibilmente sporca di residui, valuta una pulizia leggera *prima* dell’ispezione (altrimenti alcuni difetti si confondono). Nota: la fonte consiglia di **lasciare la pulizia a ultrasuoni per la fine**, perché dopo la pulizia diventa più difficile riconoscere le evidenze del danno da liquidi.
3. **Stato scheda**: ispeziona a scheda **spenta** e senza alimentazione.

## 2) Edge del PCB (priorità alta)
- **Ispeziona sempre gli edge del PCB**: la fonte sottolinea che “la maggior parte delle volte” il problema è in quella zona.
- Cerca segni di:
  - corrosione/ossidazione,
  - tracce bruciate,
  - polvere verde/“green dust”,
  - ruggine o degrado dei probe point.

## 3) Probe point: danni e corrosione
I **probe point** sono punti esposti per misure; possono corrodersi o rompersi.
- Controlla se il probe point:
  - appare “mangiato”/ossidato,
  - ha discontinuità visibili,
  - mostra residui verdi o ruggine.
- La fonte riporta che un probe point corroso può impedire l’avvio (esempi video in fonte).

## 4) Corti indotti da umidità/polvere
- Anche ciò che sembra “solo polvere” può creare un **corto parziale** tra pin.
- La fonte indica che questi casi possono essere risolti con **flux e saldatura** (rework mirato) dopo aver rimosso/gestito il residuo.

## 5) Corrosione sotto BGA (riconoscimento visivo)
- In presenza di chip **BGA**, la corrosione può essere **sotto il package**: i contatti elettrici sono sotto, quindi il danno può non essere immediatamente evidente.
- La fonte evidenzia che a volte è “ovvio”, ma in altri casi serve un occhio allenato per riconoscerlo.
- Se noti indizi (degrado attorno, segni di liquido, pattern sospetti), pianifica verifiche/azioni di rework coerenti (da verificare in base al caso).

## 6) Componenti “funzionanti” ma non affidabili
- La fonte avverte: componenti con corrosione possono **passare i test**, ma **non durare**.
- Quindi, se visivamente trovi corrosione su:
  - pad,
  - componenti,
  - saldature,
  - probe point,
  valuta un **rework corretto** per una riparazione duratura.

### Nota importante sulla pulizia
- La fonte consiglia: **lasciare la pulizia a ultrasuoni per la fine**.
- Motivo: una volta pulita la scheda, le evidenze del danno da liquidi diventano più difficili da individuare.

## 7) “Bad legs” sugli IC
- Controlla anche le **gambe/leg degli IC**: possono essere compromesse e non sempre sono immediatamente evidenti.

## 8) Ispezione ad angolo (tilt)
- **Inclina la scheda**: la fonte indica che l’angolazione può far emergere corrosione nascosta che non si vede guardando “dritto”.

## 9) Saldature scarse: cosa cercare
- Verifica che i giunti siano:
  - uniformi,
  - con flusso corretto,
  - senza grumi,
  - senza giunzioni incomplete.
- La fonte richiama l’importanza di saldature “che non clumpano” e che siano correttamente formate.

## 10) Esempio concettuale: probe point non funzionale
La fonte descrive un caso in cui un probe point appariva “in cattivo stato”, ma il percorso elettrico era limitato a una funzione di test/measurement; il vero problema era il **componente/pad** associato.
- Lezione pratica: non fermarti al “probe point brutto”; verifica sempre cosa serve davvero elettricamente (da verificare sul singolo PCB tramite schema/board view).

## 11) Checklist rapida (da usare sempre)
1. Edge PCB (alta priorità)
2. Probe point: corrosione/rotture
3. Zone con residui: possibili corti da umidità/polvere
4. Indizi di corrosione attorno a BGA (anche se non evidente)
5. Gambe IC (bad legs)
6. Saldature: uniformità, assenza di incompletezza/grumi
7. Ispezione ad angolo (tilt) per corrosione nascosta
8. Pianifica pulizia (ultrasuoni) **alla fine**

## Collegamenti utili
- Tecnica di ricerca corti: [ricerca-corto-iniezione-bassa-tensione-e-termocamera](../tecniche/ricerca-corto-iniezione-bassa-tensione-e-termocamera.md)
- Tecnica di ricerca corti su rail: [diagnosi-e-rimozione-corto-su-rail-con-capacitore-in-corto](../tecniche/diagnosi-e-rimozione-corto-su-rail-con-capacitore-in-corto.md)
- Tecnica di ispezione/diagnosi da liquidi (contesto): [sintomi/corto-su-rail-da-umidita-o-polvere-con-impatti-visivi](../sintomi/corto-su-rail-da-umidita-o-polvere-con-impatti-visivi.md)
