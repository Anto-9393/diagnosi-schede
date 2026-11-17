---
titolo: Yangtze U3300 — rimozione shield dura e sostituzione (precauzioni schermo/baseband)
tipo: tecnica
riassunto: 'Tecnica per sostituire Yangtze U3300 su iPhone XR: rimozione shield bottom
  con max heat/max air e nozzle grande, taglio con tin snips, e precauzioni per evitare
  float/urti su Baseband/WTR.'
modelli:
- iPhone XR
fonti:
- raw/repairwiki/pagine/iphone-xr-not-charging.md
- raw/repairwiki/pagine/iphone-xr-not-powering-on-not-charging.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Scopo
Sostituire [Yangtze U3300](../componenti/yangtze-u3300.md) quando è la causa più probabile di “non carica / assorbimento anomalo” su iPhone XR, gestendo correttamente la rimozione della shield molto dura.

## Quando usarla
- Diagnosi coerente con guasto Yangtze (fonte: iPhone XR non si avvia e/o non carica, con assorbimento a basso amperaggio).
- Shield di Yangtze “molto dura” da rimuovere.

## Attrezzatura (da banco)
- Stazione ad aria calda
- Saldatore a filo
- Multimetro
- [Termocamera](../strumenti/termocamera.md) (utile per controllare distribuzione calore)

## Procedura (passo-passo)
### 1) Conferma che il problema è coerente con Yangtze
La fonte riporta che su iPhone XR l’IC di carica che fallisce più spesso è **Yangtze (U3300)**.

Inoltre, la fonte descrive come sintomi:
- **Not powering on**
- **Not Charging**
- **Low amperage draw** da DC Power Supply
- **No short to ground** su **VDD Main**, **VDD Boost** o **PP3V0_NAND**

> Valori numerici specifici (es. 0.013 A / 82 mA prima del prompt) presenti nella pagina tecnica esistente: **da verificare** se derivano dalla stessa fonte o da altra.

### 2) Preparazione rimozione shield bottom (molto dura)
Per rimuovere la shield che copre Yangtze, la fonte indica:
- usare **max heat**
- usare **max air**
- usare **largest nozzle**

La fonte aggiunge che la shield:
- richiede **molto calore** oppure
- può richiedere **tin snips** per **tagliarla**

### 3) Rimozione shield
- Applicare calore in modo controllato con **max heat/max air** e **nozzle grande**.
- Se necessario, usare **tin snips** per tagliare la shield (la fonte lo indica come alternativa quando la rimozione richiede troppo calore).

### 4) Precauzioni critiche durante la rimozione (schermo/PCB)
La fonte mette enfasi su:
- **EXTREMELY careful not to float anything**
- **not to knock off components**
- attenzione alla **forza meccanica**: troppa forza può **flex the board** e danneggiare **internal traces**

### 5) Sostituzione Yangtze U3300
- Una volta rimossa la shield, la fonte indica che **Yangtze è abbastanza facile da sostituire**.
- Rimuovere [Yangtze U3300](../componenti/yangtze-u3300.md) e installare il ricambio.

### 6) Rischi sotto shield: Baseband/WTR e altri IC
La fonte specifica che sotto questa shield stanno:
- **wireless charging IC (Iktara)**
- **baseband PMU**
- **baseband CPU**

Quindi durante tutta la procedura:
- evitare di **float** componenti/aree sotto shield
- evitare urti/sollevamenti che possano creare contatti indesiderati o danneggiare piste

## Verifica post-intervento
La pagina tecnica esistente riporta un criterio di conferma basato su assorbimento (es. “82 mA prima del prompt di boot” “cleared”). La fonte esterna fornita qui non include quel valore numerico: **da verificare**.

In ogni caso, come verifica funzionale coerente con la fonte:
- ripetere test di **power on** e **charging**
- verificare che non ci sia **low amperage draw** anomalo

## Note di troubleshooting correlate (da fonte)
- In alcuni casi, la fonte segnala che un **liquid damaged ear speaker flex** può causare **no charging**; prova a **testare con ear speaker flex scollegato**.

## Rischi / errori comuni (da fonte)
- Shield difficile: usare **max heat/max air** e **largest nozzle**; se serve, **tin snips**.
- **Float** di componenti/aree sotto shield → rischio di problemi.
- **Knock off components** durante la rimozione.
- Troppa forza → **flex del board** e possibile danno a **internal traces**.

## Collegamenti utili
- [Yangtze U3300](../componenti/yangtze-u3300.md)
- [Termocamera](../strumenti/termocamera.md)
