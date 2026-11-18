---
titolo: How To Repair iPad Air 6 12.9" Touch Not Working
tipo: fonte_esterna
url: https://repair.wiki/w/How_To_Repair_iPad_Air_6_12.9%22_Touch_Not_Working
cronologia: https://repair.wiki/w/How_To_Repair_iPad_Air_6_12.9%22_Touch_Not_Working?action=history
revisione: '2026-02-18T02:48:52Z'
categorie: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# How To Repair iPad Air 6 12.9" Touch Not Working

> Fonte: [How To Repair iPad Air 6 12.9" Touch Not Working — repair.wiki](https://repair.wiki/w/How_To_Repair_iPad_Air_6_12.9%22_Touch_Not_Working), CC BY-SA 3.0. Autori: vedi cronologia.

## Problem description
iPad Air 6 presents with no touch response, while the display image appears normal. Replacing the display with a known-good screen does not restore touch functionality, confirming a logic board issue.

The most common cause in this case is a shorted capacitor on the touch signal line, preventing proper communication between the touch controller and digitizer.

## Symptoms
- Display works normally
- No touch response at all
- No ghost touch
- Known-good display does not fix issue
- Device boots and functions otherwise normally

## Solution
### Diagnostic Steps
#### 1. Confirm Display Is Not the Issue
- Install a known-good display
- If touch still does not work → proceed to board diagnostics

----

#### 2. Check Touch Line in Diode / Resistance Mode
- Identify touch-related rail at FPC connector
- Measure in diode or resistance mode
- Compare to known-good board if available

❌ Near 0 reading indicates short to ground
----

#### 3. Locate the Short Using Voltage Injection
1. Set DC power supply to:
1. * Low voltage (1V–2V)
1. * Current limit ~1–2A
1. Inject voltage into the shorted touch rail
1. Apply rosin/flux over suspected capacitor area
1. Observe which component heats up first

The shorted capacitor will:

- Warm up quickly
- Melt rosin faster than surrounding components

### Repair Steps
1. Disconnect battery
1. Inject voltage and identify faulty capacitor
1. Apply flux
1. Remove shorted capacitor carefully
1. Clean pads and inspect for damage
1. Install matching capacitor from donor board
1. Inspect solder joints under microscope
1. Reassemble device
1. Test touch functionality
