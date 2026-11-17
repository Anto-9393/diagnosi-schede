---
titolo: I2C/connessione batteria — connettore screw/FPC e contatto verso motherboard
tipo: componente
riassunto: Connessione batteria instabile (screw mancante/errato, FPC danneggiato,
  pin sollevati o contatto crepato) → batteria bloccata (1%/0%), non carica e possibili
  restart; controllare serraggio e integrità FPC, poi test batteria.
modelli:
- iPad Air 1
- iPad Air 2
- iPad 5
- iPad 6
- iPad 7
- iPad 8
- iPad 9
- iPad Air 3
- iPad Pro 11" 1st Gen (2018)
- iPad Pro 11" 2nd Gen (2020)
- iPad Pro 11" 3rd Gen (2021)
- iPad Pro 10.5
- iPad Pro 12.9" 1st Gen (2015)
- iPad Pro 12.9" 3rd Gen (2018)
- iPad Pro 12.9" 4th Gen (2020)
- iPad Pro 12.9" 5th Gen (2021)
- iPad Pro 12.9" 6th Gen (2022)
- iPad Air 4 (5 Pin)
- iPad Pro 9.7"
- iPad Pro 12.9" 2nd Gen (2017)
fonti:
- raw/repairwiki/pagine/how-to-fix-iphone-14-not-charging-due-to-open-i2c-line-at-battery-connector.md
- raw/repairwiki/pagine/how-to-fix-iphone-8-not-charging-after-screen-repair-stuck-at-0-battery-level.md
- raw/repairwiki/pagine/ipad-not-charging-battery-always-reporting-1-percent-charge.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Funzione
La fonte descrive un problema di **connessione tra motherboard e batteria** come causa tipica di:
- **batteria bloccata** a una percentuale fissa (es. **sempre 1%**)
- **mancata carica**
- possibili **restart casuali**.

La connessione avviene tramite **connettore batteria** (con **screw** di fissaggio) e **Battery FPC**; se il connettore non è ben serrato o è danneggiato, la comunicazione/lettura batteria verso la motherboard risulta instabile.

> Nota: la fonte non nomina sigle I2C specifiche per iPad; qui si tratta il connettore batteria come causa/controllo generale.

## Dove si trova
- **Sul connettore batteria**: la fonte indica di controllare che lo **screw** sul connettore batteria sia **presente e avvitato correttamente**.
- **Sulla Battery FPC**: dopo aver rimosso la motherboard dall’alloggiamento, ispezionare la **Battery FPC** per danni fisici (comune se il dispositivo è stato aperto prima e qualcosa ha disconnesso la batteria).

## Sintomi tipici quando si guasta (da fonte)
- **Battery percentage sempre bloccata a 1%**
- **iPad non carica**
- **restart casuali** ogni pochi minuti.

Se l’iPad riavvia, la fonte suggerisce di controllare i **panic logs**: cercare un riferimento ai sensori **TG0B** e **TG0V** per capire se il problema è legato alla batteria o a una comunicazione batteria↔motherboard.

## Diagnosi — controlli rapidi (da fonte)
### 1) Controllo screw connettore batteria
- Aprire il dispositivo e verificare che lo **screw sul battery connector sia presente e avvitato correttamente**.
- Se lo **screw manca**, la fonte dice che può causare i problemi sopra (1% fisso, non carica, restart).

### 2) Ispezione Battery FPC
- Rimuovere la motherboard dall’alloggiamento e **ispezionare la Battery FPC** per danni fisici.
- La fonte segnala che è comune che il connettore FPC venga danneggiato se il device è stato aperto in precedenza e qualcosa è stato inserito per disconnettere la batteria.

### 3) Verifica contatto “solido”
- La fonte suggerisce di **toccare la connessione con una coppia di tweezers** per assicurarsi che sia **solida** e **non crepata**.

### 4) Test batteria
- Se tutto sembra ok (screw presente, FPC integra, contatto solido), la fonte indica come step successivo **testare una nuova batteria**.

## Riparazione — ripristino connessione (da fonte)
### A) Screw mancante o errato
- Se lo **screw è mancante**, installare un **nuovo screw**.
- La fonte avverte:
  - assicurarsi che lo screw non sia **troppo lungo** (altrimenti il connettore non viene spinto correttamente nella batteria)
  - **non stringere troppo**: può danneggiare l’**FPC**.
- La fonte aggiunge che uno screw troppo serrato può **piegare l’FPC** e causare il **sollevamento dei pin laterali**.

**Misura indicata (da fonte):** molti iPad usano uno screw **1.8–2.3mm Phillips**.

### B) Connettore/FPC danneggiato
- Se il connettore è danneggiato, la fonte indica di **sostituire il connettore**.
- Procedura (da fonte, a livello generale):
  1. Raccomandazione: aggiungere **low melt solder** sulle connessioni della motherboard per facilitare la riparazione.
  2. Usare **hot air** per **desaldare l’FPC**.
  3. Con la board ancora calda, usare il **saldatore con punta a bit** per **pulire i fori** (può richiedere parecchio calore; se serve aiutarsi con hot air).
  4. Posizionare il **nuovo connettore** e aggiungere **saldatura fresca**.

### C) Verifica post-riparazione
Dopo la riparazione, la fonte richiede:
- verificare che l’iPad riporti la **percentuale batteria corretta**
- verificare che il dispositivo **non si riavvii**
- verificare che l’iPad **carichi normalmente**.

## Su iPad (famiglie indicate dalla fonte)
La fonte raggruppa i modelli che usano **la stessa parte** del connettore batteria:
- **iPad Air 1 / Air 2** e **iPad 5/6/7/8/9**
- **iPad Air 3**
- **iPad Pro 11" 1st Gen (2018) / 11" 2nd Gen (2020) / 11" 3rd Gen (2021)**
- **iPad Pro 10.5**
- **iPad Pro 12.9" 1st Gen (2015) / 3rd Gen (2018) / 4th Gen (2020) / 5th Gen (2021) / 6th Gen (2022)**
- **iPad Air 4 (5 Pin)**
- **iPad Pro 9.7"**
- **iPad Pro 12.9" 2nd Gen (2017) (5 Pin)**

> Valori/part number: da verificare (la fonte non riporta sigla componente).

## Componenti correlati (da fonte)
- **Batteria**: vedi [batteria](../componenti/batteria.md)

## Collegamenti utili
- Sintomo correlato (da piano): [low-battery-schermo-ma-non-carica.md](../sintomi/low-battery-schermo-ma-non-carica.md)
- Sintomo correlato (da piano): [non-carica-batteria-non-rilevata-iphone-12-pro-max-i2c-0-2v.md](../sintomi/non-carica-batteria-non-rilevata-iphone-12-pro-max-i2c-0-2v.md) (per analogia di “batteria non letta”, anche se la fonte qui è iPad)
