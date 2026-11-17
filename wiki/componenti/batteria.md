---
titolo: Batteria — accumulatore (Li-ion)
tipo: componente
riassunto: 'Aggiunta integrazione: danno da vite vicino al connettore batteria può
  causare “not powering on” (da fonte esterna), ma batteria difettosa resta la causa
  più comune per “low battery screen ma non carica”.'
modelli:
- iPad Pro 12.9 5th Gen
fonti:
- raw/repairwiki/pagine/how-to-fix-an-ipad-air-that-shows-the-low-battery-screen-but-will-not-charge.md
- raw/repairwiki/pagine/ipad-pro-12-9-5th-gen-not-powering-on-due-to-long-screw-damage.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Funzione
La batteria fornisce l’alimentazione al dispositivo. Nel caso descritto dalla fonte, il tablet mostra lo schermo “low battery” quando viene collegato al caricatore, ma non riesce a ricaricarsi/tenere la carica.

## Dove si trova
Da verificare (la fonte non indica posizione/MP).

## Sintomi tipici quando si guasta (da fonte)
- Il dispositivo mostra lo **schermo low battery** quando si collega il caricatore, ma **non carica**.
- Lo **schermo va in blank** (si spegne) **appena il caricatore viene scollegato**.
- La batteria è **troppo bassa** per alimentare correttamente l’iPad.

## Cause più probabili (da fonte)
- **Batteria vecchia o difettosa** che necessita di sostituzione.

## Misure utili
Da verificare (la fonte non riporta misure/valori).

## Modelli su cui compare
La fonte è specifica per **iPad Air** (modello non indicato nel testo fornito).

## Note operative
- Se il comportamento è coerente con “low battery screen ma non carica”, la fonte indica come causa più comune una batteria usurata/difettosa e quindi la **sostituzione della batteria**.

## Criteri/integrazione per il sintomo “low battery screen ma non carica”
Quando il dispositivo:
1) mostra **low battery** appena collegato al caricatore,
2) **non** aumenta la carica (non “tiene” l’alimentazione),
3) e lo schermo **si spegne** subito dopo lo scollegamento del caricatore,

la fonte considera la causa più comune una **batteria vecchia/difettosa** da sostituire.

Link sintomo: [low-battery-schermo-ma-non-carica](../sintomi/low-battery-schermo-ma-non-carica.md)

---

## Su iPad Pro 12.9 5th Gen — not powering on dopo riparazione (danno da vite vicino al connettore batteria)
> Nota: questa sezione non dice che la batteria sia difettosa; descrive un **danno meccanico da vite** che può interrompere una linea di alimentazione e portare a “not powering on”.

### Sintomi (da fonte)
- Con iPad collegato a **USB amp meter**: assorbe vicino a **0.02 A**, poi sale rapidamente a circa **0.5 A** e torna vicino a **0 A**.
- Con iPad collegato a **DCPSU**: assorbe **0.00 A** prima del prompt di boot, poi arriva a circa **0.014–0.025 A** dopo il prompt di boot.
- Presenza visibile di **danno da vite lunga** sullo standoff sopra le **screen FPC** nella zona centrale della scheda.
- Applicando pressione sulla board vicino allo standoff, a volte si riesce a far partire l’iPad.

### Causa più probabile (da fonte)
- **Traccia/via rotta sotto lo standoff** della vite lunga.
- In particolare la fonte indica come più probabile la linea **PP3V3_BSB** e/o la via che porta quella linea più in profondità.

### Riparazione (da fonte)
1. Rimuovere lo standoff con vite lunga (taglio delicato della top layer o rimozione con hot air).
2. Grattare via gli strati attorno allo standoff rimosso, con estrema cautela.
3. Verificare se la via che porta **PP3V3_BSB** è **allentata** o se la linea tra **C8300** e la via è **interrotta/danneggiata**.
4. Se danneggiata/allentata: eseguire un **jumper wire** dalla linea che va a **C8300** alla via.
5. Verificare un normale ciclo di boot su **DCPSU** e, se tutto ok, coprire l’area con **conformal coating**.

### Nota di workaround (da fonte)
- In alcuni casi (se serve solo data recovery) si può **clampare lo standoff** per applicare pressione alla via e ripristinare il contatto temporaneamente.

### Collegamento al “danno da vite vicino al connettore batteria”
Questa integrazione è utile quando il problema di “not powering on” compare **dopo** una riparazione con rimozione del display/schermo e si osserva **danno da vite lunga** vicino all’area del connettore batteria: la fonte attribuisce il problema a **PP3V3_BSB** (non a batteria difettosa).
