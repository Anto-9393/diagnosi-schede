---
titolo: How To Fix an iPhone 7 Stuck In DFU Mode. iTunes Error Code 4014
tipo: fonte_esterna
url: https://repair.wiki/w/How_To_Fix_an_iPhone_7_Stuck_In_DFU_Mode._iTunes_Error_Code_4014
cronologia: https://repair.wiki/w/How_To_Fix_an_iPhone_7_Stuck_In_DFU_Mode._iTunes_Error_Code_4014?action=history
revisione: '2024-01-25T06:45:35Z'
categorie: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# How To Fix an iPhone 7 Stuck In DFU Mode. iTunes Error Code 4014

> Fonte: [How To Fix an iPhone 7 Stuck In DFU Mode. iTunes Error Code 4014 — repair.wiki](https://repair.wiki/w/How_To_Fix_an_iPhone_7_Stuck_In_DFU_Mode._iTunes_Error_Code_4014), CC BY-SA 3.0. Autori: vedi cronologia.

## Problem description
How to fix an iPhone 7 that is stuck in DFU Mode. When you try to flash an update or restore, it will fail with Error 4014.

## Symptoms
- You get no image from the screen
- You plug into computer and iTunes/3U tools detects it in DFU mode
- If you try to Update or Restore, you get these results:
  - iTunes Error Code: Error 401
  - 3u Tools Easy Flash: Fails at 19%

### Solution
Error 4014 is usually "NAND not detected".
- Check the caps around NAND to see if they're shorted.
  - If there's a short, remove the shorted cap and try to boot the phone up.
- If no short, pull the NAND and connect it to the JC P7 NAND programmer and see if it's readable
  - If it doesn't read, the NAND is dead and needs to be replaced
  - If it does read a NAND, then you can reball NAND and install it again. The phone should boot right up.
