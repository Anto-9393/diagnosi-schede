---
titolo: Restart casuali con panic log — cause probabili e diagnosi
tipo: sintomo
riassunto: 'Per restart casuali: leggere panic-full, identificare il sensore/cavo
  non rilevato dal log e verificare flex (prossimità/charging/power), batteria/dati,
  NAND, taptic engine e possibili problemi di separazione/sandwich.'
modelli: []
fonti:
- raw/repairwiki/pagine/how-to-troubleshoot-and-fix-iphone-random-restarts-using-panic-logs.md
aggiornato: '2026-11-16'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Sintomo
Restart casuali (o ogni pochi minuti) con indicazioni nel panic log su sensori/parti non rilevati.

La fonte indica che iPhone/iPad “restart randomly” e che ogni modello ha sensori unici: se l’OS non li rileva, può riavviare.

## Dove leggere il panic log (metodo)
1. Sul dispositivo: **Impostazioni → Privacy → Analytics & Improvements → Analytics Data**.
2. Scorrere fino ai file che iniziano con **`panic-full...`**.
3. Aprire il file **più recente** (data più recente).
4. Usare il messaggio del panic log per capire **quale sensore/parte non viene rilevata** e seguire la soluzione dedicata per modello.

> Nota: la fonte cita anche un tool esterno per consultare/interpretare i log: **https://panic.dankmeme.trade** (da verificare per compatibilità con i modelli specifici).

## Cause probabili (in base ai messaggi tipici del panic log)
Di seguito i messaggi “common panic log faults” riportati dalla fonte. La diagnosi pratica è: **verificare la parte associata al codice** (flex/cavo, batteria, NAND, taptic engine, ecc.) e poi confermare con misure/controlli.

### iPhone 12 e serie precedenti
- **`mic1`** — *charging port flex* (SE 2020: possibile board issue, da verificare)
- **`mic2`** — *power button flex*
- **`prs0`** — *charging port flex*
- **`tg0b`** — *battery, battery connector or battery data line*
- **`ans2`** — *NAND related*

### iPhone 13
- **`0x800`** — *charging port flex*
- **`0x1000`** — *proximity flex*
- **`0x1800`** — *charging port flex & proximity flex cable*
- **`0x400`** — *sandwich separation*

### iPhone 14 e 14 Plus
- **`0x400000`** — *Wireless Charging Flex (Back Glass)*
- **`0x100000`** — *Charging Port Flex*
- **`0x500000`** — *Check the taptic engine as well as the charging port flex or a communication problem with the battery*
- **`0x200000`** — *Proximity Flex Cable*

### iPhone 14 Pro e 14 Pro Max
- **`0x80000`** — *proximity flex*
- **`0x40000`** — *charging port flex*
- **`0x10000`** — *power button flex*
- **`0x20000`** — *sandwich separation*

### iPhone 15 e 15 Plus
- **`0x200000`** — *Wireless Charging Flex (Back Glass)*
- **`0x80000`** — *Charging Port Flex*
- **`0x100000`** — *Proximity Flex Cable*

### iPhone 15 Pro e 15 Pro Max
- **`0xa1`** — *battery*
- **`0x300000`** — *Charging Port Flex*
- **`0x400000`** — *Wireless Charging Flex*
- **`0x700000`** — *Charging Port + Wireless Charging Flex*

### Codici “universal” (iPhone 13 up, Hex + Decimal)
La fonte fornisce una mappatura utile per interpretare i codici:
- **`0x20` (32)** — Charging circuit
- **`0x40` (64)** — Gas gauge
- **`0x41` (65)** — Battery data
- **`0xa1` (161)** — Battery sensor
- **`0xa9` (169)** — Battery data variant
- **`0x400` (1024)** — Gyro
- **`0x800` (2048)** — Charge port
- **`0x1000` (4096)** — Proximity
- **`0x4000` (16384)** — Battery sensor
- **`0x20000` (131072)** — Gyro (14 Pro+)
- **`0x40000` (262144)** — Charge port (14 Pro+)
- **`0x80000` (524288)** — Proximity (14–17)
- **`0x100000` (1048576)** — Power button
- **`0x200000` (2097152)** — Front sensor / Wireless coil
- **`0x300000` (3145728)** — USB‑C (Pro models)
- **`0x400000` (4194304)** — Wireless coil
- **`0x500000` (5242880)** — Battery

