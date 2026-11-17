---
titolo: Yangtze U3300 — Charging IC (iPhone XS)
tipo: componente
riassunto: 'Su iPhone XS, quando il telefono si avvia ma non carica, la fonte indica
  Yangtze (U3300) come causa frequente: spesso sostituendolo si risolvono problemi
  “tipo Tristar”; in rari casi può essere Hydra.'
modelli:
- iPhone XS
fonti:
- raw/repairwiki/pagine/iphone-xr-not-charging.md
- raw/repairwiki/pagine/iphone-xr-not-powering-on-not-charging.md
- raw/repairwiki/pagine/iphone-xs-not-charging.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Funzione
Yangtze (U3300) è l’**IC di carica**.

## Dove si trova (iPhone XS)
**Da verificare** (la fonte fornita parla di iPhone XS “not charging” ma non riporta la posizione fisica di U3300).

## Sintomi tipici quando si guasta (iPhone XS)
- Il telefono **si avvia** ma **non carica**.
- La fonte collega Yangtze a problemi “**Tristar**” (stesso tipo di comportamento visto su iPhone 7 e modelli più vecchi).
- In diagnosi con assorbimento molto basso: se si osserva **0,006 A o qualcosa di molto basso**, la fonte consiglia di **provare a sostituire Yangtze**.
- In rari casi, la causa può essere **Hydra**.

## Misure utili (iPhone XS)
> Valori dalla fonte, condizioni da rispettare.

- **Assorbimento molto basso in fase di test**: se ottieni **0,006 A** (o comunque “very low”), la fonte suggerisce di **sostituire Yangtze (U3300)**.
- **Test “split sandwich”**: la fonte raccomanda di **separare** (split the sandwich) e testare con **solo top board, batteria, charging port e screen** per isolare la causa.

## Condizioni/Note diagnostiche (iPhone XS)
- La fonte indica che, in alcuni casi, il problema “no charging” può derivare da **liquid damage** su **ear speaker flex** (con flood illuminator Face ID e sensore ALS): la corrosione può **cortocircuitare linee dati** e causare “bootlooping, not charging and other random issues”.
- La fonte propone, se sospetti danno da liquido sul flex:
  - sostituire il flex (perdi Face ID), oppure
  - rimuovere in modo sicuro il flood illuminator, pulire la corrosione e riposizionare, oppure
  - se non riparabile, **swap dei sensori** su un flex nuovo.

## Precauzioni in sostituzione (iPhone XS)
- La fonte non fornisce dettagli operativi di rimozione/saldatura per U3300 su iPhone XS.
- Precauzione diagnostica: prima di cambiare U3300, la fonte consiglia di **scollegare** molte parti (ear speaker flex, power button flex, camere, antenne, ecc.) e lasciare solo **screen, charging port e battery** per il test.

## Su iPhone XS (riassunto)
- Componente: **Yangtze (U3300)**
- Quando sospettarlo: **no charging** con telefono che **si avvia**, comportamento “tipo Tristar”, e/o assorbimento **~0,006 A** o molto basso durante test.
- Conferma consigliata dalla fonte: **split sandwich** e test con top board + batteria + charging port + screen; se ancora “very low”, sostituire Yangtze.
- Alternativa rara: **Hydra**.

## Link utili
- Tecnica (da fonte): [sostituzione-yangtze-u3300-e-precauzioni-schermo](../tecniche/sostituzione-yangtze-u3300-e-precauzioni-schermo.md)
- Sintomo correlato (piano): [non-carica-0-013a-iphone-xr](../sintomi/non-carica-0-013a-iphone-xr.md) (nota: valore/telefono diversi; usare come riferimento di sintomo, non come valore atteso per XS)
