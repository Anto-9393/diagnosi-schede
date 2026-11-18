---
titolo: How To Fix an iPhone 14 that is shows temperature warning and does not charge
tipo: fonte_esterna
url: https://repair.wiki/w/How_To_Fix_an_iPhone_14_that_is_shows_temperature_warning_and_does_not_charge
cronologia: https://repair.wiki/w/How_To_Fix_an_iPhone_14_that_is_shows_temperature_warning_and_does_not_charge?action=history
revisione: '2025-09-08T22:23:30Z'
categorie: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
figure:
- file: 1A-before-boot.png
  didascalia: Figure 1 - Example of 1A of consumption before prompt to boot
- file: Shorted cap boardview.png
  didascalia: Figure 3 - Shorted Capacitor on SPKRAMP_TOP_VBOOST line shown on Boardview
- file: Shorted cap.png
  didascalia: Figure 2 - Shorted capacitor on SPKRAMP_TOP_VBOOST line
- file: Iphone temp warning.png
  didascalia: Figure 1 - Example of Temperature warning on iPhone
---

# How To Fix an iPhone 14 that is shows temperature warning and does not charge

> Fonte: [How To Fix an iPhone 14 that is shows temperature warning and does not charge — repair.wiki](https://repair.wiki/w/How_To_Fix_an_iPhone_14_that_is_shows_temperature_warning_and_does_not_charge), CC BY-SA 3.0. Autori: vedi cronologia.

## Problem description
iPhone 14 shows temperature warning when powered on. Device charges normally while powered off but does not charge when turned on. Severe overheating occurs once the phone boots.

## Symptoms
- Temperature warning appears after boot.
- Phone charges when powered off, but not when powered on.
- Device overheats rapidly while powered on.
- On DCPS: pre-boot draw ~1A before prompt to boot, then device boots normally.

## Diagnostic Steps
1. Connect to DCPS and observe current draw – confirm abnormal 1A draw before prompt to boot.
1. Check with thermal camera – locate rapid heating component.
1. Identify shorted capacitor on SPKRAMP_TOP_VBOOST line.
## Repair Steps
1. Remove motherboard from housing, split layer and perform resistance measurement on SPKRAMP_TOP_VBOOST rail.
1. Confirm low resistance indicating short.
1. Identify and remove the shorted capacitor from the rail.
1. Recheck resistance to confirm short is cleared.
1. Reassemble device and test boot with DCPS – ensure pre-boot current draw normalizes.
1. Power on phone and check charging behavior – should now charge normally without temperature warning.
1. Verify device stability under load (charging + usage) before closing repair.
