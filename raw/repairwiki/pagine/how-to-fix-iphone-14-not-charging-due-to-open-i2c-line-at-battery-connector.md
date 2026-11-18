---
titolo: How To Fix iPhone 14 Not Charging due to open i2c line at battery connector
tipo: fonte_esterna
url: https://repair.wiki/w/How_To_Fix_iPhone_14_Not_Charging_due_to_open_i2c_line_at_battery_connector
cronologia: https://repair.wiki/w/How_To_Fix_iPhone_14_Not_Charging_due_to_open_i2c_line_at_battery_connector?action=history
revisione: '2026-02-22T02:49:33Z'
categorie: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
figure:
- file: Ip14 I2c2 location.png
  didascalia: iPhone 14/Plus I2C2_SMC_CHARGER_BI_GG_SDA_1V8 Pin Location on Battery
    Connector
- file: Ip14 i2c2 jumper1.png
  didascalia: iPhone 14/ Plus Jumper Location on Other Side
- file: Ip14 i2c2 jumper2.png
  didascalia: iPhone 14/ Plus Jumper Location on Battery Connector
---

# How To Fix iPhone 14 Not Charging due to open i2c line at battery connector

> Fonte: [How To Fix iPhone 14 Not Charging due to open i2c line at battery connector — repair.wiki](https://repair.wiki/w/How_To_Fix_iPhone_14_Not_Charging_due_to_open_i2c_line_at_battery_connector), CC BY-SA 3.0. Autori: vedi cronologia.

## Problem description
iPhone 14 comes in with no charging. The device may power on but does not accept charge from a known-good cable and adapter.

During board-level diagnostics, the line:<blockquote>I2C2_SMC_CHARGER_BI_GG_SDA_1V8</blockquote>at the battery connector measures OL (open line) instead of normal diode/voltage value.

This open data line prevents proper communication between the battery gas gauge and charging subsystem, resulting in no charging.

## Symptoms
- Device does not charge
- No charging icon
- Battery percentage may be stuck or inaccurate
- Known-good cable and charger do not fix issue
- No visible damage to charging port
- Device powers on but refuses to increase battery %

## Solution
### Diagnostic Steps
#### 1. Confirm Charging Fault
- Test with known-good cable and brick
- Verify no charging current increase
- Confirm dock flex is not at fault

----

#### 2. Measure Battery Connector I2C Line
- Set multimeter to diode mode
- Probe I2C2_SMC_CHARGER_BI_GG_SDA_1V8 at battery connector

Expected:

- .350 (not OL)

Faulty:

- OL (open line)

----

#### 3. Trace the Line
- Locate corresponding test point or opposite-side pad
- Measure continuity between:
  - Battery connector pin
  - Other side of board / test pad

If no continuity → trace is broken.

### Repair Steps
1. Disconnect battery
1. Locate affected battery connector pin
1. Identify alternative test point / via on opposite side of board
1. Verify donor point has correct diode reading
1. Run a fine jumper wire between:
1. * Working side of the line
1. * Battery connector pin
1. Secure jumper properly
1. Inspect for shorts
1. Reassemble device
