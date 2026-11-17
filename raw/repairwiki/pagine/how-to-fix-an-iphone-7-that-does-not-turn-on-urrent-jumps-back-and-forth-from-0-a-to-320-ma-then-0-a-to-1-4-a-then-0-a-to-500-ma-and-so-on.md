---
titolo: How To Fix an iPhone 7 That Does Not Turn On, urrent jumps back and forth
  from 0 A to 320 mA, then 0 A to 1.4 A, then 0 A to 500 mA, and so on
tipo: fonte_esterna
url: https://repair.wiki/w/How_To_Fix_an_iPhone_7_That_Does_Not_Turn_On%2C_urrent_jumps_back_and_forth_from_0_A_to_320_mA%2C_then_0_A_to_1.4_A%2C_then_0_A_to_500_mA%2C_and_so_on
cronologia: https://repair.wiki/w/How_To_Fix_an_iPhone_7_That_Does_Not_Turn_On%2C_urrent_jumps_back_and_forth_from_0_A_to_320_mA%2C_then_0_A_to_1.4_A%2C_then_0_A_to_500_mA%2C_and_so_on?action=history
revisione: '2024-01-20T20:57:53Z'
categorie: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# How To Fix an iPhone 7 That Does Not Turn On, urrent jumps back and forth from 0 A to 320 mA, then 0 A to 1.4 A, then 0 A to 500 mA, and so on

> Fonte: [How To Fix an iPhone 7 That Does Not Turn On, urrent jumps back and forth from 0 A to 320 mA, then 0 A to 1.4 A, then 0 A to 500 mA, and so on — repair.wiki](https://repair.wiki/w/How_To_Fix_an_iPhone_7_That_Does_Not_Turn_On%2C_urrent_jumps_back_and_forth_from_0_A_to_320_mA%2C_then_0_A_to_1.4_A%2C_then_0_A_to_500_mA%2C_and_so_on), CC BY-SA 3.0. Autori: vedi cronologia.

## Problem description
No Power — After prompt to boot on DC power supply, current jumps back and forth from 0 A to 320 mA, then 0 A to 1.4 A, then 0 A to 500 mA, and so on
## Symptoms
- No current draw before prompt to boot on DC power supply
- After prompt to boot, you see the current jump quickly between 0 A and various values, like 0 A > 320 mA > 0 A > 1.4 A > 0 A > 500 mA

## Solution
### Diagnostic Steps
- Check for shorts around NAND
- Usually you'll find these lines with a shorted capacitor:
  - PP3V0_NAND
  - PP0V9_NAND
- If so, find the shorted capacitor by injecting voltage

**Please note:** PMIC (U1801) will often show lots of heat if you're testing with the DCPS connected through the battery connector but it's not the cause of the short. The short is at the capacitor next to NAND, but since you're connected to the battery connector, the current has to flow through PMIC to get to the short cap, hence the PMIC heats up.

### Another Possible Cause:
Sometimes, you'll see this same behavior when PP1V8_SDRAM or PP1V1_SDRAM is shorted. If this is the case, you'll need to check for heat above the CPU. If you find PP1V8_SDRAM or PP1V1_SDRAM is shorted and find heat above the CPU, then it's a RAM short.

You'll need to replace RAM to solve it. This a very advanced repair and should only be done by those who've mastered this repair. It's very easy for things to go wrong and damage the CPU.

### Repair Steps
Once you find the shorted capacitor, you can remove it and confirm the short is cleared.
