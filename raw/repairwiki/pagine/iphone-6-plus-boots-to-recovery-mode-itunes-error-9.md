---
titolo: IPhone 6 Plus Boots to recovery mode iTunes Error 9
tipo: fonte_esterna
url: https://repair.wiki/w/IPhone_6_Plus_Boots_to_recovery_mode_iTunes_Error_9
cronologia: https://repair.wiki/w/IPhone_6_Plus_Boots_to_recovery_mode_iTunes_Error_9?action=history
revisione: '2025-06-05T20:06:07Z'
categorie: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# IPhone 6 Plus Boots to recovery mode iTunes Error 9

> Fonte: [IPhone 6 Plus Boots to recovery mode iTunes Error 9 — repair.wiki](https://repair.wiki/w/IPhone_6_Plus_Boots_to_recovery_mode_iTunes_Error_9), CC BY-SA 3.0. Autori: vedi cronologia.

## Problem description
On the iPhone 6 Plus this error is usually a problem between the CPU and EEPROM (U0301)

## Symptoms
- The phone boots straight into recovery mode

- iTunes produces the error 9 when restoring the device

## Diagnostic Steps
In order to verify that in fact the issue is between the CPU and EEPROM we must take diode readings on two resistors, these two components are located under a shield, in order to reveal them you must remove a tiny bit of metal in the position of the image below.

The next step is to measure the two resistors in diode mode, they both must have a value of around 0.484, on some devices both lines will read bad and on some devices only one is faulty.

### Repair Steps
**This repair is really difficult and is not advised for people without experience please practice on a scrap board  first.**

These two lines go to the CPU and "easiest" way to fix it is by making a small hole in the CPU.

Start by removing the metal shield on top of the CPU.

Next we will make a small hole in the bottom left corner of the CPU, below is an image of the area that can be cut.

To make the hole there are two tools that can be used a X-Acto knife or a small precision tool like the Qianli DM360.

Do this process really slowly and if you want you can add some isopropyl alcohol to help clear the debris and you will also see your work better.

At some point you will arrive at some grey pads, this means that you're getting close, keep scraping really slowly.

After you scrape a little bit you will start to see the line inside the CPU, the two lines that we are after are these ones.

After locating these two lines stop scraping and use UV mask to cover everything in that area except those lines, like this:

After applying UV mask add solder to those two exposed pads.

Now you need to solder 2 jumoing wires from those 2 points to the resistors.

After soldering the wires check for a short on PP1V8_SDRAM you can do this on this cap.

After confirming there is no short, protect the jumping wires with UV mask, you can basically cover the hole you made.

After this, connect the iPhone to iTunes again and do a restore.

Don't forget to install the metal shield on top of the CPU.
