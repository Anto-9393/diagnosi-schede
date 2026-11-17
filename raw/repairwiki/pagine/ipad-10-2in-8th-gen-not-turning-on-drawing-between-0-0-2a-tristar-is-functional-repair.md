---
titolo: IPad 10.2in 8th Gen Not turning on, drawing between 0-0.2A, tristar is functional
  repair
tipo: fonte_esterna
url: https://repair.wiki/w/IPad_10.2in_8th_Gen_Not_turning_on%2C_drawing_between_0-0.2A%2C_tristar_is_functional_repair
cronologia: https://repair.wiki/w/IPad_10.2in_8th_Gen_Not_turning_on%2C_drawing_between_0-0.2A%2C_tristar_is_functional_repair?action=history
revisione: '2024-11-08T06:17:48Z'
categorie: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# IPad 10.2in 8th Gen Not turning on, drawing between 0-0.2A, tristar is functional repair

> Fonte: [IPad 10.2in 8th Gen Not turning on, drawing between 0-0.2A, tristar is functional repair — repair.wiki](https://repair.wiki/w/IPad_10.2in_8th_Gen_Not_turning_on%2C_drawing_between_0-0.2A%2C_tristar_is_functional_repair), CC BY-SA 3.0. Autori: vedi cronologia.

## Problem description
Solving an issue where the iPad 10.2in 8th gen would not turn on, cycles power draw from 0A to 0.300A then the screen would flash and cycle again and the Tristar is working as intended.

## Symptoms
- Flashing screen
- Cycling power draw (0-0.3A)

## Solution
This specific problem was caused by bad PMIC failing to output GPIO_PMU_TO_LCD_PWREN. 

Replacing PMIC solved the issue.
