---
titolo: IPad Pro 12.9 5th Gen Touch Screen Not Working
tipo: fonte_esterna
url: https://repair.wiki/w/IPad_Pro_12.9_5th_Gen_Touch_Screen_Not_Working
cronologia: https://repair.wiki/w/IPad_Pro_12.9_5th_Gen_Touch_Screen_Not_Working?action=history
revisione: '2025-10-31T19:19:41Z'
categorie: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
figure:
- file: IPad Pro 12.9 Gen 5 PP15V0 TOUCH FILT.png
  didascalia: Fig 1. Check PP15V0_TOUCH_FILT for shorts for No Touch issue
- file: IPad Pro 12.9 Gen 5 PP15V0 TOUCH LDO.png
  didascalia: Fig 2. Check PP15V0_TOUCH_LDO for shorts
- file: IPad Pro 12.9 Gen 5 PP15V0 TOUCH.png
  didascalia: Fig 3. Check PP15V0_TOUCH for shorts
---

# IPad Pro 12.9 5th Gen Touch Screen Not Working

> Fonte: [IPad Pro 12.9 5th Gen Touch Screen Not Working — repair.wiki](https://repair.wiki/w/IPad_Pro_12.9_5th_Gen_Touch_Screen_Not_Working), CC BY-SA 3.0. Autori: vedi cronologia.

## Problem description
Fixing a problem where the iPad turns on but the touch screen does not respond to any input.
## Symptoms
- Non working touch

## Solution
Check for shorts on the capacitors near the two BCM15957A0 touch controllers above the lower display connectors. Often there will be a failed capacitor causing no touch.

Check the following lines for shorts. It could be an IC or a bad capacitor

- PP15V0_TOUCH_FILT (Fig 1)
- PP15V0_TOUCH_LDO (Fig 2)
- PP15V0_TOUCH (Fig 3)

If a capacitor is shorted, you can just remove it & leave it off. The touch issue should be solved

If an IC is shorted, then you'll need to replace it.
