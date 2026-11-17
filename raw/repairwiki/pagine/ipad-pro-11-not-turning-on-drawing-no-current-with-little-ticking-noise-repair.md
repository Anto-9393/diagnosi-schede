---
titolo: IPad Pro 11 Not turning on, drawing no current with little ticking noise repair
tipo: fonte_esterna
url: https://repair.wiki/w/IPad_Pro_11_Not_turning_on%2C_drawing_no_current_with_little_ticking_noise_repair
cronologia: https://repair.wiki/w/IPad_Pro_11_Not_turning_on%2C_drawing_no_current_with_little_ticking_noise_repair?action=history
revisione: '2024-02-04T14:07:31Z'
categorie: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# IPad Pro 11 Not turning on, drawing no current with little ticking noise repair

> Fonte: [IPad Pro 11 Not turning on, drawing no current with little ticking noise repair — repair.wiki](https://repair.wiki/w/IPad_Pro_11_Not_turning_on%2C_drawing_no_current_with_little_ticking_noise_repair), CC BY-SA 3.0. Autori: vedi cronologia.

## Problem description
Solving an issue where the iPad 11" 1st gen is not turning on with ticking noise. 

## Symptoms
- Ticking noise
- Drawing 0A (no current)
- Not turning on

## Solution
This specific problem was traced to a shorted line on PMIC/CD3217. The culprit was a shorted cap C3800 (Figure 1).

It could also be one (or both) the 2 "middle pins connecting from the board to the battery (clk and dat0) that could have been damaged when the battery gets lifted, just make a straight jumper from the motherboard to the battery and that will solve the issue.
