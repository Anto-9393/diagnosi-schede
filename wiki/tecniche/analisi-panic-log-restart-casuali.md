---
titolo: Analisi panic log / restart casuali — guida operativa (TG0B/TG0V)
tipo: tecnica
riassunto: Aggiunge come sotto-check nei panic log la presenza di TG0B/TG0V per distinguere
  guasto batteria vs problema di comunicazione batteria↔mobo.
modelli: []
fonti:
- raw/repairwiki/pagine/how-to-troubleshoot-and-fix-iphone-random-restarts-using-panic-logs.md
- raw/repairwiki/pagine/ipad-not-charging-battery-always-reporting-1-percent-charge.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# Analisi panic log / restart casuali — guida operativa (TG0B/TG0V)

> Tecnica generale per iPhone/iPad con riavvii casuali o a intervalli.

Questa pagina integra la guida esistente con un criterio specifico indicato dalla fonte esterna: **se nel panic log compaiono riferimenti ai sensori TG0B e TG0V**, il problema è da ricondurre **alla batteria** oppure a un **problema di comunicazione tra batteria e motherboard**.

## 1) Obiettivo diagnostico
Gli iPhone/iPad possono riavviarsi in modo casuale o ogni pochi minuti in base a scenari diversi. La fonte indica che ogni modello tende ad avere sensori specifici che devono essere rilevati dall’OS: se non vengono rilevati, il sistema può riavviarsi.

## 2) Primo step: test con parti note-good
La fonte raccomanda di **testare la scheda problematica con tutte le parti note-good** (parti già testate e confermate non causare restart).

## 3) Dove trovare il panic log su iOS
Per recuperare il panic log:
1. Vai su **Impostazioni → Privacy → Analytics & Improvements → Analytics Data**
2. Scorri fino ai file che iniziano con **"panic-full..."**
3. Apri il file **più recente** (in base alla data nel nome/nel contenuto)

## 4) Interpretazione: HEX vs DEC
La fonte richiama due formati:
- **HEX**: inizia con **"0x....."**
- **DEC**: è **decimale**

In pratica, quando nel panic log trovi un valore in HEX, puoi convertirlo/ricondurlo ai codici decimali equivalenti (la fonte fornisce una tabella “universal codes” per iPhone 13 e superiori).

## 5) Codici/messeggi comuni (per restringere l’area)
La fonte elenca messaggi/codici ricorrenti utili a indirizzare la ricerca del componente/cavo/sensore.

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
- **0x500000** — Check taptic engine + charging port flex oppure comunicazione problem con la batteria
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

### Universal codes (iPhone 13 up) — HEX + Decimal
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

## 6) Sotto-check aggiuntivo: TG0B / TG0V (batteria vs comunicazione)
Se il device **si riavvia** e/o mostra sintomi legati alla batteria (es. percentuale batteria bloccata e mancata ricarica), la fonte esterna indica un criterio specifico da cercare nel panic log:

- **Cerca nel panic log riferimenti ai sensori/termini TG0B e TG0V**.
- **Se TG0B e TG0V sono presenti nel panic log**, il problema è da considerare **correlato alla batteria** oppure a un **problema di comunicazione tra batteria e motherboard**.

> Nota: la fonte esterna specifica che **tg0b** può riferirsi a **battery, battery connector o battery data line**.

### Cosa fare quando TG0B/TG0V sono presenti (workflow coerente con la fonte)
1. **Verifica meccanica del connettore batteria**: controllare che la vite del connettore batteria sia presente e avvitata correttamente.
2. **Ispezione del Battery FPC**: rimuovere la motherboard e controllare il Battery FPC per danni fisici (la fonte indica che è comune che il connettore FPC sia danneggiato se il device era già stato aperto o se qualcosa è stato inserito per scollegare la batteria).
3. **Controllo contatto**: la fonte suggerisce di toccare la connessione con una coppia di tweezers per verificare che sia solida e non crepata.
4. Se tutto sembra ok: **test con una nuova batteria**.

## 7) Collegamento alle procedure modello-specifiche
La fonte rimanda a pagine “solution list” per modelli specifici (link esterni repair.wiki presenti nella pagina originale).

## 8) Come usare i panic log per guidare la sostituzione
Workflow coerente con la fonte:
1. Recupera il **panic-full...** più recente.
2. Identifica nel log i **messaggi/codici** (HEX o DEC).
3. Usa la tabella/categorie della fonte per associare il codice a un’area (es. charging port flex, proximity flex, battery, wireless coil, ecc.).
4. **Aggiungi il sotto-check TG0B/TG0V**: se presenti, dai priorità a verifiche/repair su **batteria e connessione batteria↔mobo**.
5. Torna allo step 1: verifica la causa sostituendo/validando con **parti note-good** l’area indicata dal panic log.

## Rischi / note operative
La fonte non descrive rischi specifici di procedura (es. gestione batteria, ESD, ecc.). Da verificare per la parte di sicurezza operativa.
