---
titolo: iPhone XR
tipo: dispositivo
riassunto: 'Caso iPhone XR: non boot, carica a 0.013A e DCPS 82mA prima del prompt;
  sostituzione Yangtze (U3300) e verifica post-riparazione.'
modelli:
- iPhone XR
fonti:
- raw/repairwiki/pagine/iphone-xr.md
- raw/repairwiki/pagine/iphone-xr-not-charging.md
aggiornato: '2026-11-17'
categoria: phone
codici_modello: []
componenti_chiave:
- Yangtze (U3300)
casi: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# iPhone XR — non carica / nessun boot (Yangtze U3300)

## Sintomi (da fonte)
- Il telefono **non fa boot** né con tasto power né collegandolo al caricatore.
- In carica assorbe circa **0.013 A**.
- Su **DC Power Supply (DCPS)** assorbe circa **82 mA** **prima** del prompt di boot.

## Diagnosi (probabilità dalla fonte)
- **Culprit più probabile: Yangtze (U3300)**.
- La fonte indica che **U3300 è il “Charging IC”** per questo modello.

## Riparazione
1. **Sostituzione Yangtze (U3300)**.
2. **Verifica post-riparazione**: controllare se l’assorbimento **82 mA prima del prompt di boot** risulta **“cleared”** (rimosso/risolto), per confermare che il problema è stato risolto.

## Note operative / rischi (da fonte)
- La **shield** sopra Yangtze è **molto difficile** da rimuovere.
  - La fonte raccomanda di aggiungere **low melt solder a 138°C** a **tutti** i giunti di saldatura lungo i bordi per facilitarne la rimozione.
- Durante la rimozione/operazione sulla shield si può **floatare** (sollevare/alterare) il **Baseband** o il **WTR** che stanno sotto la shield, con rischio di **problemi baseband**.

## Caso alternativo (da fonte)
- In alcuni casi, un **liquid damaged ear speaker flex** può causare **no charging**.
- Prova a **testare con ear speaker flex scollegato**.

## Collegamenti utili
- [Yangtze U3300](../componenti/yangtze-u3300.md)
- [DC Power Supply (DCPS)](../strumenti/alimentatore-da-banco.md)
- [Termocamera](../strumenti/termocamera.md)
