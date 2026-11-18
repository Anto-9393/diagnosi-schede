---
titolo: How To Fix iPhone 13 Pro No Power or No IMEI After Backglass Repair
tipo: fonte_esterna
url: https://repair.wiki/w/How_To_Fix_iPhone_13_Pro_No_Power_or_No_IMEI_After_Backglass_Repair
cronologia: https://repair.wiki/w/How_To_Fix_iPhone_13_Pro_No_Power_or_No_IMEI_After_Backglass_Repair?action=history
revisione: '2025-12-03T06:39:26Z'
categorie: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# How To Fix iPhone 13 Pro No Power or No IMEI After Backglass Repair

> Fonte: [How To Fix iPhone 13 Pro No Power or No IMEI After Backglass Repair — repair.wiki](https://repair.wiki/w/How_To_Fix_iPhone_13_Pro_No_Power_or_No_IMEI_After_Backglass_Repair), CC BY-SA 3.0. Autori: vedi cronologia.

## Problem description
After back-glass replacement, the device may show:

- No IMEI
- No modem firmware
- No cellular service
- Device completely dead (no power)

This increasingly common failure happens when shops use back-glass cracking tool on the baseband zone of the sandwich logic board.

## Symptoms
- “No IMEI” in Settings > General > About
- “Modem Firmware: N/A”
- High current jump on DCPS
- If the device has been restored with baseband issues, you will have to restore it again after fixing the baseband issue  
- If the phone is not wiped, do not restore it. Only perform an update. Restoring may result in the device getting stuck on the Hello/activation screen
- Full dead device

## Solution
### Diagnostic Steps
#### 1. Visual Inspection
- Inspect lower board under microscope
- Look for:
  - Hairline cracks on BB_PMU
  - Dent in the board from the backglass punch tool

(This is extremely common on iPhone 13 Pro / 14 Pro and Pro Max due to PMU location being very close to the back glass.)
----

#### 2. Software Diagnostics
If phone still powers on:

- *#06# → No IMEI
- Settings → Modem Firmware = N/A

----

#### 3. DC Power Supply Test
- Connect lower board only
- Press power:
  - High Boot Current jump -> Short

----

#### 4. Short Check
- Check around BB_PMU for shorts 

### Repair Steps
#### 1. Split the Logic Board (Sandwich Board Separation)
- Preheat to ~160–180°C
- Insert thin blades to separate upper & lower board

#### 2. Remove the Cracked BB_PMU
- Clean Underfill around BB_PMU (Be careful of components around BB_PMU)
- Apply flux
- Carefully lift BB_PMU
- Inspect for damaged pads
- Clean with wick + fresh solder

#### 3. Prepare & Reball New BB_PMU
- Use correct stencil for the model
- Inspect ball alignment carefully under microscope

#### 4. Install New BB_PMU
- Align orientation markers correctly
- Reflow until IC self-centers
- Allow cooldown
- Clean board and inspect joints

#### 5. Reconnect Upper & Lower Boards
- Align contacts
- Inspect under microscope for proper seam contact

#### 6. Final Testing
- Connect to DCPS → verify normal boot current
- Boot device:
  - IMEI should appear
  - “Modem Firmware” should show correct version
- Test cellular, Wi-Fi calling, and SIM detection
