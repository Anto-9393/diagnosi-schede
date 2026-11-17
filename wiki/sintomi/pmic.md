---
titolo: PMIC — pattern di corrente su DCPS (iPhone 11 dead/not charging)
tipo: sintomo
riassunto: 'iPhone 11: dopo prompt di boot la corrente su DCPS sale e si blocca a
  ~0.140–0.150 A; boot solo separando la logica → sospetto contatto CPU/cold solder
  (da distinguere da corto rail).'
modelli:
- iPhone 11
fonti:
- raw/repairwiki/pagine/how-to-repair-iphone-11-dead-not-charging.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Sintomo / pattern
Su iPhone 11 “dead / not charging”:
- **Non si accende**.
- Collegato a **DC power supply**: dopo il **prompt to boot**, la **corrente sale a ~0.140–0.150 A** e **rimane bloccata** (stallo).
- Se si **separa la logica** (lower/upper layer), il telefono **boota normalmente**, indicando che il problema è legato al **contatto CPU**.
- Il problema **si ripresenta** quando si rimonta la scheda (ricompare lo stesso stallo di corrente) finché non si interviene sul **reball CPU**.

> Nota fonte: la causa descritta è **cold solder issues sotto la CPU** (perdita di contatto intermittente con la logica), non un guasto “PMIC” in senso stretto; però il **pattern di corrente su DCPS** è utile come **differenziale** durante la diagnosi dell’area power/PMIC.

## Diagnosi differenziale: corto rail vs contatto CPU (cold solder)
### Più probabile: contatto CPU/cold solder sotto CPU
- Stallo su DCPS **dopo prompt to boot** con corrente **~0.140–0.150 A**.
- **Boot riuscito** quando si **splitta** la logica in due layer.
- **Ricaduta** nello stesso stallo quando si rimonta.

### Da verificare: corto su rail / assorbimento anomalo “da PMIC/linee”
La fonte non descrive direttamente un corto su rail per questo caso specifico; quindi la distinzione va fatta con misure dedicate (da verificare) e con le tecniche già presenti in wiki.

## Misure utili (da fare durante la diagnosi)
1. **DC power supply**: osservare il comportamento **dopo prompt to boot**.
   - Valore atteso nel caso fonte: **0.140–0.150 A** con **blocco**.
2. **Split logic board** (lower/upper layer):
   - Se il dispositivo **boota normalmente** con i layer separati → sospetto **contatto CPU/cold solder**.

## Riparazione associata (dalla fonte)
- **Reball CPU** dopo split e ispezione delle saldature sotto CPU.
- Dopo reball: su DCPS il dispositivo **dovrebbe boottare normalmente**.

## Collegamenti utili
- [componenti/pmic.md](../componenti/pmic.md)
- [strumenti/alimentatore-da-banco.md](../strumenti/alimentatore-da-banco.md)
- [tecniche/test-dcps-e-diagnosi-kraken-ic.md](../tecniche/test-dcps-e-diagnosi-kraken-ic.md)
- [tecniche/sandwich-board-separation-e-reball-bb-pmu.md](../tecniche/sandwich-board-separation-e-reball-bb-pmu.md)
- [dispositivi/iphone-11.md](../dispositivi/iphone-11.md)
