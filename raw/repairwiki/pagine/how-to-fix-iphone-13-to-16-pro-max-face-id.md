---
titolo: How to fix iPhone 13 to 16 pro max Face ID
tipo: fonte_esterna
url: https://repair.wiki/w/How_to_fix_iPhone_13_to_16_pro_max_Face_ID
cronologia: https://repair.wiki/w/How_to_fix_iPhone_13_to_16_pro_max_Face_ID?action=history
revisione: '2025-08-25T21:22:49Z'
categorie: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
figure:
- file: Unable-to-setup-faceid.png
  didascalia: Unable to setup Face ID
- file: Abnormal-faced.png
  didascalia: Face ID showing Fused
- file: Normal-faceid.png
  didascalia: Face ID Normal
- file: Face-id-success.png
  didascalia: Face ID successfully setup
---

# How to fix iPhone 13 to 16 pro max Face ID

> Fonte: [How to fix iPhone 13 to 16 pro max Face ID — repair.wiki](https://repair.wiki/w/How_to_fix_iPhone_13_to_16_pro_max_Face_ID), CC BY-SA 3.0. Autori: vedi cronologia.

## Problem description
Face ID stops working because the TrueDepth sensor module is shorted.

This is most often caused by:

- Water damage
- Accidental damage while the device is open during other repairs (e.g., display replacement, battery replacement etc.)

## Symptoms
- Settings → About → Parts & Service History → “Issue with Face ID detected”
- Unable to set up Face ID
- Face ID unavailable

## Diagnostic Steps
1. Attempt to set up Face ID in Settings → Face ID & Passcode.
1. Confirm history of water damage or previous repair work with the customer.
1. Inspect the TrueDepth module for visible damage or corrosion.

## Repair Steps
1. Open the iPhone and disconnect/remove the TrueDepth camera module.
1. Power on the phone without the module connected and connect it to a PC.
1. Open JC Repair Assistant on the PC and connect a JC V1S Pro or V1SE programmer. [You will need [13-16 Series Face ID Activation / Read & Write Adaptor](https://www.diyfixtool.com/products/jcid-iphone-13-16-face-id-repair-tag-on-fpc-activation-board?srsltid=AfmBOoqwf36a-mVB3p8K7Fh2yab9pB1hK2pTHb8EGty47QR_I6QD_2bo&variant=47556754473189)]
1. Perform a cloud backup of the TrueDepth module data using JC software.
1. Test TrueDepth module and confirm module fuses.
1. Click Activate and wait until the process completes.
1. Connect the respective Tag-on flex cable to the JC programmer.
1. Write the corresponding device Face ID data onto the flex from the backup.
1. Verify that the flex shows the original TrueDepth data.
1. Connect the Tag-on flex to the TrueDepth module and recheck in JC software/programmer: Should now show “NORMAL” instead of “FUSED”.
1. Fold the Tag-on flex according to your iPhone model (follow JC’s reference videos).
1. Reinstall the TrueDepth module with the Tag-on flex attached.
1. Power on the phone and verify that Face ID is fully functional.
