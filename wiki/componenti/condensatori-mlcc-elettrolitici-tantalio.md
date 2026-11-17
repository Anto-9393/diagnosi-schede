---
titolo: Condensatori (MLCC, elettrolitici, tantalio) — corrosione/contaminazione “apparentemente
  ok” ma non durevole
tipo: componente
riassunto: 'Corrosione e contaminazione possono far sembrare un condensatore “funzionante”
  ai test, ma renderlo instabile: dopo pulizia serve rework dei punti ossidati per
  una riparazione durevole.'
modelli: []
fonti:
- raw/repairwiki/pagine/capacitors-repair-basics.md
- raw/repairwiki/pagine/how-to-fix-an-iphone-14-that-is-shows-temperature-warning-and-does-not-charge.md
- raw/repairwiki/pagine/how-to-fix-an-iphone-8-that-has-no-power-does-not-boot.md
- raw/repairwiki/pagine/how-to-fix-iphone-x-that-does-not-power-on.md
- raw/repairwiki/pagine/how-to-repair-ipad-6-no-power.md
- raw/repairwiki/pagine/iphone-11-not-powering-on-2a-or-higher-power-draw-after-prompt-to-boot.md
- raw/repairwiki/pagine/iphone-11-not-powering-on-after-prompt-to-boot-current-jumps-back-and-forth-from-0-a-to-320-ma-then-0-a-to-1-4-a-then-0-a-to-500-ma-and-so-on.md
- raw/repairwiki/pagine/iphone-11-pro-and-iphone-11-pro-max-not-powering-on-2a-or-higher-power-draw-after-prompt-to-boot.md
- raw/repairwiki/pagine/iphone-xr-not-powering-on-with-heat-above-the-cpu.md
- raw/repairwiki/pagine/iphone-xs-not-powering-on-pulls-2a-or-more-before-promt-to-boot.md
- raw/repairwiki/pagine/resistors-repair-basics.md
- raw/repairwiki/pagine/short-circuits-repair-basics.md
- raw/repairwiki/pagine/visual-inspection-repair-basics.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Perché corrosione/contaminazione ingannano
Nei guasti su rail di alimentazione, un condensatore (MLCC/elettrolitico/tantalio) può **apparire ok** durante le verifiche “rapide” (es. letture non immediatamente in corto), ma la **corrosione/ossidazione** o residui di liquido possono:
- degradare la qualità dei **giunti di saldatura** e delle piazzole;
- creare micro-impedenze/micro-percorsi che non si manifestano subito come corto “dead”,
- peggiorare nel tempo (riparazione non durevole).

> Fonte: [Visual Inspection - Repair Basics](../fonti/visual-inspection-repair-basics.md) (componenti con corrosione possono apparire funzionali ma “won't last”; rework essenziale).

## Segnali visivi da cercare (anche se il componente “passa” i test)
Durante l’ispezione, non limitarti alla lettura del componente: controlla anche l’area attorno.
- **Corrosione/ossidazione** su piazzole e saldature.
- **Polvere verde/“green dust”**, tracce di bruciatura o discolorazioni.
- **Probe point/aree di misura** che possono essere danneggiate: a volte il problema è nel punto di saldatura/contatto, non nel componente “in prova”.
- Ispezione **inclinando** la scheda: la corrosione nascosta può non essere visibile guardando perpendicolare.

> Fonte: [Visual Inspection - Repair Basics](../fonti/visual-inspection-repair-basics.md) (corrosione come marker; ispezione ad angolo; probe point damage; componenti che non dureranno).

## Perché dopo pulizia diventa più difficile “vedere” il problema
La fonte sottolinea che è spesso utile lasciare la **pulizia a ultrasuoni per la fine**: una volta pulita la board e rimossa l’evidenza del danno da liquido, le aree corrose diventano **molto più difficili da individuare**.

> Fonte: [Visual Inspection - Repair Basics](../fonti/visual-inspection-repair-basics.md).

## Regola pratica: rework dopo pulizia (per riparazioni durevoli)
Anche se un condensatore sembra funzionare al test, se l’area mostra corrosione/contaminazione:
1. **Esegui ispezione visiva accurata prima** della pulizia (anche ad angolo).
2. Dopo pulizia, quando l’evidenza visiva è sparita, fai comunque il **rework** delle zone interessate (condensatore e/o piazzole/giunti coinvolti), perché la corrosione può aver compromesso la durata del contatto.

> Fonte: [Visual Inspection - Repair Basics](../fonti/visual-inspection-repair-basics.md) (rework essenziale; ultrasonic cleaning meglio alla fine).

## Collegamenti utili
- Ispezione e “trust your eyes”: [Visual Inspection - Repair Basics](../fonti/visual-inspection-repair-basics.md)
- Corti su rail e condensatori in corto: Condensatori (MLCC, elettrolitici, tantalio) — corto su rail di alimentazione
- Tecnica generale per localizzare corti su rail: [tecniche/ricerca-corto-iniezione-bassa-tensione-e-termocamera.md](../tecniche/ricerca-corto-iniezione-bassa-tensione-e-termocamera.md)

## Nota
Questa pagina integra la parte “corto su rail” con il tema **affidabilità**: la fonte esterna non fornisce valori, net o soglie specifiche per MLCC/elettrolitici/tantalio in presenza di corrosione; i dettagli operativi (es. cosa reworkare esattamente in ogni caso) vanno definiti da ispezione e dalla diagnosi del corto/instabilità.
