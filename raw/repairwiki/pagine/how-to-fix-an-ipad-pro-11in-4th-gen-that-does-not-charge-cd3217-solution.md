---
titolo: How To Fix an iPad Pro 11in 4th Gen That Does Not Charge, CD3217 Solution
tipo: fonte_esterna
url: https://repair.wiki/w/How_To_Fix_an_iPad_Pro_11in_4th_Gen_That_Does_Not_Charge%2C_CD3217_Solution
cronologia: https://repair.wiki/w/How_To_Fix_an_iPad_Pro_11in_4th_Gen_That_Does_Not_Charge%2C_CD3217_Solution?action=history
revisione: '2024-02-04T13:59:31Z'
categorie: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
figure:
- file: IPad Pro 11in 4th Gen - Not Charging.png
  didascalia: iPad Pro 11in 4th Gen - Not Charging properly. It is only showing 5V
    charging, instead of 15V
- file: IPad Pro 11in 4th Gen - CD3217.png
  didascalia: iPad Pro 11in 4th Gen - CD3217 & it's paired ROM location & where to
    check for shorts.
- file: IPad Pro 11in 4th Gen - Charging Properly.png
  didascalia: iPad Pro 11in 4th Gen - Charging properly after CD3217 and ROM Replacement
---

# How To Fix an iPad Pro 11in 4th Gen That Does Not Charge, CD3217 Solution

> Fonte: [How To Fix an iPad Pro 11in 4th Gen That Does Not Charge, CD3217 Solution — repair.wiki](https://repair.wiki/w/How_To_Fix_an_iPad_Pro_11in_4th_Gen_That_Does_Not_Charge%2C_CD3217_Solution), CC BY-SA 3.0. Autori: vedi cronologia.

## Problem Description
iPad Pro 11in, 4th Generation will not charge. This no charging issue will cause the iPad to appear to have no power unless you are testing using a fully charged battery or power supply.
This issue is normally caused by a faulty CD3217 charging IC. When replacing these components it is important that you use a matching CD3217 chip from a donor motherboard and you will need to swap over the paired ROM chip (U3890- is the ROM chip on this specific model) 

This problem can apply to these models:

- A2759
- A2761
- A2435
- A2762

## Symptoms
Typically these symptoms will include the iPad not charging, the device may appear to have no power if your battery is depleted. If your battery still has some charge left you will not see a charging symbol when the charger is plugged in and the battery percentage will not rise. 

Using a USB meter you may encounter the following readings 5V 0.620A

With a faulty CD3217, the iPad will remain stuck at 5V, indicating there's a problem. Otherwise, it should be charging at the standard 15V. 

## Solution
### Diagnostic Steps
- First, we must determine that we are dealing with a charging issue and rule out the possibility of a no power issue. (using a charged battery or booting from a power supply) 
- Next, we can rule out a faulty charging port by testing with a good known part
- Diode mode around CD3217 checking for any shorted components. 

Mainly focusing on the 3 large capacitors next to the chip

- PP_LDO_CORE
- PP3V3_ACE_LDO (Typically the shorted line)
- PP3V3_S2_ACE

If these components are reading short, you know you have a faulty CD2317 charging IC and located your problem. 

### Repair Steps
Now that you have identified the faulty component, you will need to remove the faulty CD3217 and check the area for shorts with the chip removed.

If all shorts have been cleared then we will proceed to locating a replacement chip. 

These chips can be found on similar iPad Pro model boards with USB C. 

Along with the CD3217 chip, you will also need to transfer over the paired ROM chip from the donor motherboard. (without swapping over this second chip your new charging IC will not function) 

It is important that you use the ROM chip from the exact board you took the CD3217 from. In this example the ROM chip was U3890 (on most boards this chip will be labeled as 8NXXXX) 

For example 8N150, 8N030, etc.
