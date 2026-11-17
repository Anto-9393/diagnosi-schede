---
titolo: Kraken IC — USB/charging controller (iPhone 12 Pro)
tipo: componente
riassunto: 'Kraken IC guasto: non carica, touch morto e/o mancata rilevazione USB;
  diagnosi con ispezione e test DCPS per corrente anomala/spike in boot.'
modelli:
- iPhone 12 Pro
fonti:
- raw/repairwiki/pagine/how-to-fix-an-iphone-12-pro-that-is-not-charging-and-touch-not-working.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Funzione
Il **Kraken IC** (USB/charging controller) gestisce le funzioni di **carica via porta USB** e la **rilevazione/handshake** legata all’alimentazione. Nella fonte è indicato come causa frequente di problemi combinati **carica + touch**.

## Dove si trova
**Da verificare** (la fonte non specifica posizione/coordinate sulla scheda; parla solo di “isolare l’area dell’IC Kraken”).

## Sintomi tipici quando si guasta
Dalla fonte:
- **iPhone non carica**.
- **Nessuna risposta** quando si collega il caricatore.
- **Touchscreen non funziona**.
- Il dispositivo **si accende mentre è collegato a DCPS**, ma **non rileva la connessione USB**.
- Possibile **corrente anomala / spike irregolare** su DCPS quando si tenta il boot.

## Criteri diagnostici (DCPS)
Dalla fonte (test con alimentatore da banco DC):
1. Collegare l’iPhone a **DCPS**.
2. Osservare il comportamento della **corrente assorbita** quando si prova ad avviare/boot.
3. Se la corrente è **anomala** e/o compare uno **spike irregolare** “quando si tenta di fare il boot” → **probabile problema Kraken IC**.

> Nota: la fonte non riporta valori numerici attesi (da verificare).
