---
titolo: IPhone 13 Pro and 13 Pro Max No Touch Problem
tipo: fonte_esterna
url: https://repair.wiki/w/IPhone_13_Pro_and_13_Pro_Max_No_Touch_Problem
cronologia: https://repair.wiki/w/IPhone_13_Pro_and_13_Pro_Max_No_Touch_Problem?action=history
revisione: '2026-02-09T05:24:25Z'
categorie: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# IPhone 13 Pro and 13 Pro Max No Touch Problem

> Fonte: [IPhone 13 Pro and 13 Pro Max No Touch Problem — repair.wiki](https://repair.wiki/w/IPhone_13_Pro_and_13_Pro_Max_No_Touch_Problem), CC BY-SA 3.0. Autori: vedi cronologia.

## Problem description
iPhone 13 pro/ pro max boots normally but touchscreen does not respond at all. Display shows image, but there is no touch input on the entire panel. Replacing the screen does not fix the issue.

## Symptoms
- Touchscreen not responding at all
- Screen replacement does not fix the problem
- GR on display connector is normal

## Solution
The problem generally is due to a faulty capacitor that is placed on the touch boost line. Replacing the capacitor **C8901**and (**8903** **only** in iPhone 13 pro max)(according to JC Drawing) fixes the issue.

### Diagnostic Steps
1. Check diode values on the connector, if you see any unusual reading trace it or else continue to the next step if all diode values are good.
1. Check for voltage on the PP5V1_TOUCH_VDDTX_S2:
1. * You cannot normally check voltage on this line
1. * In order to check voltage on this line you have to manually enable the ic by giving it an enable signal and here is how to do it:
1. ** Plug the DCPS cable/ battery to the phone 3.8-4.2 volts
1. ** Inject 1.8v at lowest possible Ampere on pin #49(according to JC DRAWING) to enable the LDO output
1. ** Check the output voltage on pin #54(according to JC DRAWING)
1. ** If you get no voltage output then proceed to the repair steps

### Repair Steps
1. Split the board in half
1. Check the capacitor C8901+(C8903 only in 13 pro max), if shorted it MUST be replaced.

NOTE: (if you don't replace this capacitor phone will still have no touch problem)

1. Recheck for shorts
1. In some rare cases of which short is not cleared:
1. * You have to replace the u8900
1. * Check diode value under the ic before replacing it
1. * Replace the ic and the capacitor
1. Test the touch function, it should be restored.
