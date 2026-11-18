---
titolo: IPad Pro 9.7 Not Powering on, 2a or Higher Power Draw before Prompt to Boot
tipo: fonte_esterna
url: https://repair.wiki/w/IPad_Pro_9.7_Not_Powering_on%2C_2a_or_Higher_Power_Draw_before_Prompt_to_Boot
cronologia: https://repair.wiki/w/IPad_Pro_9.7_Not_Powering_on%2C_2a_or_Higher_Power_Draw_before_Prompt_to_Boot?action=history
revisione: '2025-07-20T19:50:12Z'
categorie: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
figure:
- file: 2+Amps.gif
  didascalia: ''
- file: IPad Pro 9.7 Example.png
  didascalia: iPad Pro 9.7 Example
- file: Water by a chip.png
  didascalia: Water by a chip
---

# IPad Pro 9.7 Not Powering on, 2a or Higher Power Draw before Prompt to Boot

> Fonte: [IPad Pro 9.7 Not Powering on, 2a or Higher Power Draw before Prompt to Boot — repair.wiki](https://repair.wiki/w/IPad_Pro_9.7_Not_Powering_on%2C_2a_or_Higher_Power_Draw_before_Prompt_to_Boot), CC BY-SA 3.0. Autori: vedi cronologia.

## Problem description
iPad Pro 9.7 not powering on with 2a or higher power draw from DCPS before prompt to boot.

## Solution
If this iPad draws any current before prompt to boot it means there is a short on the motherboard.

The first step it to inspect the motherboard for any blown components and water damage.

If there is no water damage, is is most likely a shorted component on any of the below lines:

- **PP_VCC_MAIN** 
- **PP_BATT_VCC** 
- **PPSTROBE_LX**
- **PPVCC_HIGH**

The most common line to have a short is VCC_MAIN.

To detect the short you'll need to inject voltage (4 V / 2 A) directly into the line you measured as short and use freeze spray (see here https://youtu.be/3MtLSQJvQxI) or thermal camera (see here: https://youtu.be/fkd4iDjgfvc) to spot the capacitor that is shorted.

On this iPad when there is a short on VCC_MAIN U8500 will also get hot dont assume immediately that U8500 is the cause look around the board for other hot spots.

If the Short is on a Chip you need to replace that component.

If the Short is on decoupling capacitor you can remove it from the board most of the times the capacitance wont drop that much to affect the function of the device.

If there is water damage, corrosion may be the cause of the short sometimes cleaning the corrosion is enough to clear the short however if you see signs of water by a chip it probably means there is water under the IC and you have remove it clean the corrosion aand reball or replace the Chip.

After removing the shorted component you can take a diode reading of the line a healthy VCC Main should have a vault between 0.400 and 0.500.
