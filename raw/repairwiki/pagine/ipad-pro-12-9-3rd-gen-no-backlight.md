---
titolo: IPad Pro 12.9 3rd Gen No Backlight
tipo: fonte_esterna
url: https://repair.wiki/w/IPad_Pro_12.9_3rd_Gen_No_Backlight
cronologia: https://repair.wiki/w/IPad_Pro_12.9_3rd_Gen_No_Backlight?action=history
revisione: '2025-07-20T22:01:04Z'
categorie: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
figure:
- file: Placeholder image.jpg
  didascalia: Example image (Figure 1) -- No image yet. Help expand this page by uploading
    it!
- file: IPad Pro 12.9 2018 FPC diode readings.png
  didascalia: ''
- file: IPad Pro 12.9 2018 Backlight Circuit.png
  didascalia: ''
---

# IPad Pro 12.9 3rd Gen No Backlight

> Fonte: [IPad Pro 12.9 3rd Gen No Backlight — repair.wiki](https://repair.wiki/w/IPad_Pro_12.9_3rd_Gen_No_Backlight), CC BY-SA 3.0. Autori: vedi cronologia.

## Problem description
The iPad turns on but backlight is not working you can only see something if you point a flashlight at the screen

## Symptoms
- The iPad turns on but it has no backlight

## Diagnostic Steps
First always try a working screen to prove you dont have a parts problem.

If a new display doesnt solve the backlight issue the next step is to diagnose the motherboard.

Start by doing a visual inspection of the FPC connectors if everything looks ok using you multimeter take diode readings of the FPC and compare with the image bellow.

The next step is to inspect the backlight circuit of the motherboard (it is common to have a blow capacitor here)

### Repair Steps
If there is physical damage to the FPC connectors, replace them. The best method is to use a hot air station to desolder the old FPC, clean the old solder from the motherboard, apply new solder, align the new FPC, and use the hot air station to solder it. (Be careful not to use excessive heat, as it may melt the FPC).

When taking diode readings of the FPC, if you measure a line that should read, for example, 0.500V but get 0.100V or 0.000V, it indicates a short on that line. The best way to trace the short is to inject voltage into the line with a DCPS and use a thermal camera to identify which component heats up.

If you measure a line that should read 0.500V but get OL (Open Line), it indicates a disconnection in the circuit. To trace the issue, consult the board view to follow the line’s path.

If a filter connected to the backlight connector is open, replace it with one matching the same specifications (refer to the schematics) or source it from a donor board.

If you see a shorted capacitor on the PPLED_OUT line the 3 diodes on the same line will probably be damaged, you must replace them with one matching the same specifications (refer to the schematics) or source it from a donor board.

If none of the above steps resolve the no backlight issue, the next step is to replace U8100.
