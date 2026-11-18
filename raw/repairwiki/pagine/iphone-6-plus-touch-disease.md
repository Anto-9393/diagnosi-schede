---
titolo: IPhone 6 Plus Touch Disease
tipo: fonte_esterna
url: https://repair.wiki/w/IPhone_6_Plus_Touch_Disease
cronologia: https://repair.wiki/w/IPhone_6_Plus_Touch_Disease?action=history
revisione: '2025-06-19T13:27:46Z'
categorie: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
figure:
- file: IPhone 6 Plus Touch Disease.jpg
  didascalia: iPhone 6 Plus Touch Disease!
- file: Where to remove the underfill.png
  didascalia: Where to remove the underfill
- file: 007 Blade.png
  didascalia: 007 Blade
- file: U2402 Location.png
  didascalia: U2402 Location
- file: M1 Jumper.png
  didascalia: M1 Jumper
---

# IPhone 6 Plus Touch Disease

> Fonte: [IPhone 6 Plus Touch Disease — repair.wiki](https://repair.wiki/w/IPhone_6_Plus_Touch_Disease), CC BY-SA 3.0. Autori: vedi cronologia.

## Problem description
The iPhone turns on but touch doesn't work or its intermittent

## Symptoms
- Touch does not work
- Touch is intermittent
- Touch doesn't work and some weird lines show up in the top part of the screen when you flex the phone

## Solution
Usually on phones with no touch we start by taking diode measurements of the FPC connectors on the iPhone 6 Plus we can skip that. This issue is old and it was really common, at some point Apple was even involved in a lawsuit over this issue

This issue is caused by a disconection of the black touch IC U2402.

### Repair Steps
To fix this issue we will need to remove the U2402 and run a small jumper wire to avoid the problem coming back.

The first step is to take out the motherboard out.

If this is your first time doing this repair I recommend that you remove the underfill from these components. Since we will work on the backside of them they may disconnect, if these components disconnect it may cause problems like the front camera not working, the earpiece not working.

To remove this underfill it doesnt take much heat i recomend using your heatgun and a 007 blade like the image bellow.

After removing the underfill we can proced to remove the touch IC.

The touch ic is located on the back side of the motherboard near the WIFI IC.

Use your heat gun to desolder the chip be careful to not use excessive heat since the CPU is on the other side and excessive heat may cause it to disconnect.

After removing the IC add some low-melt solder with your soldering iron to the pads on the motherboard to make it easier to clean.

Clean the solder from the pads on the motherboard.

After cleaning the pads, check for any ripped pads, you may have one missing that is common to break the "M1" pad.

Even if the pad is not missing i recomend to make the jump anyway since it is common for the pad to brake and issue will come back.

After doing the jump, you can reball the old chip and solder it back on the board or you can buy a pre-balled one.

### Final Testing
Make sure touch is working properly, gently flex the phone and check if it's working well, no line appear on the screen.

Test every function of the device, it is common to have issues with the front camera after this repair due to those components mentioned before.
