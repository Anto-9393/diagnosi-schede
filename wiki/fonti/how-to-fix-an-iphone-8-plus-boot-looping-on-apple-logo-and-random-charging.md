---
titolo: Fonte — iPhone 8 Plus boot loop su logo Apple e charging random (Hydra/Tristar/PMIC)
tipo: fonte
riassunto: 'Riassunto della fonte esterna: iPhone 8 Plus in boot loop su logo Apple
  con ricarica intermittente; diagnostica DCPS con sospetto Hydra/Tristar/PMIC e verifica
  tramite ispezione/termica e sostituzioni (porta Lightning flex, camera frontale,
  Hydra IC).'
modelli:
- iPhone 8 Plus
fonti:
- raw/repairwiki/pagine/how-to-fix-an-iphone-8-plus-boot-looping-on-apple-logo-and-random-charging.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# How to Fix an iPhone 8 Plus boot looping on apple logo and random charging — repair.wiki (CC BY-SA 3.0)

## Problema (descrizione)
- Dispositivo bloccato in **boot loop sul logo Apple**.
- Avvio **a volte** ma **non stabile**.
- **Ricarica incoerente**: a volte carica, a volte no.

## Sintomi riportati
- **Apple logo loop** e boot non affidabile.
- **Charging random**.
- **Batteria nuova testata**: nessun miglioramento.
- Su **DCPS**: la corrente sale con un comportamento anomalo quando si prova ad avviare.
- **Non carica in modo consistente** anche con **cavi noti buoni**.
- **Hydra IC**: in ispezione termica risulta **calda/scalda**.

## Diagnostica (passi della fonte)
### 1) Ispezione visiva
- Controllo di **corrosione o danni** attorno a:
  - **Hydra IC**
  - **Tristar**
  - **connettore batteria**

### 2) Analisi con DCPS
- La fonte indica che la sequenza pre-boot “normale” dovrebbe **rampare** così:
  - **0.020A → 0.080A → 0.200A**
- Un **salto diretto a 0.200A** viene interpretato come indicazione di guasto nella **catena Hydra/Tristar/PMIC**.

### 3) Parts swapping (sostituzioni/test)
- **Sostituzione batteria**: nessun effetto.
- Test con:
  - **charging port flex** noto buono
  - **front facing camera** nota buona

### 4) Controllo termico
- **Hydra IC** che **scalda** (thermal inspection) → supporta l’ipotesi di anomalia sul componente.

## Riparazione (passi della fonte)
1. **Sostituire/testare il charging port flex**.
2. **Sostituire/testare la front facing camera**.
3. Se il problema persiste → **sostituire Hydra IC**.
4. Verificare su **DCPS**:
   - boot e charging behavior
   - aspettarsi il **ramping corretto** (come da sequenza indicata in diagnosi)
5. Confermare finale:
   - boot **stabile**
   - charging **consistente**
   - **profilo termico normale**

## Componenti citati dalla fonte (per collegamenti wiki)
- [Hydra IC](../componenti/hydra-ic.md)
- [Tristar](../componenti/tristar.md)
- [PMIC](../componenti/pmic.md)

## Note di integrazione per la wiki
- Valori DCPS e interpretazione “salto diretto a 0.200A” sono riportati dalla fonte; per misure operative e procedure dettagliate fare riferimento alle pagine:
  - [DCPS](../strumenti/alimentatore-da-banco.md)
  - [Test DCPS e diagnosi Kraken IC](../tecniche/test-dcps-e-diagnosi-kraken-ic.md)
  - [Test Tristar](../tecniche/test-tristar-e-diagnosi-non-carica-iphone.md)
  - [Test Hydra/PMIC](da verificare)
