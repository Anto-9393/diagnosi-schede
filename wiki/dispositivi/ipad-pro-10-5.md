---
titolo: iPad Pro 10.5
tipo: dispositivo
riassunto: 'iPad Pro 10.5 (A1701/A1709): non carica e/o non viene rilevuto da PC;
  spesso causa U3500 (Tristar).'
modelli:
- iPad Pro 10.5
fonti:
- raw/repairwiki/pagine/ipad-pro-10-5.md
- raw/repairwiki/pagine/how-to-repair-ipad-pro-10-5-not-charging-or-not-detected-by-pc.md
aggiornato: '2026-11-17'
categoria: tablet
codici_modello:
- A1701
- A1709
componenti_chiave:
- tristar
casi: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# iPad Pro 10.5

- Uscita: 2017-06-13
- Codici modello: A1701, A1709

## Guasti tipici e casi

### Non carica e non rilevato da PC (U3500/Tristar)

**Sintomi tipici (da fonte):**
- iPad non carica
- nessuna icona di ricarica
- PC non rileva il dispositivo
- nessun suono di riconoscimento USB su PC
- sostituire cavo e alimentatore non risolve
- il dispositivo può comunque accendersi se la batteria ha carica

**Nota compatibilità (da fonte):**
- “USB IC (U3500) Tristar should match for best compatibility and is compatible with iPhone 7 / 7 Plus (610A3B)” (da verificare i dettagli di matching su ricambi disponibili).

## Diagnosi (da fonte)

### 1) Check corrente assorbita
1. Collegare il dispositivo a un **alimentatore da banco (DC power supply)**.
2. Premere il pulsante di accensione.
3. Verificare che l’assorbimento sia **< 100 mA** al primo click.

**Interpretazione (da fonte):**
- assorbimento **basso o anomalo** → supporta guasto del controller USB.

### 2) Dock test
- Sostituire la **porta di ricarica** con un **dock flex noto buono**.
- Testare **ricarica** e **rilevamento PC**.

**Interpretazione (da fonte):**
- se ricarica e rilevamento PC **continuano a fallire** → il problema **non** è il dock.

### 3) Conferma guasto U3500 (Tristar)
Procedere alla sostituzione di Tristar se:
- comportamento della corrente **anomalo**
- dock test **passa**
- **nessun** rilevamento PC
- **nessuna** negoziazione/attivazione di ricarica via USB

## Riparazione (da fonte)
1. Scollegare la batteria.
2. Rimuovere la logic board.
3. Rimuovere l’armatura/schermo protettivo che copre **U3500**.
4. Applicare flussante.
5. Rimuovere **U3500** con hot air controllata.
6. Pulire i pad con attenzione.
7. Installare un **U3500 noto buono**.
8. Ispezionare i giunti saldati sotto microscopio.
9. Rimontare.
10. Test finali:
   - funzione di ricarica
   - rilevamento PC

## Collegamenti utili
- [Tristar](../componenti/tristar.md)
- [Tester Tristar](../strumenti/tester-tristar.md)
- [DC power supply (DCPS)](../strumenti/alimentatore-da-banco.md)
- [tecniche/test-tristar-e-diagnosi-non-carica-iphone](../tecniche/test-tristar-e-diagnosi-non-carica-iphone.md)
