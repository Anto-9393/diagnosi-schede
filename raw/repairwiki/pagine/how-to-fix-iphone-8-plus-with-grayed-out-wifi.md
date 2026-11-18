---
titolo: How To Fix iPhone 8 Plus with Grayed Out WiFi
tipo: fonte_esterna
url: https://repair.wiki/w/How_To_Fix_iPhone_8_Plus_with_Grayed_Out_WiFi
cronologia: https://repair.wiki/w/How_To_Fix_iPhone_8_Plus_with_Grayed_Out_WiFi?action=history
revisione: '2024-02-04T10:24:35Z'
categorie: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# How To Fix iPhone 8 Plus with Grayed Out WiFi

> Fonte: [How To Fix iPhone 8 Plus with Grayed Out WiFi — repair.wiki](https://repair.wiki/w/How_To_Fix_iPhone_8_Plus_with_Grayed_Out_WiFi), CC BY-SA 3.0. Autori: vedi cronologia.

## Problem description
How to fix iPhone 8 Plus with grayed out wifi. This is most common on iPhone 8 Plus, not so much on iPhone 8, but still possible.

## Symptoms
- WiFi button is grayed out
- No WiFi at all
- You can't enable WiFi
- WiFi toggle button is grayed out in the settings
- WiFI button is not clickable in the control panel This means there is a board issue. It is not an antenna or flex issue, as they don't cause the button itself to be grayed out.

## Solution
- In most cases, there are ripped pads on the corner, under the WiFi (WLAN_W) chip. See Figure 1
- Pins 19, 20, 22 and 23 must be jumped to their respective traces.
- For Example: iPhone 8 Plus - 4 Jumper solution for Grayed Out WiFi
- Once the jumpers are in place, use UV mask to cover them, to prevent any shorting/bridging/movement
- Reball the original WiFi IC & place back.

**See full repair tutorial here: <nowiki>https://youtu.be/eVmKNJ7nsgI</nowiki>**

If the WiFi chip ends up having torn pads, you must replace the WiFi IC.

For this, you'll need to also unbind (aka unlock) the WiFi chip via the NAND.

The NAND is what has the paired info for the WiFi chip.

You can unlock the WiFi using the iRepair P10 using Purple Mode to reprogram the NAND & unpair the WiFi chip.

It is done via USB. No need to desolder the NAND.
