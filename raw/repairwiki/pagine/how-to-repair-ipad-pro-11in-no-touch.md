---
titolo: How To Repair iPad Pro 11in No Touch
tipo: fonte_esterna
url: https://repair.wiki/w/How_To_Repair_iPad_Pro_11in_No_Touch
cronologia: https://repair.wiki/w/How_To_Repair_iPad_Pro_11in_No_Touch?action=history
revisione: '2025-11-12T15:13:53Z'
categorie: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# How To Repair iPad Pro 11in No Touch

> Fonte: [How To Repair iPad Pro 11in No Touch — repair.wiki](https://repair.wiki/w/How_To_Repair_iPad_Pro_11in_No_Touch), CC BY-SA 3.0. Autori: vedi cronologia.

## Problem description
The iPad Pro 11” (2nd Gen, 2020) may power on and display image normally, but touch does not respond at all. The issue can persist across multiple screen assemblies, leading to confusion during diagnosis.

## Symptoms
- Display image appears normal, but no touch response.
- Device powers and charges as expected.
- Replacing display assembly does not restore touch.
- PP1V5V0_TOUCH_LDO rail shows shorted to ground or a low resistance reading.
- No visible water or physical damage.

## Solution
Locate and remove the faulty capacitor(s) on the PP1V5V0_TOUCH_LDO rail near the Touch Controller IC. Replacing or removing the defective cap restores proper LDO voltage regulation and revives touch functionality.

### Diagnostic Steps
1. Visual Inspection

- Inspect the logic board area near the BCM15957 Touch Controller IC.
- Look for any burnt, cracked, or corroded capacitors.

2. Diode Mode Measurement

- Measure PP1V5V0_TOUCH_LDO in diode mode (red probe on ground).
- Normal reading ≈ 0.450–0.500V.
- Faulty board often reads ≈ 0.00V or a low value, suggesting a partial short or leakage on this line.

3. Voltage Measurement (Powered)

- Power the board and measure PP1V5V0_TOUCH_LDO.
- Expected voltage: ~1.5V.
- If lower or 0, isolate the faulty capacitor.

### Repair Steps
1. Preparation

- Remove logic board from housing.
- Shield off nearby components to prevent heat damage.

2. Component Isolation

- Using thermal camera, freeze spray or alcohol, identify the capacitor that warms up first on current injection (low voltage, ~1V).

3. Rework

- Remove the defective capacitor using hot air.
- Clean the area and check diode readings.
- Replace the faulty cap with an equivalent from donor board if available.

4. Testing

- Reassemble logic board, connect display, and test touch functionality.
