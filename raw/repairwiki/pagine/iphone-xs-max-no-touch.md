---
titolo: IPhone XS Max No Touch
tipo: fonte_esterna
url: https://repair.wiki/w/IPhone_XS_Max_No_Touch
cronologia: https://repair.wiki/w/IPhone_XS_Max_No_Touch?action=history
revisione: '2025-08-18T22:05:09Z'
categorie: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# IPhone XS Max No Touch

> Fonte: [IPhone XS Max No Touch — repair.wiki](https://repair.wiki/w/IPhone_XS_Max_No_Touch), CC BY-SA 3.0. Autori: vedi cronologia.

## Problem description
The device turns on but touch does not work

## Symptoms
- Touch doesnt work.

## Solution
The most common issue on iPhone XS Max with no touch is a disconnection between the top and bottom boards, but in this guide we will go over diagnostic steps that should cover the main causes of no touch.

### Diagnostic Steps
The first step is to always rule out faulty parts. Start by testing a new display.

If a new display doesnt not solve the issue inspect the Touch FPC for any physical damage or liquid damage.

Take diode readings of the Touch FPC and compare them with the image on the side.

If everything is ok the next step is to check if the main touch voltages are present.

These voltages can be measured here, keep in mind that these voltages may only show up with the device powered on and a display connected.

PN6V7_RACER

PN3V5_RACER

PN10V0_RACER

PN1V8_TOUCH_RACER_S2

PN1V1_RACER

PN5V25_TOUCH_VDDH

If these voltages are present/or missing the next thing to do is split the boards, the most common issue is to have a crack on a solder joint between the interposer and the top board or a ripped pad.

The first thing you should do after splitting the boards is to check for any ripped pads, if you have any you need to check with a program like ZXW and see where that line goes.

Test with a tool similar to iSocket and turn on the phone and see if Touch works, if it is all you have to do is to reball the motherboard.

## Repair Steps
If by replacing by trying a new display the touch fault is solved all you have to do its to replace the display.

If there is a any physical damage to the FPC the solution is to replace it. The best method is to use a hot air station to desolder the old FPC, clean the old solder from the motherboard, apply new solder, align the new FPC, and use the hot air station to solder it. Be careful not to use excessive heat, as you may cause a solder bridge under the motherboard.

When taking diode readings of the FPC, if you measure a line that should read, for example, 0.500V but get 0.100V or 0.000V, it indicates a short on that line. The best way to trace the short is to inject voltage into the line with a DCPS and use a thermal camera to identify which component heats up. Fallow this guide how to find the short Short Circuits - Repair Basics

If you measure a line that should read 0.500V but get OL (Open Line), it indicates a disconnection in the circuit. To trace the issue, consult the board view to follow the line’s path.

If Touch works fine using the iSocket tool the motherboard must be reballed.

If Voltages are missing this may be due to a faulty U5600 (LM3373A2YKA) this creates most of these, i have seen this IC faulty 2 times.

U5600 can be found online easily on many suppliers it is also present on iPhone X , iPhone XS and iPhone XS Max.

If you have ripped pads they may not be needed check on a boardview software like ZXW what they do if the line you check has the name "RACER" or "Touch" it needs to be rebuild.

If you need to rebuild a pad it is recommend to watch this video by rewa on youtube: https://www.youtube.com/watch?v=I_6xZVY7sFM

## Final Testing
After assembling the phone, ensure every function is working as expected, not just the touch circuit.
