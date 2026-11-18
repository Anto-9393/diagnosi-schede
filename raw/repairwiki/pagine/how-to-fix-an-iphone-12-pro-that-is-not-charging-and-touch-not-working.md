---
titolo: How To Fix an iPhone 12 Pro that is not charging and touch not working
tipo: fonte_esterna
url: https://repair.wiki/w/How_To_Fix_an_iPhone_12_Pro_that_is_not_charging_and_touch_not_working
cronologia: https://repair.wiki/w/How_To_Fix_an_iPhone_12_Pro_that_is_not_charging_and_touch_not_working?action=history
revisione: '2025-09-08T21:09:08Z'
categorie: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
figure:
- file: Iphone 12-pro usb ic.png
  didascalia: iPhone 12 / 12 Pro USB (Kraken) IC
- file: Iphone 12 mini usb ic.png
  didascalia: iPhone 12 Mini USB (Kraken) IC
- file: Iphone 12 pro max usb ic.png
  didascalia: iPhone 12 Pro Max USB (Kraken) IC
---

# How To Fix an iPhone 12 Pro that is not charging and touch not working

> Fonte: [How To Fix an iPhone 12 Pro that is not charging and touch not working — repair.wiki](https://repair.wiki/w/How_To_Fix_an_iPhone_12_Pro_that_is_not_charging_and_touch_not_working), CC BY-SA 3.0. Autori: vedi cronologia.

## Problem description
The iPhone 12 Pro may present with charging issues and/or loss of touch functionality. This is often linked to failure of the USB IC, also known as the Kraken IC.

The failure is commonly triggered by use of aftermarket or poor-quality chargers, though the IC may also fail spontaneously.

## Symptoms
- iPhone does not charge.
- No response when connecting to charger.
- Touchscreen not working.
- Device powers on while using DCPS, but fails to detect USB connection.
- May show unusual current draw on DCPS when attempting to boot.

## Diagnostic Steps
1. Test with Known Good Parts
1. * Try a known good charging port flex and battery.
1. * If issue persists, suspect board-level fault.
1. Visual Inspection
1. * Check for board-level damage, corrosion, or signs of liquid ingress near USB/charging IC area
1. DC Power Supply Test
1. * Connect device to DCPS.
1. * If current draw is abnormal (irregular spike when prompting to boot) → likely Kraken IC issue.

## Repair Steps
1. Board Access
1. * Remove logic board carefully.
1. * Split the sandwich layer.
1. * Isolate charging IC area (Kraken).
1. Preparation
1. * Apply flux around Kraken IC.
1. * Use hot air station with controlled airflow & temperature.
1. IC Replacement
1. * Remove faulty Kraken IC.
1. * Clean pads with solder wick and flux.
1. * Reball or use new IC.
1. * Align and reflow replacement Kraken IC.
1. Testing
1. * Reassemble device.
1. * Connect to charger → check charging function.
1. * Verify touch response is fully restored.
