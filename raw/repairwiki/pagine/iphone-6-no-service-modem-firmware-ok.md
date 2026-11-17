---
titolo: IPhone 6 No Service Modem Firmware OK
tipo: fonte_esterna
url: https://repair.wiki/w/IPhone_6_No_Service_Modem_Firmware_OK
cronologia: https://repair.wiki/w/IPhone_6_No_Service_Modem_Firmware_OK?action=history
revisione: '2025-07-07T22:25:49Z'
categorie: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# IPhone 6 No Service Modem Firmware OK

> Fonte: [IPhone 6 No Service Modem Firmware OK — repair.wiki](https://repair.wiki/w/IPhone_6_No_Service_Modem_Firmware_OK), CC BY-SA 3.0. Autori: vedi cronologia.

## Problem description
The iPhone is unable get celular service

## Symptoms
- The iPhone is unable get celular service

## Solution
On the iPhone 6 this issue is ussualy caused by 2 broken pads under the Baseband CPU(V1 and U1)

### Diagnostic Steps
Confirming the fault go to settings and check if modem firmware is present if it is this means the Baseband PMU is working.

On the Dial app input the code ***#06#** a pop up window should show up with the IMEI of the iPhone.

Doing these steps confirms the fault is with the Baseband CPU
### Repair Steps
Diasamble the iPhone the Baseband CPU is located on the lower side of the motherboard under a EMI Shield, in order to acess the Baseband we have to remove this shield, on this part of the motherboard there is a lot of ground so it will take quite a bit of heat to remove it.

After removing the shield the next step is to focus on the baseband CPU, unlike modern iPhones the baseband CPU on the iPhone 6 is not underfield, while the board is still hot using your hot air gun desolder the Baseband CPU and put it a side **but dont lose it.**

While the board is hot from removing the Baseband add low melt solder to the pads on the motherboard then using solder wick clean the pads.

After cleaning the pads do a visual inspection it is common to remove a few pads in this process there are quite a few pads that are unused and come of easy. The pads with the color blue on the image bellow are fine if removed.

After completing your inspection lets focus on the V1 and U1 pads, these pads are common to break.

To repair the pads you need to do a small jump

First Scrape these points:

Then add some solder and solder a thing of wire like this 

Then after this is done you can add a bit of solder mask to the points you scrape like this:

After this is done you have to reball the Baseband CPU, you can not replace this component you have to reball it.

After reballing the Baseband solder the chip back on the board.

## Final Testing
After soldering the iPhone go to the dial app and insert once more the code *#06# and check for the pop up window with IMEI.

Insert a SIM card and make sure the iPhone is able to get service.

Make a phone call.

1.
