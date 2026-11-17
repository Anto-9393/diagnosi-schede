---
titolo: Diodi — avvertenze diagnostiche prima del test (diode mode)
tipo: componente
riassunto: 'Prima di interpretare diode mode: controllare probe point e saldature
  compromesse per evitare letture “false” (es. short apparenti).'
modelli: []
fonti:
- raw/repairwiki/pagine/diodes-repair-basics.md
- raw/repairwiki/pagine/iphone-xr-not-powering-on-with-heat-above-the-cpu.md
- raw/repairwiki/pagine/iphone-xs-not-powering-on-pulls-2a-or-more-before-promt-to-boot.md
- raw/repairwiki/pagine/resistors-repair-basics.md
- raw/repairwiki/pagine/short-circuits-repair-basics.md
- raw/repairwiki/pagine/visual-inspection-repair-basics.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Scopo
Questa pagina integra la diagnostica in **diode mode** con le avvertenze più importanti: molte letture “anomale” (es. cadute troppo basse o “short” apparenti) possono essere causate da **probe point danneggiati** o **saldature compromesse**, non dal diodo in sé.

## Prima di interpretare la lettura: verifica i punti di misura
### 1) Controlla probe point corrotti/rotti
I **probe point** sono punti esposti usati per misure su rail e segnali; possono **corrodersi** o **rompersi**, dando letture fuorvianti.
- Se il probe point è corroso/ossidato o ha micro-interruzioni, il multimetro può leggere valori “strani” (da verificare in base al caso), anche se il componente sotto è sano.
- La fonte sottolinea che i probe point danneggiati sono un problema reale e spesso richiedono attenzione specifica.

Riferimento: [Visual Inspection - Repair Basics](../fonti/visual-inspection-repair-basics.md).

### 2) Ispeziona saldature e giunzioni “che sembrano ok”
La fonte evidenzia che componenti con corrosione possono **apparire funzionali al test**, ma poi “non dureranno” se non si fa rework corretto.
- Anche una saldatura apparentemente passabile può essere compromessa (es. giunto incompleto, clump, flusso non uniforme).
- Se stai usando diode mode per concludere “corto su rail” o “diodo in corto”, prima verifica che il punto di contatto (pad/probe/saldatura) sia affidabile.

Riferimento: [Visual Inspection - Repair Basics](../fonti/visual-inspection-repair-basics.md).

### 3) Considera la corrosione “nascosta” (anche sotto componenti)
La fonte ricorda che la corrosione può essere **sotto chip BGA** o comunque non immediatamente visibile.
- Se la lettura in diode mode non torna e l’area è stata esposta a liquidi/ossidazione, la causa può essere sotto il package o su connessioni non visibili direttamente.

Riferimento: [Visual Inspection - Repair Basics](../fonti/visual-inspection-repair-basics.md).

## Come evitare letture “false” in diode mode
### A) Non fidarti della sola lettura: conferma con ispezione
La fonte insiste sul principio: “**Trust your eyes**” prima di complicare la diagnosi.
- Se vedi corrosione, polvere/ossido, tracce bruciate o saldature sospette, tratta la lettura come **sospetta** finché non sistemi/ricontrolli.

Riferimento: [Visual Inspection - Repair Basics](../fonti/visual-inspection-repair-basics.md).

### B) Attenzione ai corti “da sporcizia/umidità”
La fonte descrive che anche “polvere” apparentemente innocua può causare **micro-corto** tra pin.
- In questi casi, diode mode può sembrare indicare un guasto del diodo, ma la causa è un **ponte** tra contatti.

Riferimento: [Visual Inspection - Repair Basics](../fonti/visual-inspection-repair-basics.md).

## Collegamenti utili
- Pagina componente (test e interpretazione): [Diodi — test e guasti (anodo/catodo)](./diode.md)
- Ispezione e probe point: [Visual Inspection - Repair Basics](../fonti/visual-inspection-repair-basics.md)
- Tecnica per test diodi: [test-diodi](../tecniche/test-diodi.md)

## Checklist rapida (prima di concludere “diodo in corto”)
1. Probe point: integro e non corroso/ossidato.
2. Pad/saldature: giunto uniforme, senza ponti o incompletezza.
3. Area: nessun segno di corrosione/umidità/polvere che possa fare ponte.
4. Se il board è stato bagnato: considera corrosione nascosta (anche sotto package).
5. Solo dopo: interpreta diode mode e/o passa a test di conferma.

> Nota: i dettagli numerici/criteri di interpretazione diode mode (es. valori attesi) restano nella pagina [Diodi — test e guasti (anodo/catodo)](./diode.md).
