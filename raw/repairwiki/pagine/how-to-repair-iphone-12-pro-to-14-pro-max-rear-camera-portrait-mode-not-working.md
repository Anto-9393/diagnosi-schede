---
titolo: How to repair iPhone 12 pro to 14 pro max rear camera portrait mode not working
tipo: fonte_esterna
url: https://repair.wiki/w/How_to_repair_iPhone_12_pro_to_14_pro_max_rear_camera_portrait_mode_not_working
cronologia: https://repair.wiki/w/How_to_repair_iPhone_12_pro_to_14_pro_max_rear_camera_portrait_mode_not_working?action=history
revisione: '2025-08-30T18:05:40Z'
categorie: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
figure:
- file: Portrait-mode-issue.gif
  didascalia: Rear cam portrait mode not working due to replacement with different
    non-programmed sensor.
- file: Jcid brushing option.png
  didascalia: Brushing unbind in JCID Repair Assistant software.
---

# How to repair iPhone 12 pro to 14 pro max rear camera portrait mode not working

> Fonte: [How to repair iPhone 12 pro to 14 pro max rear camera portrait mode not working — repair.wiki](https://repair.wiki/w/How_to_repair_iPhone_12_pro_to_14_pro_max_rear_camera_portrait_mode_not_working), CC BY-SA 3.0. Autori: vedi cronologia.

Note: This process applies to iPhone 12 Pro  through iPhone 14 Pro Max (All the Pro Models).

## Problem description
On iPhone 12 Pro  through iPhone 14 Pro Max (Pro / Pro Max Series), the LiDAR sensor can stop working due to:

- Drop or physical damage.
- Water/moisture damage affecting the sensor or flex.
- Technician error - failing to transfer the original paired LiDAR sensor when replacing the rear housing. 

## Symptoms
- Measure app not working
- Cannot use AR features relying on LiDAR
- In camera app → Portrait mode fails (see fig. 1)
- Sensor missing from diagnostics

## Diagnostic Steps
1. Open the Measure app → confirm LiDAR cannot detect objects.
1. Open portrait mode on rear camera → Confirm it doesn't work.
1. Check if rear housing was replaced previously → ask customer .
1. If still non-functional → proceed to replacement + reprogramming.

## Repair Steps
1. Disassembly:  Remove display, disconnect battery. Remove rear camera module. Remove shield covering the LiDAR sensor → take out faulty sensor.
1. Brushing unbind & Backing up data: Reconnect display & battery. Connect iPhone to PC. Launch JC Repair Assistant → Read phone. Select Brushing.Import firmware → Flash device. If stuck in recovery mode → repeat flash in 3uTools. After brushing unbind and flash is complete, LiDAR sensor data is backed up to the cloud automatically.
1. Programming JCID LiDAR sensor: Connect JCID Programmable LiDAR sensor to programmer and write the correct data matching the phone.
1. Reassembly:  Install the programmed LiDAR into the iPhone. Reinstall rear camera + shields. Reconnect all flexes and battery.
1. Verification: Boot iPhone. Test Portrait mode functions in camera. Open Measure app → confirm proper distance detection.
