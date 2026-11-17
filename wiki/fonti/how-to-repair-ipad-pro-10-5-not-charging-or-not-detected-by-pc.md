---
titolo: Fonte — How to Repair iPad Pro 10.5 not charging or not detected by pc
tipo: fonte
riassunto: 'Caso iPad Pro 10.5 che non carica e non viene rilevuto da PC: diagnosi
  con consumo <100 mA e dock test, poi conferma/ricambio U3500 (Tristar).'
modelli:
- iPad Pro 10.5
fonti:
- raw/repairwiki/pagine/how-to-repair-ipad-pro-10-5-not-charging-or-not-detected-by-pc.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# How to Repair iPad Pro 10.5 not charging or not detected by pc (repair.wiki)

> Fonte: [How to Repair iPad Pro 10.5 not charging or not detected by pc — repair.wiki](https://repair.wiki/w/How_to_Repair_iPad_Pro_10.5_not_charging_or_not_detected_by_pc), CC BY-SA 3.0.

## Contesto / descrizione problema
- iPad Pro 10.5” **non carica** e **non viene rilevato dal PC** quando collegato.
- Possibili segnali: **nessuna icona di carica**, **nessun suono di riconoscimento USB** su PC, **nessuna comunicazione dati**.
- Sostituzione di **cavo** e **brick** non risolve.
- Nella maggior parte dei casi la causa è il **controller USB U3500 (Tristar)**.

Nota fonte: “USB IC (U3500) Tristar should match for best compatibility and is compatible with iPhone 7 / 7 Plus (610A3B)”. (dettaglio compatibilità da verificare in base al ricambio disponibile)

## Sintomi riportati
- iPad non carica
- nessuna icona di carica
- PC non rileva il dispositivo
- nessun suono di riconoscimento USB
- cavo e adattatore nuovi non risolvono
- il dispositivo può comunque accendersi se la batteria ha carica

## Diagnosi (passi chiave)
### 1) Check corrente assorbita (consumo)
- Collegare il dispositivo a un **alimentatore DC**.
- Premere il tasto power.
- Verificare che l’assorbimento sia **< 100 mA all’istante iniziale**.
- La fonte indica che **consumo basso o anomalo** supporta un guasto del **controller USB**.

### 2) Dock test
- Sostituire il **charge port** con un **dock flex noto buono**.
- Testare **carica** e **rilevamento PC**.
- Se **carica e rilevamento** continuano a fallire → dock non è la causa.

### 3) Conferma guasto U3500 (Tristar)
Procedere alla sostituzione Tristar se:
- comportamento del consumo anomalo
- dock test passa
- nessun rilevamento PC
- nessuna negoziazione/handshake di carica/comunicazione (come descritto: “no PC detection / no charging negotiation”)

## Riparazione (procedura riportata)
1. Scollegare la batteria.
2. Rimuovere la logic board.
3. Rimuovere la protezione/armatura/shield che copre **U3500**.
4. Applicare flussante.
5. Rimuovere **U3500** con hot air controllata.
6. Pulire con attenzione i pad.
7. Installare un **U3500 noto buono**.
8. Ispezionare i giunti di saldatura sotto microscopio.
9. Rimontare.
10. Testare:
   - funzione di carica
   - rilevamento PC

## Collegamenti utili in wiki (da usare per approfondire)
- Componente: [Tristar](../componenti/tristar.md) (U3500)
- Sintomo: [non carica o non rilevato da PC](../sintomi/non-carica-o-non-rilevato-da-pc.md)
- Dispositivo: [iPad Pro 10.5](../dispositivi/ipad-pro-10-5.md)
- Tecnica (diagnosi DCPS/rail): [test-dcps-e-diagnosi-kraken-ic](../tecniche/test-dcps-e-diagnosi-kraken-ic.md)
- Tecnica (Tristar / non carica): [test-tristar-e-diagnosi-non-carica-iphone](../tecniche/test-tristar-e-diagnosi-non-carica-iphone.md)
- Strumento (DCPS): [dc-power-supply-dcps](../strumenti/alimentatore-da-banco.md)
