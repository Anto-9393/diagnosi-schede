---
titolo: Visual Inspection — Repair Basics (fonte esterna)
tipo: fonte
riassunto: 'Guida pratica: ispezione visiva della logic board, ricerca danni su probe
  point/leg IC, corrosione (anche sotto BGA), corti da umidità e rework dei giunti
  saldati compromessi.'
modelli: []
fonti:
- raw/repairwiki/pagine/visual-inspection-repair-basics.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

> Fonte: [Visual Inspection - Repair Basics — repair.wiki](https://repair.wiki/w/Visual_Inspection_-_Repair_Basics), CC BY-SA 3.0.

## Scopo della fonte
La fonte insiste sul fatto che, nella riparazione di schede logiche, l’ispezione visiva spesso precede (e guida) la diagnosi: “fidati dei tuoi occhi” prima di entrare in analisi troppo astratte.

## Cosa controllare durante l’ispezione
- **Bordi della scheda**: la maggior parte dei problemi viene indicata come localizzabile in quell’area.
- **Probe point danneggiati**: punti di test/esposizione possono **corrodere o rompersi**; possono sembrare ancora “misurabili” ma essere compromessi.
- **Danni da liquidi**: corrosione, ruggine, tracce bruciate e “green dust” sono considerati marker utili per risalire alla causa.
- **Corrosione sotto BGA**: la fonte ricorda che la corrosione può essere **sotto chip BGA** (contatti sotto la package), quindi non sempre è evidente “a colpo d’occhio”.
- **Leg (pin) degli IC**: controllare attentamente le gambe dei chip, perché il difetto può non essere immediatamente visibile.
- **Ispezione inclinata**: inclinare la scheda aiuta a far emergere corrosione nascosta non visibile in visione frontale.
- **Qualità dei giunti di saldatura**: anche giunti “che sembrano ok” possono essere difettosi (grumi, giunti incompleti).

## Corti da umidità/polvere
La fonte descrive che ciò che può sembrare “solo polvere” può in realtà causare un **parziale corto tra pin** (corto da umidità/contaminazione). In quel caso viene indicato che spesso la riparazione può essere fatta con **flux e saldatura** (da contestualizzare sul caso reale).

## Giunti e componenti che “passano i test” ma non dureranno
Punto chiave: componenti con corrosione possono **risultare funzionali in test**, ma la riparazione non sarà stabile nel tempo. La fonte sottolinea l’importanza del **rework corretto**.

## Pulizia: quando farla
La fonte suggerisce di **lasciare l’ultrasonic cleaning per la fine**: una volta pulita la scheda e rimossa l’evidenza del danno da acqua, le aree corrose diventano più difficili da individuare.

## Probe point “non funzionali”
La fonte riporta un esempio concettuale: alcuni probe point possono essere presenti per misurazione, ma il percorso elettrico può portare a un nodo che serve solo a quel test (es. collegamento a un singolo componente). In questi casi:
- il **probe point** può essere danneggiato,
- ma la riparazione reale deve concentrarsi sul **componente e sul pad/saldatura** che effettivamente fanno parte del circuito.

## Esercizio finale
La fonte chiude con un esercizio (“Can you see what’s wrong?”) per allenare l’occhio a riconoscere il difetto in foto/figure.

## Collegamenti utili (wiki)
- Tecnica generale di ispezione: tecniche/analisi-visiva-e-ispezione-logic-board.md
- Sintomo correlato a danni visivi da contaminazione: [corto-su-rail-da-umidita-o-polvere-con-impatti-visivi](../sintomi/corto-su-rail-da-umidita-o-polvere-con-impatti-visivi.md)
- Componenti spesso coinvolti in rework/diagnosi dopo ispezione: [diode](../componenti/diode.md), [transistor-mosfet-bjt-igbt-fet](../componenti/transistor-mosfet-bjt-igbt-fet.md), [condensatori-mlcc-elettrolitici-tantalio](../componenti/condensatori-mlcc-elettrolitici-tantalio.md)
- Strumento per evidenziare differenze termiche/aree sospette: [termocamera](../strumenti/termocamera.md)
