---
titolo: How To Fix iPhone XS or Max Black Screen After Apple Logo
tipo: fonte_esterna
url: https://repair.wiki/w/How_To_Fix_iPhone_XS_or_Max_Black_Screen_After_Apple_Logo
cronologia: https://repair.wiki/w/How_To_Fix_iPhone_XS_or_Max_Black_Screen_After_Apple_Logo?action=history
revisione: '2025-11-24T06:09:06Z'
categorie: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
figure:
- file: NAND XS.png
  didascalia: iPhone XS/XS MAX NAND
- file: BACKUP SYSCFG.png
  didascalia: '[[File:SELECT GENSYSCFG.png'
- file: WRITE OGSYSCF.png
  didascalia: ''
- file: WRITE SYSCFG.png
  didascalia: ''
---

# How To Fix iPhone XS or Max Black Screen After Apple Logo

> Fonte: [How To Fix iPhone XS or Max Black Screen After Apple Logo — repair.wiki](https://repair.wiki/w/How_To_Fix_iPhone_XS_or_Max_Black_Screen_After_Apple_Logo), CC BY-SA 3.0. Autori: vedi cronologia.

## Problem description
iPhone XS Max boots, shows Apple logo, but when the system hands off to SpringBoard, the screen goes black.

Phone stays ON (touch works, device detected by PC), but no image after logo.

This issue is caused by corrupted System Configuration inside NAND.

## Symptoms
- Apple logo appears normally.
- When boot continues → screen goes black.
- Device still functions:
  - Touch is active
  - Device detected by PC/3uTools
  - Fresh restored device still shows same issue
- Secondary display symptoms:
  - Chinese LCD/OLED → same behavior
- Not related to upper board, filters, or any DISPLAY_POWER/DISPLAY_DATA line.

## Solution
]]

### Diagnostic Steps
#### 1. Confirm Display Symptom
- Test with known-good aftermarket LCD (cheap Chinese LCD).
- Apple logo appears → disappears → screen black.

#### 2. Confirm Device Boots
Connect to PC / 3uTools:

- Device enters activation screen internally.
- Touch inputs register.
- Confirms phone is alive, only image fails after kernel handoff.

#### 3. Inspect Board
- Separate XS Max sandwich board.
- Clean underfill around display filters.
- Check PP3V0_DISPLAY and other display-related resistances — all normal.

### Repair Steps
#### 1. Remove NAND
- Separate upper board from RF board.
- Remove NAND.

#### 2. Read NAND
Use JC BGA110 adapter:

- Perform full read.
- Extract device-specific fields (Serial Number, BT Mac & WiFi Mac Address).

#### 3. Prepare Clean Image
Inside programmer software:

- Select "iPhone XS or XS MAX" as per your device.
- Paste original essential data (SN, WiFi/Bluetooth MAC).
- Do NOT change storage capacity.

#### 4. Write NAND
- Write generated clean configuration.
- Verify write success.

#### 5. Reball NAND
- Reball original IC (or replace with same capacity).
- Clean pads, apply flux, align properly.

#### 6. Solder NAND Back
- Same careful angle as removal.
- Avoid overheating CPU.

#### 7. Restore Device
- Use board tester or reassembled phone (bottom board + battery + screen).
- Connect to PC → full IPSW restore.

#### 8. Verify Fix
- Device should restore successfully.
- Full image/function restored.
