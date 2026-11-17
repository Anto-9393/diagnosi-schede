---
titolo: iPad 10.2 (8th gen) — non si accende (schermo lampeggia, assorbimento 0–0.3
  A) con Tristar funzionale
tipo: fonte
riassunto: 'iPad 10.2 8th gen: non si accende con assorbimento 0–0.3 A e schermo che
  lampeggia; Tristar risulta OK, causa PMIC guasto (GPIO_PMU_TO_LCD_PWREN).'
modelli:
- iPad 10.2 (8th gen)
fonti:
- raw/repairwiki/pagine/ipad-10-2in-8th-gen-not-turning-on-drawing-between-0-0-2a-tristar-is-functional-repair.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Sintomi (da fonte)
- Schermo che lampeggia.
- Cicli di assorbimento: da 0 A fino a ~0,3 A (0–0,3 A).
- Il dispositivo non arriva all’avvio ("not turning on").

## Diagnosi (da fonte)
- Il Tristar risulta funzionale.
- La causa indicata dalla fonte è un **PMIC difettoso** che **non riesce a pilotare l’uscita**:
  - `GPIO_PMU_TO_LCD_PWREN`

## Misure/riscontri riportati (da fonte)
- Con alimentazione/avvio ciclico: assorbimento che oscilla tra **0 A e ~0,3 A**.
- Durante il ciclo: **schermo lampeggia**.

## Riparazione (da fonte)
- **Sostituzione del PMIC**.
- Dopo la sostituzione: problema risolto.

## Collegamenti utili
- [PMIC](../componenti/pmic.md)
- [Tristar](../componenti/tristar.md)
- [sintomi — non si accende (ciclo assorbimento 0–0.3A, schermo lampeggia)](../sintomi/non-si-accende-ciclo-assorbimento-0-0-3a-schermo-lampeggia.md)
