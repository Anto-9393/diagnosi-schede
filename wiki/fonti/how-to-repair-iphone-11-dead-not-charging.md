---
titolo: Fonte — How to repair iPhone 11 Dead Not Charging
tipo: fonte
riassunto: 'Procedura per iPhone 11 “dead not charging”: diagnosi via assorbimento
  0.140–0.150 A e conferma con split board; riparazione tramite reball CPU per cold
  solder sotto CPU.'
modelli:
- iPhone 11
fonti:
- raw/repairwiki/pagine/how-to-repair-iphone-11-dead-not-charging.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# How to repair iPhone 11 Dead Not Charging (repair.wiki)

> Fonte: [How to repair iPhone 11 Dead Not Charging — repair.wiki](https://repair.wiki/w/How_to_repair_iPhone_11_Dead_Not_Charging), CC BY-SA 3.0. Autori: vedi cronologia.

## Note di sicurezza / limitazioni (da fonte)
- La procedura è indicata **solo per recupero dati**.
- È una riparazione **estremamente delicata** e **non raccomandata per uso a lungo termine**.
- Dopo il reball della CPU, la **factory underfill (glue) sotto la CPU** non sarà più presente: il dispositivo diventa più vulnerabile a danni (anche da cadute o flessioni del PCB).
- Non è garantita l’affidabilità oltre l’estrazione dati.

## Descrizione problema (da fonte)
L’iPhone 11 è soggetto a **cold solder issues sotto la CPU**, tipicamente causati da:
- cicli di riscaldamento/raffreddamento nel tempo (stress termico)
- cadute o flessione della scheda
- debolezza dei giunti di saldatura in produzione

Conseguenza: la CPU **perde contatto in modo intermittente** con la logica.

## Sintomi (da fonte)
- Il telefono **non si accende**.
- Collegato a **DC power supply**: dopo il prompt di boot, la **corrente sale e si stabilizza** tra **0.140–0.150 A**, poi il processo resta “bloccato”.
- Se si **separa lo stack della logica** (lower e upper layer), il device **boota** normalmente → conferma problema di contatto sotto CPU.
- Il problema **si ripresenta** finché non si esegue il **reball** della CPU.

## Diagnosi (da fonte)
1. Collegare il telefono a una **DC power supply** e osservare il comportamento della corrente:
   - dopo il prompt di boot, lo stallo avviene con assorbimento **~0.140–0.150 A**.
2. **Split della logic board** (separare lower e upper layer):
   - se il telefono boota normalmente con i layer separati, si sospetta **cold solder sotto CPU**.
3. Riassemblare:
   - il dispositivo torna nello stesso stato di stallo (conferma).

## Riparazione (da fonte)
1. Rimuovere la **logic board** e **split** delle due parti.
2. Ispezione al microscopio delle **saldature/ball della CPU**:
   - cercare segni di **cracked/cold joints** (da fonte: possono essere visibili).
3. **Reball CPU**:
   - rimuovere il residuo di saldatura dalle **pad**
   - applicare **fresh solder balls** con stencil corretto
   - eseguire **reflow** della CPU con **profilo di temperatura controllato**
4. Riassemblare i layer e reinstallare la CPU.
5. Test su **DC power supply**:
   - il device dovrebbe **bootare normalmente**.

## Collegamenti utili (pagine wiki)
- Dispositivo: [iPhone 11](../dispositivi/iphone-11.md)
- Tecnica correlata (split/reball BB-PMU): [sandwich-board-separation-e-reball-bb-pmu](../tecniche/sandwich-board-separation-e-reball-bb-pmu.md)
