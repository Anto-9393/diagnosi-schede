---
titolo: Capacitori — test e sostituzione
tipo: tecnica
riassunto: 'Procedura generale per testare e sostituire i capacitori: scarica, test
  corto fuori circuito, misure con LCR (C/ESR) e criteri di sostituzione.'
modelli: []
fonti:
- raw/repairwiki/pagine/capacitors-repair-basics.md
- raw/repairwiki/pagine/ipad-not-charging-battery-always-reporting-1-percent-charge.md
- raw/repairwiki/pagine/resistors-repair-basics.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Scopo
Questa pagina raccoglie una procedura **generale** per verificare e sostituire i capacitori su schede iPhone/iPad, basata su [Capacitors - Repair Basics](https://repair.wiki/w/Capacitors_-_Repair_Basics) (repair.wiki).

> Nota: la fonte fornita in input include anche una pagina su **resistori**; i contenuti qui sotto sono quelli già presenti nella pagina esistente e risultano attribuiti ai **capacitori** (da verificare se la parte “resistors-repair-basics” è stata inclusa per errore).

## 1) Ispezione visiva (prima di misurare)
1. Controlla il componente.
2. Se noti **discolorazione** o **rigonfiamento** del case (soprattutto su **elettrolitici**), considera il componente **da sostituire**.

## 2) Scarica del condensatore (obbligatoria)
Prima del test, assicurati che il condensatore sia scarico.
- Scarica i terminali **cortocircuitandoli con una resistenza da 20–100 Ω** finché la tensione sul condensatore non scende a **0 V**.

## 3) Test “short” fuori circuito (multimetro in resistenza)
Secondo la fonte, i condensatori spesso guastano **in corto**.
1. Rimuovi/isolalo dal circuito (test **fuori circuito**).
2. Metti il multimetro in **modalità resistenza**.
3. Osserva il comportamento nel tempo:
   - All’inizio puoi leggere **resistenza bassa** perché il condensatore si sta caricando.
   - La resistenza dovrebbe **aumentare con il tempo**.
   - La fonte indica come ideale che entro **~10 s** la resistenza arrivi nell’ordine dei **kΩ**.

**Interpretazione (da fonte):**
- Se la resistenza resta bassa/stabile (non sale) → sospetto forte di **corto**.

## 4) Test con LCR meter fuori circuito (C e ESR)
Se non hai trovato un corto ma il comportamento del circuito resta anomalo/subottimale, passa a misure più informative.
1. Testa **fuori circuito** con **LCR meter**.
2. LCR meter ti permette di misurare:
   - **Capacitance (C)**
   - **ESR** (Equivalent Series Resistance)
3. La fonte consiglia di confrontare l’**ESR** con un condensatore **simile** presente in circuito, perché l’ESR varia tra tipologie.
4. In generale:
   - **ESR più alto** = prestazioni del condensatore **meno desiderabili**.

### Criteri di accettabilità (da fonte)
- **Capacitance (C):** misura entro il **±5%** del valore nominale → accettabile.
- **Elettrolitici:** tolleranza fino a **±20%** → ancora accettabile.

## 5) Sostituzione — criteri pratici (da fonte)
Quando sostituisci un condensatore guasto, la fonte indica questi punti (in ordine di importanza pratica):

1. **Capacitance (C)**
   - Scegli **lo stesso valore di capacità**.
   - È **particolarmente importante** se il condensatore era usato in **circuiti di timing**.
   - Se era usato per **voltage smoothing** (filtraggio/attenuazione ripple), **capacitance maggiore** può funzionare comunque.

2. **Voltage rating (tensione nominale)**
   - Scegli una tensione nominale **uguale o superiore** a quella originale.
   - La fonte collega una tensione nominale più alta a **dimensioni fisiche maggiori**.

3. **Tipo di condensatore**
   - Preferisci lo **stesso tipo**.
   - In alternativa, puoi usare un tipo diverso se le **dimensioni** non sono un vincolo.

4. **Dimensioni fisiche / footprint**
   - Preferisci dimensioni **uguali**.
   - Se non disponibili e non ci sono vincoli dimensionali, puoi scegliere anche **più grande o più piccolo**, purché rispetti **tensione nominale** e funzione “come l’originale”.

## Note operative (da fonte)
- La fonte afferma che i condensatori spesso falliscono **in corto**: per questo il test in resistenza fuori circuito è un primo step utile.
- Per misure di valore e ESR, la fonte raccomanda **LCR meter fuori circuito**.

## Rischi / attenzioni
- La fonte richiede esplicitamente la **scarica** prima del test (resistenza 20–100 Ω fino a **0 V**).
- Dettagli su rischi specifici di saldatura/gestione termica non sono presenti nella fonte: **da verificare**.

## Link utili
- Fonte: [Capacitors - Repair Basics](https://repair.wiki/w/Capacitors_-_Repair_Basics)
