---
titolo: iPad 10
tipo: dispositivo
riassunto: 'Caso iPad 10.2 8th gen: schermo lampeggia e assorbimento cicla 0–0,3 A;
  Tristar OK; PMIC guasto su GPIO_PMU_TO_LCD_PWREN; sostituzione PMIC risolutiva.'
modelli:
- iPad 10
fonti:
- raw/repairwiki/pagine/ipad-10.md
- raw/repairwiki/pagine/ipad-10-2in-8th-gen-not-turning-on-drawing-between-0-0-2a-tristar-is-functional-repair.md
aggiornato: '2026-11-17'
categoria: tablet
codici_modello: []
componenti_chiave:
- PMIC
- Tristar
casi: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# iPad 10 — non si accende (ciclo assorbimento 0–0,3 A)

## Sintomi
- **Schermo lampeggia**
- **Ciclo assorbimento**: da **0 A a 0,3 A** (0–0,3 A)

## Diagnosi (da fonte)
- **Tristar funzionale** (da fonte)
- Il problema è stato attribuito a **PMIC difettoso** che **non riusciva a fornire** il segnale **`GPIO_PMU_TO_LCD_PWREN`**.

## Intervento
- **Sostituzione PMIC**

## Esito
- **Risoluzione** del problema dopo la sostituzione del **PMIC**.

## Collegamenti utili
- Sintomo correlato: [non-si-accende-ciclo-assorbimento-0-0-3a-schermo-lampeggia](../sintomi/non-si-accende-ciclo-assorbimento-0-0-3a-schermo-lampeggia.md)
- Componente: [PMIC](../componenti/pmic.md)
- Componente: [Tristar](../componenti/tristar.md)