## Metodo di diagnosi (workflow pratico)
La fonte suggerisce un approccio “per esclusione”:
1. **Testare la board con parti note buone**: usare componenti già verificati (known good parts) per escludere che il problema sia dovuto a componenti sostitutivi.
2. **Leggere il panic log** e identificare il **sensore/parte non rilevata** dal messaggio.
3. **Concentrarsi sulla famiglia di componenti** indicata dal codice:
   - flex/cavi (charging port, proximity, power button, wireless/back glass)
   - batteria (connettore/dati/sensore)
   - NAND (se `ans2`)
   - taptic engine (se indicato dal codice `0x500000` per 14/14 Plus)
   - possibile **sandwich separation** (se indicato `0x400` o `0x20000`)
4. Applicare la **procedura di riparazione dedicata per modello** (la fonte rimanda a pagine specifiche).

## Componenti/dispositivi da verificare (link)
La fonte non fornisce sigle di componenti (CD/IC/net) né posizioni esatte; quindi i link qui sono **a pagine di sintomo/dispositivo da creare o già presenti**.

Da verificare (da collegare a pagine componenti quando disponibili):
- **Flex/connector Charging Port** (codici: `mic1`, `prs0`, `0x800`, `0x100000`, `0x40000`, `0x80000`, `0x300000`, ecc.)
- **Flex/connector Proximity** (codici: `0x1000`, `0x1800`, `0x200000`, `0x80000`, `0x100000`, ecc.)
- **Flex/connector Power button** (codici: `mic2`, `0x10000`, `0x100000`)
- **Wireless Charging Flex / Back Glass / Wireless coil** (codici: `0x400000`, `0x200000` su 15/15 Plus, `0x400000` su 15 Pro, ecc.)
- **Batteria / connettore / linea dati / gas gauge** (codici: `tg0b`, `0xa1`, `0x41`, `0x40`, `0x500000`, ecc.)
- **NAND** (codice: `ans2`)
- **Taptic engine** (indicazione esplicita per `0x500000` su 14/14 Plus)
- **Sandwich separation** (codici: `0x400` su 13, `0x20000` su 14 Pro)

## Pagine correlate (soluzioni per modello, dalla fonte)
La fonte elenca pagine dedicate per modello; da usare dopo aver identificato il codice nel panic log:
- [How To Fix an iPhone X That Randomly Restarts](https://repair.wiki/w/How_To_Fix_an_iPhone_X_That_Randomly_Restarts)
- [How To Fix an iPhone XS and XS Max That Randomly Restarts](https://repair.wiki/w/How_To_Fix_an_iPhone_XS_That_Randomly_Restarts)
- [How To Fix an iPhone 11 That Randomly Restarts](https://repair.wiki/w/How_To_Fix_an_iPhone_11_That_Randomly_Restarts)
- [How To Fix an iPhone 11 Pro and 11 Pro Max That Randomly Restarts](https://repair.wiki/w/How_To_Fix_an_iPhone_11_Pro_That_Randomly_Restarts)
- [How To Fix an iPhone 12 Series That Randomly Restarts](https://repair.wiki/w/How_To_Fix_an_iPhone_12_That_Randomly_Restarts)
- [How To Fix an iPhone 13 Series That Randomly Restarts](https://repair.wiki/w/How_To_Fix_an_iPhone_13_That_Randomly_Restarts)
- [How To Fix an iPhone 14 and 14 Plus That Randomly Restarts](https://repair.wiki/w/How_To_Fix_an_iPhone_14_That_Randomly_Restarts)
- [How To Fix an iPhone 14 Pro and 14 Pro Max That Randomly Restarts](https://repair.wiki/w/How_To_Fix_an_iPhone_14_Pro_That_Randomly_Restarts)
- [How To Fix an iPhone 15 and 15 Plus That Randomly Restarts](https://repair.wiki/w/How_To_Fix_an_iPhone_15_That_Randomly_Restarts)
- [How To Fix an iPhone 15 Pro and 15 Pro Max That Randomly Restarts](https://repair.wiki/w/How_To_Fix_an_iPhone_15_Pro_That_Randomly_Restarts)
- [How To Fix an iPhone SE 2020 That Randomly Restarts](https://repair.wiki/w/How_To_Fix_an_iPhone_SE_2020_That_Randomly_Restarts)
- [How To Fix an iPhone SE 2020 with No Touch and/or 3 Min Restart (Mic1 Problem)](https://repair.wiki/w/How_To_Fix_an_iPhone_SE_2020_with_No_Touch_and/or_3_Min_Restart_(Mic1_Problem))
