---
titolo: IPhone 15 Pro Max Dead and Not Charging
tipo: fonte_esterna
url: https://repair.wiki/w/IPhone_15_Pro_Max_Dead_and_Not_Charging
cronologia: https://repair.wiki/w/IPhone_15_Pro_Max_Dead_and_Not_Charging?action=history
revisione: '2025-09-08T21:13:32Z'
categorie: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
figure:
- file: 15pro-dcps.png
  didascalia: Figure 1 - iPhone 15 Pro Max DCPS reading before prompt to boot example
- file: Charging-ic-thermal.png
  didascalia: Figure 2 - Example of charging IC heating up under thermal camera
- file: Ip-15p-charging-ic.png
  didascalia: Figure 3 - iPhone 15 Pro / Pro Max Charging IC (International Variant)
- file: Ip-15p-charging-ic-usa.png
  didascalia: Figure 4 - iPhone 15 Pro/Max Charging IC (USA Variant)
---

# IPhone 15 Pro Max Dead and Not Charging

> Fonte: [IPhone 15 Pro Max Dead and Not Charging — repair.wiki](https://repair.wiki/w/IPhone_15_Pro_Max_Dead_and_Not_Charging), CC BY-SA 3.0. Autori: vedi cronologia.

## Problem description
iPhone 15 Pro Max appears dead and will not turn on or charge when on battery. When connected to a DC Power Supply (DCPS), the device consumes 0.105-0.130 A of current before prompt to boot and boots normally after prompt. Thermal imaging shows the charging IC heating abnormally. 
## Symptoms
- Device appears dead, no response to power button or charger.
- No charging indication on screen.
- Device only boots when connected to DCPS.
- DCPS reading: 0.105-0.130 A before prompt to boot.
- Charging IC visibly heats up on a thermal camera.

## Diagnostic Steps
1. Connect iPhone to DC Power Supply; check current draw:
1. * 0.105-0.130 A pre-boot draw indicates boot sequence initiates.
1. Attempt to prompt the phone to boot using power button.
1. Observe thermal camera or use Rosin to detect heat source:
1. * Charging IC heating confirms failure.

## Repair Steps
1. Disassemble Device:
1. * Remove display and disconnect battery.
1. Board-Level Work:
1. * Remove motherboard from housing.
1. * Split Layers
1. * Isolate charging IC area (use thermal shielding).
1. Remove Faulty Charging IC:
1. * Use hot air + flux, carefully lift the IC.
1. Clean and Prepare Pads:
1. * Wick old solder and inspect for pad damage.
1. Install New Charging IC:
1. * Reball, align, and install.
1. Test Booting and Charging:
1. * Connect to DCPS, verify normal reading before prompt to boot.
1. * Check battery charging functionality.
1. Reassemble Device:
1. * Confirm full functionality before sealing.
