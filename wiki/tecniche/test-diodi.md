---
titolo: Test diodi — tecnica (diode scale su Tristar U1700)
tipo: tecnica
riassunto: 'Su iPad 7: usare diode scale per verificare il drop di tensione sul Tristar
  U1700 (600 mV → ~30 mV); se non c’è drop, sostituire U1700.'
modelli:
- iPad 7
fonti:
- raw/repairwiki/pagine/diodes-repair-basics.md
- raw/repairwiki/pagine/ipad-7-not-charging.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Scopo
Verificare rapidamente il funzionamento del **Tristar U1700** misurando il **drop di tensione** con il multimetro in **diode scale**. La fonte indica che il Tristar deve ridurre il drop da ~**600 mV** a **~30 mV (o meno)**.

> Fonte: IPad 7 Not Charging — repair.wiki

## Dove si misura
- Misura il drop di tensione **sul Tristar U1700**.
- La fonte non specifica i **punti esatti di misura** (quali pin/net), quindi **da verificare** sullo schema/boardview o con continuità/identificazione pin.

> Fonte: IPad 7 Not Charging — repair.wiki

## Procedura (diode scale)
1. Metti il multimetro in **diode scale**.
2. Esegui la misura del **drop di tensione** sul circuito relativo al **Tristar U1700**.
3. Confronta il valore letto con la soglia attesa:
   - **Atteso**: drop ridotto da ~**600 mV** a **~30 mV (o meno)**.
   - **Se non c’è drop** (cioè non vedi la riduzione attesa): **Tristar U1700 guasto** → **swap U1700**.

> Fonte: IPad 7 Not Charging — repair.wiki

## Criterio operativo (decisione swap)
- Se il **Tristar U1700** “non fa drop” (non riduce il valore come indicato): **sostituisci U1700**.

> Fonte: IPad 7 Not Charging — repair.wiki

## Note diagnostiche collegate (contesto)
- La fonte riporta che su iPad 7 la mancata carica è spesso dovuta a: **batteria**, **charge port**, oppure **Tristar**.
- La fonte specifica che il Tristar usato su iPad 7 è **610A3B** e che è “common to fail” soprattutto con **cavi di bassa qualità**.

> Fonte: IPad 7 Not Charging — repair.wiki

## Collegamenti utili
- [Tristar](../componenti/tristar.md)
- [Test diodi — tecnica (diode mode multimetro)](./test-diodi.md)
