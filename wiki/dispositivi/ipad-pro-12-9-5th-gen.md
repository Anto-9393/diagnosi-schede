---
titolo: iPad Pro 12.9 5th Gen
tipo: dispositivo
riassunto: 'iPad Pro 12.9 5th Gen (A2378/A2379/A2461/A2462): non-powering dopo rimozione
  schermo per vite lunga su standoff; tipico su USB/DCPSU e riparazione su PP3V3_BSB/via.'
modelli:
- iPad Pro 12.9 5th Gen
fonti:
- raw/repairwiki/pagine/ipad-pro-12-9-5th-gen.md
- raw/repairwiki/pagine/ipad-pro-12-9-5th-gen-not-powering-on-due-to-long-screw-damage.md
aggiornato: '2026-11-17'
categoria: tablet
codici_modello:
- A2378
- A2379
- A2461
- A2462
componenti_chiave: []
casi: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# iPad Pro 12.9 5th Gen

- Uscita: 2021-05-21
- Codici modello: A2378, A2379, A2461, A2462

## Guasti tipici e casi

### Non-powering dopo riparazione schermo: danno da vite lunga su standoff (PP3V3_BSB)

**Fonte:** [IPad Pro 12.9 5th Gen not powering on due to long screw damage — repair.wiki](https://repair.wiki/w/IPad_Pro_12.9_5th_Gen_not_powering_on_due_to_long_screw_damage), CC BY-SA 3.0.

**Descrizione problema**
- iPad Pro 12.9 5th Gen (e probabilmente iPad 12.9 6th gen) può andare in **non-powering** dopo qualsiasi riparazione in cui lo schermo viene rimosso.
- La causa più probabile è un **danno da vite lunga** sullo **standoff** vicino al connettore batteria, al centro della board: c’è una vite più lunga delle altre; se inserita in uno standoff sbagliato anche di poco, può **rompere una linea di alimentazione necessaria**.

**Sintomi (misure)**
- Con iPad collegato a **USB amp meter**: assorbe **~0.02 A**, poi **sale rapidamente a ~0.5 A** e poi torna vicino allo **0 A**.
- Con iPad collegato a **DCPSU**: assorbe **0.00 A** prima del prompt di boot e arriva solo a **~0.014–0.025 A** dopo il prompt di boot.
- Presenza visibile di **danno da vite lunga** sullo standoff sopra le **screen FPC** in mezzo alla board.
- Applicando **pressione sulla board vicino allo standoff** durante il tentativo di boot, a volte l’iPad riesce ad accendersi.

**Diagnosi più probabile**
- **Traccia/via rotta sotto il terminale della vite**.
- In particolare: **PP3V3_BSB** e/o la **via** che porta quella linea più in profondità nella board.
- Verificare e riparare anche eventuali **altre linee** danneggiate.

**Riparazione (da fonte)**
1. Rimuovere lo standoff con vite lunga danneggiato.
   - Opzione A: tagliare con attenzione lo strato superiore della board attorno allo standoff.
   - Opzione B: usare **hot air** per scaldare e rimuovere lo standoff.
2. Con **lametta/scalpel**, grattare via gli strati della board in una piccola area attorno allo standoff rimosso.
   - Attenzione a non rompere altre linee.
   - La linea **PP3V3_BSB** risulta **leggermente sopra e a destra** dello standoff.
3. Controllare se la **via** che porta **PP3V3_BSB** più in profondità è **allentata** o se la linea che va da **C8300** alla via è **interrotta/danneggiata**.
4. Se linea danneggiata o via allentata: eseguire un **jumper wire** dalla linea che va a **C8300** alla via.
5. Verificare che l’iPad faccia un **normale boot cycle su DCPSU** e che tutto funzioni.
6. Se ok: coprire l’area con **conformal coating**.

**Caso particolare (da fonte)**
- Se serve solo recupero dati: si può **clampare lo standoff** per applicare pressione alla via, così da ristabilire il contatto con la linea abbastanza a far partire l’iPad e fare backup.

**Link utile (da fonte)**
- Video riparazione simile: https://youtu.be/823HF8IZckU?si=wV6fEc4ouPoI1hLm

## Note
- La pagina di dispositivo esistente risulta “Da completare”; questa sezione integra il caso specifico presente in fonte.
