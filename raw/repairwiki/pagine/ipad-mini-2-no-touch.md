---
titolo: IPad Mini 2 No Touch
tipo: fonte_esterna
url: https://repair.wiki/w/IPad_Mini_2_No_Touch
cronologia: https://repair.wiki/w/IPad_Mini_2_No_Touch?action=history
revisione: '2025-07-27T21:21:04Z'
categorie: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# IPad Mini 2 No Touch

> Fonte: [IPad Mini 2 No Touch — repair.wiki](https://repair.wiki/w/IPad_Mini_2_No_Touch), CC BY-SA 3.0. Autori: vedi cronologia.

## Problem description
The iPad turns on but touch doesn't work

## Symptoms
- Touch doesn't work

## Solution
The no touch problem can be caused a faulty digitizer or a motherboard problem.

### Diagnostic Steps
Always try a new digitizer first before assuming you have a motherboard problem.

Inspect the Touch FPC this FPC for any physical damage, it is very easy to damage this FPC by mistake.

Take diode readings of the FPC and compare with the image bellow.

The next step after cheking diode readings of the FPC is to check if the required voltages are there, these voltages are only present with the device on.

The 2 important voltages need are PP5V25_GRAPE and PP1V8_GRAPE.

## Repair Steps
- If a new digitizer resolves the no-touch issue, the repair is straightforward and quick
- If there is physical damage to the FPC connectors, replace them. The best method is to use a hot air station to desolder the old FPC, clean the old solder from the motherboard, apply new solder, align the new FPC, and use the hot air station to solder it. (Be careful not to use excessive heat, as it may melt the FPC).
- When taking diode readings of the FPC, if you measure a line that should read, for example, 0.500V but get 0.100V or 0.000V, it indicates a short on that line. The best way to trace the short is to inject voltage into the line with a DCPS and use a thermal camera to identify which component heats up.
- If you measure a line that should read 0.500V but get OL (Open Line), it indicates a disconnection in the circuit. To trace the issue, consult the board view to follow the line’s path.
- If a filter connected to the touch connectors is open, replace it with one matching the same specifications (refer to the schematics) or source it from a donor board.
- If PP5V25_GRAPE is missing the problem is with the PMIC (U8100) so replace the PMIC If PP1V8_GRAPE is missing the problem is U1700 so replace U1700
- If none of the above steps resolve the no-touch issue, the next step is to reball the CPU since the touch ic is inside the CPU.

## Final Testing
Assemble the iPad and ensure that the touch functionality works perfectly. The best way to test this is in the Notes app by drawing lines from end to end. Ensure the iPad doesn't exhibit ghost touches.

If you replaced the FPC connector make sure the Home button and case sensor also works.
