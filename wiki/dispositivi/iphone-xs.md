---
titolo: iPhone XS
tipo: dispositivo
riassunto: 'iPhone XS che si accende ma non carica: isolare ear speaker flex/Face
  ID/ALS e poi sospettare Yangtze (U3300) come causa più comune; Hydra rara.'
modelli:
- iPhone XS
fonti:
- raw/repairwiki/pagine/iphone-xs.md
- raw/repairwiki/pagine/iphone-xs-not-charging.md
aggiornato: '2026-11-17'
categoria: phone
codici_modello: []
componenti_chiave:
- yangtze-u3300
- hydra
casi: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# iPhone XS

## Codici modello
- Codici modello: **da verificare** (non indicati nella fonte).

## Guasti tipici (da fonte)
### iPhone XS si accende ma **non carica**
**Descrizione (fonte):** “iPhone XS will turn on but does not charge”.

## Regola di isolamento (ordine pratico)
1. **Scollega tutto** (fonte): ear speaker flex, power button flex, camere, antenne, ecc.
2. **Lascia solo** (fonte):
   - schermo
   - porta di ricarica
   - batteria
3. Se **non carica ancora**, procedi con test/sostituzioni mirate (fonte):
   - prova con **porta di ricarica nota buona**
   - prova con **batteria nota buona**
   - prova con **schermo noto buono**

## Sospetti principali
### 1) Ear speaker flex con flood illuminator (Face ID) + ALS (auto brightness/True Tone)
- **Quando sospettarlo (fonte):** spesso danneggiato da liquidi.
- **Perché (fonte):** i sensori sono vicino alla zona della griglia auricolare; è facile che entri liquido e che la corrosione **corti le linee dati sotto i sensori**, causando “bootlooping, not charging and other random issues”.
- **Cosa fare (fonte):**
  - sostituire il flex **perdere Face ID**
  - oppure rimuovere in modo sicuro il flood illuminator dal flex, pulire la corrosione e riposizionarlo
  - oppure, se il flex è oltre riparazione, **scambiare i sensori** su un nuovo flex

> Nota: la fonte non specifica misure elettriche dedicate a questo ramo; l’isolamento consigliato è “scollega tutto” e lascia solo le parti minime.

### 2) Yangtze (U3300) — causa più comune
- **Indicazione (fonte):** “In majority of cases, you'll find that replacing Yangtze (U3300) will solve charging problems”.
- **Relazione (fonte):** Yangtze “will give the common ‘Tristar’ issues that you would see on iPhone 7 and older models”.
- **Approccio consigliato (fonte):**
  - consiglia di **split the sandwich** e testare la ricarica con **solo**: top board, batteria, porta di ricarica e schermo.
- **Soglia/indicazione di misura (fonte):**
  - se ottieni **0.006 A** (o “something very low”), prova a **sostituire Yangtze**.

Collegamenti utili:
- [Yangtze (U3300)](../componenti/yangtze-u3300.md)
- [Tristar](../componenti/tristar.md) (per il riferimento alle “Tristar issues” citate dalla fonte)

### 3) Hydra — rara
- **Indicazione (fonte):** “In rare cases, Hydra will be the cause of the no charging”.
- **Azione (fonte):** “Replace Hydra and see if that solves it.”

Collegamenti utili:
- [Hydra](../componenti/hydra-ic.md)

## Casi
- Casi reali: **da completare** (nessun caso specifico presente nella fonte fornita).

## Fonte
- [IPhone XS Not Charging — repair.wiki](../fonti/iphone-xs-not-charging.md)
