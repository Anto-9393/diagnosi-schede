---
titolo: Diodes — Repair Basics (riassunto fonte)
tipo: fonte
riassunto: 'Riassunto della fonte esterna sui diodi: funzioni e tipi (rectifier, Schottky,
  Zener, TVS), guasti tipici e criteri di test con multimetro (diode mode) fuori circuito,
  cenno a Zener con alimentatore + resistore 1 kΩ.'
modelli: []
fonti:
- raw/repairwiki/pagine/diodes-repair-basics.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# Diodes — Repair Basics (riassunto fonte)

Fonte: [Diodes - Repair Basics — repair.wiki](https://repair.wiki/w/Diodes_-_Repair_Basics), CC BY-SA 3.0.

## Funzione del diodo (concetti base)
- Un diodo ha **Anode** e **Cathode**.
- Permette la corrente in **una sola direzione** e la blocca nell’altra.
- In datasheet/diagnosi la grandezza chiave è la **forward voltage drop** (caduta in avanti, in **Volts**).

### Terminologia utile
- **Forward bias**: positivo all’**anode**, negativo al **catode**.
- **Forward drop**: tensione ai capi del diodo quando conduce in forward bias.
- **Reverse bias**: positivo al **catode**, negativo all’**anode**.
- **Reverse breakdown voltage**: tensione di breakdown in reverse bias.
  - Per la maggior parte dei diodi è **non desiderata**.
  - Per **Zener / Avalanche / TVS** è la **modalità prevista** (entro limiti di corrente).

## Funzioni in circuiti (repair perspective)
- **One-way path**: comportamento “valvola di non ritorno”, usato in charge pumps e power converters.
- **Rectification**: conversione AC→DC (es. **full bridge** con 4 diodi).
- **Voltage regulation / reference**: Zener usati come riferimento con resistore in serie.
- **Protection**: **TVS e Zener** per spike/transienti/ESD e reverse voltage; diodi “normali” anche per protezioni di polarità (in base a come sono cablati).
- **Photodetection**: fotodiodi per conversione luce→segnale.

## Tipi di diodi (panoramica)
- **Regular/Rectifier diodes**: i più comuni; spesso in **full bridge** (4 diodi in un package).
- **Schottky diodes**: **bassa forward voltage drop** e **fast switching**; svantaggio: **higher leakage current** in reverse bias.
- **Zener diodes**: mantengono una **tensione quasi costante** in reverse breakdown; conducono “all’indietro” a una **Zener voltage** nominale.
- **LED**: emettono luce in forward bias.
- **TVS (Transient Voltage Suppression)**: protezione da spike/transienti/ESD; internamente costruiti come Zener o combinazioni (Shottky + Zener).
- **Varactor (varicap)**: capacitance variabile con reverse bias (storicamente in tuner).
- **Photo-diodes**: generano corrente con luce.

## Guasti tipici (cosa aspettarsi)
- Tendenza a guastarsi in **fully open** o **fully shorted**.
- Altri modi citati:
  - **lowered reverse breakdown voltage**
  - **increased resistance** (può causare surriscaldamento e spreco di potenza)
  - **reverse leakage current** (comportamento “resistivo” in reverse bias sotto breakdown)

## Test con multimetro (diode test mode)
### Prima: ispezione
- Verificare **danni fisici** (es. **liquid damage/corrosion**) prima del test: è indicato come il modo più rapido per identificare un diodo guasto.

### Consiglio: test fuori circuito
- È indicato come **best practice** testare **fuori dal circuito**.

### Regular / Schottky / Zener / LED (procedura)
1. Identificare **anode** e **cathode** (il **catodo** è tipicamente marcato con **band/line** sul corpo).
2. Impostare il multimetro in **diode test mode**.
3. Puntale **rosso su anode** e **nero su cathode**.
4. Atteso: lettura di **forward voltage drop** circa **0.2–0.7 V** per diodi al silicio.
   - Se mostra **“OL”** o **< 0.2 V**, il diodo è **likely faulty**.
5. **Controllo polarità**: se invertendo i puntali il diodo mostra una lettura, la fonte indica che il diodo è **faulty**.

### Note operative importanti
- **In-circuit**: possibile, ma altri componenti possono alterare la misura (in genere **abbassano** la lettura del forward drop; oppure possono far leggere il diodo come **short/leaky**).
- **LED**: molti multimetri non leggono bene LED perché arrivano a **1–2 V**, spesso sotto la forward voltage dei LED visibili.
- **Full bridge rectifier in package**: la misura è equivalente a testare **4 diodi**.

## Zener: identificazione della Zener voltage (cenno procedurale)
La fonte descrive una procedura (nel testo fornito è troncata a metà), con questi punti:
- Rimuovere il diodo dal circuito.
- Mettere un **resistore da 1 kΩ** in serie.
- Usare un **lab-bench power supply** in reverse bias (positivo al **cathode**, negativo all’altro capo del resistore).
- Mettere il multimetro in **DC voltage mode** e misurare la tensione ai capi del diodo.
- Aumentare gradualmente la tensione finché si raggiunge la conduzione Zener.

> Nota: la fonte fornita si interrompe a metà della procedura (“until th…”). Valori/criteri finali **da verificare** sul testo completo.

## Collegamenti utili (wiki)
- Tecnica generale: **tecniche/test-diodi.md** (pagina piano).
- Componenti: **componenti/diode.md** (pagina piano).
