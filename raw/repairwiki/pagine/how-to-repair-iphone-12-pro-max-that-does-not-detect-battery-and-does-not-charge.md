---
titolo: How to Repair iPhone 12 Pro Max that does not detect battery and does not
  charge
tipo: fonte_esterna
url: https://repair.wiki/w/How_to_Repair_iPhone_12_Pro_Max_that_does_not_detect_battery_and_does_not_charge
cronologia: https://repair.wiki/w/How_to_Repair_iPhone_12_Pro_Max_that_does_not_detect_battery_and_does_not_charge?action=history
revisione: '2025-09-26T02:35:04Z'
categorie: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# How to Repair iPhone 12 Pro Max that does not detect battery and does not charge

> Fonte: [How to Repair iPhone 12 Pro Max that does not detect battery and does not charge — repair.wiki](https://repair.wiki/w/How_to_Repair_iPhone_12_Pro_Max_that_does_not_detect_battery_and_does_not_charge), CC BY-SA 3.0. Autori: vedi cronologia.

## Problem Description
An iPhone 12 Pro Max shows no charging and battery not detected, even after replacing the charging port, using a new cable and charging cable/brick.

- Battery connector voltage (BATT_VCC) reads 3.7–4.0 V (normal).
- Charging IC and USB IC measure fine.
- Battery FPC diode readings normal.

Root cause: low I²C voltage (0.2V instead of 1.8V) on SDA/SCL pins.

Tracing these lines leads to U2470, the battery data level translator IC.

Replacing U2470 restores I²C communication, allowing the phone to detect the battery and charge normally.
----

## Symptoms
- iPhone does not charge or power from the battery.
- Battery percentage not displayed, device may only run on DCPS.
- No corrosion or damage visible on battery connector area.

----

## Diagnostic Steps
1. Measure Battery Connector Voltage
1. * BATT_VCC → 3.7–4.0V = ✅ Good
1. * If missing, diagnose power path first.
1. Check Battery FPC Diode Mode
1. * All lines read within normal range = ✅
1. Measure I²C Lines (SCL/SDA)
1. * Expected: ~1.8 V
1. * Observed: ~0.2 V → indicates line is being pulled low.
1. Trace I²C Lines to U2470
1. * Locate U2470 (near battery FPC).
1. * Check for damage/corrosion.
1. * If clean, suspect internal short or failure pulling bus low.

----

## Repair Steps
### 1. Remove Faulty U2470
- Use hot air station to remove U2470.
- Clean pads, inspect for shorts.

### 2. Replace U2470
- Install a new/reballed U2470.
- Align carefully.

### 3. Verify Voltages
- After installation, re-check I²C voltage at battery FPC:
  - Should now be ~1.8V.

### 4. Final Test
- Connect battery, boot phone.
- Confirm battery is detected, percentage shows, and device charges.
