---
titolo: How To Repair iPhone 13 to 16 pro max Proximity sensor not working
tipo: fonte_esterna
url: https://repair.wiki/w/How_To_Repair_iPhone_13_to_16_pro_max_Proximity_sensor_not_working
cronologia: https://repair.wiki/w/How_To_Repair_iPhone_13_to_16_pro_max_Proximity_sensor_not_working?action=history
revisione: '2025-09-02T05:34:24Z'
categorie: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# How To Repair iPhone 13 to 16 pro max Proximity sensor not working

> Fonte: [How To Repair iPhone 13 to 16 pro max Proximity sensor not working — repair.wiki](https://repair.wiki/w/How_To_Repair_iPhone_13_to_16_pro_max_Proximity_sensor_not_working), CC BY-SA 3.0. Autori: vedi cronologia.

## Problem description
Front proximity and ambient light sensor failure after water damage or improper flex replacement. Replacing the flex with a non-programmed or aftermarket part removes auto-brightness and proximity functionality.

## Symptoms
- Auto-brightness toggle missing in Settings.
- Screen does not turn off during calls.
- History of water damage or prior sensor replacement.

## Diagnostic Steps
1. Confirm device history (liquid damage, part replacement).
1. Test proximity function during calls.
1. Check Settings > Accessibility > Display & Text size > auto-brightness toggle.
1. Inspect flex under microscope for corrosion or damage.
1. Confirm issue is not caused by display/logic board.

## Repair Steps
#### 1. Prepare Tools & Firmware
- Download the correct IPSW firmware for your iPhone model from [ipsw.me](https://ipsw.me) or [3uTools](https://www.3u.com).
- Install JCID Repair Assistant and 3uTools on your computer.
- Have a JCID V1SE/V1S Pro programmer and JCID photosensitive board ready.

----

#### 2. Perform Brushing & Unbind
This step unbinds factory data, preparing the device to pair  a new JCID sensor.

1. Connect the iPhone to your computer and open JCID Repair Assistant.
1. Click Read Phone to detect the device.
1. Select Brushing mode.
1. Tick both options under Brushing Options to enable unbinding.
1. Click Start Flashing & Unbinding and select your downloaded IPSW firmware.
1. Let JCID complete the brushing/unbind process.
1. Once done, the iPhone will be in Recovery Mode (expected).
1. Open 3uTools, flash the same firmware using a  Flash.

----

#### 3. Program the New JCID Sensor
1. Connect your JCID V1SE or V1S Pro programmer to your PC.
1. Attach the JCID photosensitive board and the new JCID sensor.
1. In JCID software, click 'Start testing' to verify the new sensor is functional.
1. Click 'Activate FPC' to pair the new JCID sensor with the iPhone.
1. Once activation is completed, ECID should match in both columns.

----

#### 4. Install & Test
1. Install the newly programmed sensor back into the iPhone.
1. Reassemble the device carefully.
1. Boot up the iPhone and test proximity sensor and auto-brightness functionality.
