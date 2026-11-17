---
titolo: iPhone 8 Plus
tipo: dispositivo
riassunto: 'iPhone 8 Plus in loop su Apple logo con ricarica intermittente: su DCPS
  salto diretto a 0.200A e Hydra IC che scalda; sospetto su charging port flex/FC
  camera/Hydra.'
modelli:
- iPhone 8 Plus
fonti:
- raw/repairwiki/pagine/iphone-8-plus.md
- raw/repairwiki/pagine/how-to-fix-an-iphone-8-plus-boot-looping-on-apple-logo-and-random-charging.md
aggiornato: '2026-11-17'
categoria: phone
codici_modello: []
componenti_chiave:
- hydra-ic
- tristar
- pmic
casi: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# iPhone 8 Plus — boot looping Apple logo + charging random (Hydra/Tristar/PMIC)

## Pattern guasto (da fonte)
- **Loop su logo Apple**: boot non stabile, a volte avvia ma poi fallisce.
- **Ricarica incoerente**: a volte carica, a volte no (anche con **cavi noti buoni**).
- **Batteria nuova**: testata/sostituita, **nessun cambiamento**.
- **DCPS**: quando si prova a far partire il boot, la **corrente sale direttamente a 0.200A**.
- **Ispezione termica**: **Hydra IC** mostra **riscaldamento anomalo**.

> Nota: la fonte indica come sospetto la **catena Hydra/Tristar/PMIC** in base al comportamento DCPS e al riscaldamento Hydra.

## Dove guardare (ispezione)
- Controllare **corrosione o danni** attorno a:
  - [Hydra IC](../componenti/hydra-ic.md)
  - [Tristar](../componenti/tristar.md)
  - **connettore batteria**

## Diagnostica DCPS (valori attesi vs anomalia)
- **Sequenza preboot normale (ramping atteso)**: **0.020A → 0.080A → 0.200A**.
- **Anomalia descritta**: **salto diretto a 0.200A** quando si tenta il boot.
- Interpretazione da fonte: il salto diretto suggerisce un **fault nella path Hydra/Tristar/PMIC**.

Strumenti/tecnica collegati:
- [DC power supply (DCPS)](../strumenti/alimentatore-da-banco.md)
- [Test DCPS e diagnosi Kraken IC](../tecniche/test-dcps-e-diagnosi-kraken-ic.md)

## Diagnosi per esclusione (da fonte)
1. **Sostituzione batteria**: nessun effetto (quindi non risolve).
2. **Test con charging port flex noto buono**.
3. **Test con Front facing camera noto buono**.
4. **Controllo termico**: Hydra IC che scalda → aumenta probabilità Hydra.

Componenti/aree coinvolte (da fonte):
- [Hydra IC](../componenti/hydra-ic.md)
- [Tristar](../componenti/tristar.md)
- [PMIC](../componenti/pmic.md)
- Charging port flex: **da verificare sigla/parte** (la fonte non fornisce sigle)
- Front facing camera: **da verificare sigla/parte** (la fonte non fornisce sigle)

## Riparazione (ordine indicato dalla fonte)
1. **Sostituire/testare charging port flex**.
2. **Sostituire/testare Front facing camera**.
3. Se persiste:
   - **Sostituire Hydra IC**.
4. Verifiche finali:
   - Boot **stabile**.
   - **Charging consistente**.
   - **Profilo termico normale** (Hydra non deve scaldare in modo anomalo).

## Collegamenti utili (wiki)
- Sintomo correlato: [non-carica-o-alimentazione-instabile](../sintomi/non-carica-o-alimentazione-instabile.md)
- Tecnica correlata: [test DCPS e diagnosi Kraken IC](../tecniche/test-dcps-e-diagnosi-kraken-ic.md)
- Componenti:
  - [Hydra IC](../componenti/hydra-ic.md)
  - [Tristar](../componenti/tristar.md)
  - [PMIC](../componenti/pmic.md)

## Casi reali
- **Da completare**: la fonte è una guida esterna; qui vanno inseriti i tuoi casi con misure DCPS (0.020A→0.080A→0.200A vs salto diretto), esito sostituzioni (charging port flex / front camera / Hydra) e temperatura Hydra.
