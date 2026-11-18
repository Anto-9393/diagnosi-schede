---
titolo: IPhone XR Stuck in DFU, updates successfully but goes back to DFU
tipo: fonte_esterna
url: https://repair.wiki/w/IPhone_XR_Stuck_in_DFU%2C_updates_successfully_but_goes_back_to_DFU
cronologia: https://repair.wiki/w/IPhone_XR_Stuck_in_DFU%2C_updates_successfully_but_goes_back_to_DFU?action=history
revisione: '2026-02-02T00:08:04Z'
categorie: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# IPhone XR Stuck in DFU, updates successfully but goes back to DFU

> Fonte: [IPhone XR Stuck in DFU, updates successfully but goes back to DFU — repair.wiki](https://repair.wiki/w/IPhone_XR_Stuck_in_DFU%2C_updates_successfully_but_goes_back_to_DFU), CC BY-SA 3.0. Autori: vedi cronologia.

## Problem description
Stuck in DFU mode

Flashes successfully with an update or restore but goes back to DFU mode.

## Symptoms
- Screen shows no image and pulls 0.45A via USB charging
- Does not appear to boot
- Prompt to boot on DCPS, shows it hangs around 45mA draw
- Connect to PC and it's in DFU mode
- Flash an update or restore & it goes through 100% with no errors but goes back to DFU mode

## Solution
- Check R0601 at the corner of NAND.
- This resistor connects PP1V8_IO to SPI_AP_TO_S4E_MOSI_BOOT_CONFIG1
- Clean the underfill around it & poke it hard.
- If it breaks, it must be replaced.
- Value is 4.7ohms
- After replacing it, the phone will no longer be in DFU mode & boot right up.

Migrated from old wiki
