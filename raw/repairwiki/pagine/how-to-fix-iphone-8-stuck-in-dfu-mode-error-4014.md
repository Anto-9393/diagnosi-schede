---
titolo: How To Fix iPhone 8 Stuck In DFU Mode. Error 4014
tipo: fonte_esterna
url: https://repair.wiki/w/How_To_Fix_iPhone_8_Stuck_In_DFU_Mode._Error_4014
cronologia: https://repair.wiki/w/How_To_Fix_iPhone_8_Stuck_In_DFU_Mode._Error_4014?action=history
revisione: '2024-02-09T08:47:28Z'
categorie: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# How To Fix iPhone 8 Stuck In DFU Mode. Error 4014

> Fonte: [How To Fix iPhone 8 Stuck In DFU Mode. Error 4014 — repair.wiki](https://repair.wiki/w/How_To_Fix_iPhone_8_Stuck_In_DFU_Mode._Error_4014), CC BY-SA 3.0. Autori: vedi cronologia.

## Problem description
How To Fix iPhone 8 Stuck In DFU Mode. When you try to update or restore, you will get iTunes Error Code 4014. The screen will stay dark or not lit up.

## Symptoms
- You get no image from the screen
- You plug into computer and iTunes/3U tools detects it in DFU mode
- If you try to Update or Restore, you get these results:
  - iTunes Error Code: Error 4014
  - 3u Tools Easy Flash: Fails at 19%

## Solution
### Cause:
- Error 4014 is usually "NAND not detected".

### Solutions:
- Check the caps around NAND to see if they're shorted.
  - If there's a short, remove the shorted cap and try to boot the phone up.
- If no short, pull the NAND and connect it to the JC P13 NAND programmer and see if it's readable
  - You can refer to this video for how to use the P11F Programmer: <nowiki>https://youtu.be/J6n2Bj7sG5A</nowiki>
  - If it doesn't read, the NAND is dead and needs to be replaced
  - If it does read a NAND, then you can reball NAND and install it again. The phone should boot right up.
