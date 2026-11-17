---
titolo: iPad Pro 11in 1st Gen
tipo: dispositivo
riassunto: 'iPad Pro 11in 1st Gen (A1934/A1980/A2013): mancato riconoscimento PC in
  recovery/DFU e problemi di carica—failure tipici su porta di ricarica, CD3215 e
  Tristar 610A3C.'
modelli:
- iPad Pro 11in 1st Gen
fonti:
- raw/repairwiki/pagine/ipad-pro-11in-1st-gen.md
- raw/repairwiki/pagine/ipad-pro-11in-1st-gen-not-recognized-by-pc-in-recovery-mode-or-charging-issues.md
aggiornato: '2026-11-17'
categoria: tablet
codici_modello:
- A1934
- A1980
- A2013
componenti_chiave:
- CD3215
- Tristar 610A3C
casi: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# iPad Pro 11in 1st Gen (A1934 / A1980 / A2013)

- Uscita: 2018-11-07
- Codici modello: A1934, A1980, A2013

## Guasti tipici e casi

### Sintomi (da fonte)
- iPad non si connette al PC con iTunes o 3uTools anche in **recovery** o **DFU**.
- Problemi di carica “strani”, inclusi casi di **non carica**.
- Carica dipendente dal tipo di alimentatore:
  - può caricare **solo** con caricatore **USB-C PD** capace di **15V** e **non** con **USB-A 5V** (o viceversa).

### Failure points principali (3 punti di guasto)
> La fonte indica che, per questo problema, i tre punti di failure più comuni sono: **charge port**, **CD3215**, **Tristar 610A3C**.

1) **Charge port (porta di ricarica)**
- È indicata come **il punto di failure più comune**.
- Su questo modello la fonte specifica che **la porta non è saldata alla board** e può essere sostituita facilmente per test.
- Nota: usare **porta nota buona** o ricambi **OEM/premium**; porte aftermarket possono avere problemi.

2) **CD3215**
- Gestisce principalmente la carica da **USB-PD**.
- Se fallisce:
  - l’iPad può potenzialmente caricare via **USB-A 5V**, ma **non** negoziare la carica a **15V** tramite **USB-C PD**.
- Test indicato dalla fonte:
  - con multimetro in **diode mode**, posizionare **red probe su GND** e **black probe** su ciascun lato dei **condensatori attorno al chip** per verificare che **nessun condensatore sia in corto verso GND su entrambi i lati**.
- Se viene trovato un **corto** su un condensatore attorno al CD3215, la fonte indirizza a seguire la sezione repair per CD3215.

3) **Tristar 610A3C**
- La fonte specifica che questo modello usa un Tristar **“A3C”** non retro-compatibile con altri Tristar.
- Ruolo indicato:
  - gestisce principalmente la carica **5V da USB-A**, più che la negoziazione **15V USB-C PD**.
- Dove si trova:
  - **nascosto sotto una parte dello shield** sopra i connettori FPC dello schermo, in mezzo alla board.
  - per accedere serve rimuovere abbastanza shield (la fonte suggerisce grinding tool o snips).
- Test indicato dalla fonte:
  - come per CD3215: controllare con multimetro in **diode mode** i **condensatori attorno al Tristar** per corti.
- Logica di sospetto (da fonte):
  - se hai già testato con **porta nota buona**,
  - non hai trovato corti attorno a **CD3215**,
  - l’iPad **carica con USB-C PD ma solo a 15V**,
  - e **non** carica con **USB-A 5V**,
  - allora il Tristar è “più che probabile” il colpevole.

### Test/repair (procedura riassunta dalla fonte)

#### 1) Charge port
- Sostituzione porta con **nuova** o **nota buona**.
- La fonte: “pull the old port off and replace it with the new one”.

#### 2) CD3215 — diagnosi e riparazione
- Se trovi **uno o più condensatori in corto** attorno al CD3215:
  1. Prima di sostituire l’IC, la fonte consiglia di **escludere il condensatore** come causa.
  2. Alimentatore da banco: impostare **DC a 1V/1A** (valore “low voltage like 1v/1a” nella fonte).
  3. Mettere **black probe su GND** e **red probe** sul lato del condensatore **non connesso a GND**.
  4. Usare **termocamera** o **freeze spray** per vedere quale componente scalda per primo:
     - se scalda prima un condensatore: rimuoverlo (blade/pry tool), poi verificare con multimetro in **diode mode** che il corto non sia più presente.
     - se scalda prima il **CD3215**: sostituire il **CD3215**.
  5. Dopo la sostituzione: verificare che
     - il corto non sia più presente, **oppure**
     - l’iPad riesca a negoziare **15V** con un **USB-C PD** capace di 15V,
     - e che l’iPad venga riconosciuto da **iTunes o 3uTools**.

> Nota dalla fonte: molti condensatori sono “smoothing caps” con più condensatori sulla stessa linea; se ci sono altri condensatori sulla stessa linea, potrebbe non essere necessario sostituire il singolo condensatore corto (la fonte lo dice come regola pratica).

#### 3) Tristar 610A3C — diagnosi e riparazione
- Se trovi un **condensatore in corto** attorno al Tristar:
  1. Seguire la stessa logica usata per CD3215:
     - iniezione con **DC power supply** a **bassa tensione** (la fonte rimanda ai passaggi CD3215: “injecting a small voltage into the line”)
     - **freeze spray** o **termocamera** per identificare quale componente scalda per primo
     - rimozione condensatore corto o sostituzione Tristar.
- Se **non** trovi condensatori in corto ma il Tristar resta sospetto:
  - sostituire direttamente il **Tristar 610A3C**.
  - la fonte indica che può essere reperito o prelevato da donor board (iPad Pro 11" 1st gen o iPad Pro 12.9" 3rd gen).
- Dopo la sostituzione: verificare che
  - il corto non sia più presente (se c’era),
  - l’iPad carichi a **5V** con **USB-A charger**,
  - e che venga riconosciuto da **iTunes o 3uTools**, specialmente in **recovery o DFU**.

## Componenti chiave collegati
- [CD3217](../componenti/cd3217.md) (pagina esistente; **da verificare** se contiene anche riferimenti a CD3215 o solo CD3217)
- [Tristar](../componenti/tristar.md)

> Per CD3215 e Tristar 610A3C: la fonte li cita esplicitamente, ma nelle pagine componenti esistenti non è garantito che ci sia una sezione dedicata a CD3215/610A3C. Da verificare.

## Note operative
- La fonte sottolinea che la porta di ricarica su questo modello non è saldata alla board: questo rende la sostituzione/test più diretto rispetto ad altri modelli.
- Per l’accesso al Tristar 610A3C è necessario rimuovere parte dello shield sopra i connettori FPC dello schermo.

Fonte: [IPad Pro 11in 1st Gen Not Recognized by PC in Recovery Mode or Charging Issues — repair.wiki](https://repair.wiki/w/IPad_Pro_11in_1st_Gen_Not_Recognized_by_PC_in_Recovery_Mode_or_Charging_Issues), CC BY-SA 3.0.
