---
titolo: 'Transistor (Qxxx) — BJT/FET/MOSFET/IGBT: checklist visiva gambe e saldature'
tipo: componente
riassunto: 'Checklist visiva pre-test per transistor Qxxx: bad legs, giunti incompleti,
  segni di surriscaldamento/ossidazione e cosa controllare prima del multimetro/diode
  mode.'
modelli: []
fonti:
- raw/repairwiki/pagine/transistors-repair-basics.md
- raw/repairwiki/pagine/visual-inspection-repair-basics.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Scopo (prima dei test elettrici)
Prima di misurare in **diode mode** o resistenza, fai una verifica “meccanica” su **Qxxx** (BJT/FET/MOSFET/IGBT): molti guasti da riparazione falliscono perché il componente risulta “quasi” saldato o con **gamba non affidabile**.

Fonte: [Visual Inspection - Repair Basics](../fonti/visual-inspection-repair-basics.md).

## Checklist visiva rapida (Qxxx)
### 1) Bad legs / saldature non affidabili
- Controlla **tutte le gambe** del transistor (anche quelle che “sembrano ok”). La fonte sottolinea che i **bad legs** non sono sempre evidenti a occhio.
- Cerca:
  - giunto “puntiforme” (non bagnato)
  - saldatura che non forma una continuità uniforme tra pad e gamba
  - gamba che sembra “appoggiata” ma non realmente fusa

Fonte: [Visual Inspection - Repair Basics](../fonti/visual-inspection-repair-basics.md).

### 2) Giunti incompleti / grumi / flusso irregolare
- Verifica che il giunto sia **uniforme** e che il flusso di stagno sia coerente.
- La fonte richiama che anche giunti che “si sono mossi” e sembrano colare possono essere **incompleti** o con **clumps**.

Fonte: [Visual Inspection - Repair Basics](../fonti/visual-inspection-repair-basics.md).

### 3) Segni di surriscaldamento o danno meccanico
- Ispeziona per:
  - discolorazione attorno al package
  - burn marks / segni di stress termico
  - crepe o deformazioni visibili

(Nota: i segni di surriscaldamento sono citati come indicatori generali di guasto nei transistor; per la parte “visiva” la fonte di ispezione è quella sopra.)

Fonte transistor: [Transistors - Repair Basics](../fonti/transistors-repair-basics.md).
Fonte ispezione: [Visual Inspection - Repair Basics](../fonti/visual-inspection-repair-basics.md).

### 4) Corrosione e “green dust” vicino a gambe/pad
- Cerca corrosione/ossidazione e residui (es. “green dust”).
- Se il problema è da liquidi/umidità, la fonte evidenzia che anche “polvere” può creare **corto parziale** tra pin.

Fonte: [Visual Inspection - Repair Basics](../fonti/visual-inspection-repair-basics.md).

### 5) Ispezione “di lato” (angolo) per trovare difetti nascosti
- Inclina la scheda: la fonte indica che guardando **a un angolo** emergono corrosioni nascoste che non si vedono in asse.

Fonte: [Visual Inspection - Repair Basics](../fonti/visual-inspection-repair-basics.md).

### 6) Dopo pulizia: attenzione a cosa sparisce
- La fonte consiglia di lasciare l’**ultrasonic cleaning per la fine**: una volta pulito, le evidenze del danno da liquidi diventano più difficili da individuare.

Fonte: [Visual Inspection - Repair Basics](../fonti/visual-inspection-repair-basics.md).

## Cosa fare se trovi un “bad leg” (prima di misurare)
1. Rework del giunto: rifusione/ri-saldatura del pad e della gamba interessata.
2. Se vedi corrosione: rimuovere/bonificare l’area prima di ripetere i test.
3. Solo dopo: passa ai test elettrici (diode mode / resistenza) per confermare il guasto.

Fonte (principio di rework e importanza dell’ispezione): [Visual Inspection - Repair Basics](../fonti/visual-inspection-repair-basics.md).

## Collegamenti utili
- [Tecnica: test transistor in diode mode](../tecniche/test-transistor-in-diode-mode.md)
- [Sintomo: corto su rail da MOSFET/BJT in corto](../sintomi/corto-su-rail-da-mosfet-bjt-in-corto.md)
- [Sintomo: corto su rail da umidità o polvere con impatti visivi](../sintomi/corto-su-rail-da-umidita-o-polvere-con-impatti-visivi.md)
- [Transistor (Qxxx) — BJT/FET/MOSFET/IGBT: sintomi e test](transistor-mosfet-bjt-igbt-fet.md)

## Note su limiti della checklist
- La checklist visiva non sostituisce i test: la fonte sui transistor descrive guasti (corto/aperto/leakage) e soglie di misura, ma i **net specifici** e la posizione esatta su ogni modello sono da verificare.

Fonte: [Transistors - Repair Basics](../fonti/transistors-repair-basics.md).
