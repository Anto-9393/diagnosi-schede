---
titolo: Rigel (U4400) — causa rara di short su rail di alimentazione
tipo: componente
riassunto: 'Rigel (U4400) è citato come possibile causa rara di corto su rail, ma
  la fonte raw fornita per iPhone XS non lo menziona: da verificare.'
modelli:
- iPhone 11
fonti:
- raw/repairwiki/pagine/iphone-11-not-powering-on-2a-or-higher-power-draw-after-prompt-to-boot.md
- raw/repairwiki/pagine/iphone-11-not-powering-on-after-prompt-to-boot-current-jumps-back-and-forth-from-0-a-to-320-ma-then-0-a-to-1-4-a-then-0-a-to-500-ma-and-so-on.md
- raw/repairwiki/pagine/iphone-xr-not-powering-on-with-heat-above-the-cpu.md
- raw/repairwiki/pagine/iphone-xs-not-powering-on-pulls-2a-or-more-before-promt-to-boot.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Funzione
Rigel (U4400) è indicato nella pagina esistente come possibile causa rara di **corto** su una linea di alimentazione quando l’iPhone non parte e l’assorbimento è **≥2 A prima del prompt di boot**.

> **Da verificare (coerenza fonte):** la fonte raw fornita (iPhone XS) descrive soprattutto un corto su rail legati a **PP_VDD_MAIN** / **PP_VDD_BOOST** e non menziona Rigel (U4400). La parte “Rigel (U4400)” nella pagina esistente risulta quindi **non supportata** dalla fonte raw allegata qui.

## Dove si trova
- Componente su scheda logica dell’iPhone 11 con sigla **U4400**.
- **Posizione esatta:** da verificare.

## Sintomi tipici quando si guasta
Dalla pagina esistente (iPhone 11):
- iPhone 11 **non si accende**
- assorbe **2 A o più** da DCPSU **prima** del prompt di boot
- spesso il problema è un **capacitore in corto** su rail; in casi rari può essere coinvolto **Rigel (U4400)**.

Dalla fonte raw fornita (iPhone XS):
- iPhone XS **non si accende**
- assorbe **2 A o più** da DCPSU **prima** del prompt di boot
- la causa più probabile è un **capacitore in corto** su:
  - **PP_VDD_MAIN** (più probabile)
  - **PP_VDD_BOOST** (di solito shorted quando non è VDD MAIN)
  - **Speaker Amp (U4902 o U5002)** (più raro)

> **Contraddizione/integrazione:** la fonte raw non parla di “Rigel (U4400)” e non fornisce rail/valori specifici per U4400. Da verificare se U4400 sia davvero coinvolto in questo scenario.

## Diagnosi / misure utili (con valori attesi)
La fonte raw fornita (iPhone XS) suggerisce questa logica di diagnosi:
1. **Ispezione visiva completa** della board e verifica di **danni da liquidi** sotto gli adesivi/stickers.
2. Se non ci sono danni da liquidi: cercare un **capacitore in corto** sulle linee indicate.
3. **Localizzazione del corto**: iniettare tensione **4 V / 2 A** direttamente sulla linea misurata come in corto e usare **freeze spray** o **termocamera** per individuare il componente che scalda.

Valori elettrici specifici per **Rigel (U4400)**: **da verificare** (non presenti nella fonte raw fornita).

## Cosa fare dopo aver identificato Rigel (U4400)
La pagina esistente afferma che, se Rigel (U4400) risulta in corto, si può **rimuovere il componente in corto e non sostituirlo**, e il dispositivo “will function normally with no negative effects”.

> **Da verificare:** la fonte raw fornita descrive la rimozione del **capacitore in corto** (non menziona U4400) e non conferma questa procedura specifica per Rigel (U4400).

## Modelli su cui compare
- **iPhone 11** (citato nella pagina esistente).

> Nota: la fonte raw fornita riguarda **iPhone XS** e non menziona Rigel (U4400). Da verificare l’estensione a iPhone 11.

## Collegamenti utili
- [componenti/condensatori-mlcc-elettrolitici-tantalio.md](../componenti/condensatori-mlcc-elettrolitici-tantalio.md) (causa più probabile: capacitore in corto su rail)
- [tecniche/ricerca-corto-iniezione-bassa-tensione-e-termocamera.md](../tecniche/ricerca-corto-iniezione-bassa-tensione-e-termocamera.md) (metodo di iniezione + freeze spray/termocamera)
