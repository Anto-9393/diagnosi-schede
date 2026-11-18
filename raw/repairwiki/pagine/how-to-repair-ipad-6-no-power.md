---
titolo: How To Repair IPad 6 No Power
tipo: fonte_esterna
url: https://repair.wiki/w/How_To_Repair_IPad_6_No_Power
cronologia: https://repair.wiki/w/How_To_Repair_IPad_6_No_Power?action=history
revisione: '2025-11-30T18:32:05Z'
categorie: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
figure:
- file: Ipad-6-wifi-ic.png
  didascalia: Example of iPad 6 WiFi IC (Figure 1)
- file: Ipad-6-wifi-ic-under-thermal.png
  didascalia: Example of shorted WiFi IC on iPad 6 under thermal camera view
- file: Ipad-6-wifi-ic-schematic.png
  didascalia: iPad 6 WiFi IC on BoardView Software (Figure 2)
---

# How To Repair IPad 6 No Power

> Fonte: [How To Repair IPad 6 No Power — repair.wiki](https://repair.wiki/w/How_To_Repair_IPad_6_No_Power), CC BY-SA 3.0. Autori: vedi cronologia.

## Problem description
iPad 6 shows no signs of life (no boot, no display, no vibration, no charging icon).

When connected to a DC Power Supply (DCPS), the device either:

- Current spikes directly to 1 A & above (dead short)
- Jumps directly 0.150 A and resets (partial boot but fails)

This model commonly suffers from shorts on VCC_MAIN, Tristar  failure, or WiFi IC/PMU shorts.

<nowiki>*</nowiki>***NOTE**: A proper boot sequence should be 0.050 -> 0.060 -> 0.100 -> and climbing till it reaches 1.00 A**

## Symptoms
- Completely dead, no Apple logo
- No reaction on charger
- No heat except possibly near shorted component
- DCPS shows high current

## Solution
### Diagnostic Steps
#### 1. Check Battery Voltage
- A healthy iPad 6 battery should read 3.7–4.2 V
- If battery is at 0 V, iPad may appear dead

----

#### 2. Try DC Power Supply Boot
- Connect directly to board
- Observe current draw:

| Current Behavior | Likely Fault |
| Instant spike above 1.00 A | Possible short on VCC_MAIN, WiFi IC or PMIC |
| Instant spike to .150A and cycling back | Tristar failure |
----

#### 3. Check for VCC_MAIN Short
- Multimeter to diode mode → red probe ground
- Black probe on VCC_MAIN caps
- Reading close to 0.000 = short

----

#### 4. Inspect Charging IC Region
- Check under thermal camera/rosin flux for a bad Charging IC.

----

#### 5. Check WiFi Section
- Check under thermal camera/rosin flux for a shorted WiFi IC.

### Repair Steps
#### 1. Remove the Board
Separate battery first, remove board from chassis.

#### 2. Identify Fault
Based on DCPS + thermal/rosin method:

- Shorted capacitor? → Replace
- Hot WiFi chip? → Replace
- Tristar short? → Replace Tristar

#### 3. Fix the Short
- Replace burnt/shorted capacitor
- Replace WiFi IC
- Replace Hydra charging IC

#### 4. Reassemble & Test
- Confirm proper current pattern
- Confirm charging
- Confirm successful boot
- Run WiFi test
- Plug into iTunes/PC for recognition
