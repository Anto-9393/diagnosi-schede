---
titolo: Hydra IC — controller/driver linea di carica (diagnosi heating anomalo)
tipo: componente
riassunto: 'Hydra IC: causa rara di “no charging” su iPhone XS; se scalda in modo
  anomalo e la DCPS salta a 0.200A, sospettare percorso Hydra/Tristar/PMIC e verificare
  con thermal inspection e test DCPS.'
modelli:
- iPhone 8 Plus
- iPhone XS
fonti:
- raw/repairwiki/pagine/how-to-fix-an-iphone-8-plus-boot-looping-on-apple-logo-and-random-charging.md
- raw/repairwiki/pagine/iphone-xs-not-charging.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Funzione
Hydra IC è coinvolto nel percorso di alimentazione/charging. La fonte indica che, in caso di guasto, può manifestarsi con **riscaldamento anomalo** e con comportamento anomalo della corrente misurata su alimentatore da banco (DCPS), suggerendo un fault nel percorso **Hydra/Tristar/PMIC**.

## Dove si trova
Posizione **da verificare**: la fonte non riporta coordinate precise; indica solo di controllare “around Hydra IC” con ispezione visiva e thermal inspection.

## Sintomi tipici quando si guasta
- **Heating anomalo** di Hydra IC (da confermare con thermal inspection).
- Su DCPS, durante la richiesta di boot: **corrente che salta direttamente a 0.200A** (da fonte iPhone 8 Plus).
- Comportamenti correlati riportati dalla fonte: **boot loop su Apple logo** e **carica random/inconsistente** (da fonte iPhone 8 Plus).
- Su iPhone XS: **no charging** (causa rara, in alternativa a Yangtze/U3300).

Link sintomi correlati (da verificare applicabilità al caso specifico):
- [temperatura-warning-e-non-carica.md](../sintomi/temperatura-warning-e-non-carica.md)

## Test e misure utili (con valori attesi)
### 1) Ispezione visiva
- Controllare **corrosione o danni attorno a Hydra IC**.
- La fonte iPhone 8 Plus suggerisce anche di controllare componenti correlati (Tristar e connettore batteria), ma i dettagli sono **da verificare** sul layout specifico.

### 2) Test su DCPS (ramping atteso)
La fonte iPhone 8 Plus riporta che la sequenza preboot “normale” dovrebbe **rampare** così:
- **0.020A → 0.080A → 0.200A**

Se invece si osserva:
- **salto diretto a 0.200A** quando si prova a far partire il device,

allora la fonte indica che ciò suggerisce un fault nel percorso **Hydra/Tristar/PMIC**.

> Nota: la fonte non specifica condizioni aggiuntive (es. batteria presente/rimossa, cavo inserito sì/no). Per i dettagli operativi, attenersi alla procedura DCPS della pagina tecnica collegata (da verificare quale pagina tecnica nel piano).

## Riparazione (indicazione dalla fonte)
- Prima: sostituire/testare componenti correlati (charging port flex e front facing camera, secondo la fonte iPhone 8 Plus).
- Se il problema persiste: **sostituire Hydra IC**.
- Conferma finale: **boot stabile**, **carica consistente**, **profilo termico normale**.

## Su iPhone 8 Plus
### iPhone 8 Plus — caso con heating Hydra IC e carica random
- Sintomi: **boot loop su Apple logo**, **carica random/inconsistente**, batteria nuova senza effetto.
- DCPS: corrente che **salta direttamente a 0.200A**.
- Thermal: **Hydra IC mostra heating anomalo**.
- Diagnosi/azione: se persiste dopo test/sostituzioni correlate, **sostituire Hydra IC**.

## Su iPhone XS
### iPhone XS — no charging (causa rara)
- Sintomi: **iPhone XS si accende ma non carica**.
- Priorità diagnostica indicata dalla fonte: in maggioranza dei casi risolve **sostituire Yangtze (U3300)**.
- In casi rari: **Hydra può essere la causa** del “no charging”.
- Azione indicata dalla fonte: **sostituire Hydra** e verificare se risolve.

> La fonte iPhone XS non riporta valori DCPS/thermal specifici per Hydra su questo modello: da verificare.

## Componenti correlati (da controllare insieme)
- [Tristar](../componenti/tristar.md)
- [PMIC](../componenti/pmic.md)
- [Yangtze U3300](../componenti/yangtze-u3300.md) (priorità sulla fonte iPhone XS)

## Note su sigla/net
Sigla/net di Hydra IC: **da verificare** (la fonte non riporta marcature o net specifici).
