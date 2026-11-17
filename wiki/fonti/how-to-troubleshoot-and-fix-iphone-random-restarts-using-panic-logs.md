---
titolo: Fonti — How to Troubleshoot And Fix iPhone Random Restarts Using Panic Logs
tipo: fonte
riassunto: 'Guida esterna: usare i panic log per identificare il sensore/cavo non
  rilevato e indirizzare la riparazione dei restart casuali, con elenco messaggi/codici
  tipici per serie iPhone.'
modelli: []
fonti:
- raw/repairwiki/pagine/how-to-troubleshoot-and-fix-iphone-random-restarts-using-panic-logs.md
aggiornato: '2026-11-16'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# How to Troubleshoot And Fix iPhone Random Restarts Using Panic Logs (repair.wiki)

> Fonte: [How to Troubleshoot And Fix iPhone Random Restarts Using Panic Logs — repair.wiki](https://repair.wiki/w/How_to_Troubleshoot_And_Fix_iPhone_Random_Restarts_Using_Panic_Logs), CC BY-SA 3.0.

## Obiettivo
Troubleshooting dei **restart casuali** (o ogni pochi minuti) tramite **panic log**, con indicazione di quali sensori/flex/circuiti risultano non rilevati dall’OS.

## Procedura (riassunto)
1. **Selezionare il modello iPhone** nell’utility: https://panic.dankmeme.trade.
2. Eseguire test della scheda con **tutti i componenti “known good parts”** (parti già verificate e confermate non causare restart).
3. Recuperare i **panic log** dal dispositivo:
   - Impostazioni → Privacy → Analytics & Improvements → Analytics Data
   - Scorrere fino ai file che iniziano con **"panic-full..."**
   - Aprire il file **più recente** (per data).
4. Usare la lista “Panic Log Solution List” per il modello specifico (link alle pagine di fix per serie/modello).

## Panic Log Solution List (link dalla fonte)
- iPhone X: https://repair.wiki/w/How_To_Fix_an_iPhone_X_That_Randomly_Restarts
- iPhone XS / XS Max: https://repair.wiki/w/How_To_Fix_an_iPhone_XS_That_Randomly_Restarts
- iPhone 11: https://repair.wiki/w/How_To_Fix_an_iPhone_11_That_Randomly_Restarts
- iPhone 11 Pro / Pro Max: https://repair.wiki/w/How_To_Fix_an_iPhone_11_Pro_That_Randomly_Restarts
- iPhone 12 series: https://repair.wiki/w/How_To_Fix_an_iPhone_12_That_Randomly_Restarts
- iPhone 13 series: https://repair.wiki/w/How_To_Fix_an_iPhone_13_That_Randomly_Restarts
- iPhone 14 / 14 Plus: https://repair.wiki/w/How_To_Fix_an_iPhone_14_That_Randomly_Restarts
- iPhone 14 Pro / Pro Max: https://repair.wiki/w/How_To_Fix_an_iPhone_14_Pro_That_Randomly_Restarts
- iPhone 15 / 15 Plus: https://repair.wiki/w/How_To_Fix_an_iPhone_15_That_Randomly_Restarts
- iPhone 15 Pro / Pro Max: (link presente nella fonte, testo duplicato; da verificare URL esatto)
- iPhone SE 2020: https://repair.wiki/w/How_To_Fix_an_iPhone_SE_2020_That_Randomly_Restarts
- iPhone SE 2020 con No Touch e/o restart ~3 min (Mic1): https://repair.wiki/w/How_To_Fix_an_iPhone_SE_2020_with_No_Touch_and/or_3_Min_Restart_(Mic1_Problem)

## Messaggi/“fault” comuni nel panic log (dalla fonte)
> Nota: la fonte indica che **Hex** inizia con “0x.....” e che **DEC** è decimale.

### iPhone 12 series e precedenti
- **mic1** — charging port flex (SE 2020: potrebbe essere board issue)
- **mic2** — power button flex
- **prs0** — charging port flex
- **tg0b** — battery, battery connector o battery data line
- **ans2** — NAND related

### iPhone 13 series
- **0x800** — charging port flex
- **0x1000** — proximity flex
- **0x1800** — charging port flex & proximity flex cable
- **0x400** — sandwich separation

### iPhone 14 & 14 Plus
- **0x400000** — Wireless Charging Flex (Back Glass)
- **0x100000** — Charging Port Flex
- **0x500000** — Check taptic engine + charging port flex o comunicazione con la batteria
- **0x200000** — Proximity Flex Cable

### iPhone 14 Pro & 14 Pro Max
- **0x80000** — proximity flex
- **0x40000** — charging port flex
- **0x10000** — power button flex
- **0x20000** — sandwich separation

### iPhone 15 & 15 Plus
- **0x200000** — Wireless Charging Flex (Back Glass)
- **0x80000** — Charging Port Flex
- **0x100000** — Proximity Flex Cable

### iPhone 15 Pro & 15 Pro Max
- **0xa1** — battery
- **0x300000** — Charging Port Flex
- **0x400000** — Wireless Charging Flex
- **0x700000** — Charging Port + Wireless Charging Flex

### Codici “universal” (iPhone 13 up) — Hex + Decimal (dalla fonte)
- **0x20 (32)** — Charging circuit
- **0x40 (64)** — Gas gauge
- **0x41 (65)** — Battery data
- **0xa1 (161)** — Battery sensor
- **0xa9 (169)** — Battery data variant
- **0x400 (1024)** — Gyro
- **0x800 (2048)** — Charge port
- **0x1000 (4096)** — Proximity
- **0x4000 (16384)** — Battery sensor
- **0x20000 (131072)** — Gyro (14 Pro+)
- **0x40000 (262144)** — Charge port (14 Pro+)
- **0x80000 (524288)** — Proximity (14–17)
- **0x100000 (1048576)** — Power button
- **0x200000 (2097152)** — Front sensor / Wireless coil
- **0x300000 (3145728)** — USB‑C (Pro models)
- **0x400000 (4194304)** — Wireless coil
- **0x500000 (5242880)** — Battery

## Note operative (da fonte)
- La fonte afferma che iPhone/iPad possono riavviarsi casualmente o ciclicamente in base a scenari diversi.
- La fonte collega il problema al fatto che **ogni modello ha sensori “unici”** che devono essere rilevati dall’OS; se non rilevati, può verificarsi il restart.

---

## Contraddizioni / gap
- La fonte non fornisce procedure di misura passo-passo: rimanda alle pagine specifiche per modello.
- Alcuni link nella “Panic Log Solution List” risultano testualmente duplicati o con URL non univoco (es. iPhone 15 Pro/Pro Max): **da verificare**.
