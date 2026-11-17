---
titolo: BB_PMU — PMU baseband (zona sandwich)
tipo: componente
riassunto: 'Dopo back-glass: possibile “No IMEI/No modem firmware” o device morto;
  ispezione per cricche/dent su BB_PMU, test DCPS (jump/short) e reball/reinstall
  BB_PMU.'
modelli:
- iPhone 13 Pro
- iPhone 14 Pro
- iPhone 14 Pro Max
fonti:
- raw/repairwiki/pagine/how-to-fix-iphone-13-pro-no-power-or-no-imei-after-backglass-repair.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Funzione
BB_PMU è la PMU nella zona baseband della **scheda logica sandwich**. In caso di danno meccanico durante riparazione back-glass (cracking tool), può causare mancata inizializzazione baseband.

## Dove si trova
- Sulla **lower board** (scheda inferiore) della logica sandwich.
- La fonte indica che la PMU è **molto vicina al back glass**, quindi è “estremamente comune” che il tool da back-glass crei danni in quest’area.

## Sintomi tipici quando si guasta
Dalla fonte, dopo sostituzione back-glass:
- **No IMEI**: in *Settings > General > About*
- **Modem Firmware: N/A**
- **No cellular service** (assenza servizio cellulare)
- **Device completamente morto (no power)**
- **High current jump su DCPS** → indicazione di **short**

## Diagnosi (misure/controlli utili)
### 1) Ispezione visiva (obbligatoria)
Con microscopio, ispezionare la lower board sotto la zona baseband:
- **Hairline cracks su BB_PMU**
- **Dent** (ammaccatura) nella scheda causato dal **backglass punch tool**

> La fonte specifica che questo è “estremamente comune” su **iPhone 13 Pro / 14 Pro / Pro Max** per la vicinanza della PMU al back glass.

### 2) Diagnosi software (se il telefono si accende)
- Verifica IMEI con **`*#06#`** → se **No IMEI**
- Verifica *Settings → Modem Firmware* → se **N/A**

### 3) Test alimentazione DC (DCPS)
- Collegare **solo la lower board**
- Premere power
- Se si osserva **high boot current jump** → la fonte lo interpreta come **short**

### 4) Short check attorno a BB_PMU
- Controllare **intorno a BB_PMU** per corti

## Riparazione (cosa fare)
La fonte descrive una riparazione “meccanica/elettrica” del BB_PMU:
1. **Split della logic board (sandwich board separation)**
   - Preheat a **~160–180°C**
   - Inserire **thin blades** per separare upper & lower board
2. **Rimozione BB_PMU crepato**
   - Pulire l’**underfill** attorno a BB_PMU (attenzione ai componenti vicini)
   - Applicare **flux**
   - Sollevare con cautela BB_PMU
   - Ispezionare pad danneggiati
   - Pulire con **wick + fresh solder**
3. **Preparazione & reball BB_PMU nuovo**
   - Usare **corretto stencil per il modello**
   - Verificare l’allineamento delle sfere sotto microscopio
4. **Installazione BB_PMU**
   - Allineare correttamente i **marker di orientamento**
   - Reflow finché l’IC **self-centers**
   - Lasciare raffreddare
   - Pulire board e ispezionare i giunti
5. **Riconnessione upper & lower boards**
   - Allineare i contatti
   - Ispezionare sotto microscopio la corretta “seam contact”
6. **Test finale**
   - Collegare a **DCPS** e verificare **normal boot current**
   - Avviare il device:
     - IMEI deve comparire
     - *Modem Firmware* deve mostrare la versione corretta
   - Testare: **cellular**, **Wi‑Fi calling**, **SIM detection**

## Note su restore/update (da fonte)
- Se il telefono **non è wiped**: la fonte dice **di non fare restore**, ma solo **update**.
- La fonte avverte che un **restore** può far rimanere il device bloccato sulla schermata **Hello/activation**.
- Se il telefono è stato ripristinato con problemi baseband, potrebbe essere necessario **restore di nuovo** dopo aver risolto il baseband issue.

## Su quali modelli compare (da fonte)
- **iPhone 13 Pro**
- **iPhone 14 Pro**
- **iPhone 14 Pro Max**

> Nota: la fonte non fornisce codici modello (Axxxx) né valori DCPS numerici; per i valori attesi “numerici” su DCPS è **da verificare**.
