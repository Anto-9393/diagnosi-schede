---
titolo: IPhone 5 "FindFlashMediaAndKeepout" error while booting repair
tipo: fonte_esterna
url: https://repair.wiki/w/IPhone_5_%22FindFlashMediaAndKeepout%22_error_while_booting_repair
cronologia: https://repair.wiki/w/IPhone_5_%22FindFlashMediaAndKeepout%22_error_while_booting_repair?action=history
revisione: '2024-03-02T12:16:06Z'
categorie: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
figure:
- file: FindFlashMediaAndKeepout.jpg
  didascalia: An iPhone 5 with water damage displays the <code>FindFlashMediaAndKeepout</code>
    error message.
---

# IPhone 5 "FindFlashMediaAndKeepout" error while booting repair

> Fonte: [IPhone 5 "FindFlashMediaAndKeepout" error while booting repair — repair.wiki](https://repair.wiki/w/IPhone_5_%22FindFlashMediaAndKeepout%22_error_while_booting_repair), CC BY-SA 3.0. Autori: vedi cronologia.

## Problem description
Full error:
 [NAND] _FindFlashMediaAndKeepout:601 physical nand block offset 1
 [NAND] start:356 this <ptr> PROVIDER=<ptr> flashMedia=<ptr>
 [NAND] WMR_Start:149 Apple PPN NAND Driver, Read/Write
 [NAND] WMR_Start:174 FIL_Init  [OK]
 [NAND] WMR_Open:371 VFL_Open    [OK]
 [NAND] s_cxt_boot:88 sftl: error, unclean shutdown; adopted 6016 spans
 [NAND] WMR_Open:420 FTL_Open    [OK]
 [NAND] _publishServices:642 FTL capabilities: 0x00000001
 [NAND] _ppnvflGetStruct:3469 Checking borrowed blocks - count: 23 max_count: 23
 [NAND] _fetchBorrowedList:881 number of borrowed blocks 16

## Symptoms
- Phone displays <code>FindFlashMediaAndKeepout</code> error while booting.
- When attempting to restore using iTunes, error 4013 is displayed.

## Solution
- The error is mostly associated with water damage or bad ribbon cables / connections.
- Some users report that unplugging the front camera, the back camera, the camera flash, the proximity sensor ribbon cable or even the whole display assembly can circumvent the issue. This can allow the device to be used or restored with iTunes.
- If the above methods don't work, removing the compass IC (U15) can allow the phone to boot again. The compass IC is located right next to where the front camera ribbon cable plugs in at the very edge of the PCB. It's hidden below some black adhesive tape ([see this video](https://www.youtube.com/watch?v=nc1Thaqn3J8)). The device itself will work fine without the chip, but some functions won't be available (compass, screen auto-rotation, maybe other minor things). If the device boots without the chip, installing a new chip may restore the missing functions.
