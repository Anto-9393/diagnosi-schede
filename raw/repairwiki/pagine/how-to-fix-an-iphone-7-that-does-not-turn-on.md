---
titolo: How To Fix an iPhone 7 That Does Not Turn On
tipo: fonte_esterna
url: https://repair.wiki/w/How_To_Fix_an_iPhone_7_That_Does_Not_Turn_On
cronologia: https://repair.wiki/w/How_To_Fix_an_iPhone_7_That_Does_Not_Turn_On?action=history
revisione: '2026-11-02T12:33:47Z'
categorie: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# How To Fix an iPhone 7 That Does Not Turn On

> Fonte: [How To Fix an iPhone 7 That Does Not Turn On — repair.wiki](https://repair.wiki/w/How_To_Fix_an_iPhone_7_That_Does_Not_Turn_On), CC BY-SA 3.0. Autori: vedi cronologia.

## Problem description
Pulls ≈2 A or more before you prompt to boot on DC power supply

## Symptoms
- No Power
- Doesn't turn on
- Doesn't Charge

## Solution
### Diagnostic Steps
Do a full visual inspection of the board and check for water damage under the stickers on the back. Remove the foam around the connectors to get a better look at everything. You're looking for any signs of corrosion on or around components and ICs.

If there is no water damage, is is most likely a shorted capacitor on any of the below lines:

- **PP_VDD_MAIN** — This is the most likely line to be shorted
- **PP_VDD_BOOST** — This line is usually shorted when it's not VDD MAIN
- **PP_LCM_BL_ANODE** or **PP_LCM_BL34_ANODE** — Sometimes the backlight circuit has a short and causes the same symptoms
- **PP_SPKR1_VBOOST** — This is a bit rare but it does happen

### Repair Steps
You'll need to inject voltage (4 V / 2 A) directly into the line you measured as short and use freeze spray (see here <nowiki>https://youtu.be/3MtLSQJvQxI</nowiki>) or thermal camera (see here: <nowiki>https://youtu.be/fkd4iDjgfvc</nowiki>) to spot the capacitor that is shorted.

In these cases, you can just remove the shorted capacitor and not replace it. The device will function normally with no negative effects.

In these cases, removing the shorted capacitor can restore power to the device. Whether it needs replacing depends on its role in the circuit, as some capacitors are important for power stability.

Replacing the capacitor also means applying more heat to the board, increasing the risk of damage during repair.

Replacing it means you are adding more heat to the board to reinstall it, which increases the risk of something going wrong.

If you have a case of water damage, then you'll have to pay attention to the spots on the board where there's signs of water damage.

Often, you'll find corrosion on capacitors but also under ICs.

Common ICs and areas to have corrosion and cause a VDD MAIN short:

- Under BBPMU_RF and around it, like Capacitors: C5625_RF, C5622_RF
- Back top "arm", like C2611, C2612, C2609, C2610
- Back bottom, like the backlight caps C3725, C3705, C4602, C4612
- Above and next to WiFi (WLAN_RF), like C7610_RF, C2527, C3002
- Front Top above CPU, like C3327, C3328, C3313

You'll need to visually inspect these areas to see if they're liquid damaged

**Please Note:** If you are using a DC power supply to inject voltage through the battery connector, like using an iPower Pro or DT880 (see here <nowiki>https://youtu.be/rawjB9yxe1A</nowiki>), be aware that the Tigris Mosfet Q2101 will heat up instantly. This is because the battery connector line PP_BATT_VCC connects to PP_VDD_MAIN through it, which creates lots of heat. Q2101 itself does not have a connection to ground, therefore, it's impossible for it to be shorted.

## References
