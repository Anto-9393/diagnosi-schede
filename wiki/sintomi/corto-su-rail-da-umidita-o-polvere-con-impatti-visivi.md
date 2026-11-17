---
titolo: Corto su rail da umidità o polvere con impatti visivi
tipo: sintomo
riassunto: 'Quando umidità/polvere creano un ponte tra pin o piste, il corto può sembrare
  “solo sporcizia”: ispezione mirata, pulizia e rework mirato su pad/giunzioni.'
modelli: []
fonti:
- raw/repairwiki/pagine/visual-inspection-repair-basics.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Quando sospettarlo
Sospetta un corto “da contaminazione” (umidità o polvere) quando durante l’ispezione visiva noti:
- **depositi tipo polvere/particelle** vicino a **pin di IC, probe point, pad di connettori o zone di saldatura**;
- **segni di danno localizzato** (es. aree annerite/ossidate, tracce verdi/ossidazione) che suggeriscono esposizione a liquidi o corrosione;
- **giunzioni o piste** che sembrano “quasi ok” ma presentano **contaminazione** tale da poter fare da ponte.

La fonte descrive che una contaminazione che “sembra polvere” può in realtà **parzialmente cortocircuitare i pin**, e che spesso la riparazione può richiedere **flux e saldatura** dopo la pulizia/riwork. (Vedi sezione: *Short Circuit by Moisture*.)

## Cosa cercare visivamente (check rapido)
1. **Bordi e zone di probe point**: la fonte sottolinea che spesso il problema è vicino ai bordi e che i **probe point** possono corrodersi e creare problemi. Controlla anche punti esposti e aree attorno a test pad.
2. **Contaminazione “minima” ma localizzata**: non fermarti alla prima impressione. La fonte specifica che può apparire come polvere con danno “trascurabile”, ma essere un **ponte parziale** tra pin.
3. **Corrosione nascosta sotto componenti (BGA)**: se il problema è persistente e la zona non è chiara a vista, considera che la corrosione può essere **sotto** un chip BGA e richiedere un occhio allenato.
4. **Ispezione inclinata**: la fonte consiglia di **ispezionare il PCB inclinando** la scheda per far emergere corrosione non visibile “dritto”.

## Segnali pratici che “combaciano” con contaminazione
- Il corto sembra **localizzato** (non un guasto diffuso casuale), spesso in prossimità di **pin/pad**.
- Il componente può risultare “funzionante al test” ma **non durerà**: la fonte avverte che componenti con corrosione possono apparire ok ma **fallire dopo**; serve rework corretto.

## Quando sospettare corti da contaminazione
Sospetta con priorità quando:
- vedi **polvere/particelle** in zone critiche (pin, probe point, saldature);
- ci sono **segni di esposizione a liquidi** o corrosione;
- dopo test iniziali il problema **non si risolve** finché non fai pulizia/rework sulla zona contaminata.

## Nota su pulizia e “perdere le prove”
La fonte evidenzia che **lasciare l’ultrasonica per la fine** è spesso una buona idea: dopo la pulizia aggressiva, le evidenze del danno da liquido possono diventare **molto difficili da individuare**.

## Collegamenti utili
- Ispezione visiva e cosa controllare: [tecniche/analisi-visiva-e-ispezione-logic-board.md](../tecniche/analisi-visiva-e-ispezione-logic-board.md)
- Tecnica specifica per corti su rail: [tecniche/diagnosi-e-rimozione-corto-su-rail-con-capacitore-in-corto.md](../tecniche/diagnosi-e-rimozione-corto-su-rail-con-capacitore-in-corto.md)
- Esempio di sintomo correlato (corto su rail da MOSFET in corto): [sintomi/corto-su-rail-da-mosfet-bjt-in-corto.md](../sintomi/corto-su-rail-da-mosfet-bjt-in-corto.md)
