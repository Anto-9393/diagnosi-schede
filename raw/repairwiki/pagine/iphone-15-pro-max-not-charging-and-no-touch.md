---
titolo: IPhone 15 Pro Max Not Charging and no Touch
tipo: fonte_esterna
url: https://repair.wiki/w/IPhone_15_Pro_Max_Not_Charging_and_no_Touch
cronologia: https://repair.wiki/w/IPhone_15_Pro_Max_Not_Charging_and_no_Touch?action=history
revisione: '2025-05-27T17:42:14Z'
categorie: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
figure:
- file: Iphone 15 pro max not charging.jpg
  didascalia: iPhone 15 Pro Max Not Charging.(Image by Cell Phone Repair Academy)
- file: 5V U9500 input.png
  didascalia: U9500 5V Input
- file: IPhone 15 Pro Max.png
  didascalia: IPhone 15 Pro Max Charging ICs
---

# IPhone 15 Pro Max Not Charging and no Touch

> Fonte: [IPhone 15 Pro Max Not Charging and no Touch — repair.wiki](https://repair.wiki/w/IPhone_15_Pro_Max_Not_Charging_and_no_Touch), CC BY-SA 3.0. Autori: vedi cronologia.

## Problem description
The iPhone doesn't charge and touch doesn't work

## Symptoms
- Device doesn't charge.
- Device doesn't charge and touch is also not working.

## Solution
This problem is usually associated with a bad U9500 this chip detects what is connected in the USB C port.

### Diagnostic Steps
The first step is to always rule out faulty parts. Start by testing a new display and battery.

If your device doesn't charge, this doesn't mean the U9500 is bad. This issue can also be caused by a faulty Tigris IC. A good way to test is to try a wireless charger. If the device charges with a wireless charger, it means the Tigris IC is working.

For the U9500 to work, it must have 5V on the pad below. To measure this, you will need to separate the motherboard, connect the charging port, and then connect it to a charger.

If you measure 5V at the input, it indicates that the U9500 is receiving power and should be functioning.

### Repair Steps
The U9500 doesn't work alone, it functions in conjunction with a ROM IC (U9720). This creates a challenge because we cannot replace just the U9500. To replace the U9500, we must also replace the U9720, and both components need to be sourced from a donor board, specifically from an iPhone 15 Pro Max. **They cannot be sourced from an iPhone 15 or 15 Pro.**

#### Replacing the U9500 and U9720
- Use your hot air station to desolder the old U9500 IC from the motherboard, while its still hot desolder the ROM IC U1030.
- Clean the pads on the motherboard thoroughly.
- Reball the new U9500 if it isn't pre-balled.
- Reball the new U9720.
- Use your hot air station to solder the new U9500 IC onto the motherboard.
- Solder the new U9720

After replacing the U9500 and U9720, test if the phone is charging and if the touch functionality is working. To do this, connect the charging port, screen, and battery to the top board. The iPhone 15 Pro Max can power on with just the top board. Plug the phone into a charger and use an amp meter to measure the current the phone is receiving.

After confirming that the phone is charging and the touch functionality is working as expected, the next steps are to reball the bottom board and resolder both boards back together.

## Final Testing
After assembling the phone, ensure every function is working as expected, not just the charging circuit.

Connect the phone to a fast charger and check if it fast charges using an amp meter. If it’s fast charging, it should draw 9V and around 2+ amps, depending on the battery capacity.

Connect the phone to a computer and verify that data transfer is working.

Connect USB-C headphones and confirm that audio is functioning as expected.
