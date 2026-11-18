---
titolo: How To Fix iPhone 7 That Has No Backlight or Dark Spot On Screen
tipo: fonte_esterna
url: https://repair.wiki/w/How_To_Fix_iPhone_7_That_Has_No_Backlight_or_Dark_Spot_On_Screen
cronologia: https://repair.wiki/w/How_To_Fix_iPhone_7_That_Has_No_Backlight_or_Dark_Spot_On_Screen?action=history
revisione: '2024-01-22T08:44:19Z'
categorie: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
figure:
- file: IP7 No Backlight.png
  didascalia: ''
- file: Placeholder image.jpg
  didascalia: Example image (Figure 1) -- No image yet. Help expand this page by uploading
    it!
---

# How To Fix iPhone 7 That Has No Backlight or Dark Spot On Screen

> Fonte: [How To Fix iPhone 7 That Has No Backlight or Dark Spot On Screen — repair.wiki](https://repair.wiki/w/How_To_Fix_iPhone_7_That_Has_No_Backlight_or_Dark_Spot_On_Screen), CC BY-SA 3.0. Autori: vedi cronologia.

## Problem description
iPhone 7 with a dark screen, where you can barely see anything on the screen but you can see an image.

Or if you have a dark spot on the corner of the screen

## Symptoms
- Screen is dark
- You can see an image but no light coming from screen
- There's a dark spot on the corner

## Solution
### Diagnostic Steps
### You'll want to check these first to confirm you have a board issue:
- Get a known good screen. Helps validate that you have a board issue.
- Check USB Charging Current. If an iPhone shows proper charging current (1A via USB or more), then most likely the device is alive.
- Listen to for any sounds or vibration. Helps confirm if the phone powers on.
- Turn off the phone, then plug in the charger and use a flashlight onto the center of the screen, to look for the Apple logo  This helps confirm you are getting image, but no backlight.
- Check for water damage. Often times, the backlight circuit gets hit the hardest in water damage cases.
### Repair Steps
In most cases, no backlight is caused by blown filters on the backlight circuit.

Most commonly it's due to these Filters

**iPhone 7**
- FL3903
- FL3901
- FL3902
**iPhone 7 Plus**
- FL3901
- FL4601
- FL3903
- FL4602
- FL3902
You'll need to use Diode mode on your multimeter to find the blown filter. (see video for the full process of diagnosing the backlight: https://www.youtube.com/watch?v=K-FFSMiHXPw)

Since backlight comes from the LCD connector, this is the connector you want to check the diode mode readings. Essentially, you're comparing the diode mode values of a known good board vs your problematic board. Most boardview software, like ZXW, will provide the known good diode mode values and you can use that as reference. Expect to see a small ±5-10% variance of what you get.

With a backlight issue, you should find a pin on the LCD connector to read OL, when it should be giving you a diode mode reading. This line with the OL is what you want to investigate further.

These are the lines to expect to find an issue:
- PP_LCM_BL_CAT1_CONN
- PP_LCM_BL_ANODE_CONN
- PP_LCM_BL_CAT2_CONN
- PP_LCM_BL34_CAT1_CONN (iPhone 7 Plus only)
- PP_LCM_BL34_ANODE_CONN (iPhone 7 Plus only)
- PP_LCM_BL34_CAT2_CONN (iPhone 7 Plus only)
Also, sometimes, you can get lucky and visually spot the blown filter, but it's recommended to use your multimeter to confirm it's bad, as well as check the rest are good.
- A good/working filter will have continuity across it and will have the same diode mode reading on both sides
- A blown filter will **not** have continuity across it. In diode mode, you'll find one side has a diode mode reading and the other side will have either OL or a reading that is a larger value than what it should be.
The replacement filter should be the same value of the original. You can see the values in the schematic or boardview software like ZXW.

**Please Note:** Never use a jumper wire as a replacement for a filter. This can permanently damage the phone if a surge in current occurs and there's no filter to protect the circuit.

Once you replace the filter, check that you be able to diode mode the connector again and find that the pin that was reading OL, is now giving you a proper reading.

Now you can test again and confirm the backlight is working again.
