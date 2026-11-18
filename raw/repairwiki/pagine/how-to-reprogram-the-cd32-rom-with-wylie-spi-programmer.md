---
titolo: How to reprogram the CD32 ROM with Wylie SPI Programmer
tipo: fonte_esterna
url: https://repair.wiki/w/How_to_reprogram_the_CD32_ROM_with_Wylie_SPI_Programmer
cronologia: https://repair.wiki/w/How_to_reprogram_the_CD32_ROM_with_Wylie_SPI_Programmer?action=history
revisione: '2026-01-01T22:20:41Z'
categorie: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
figure:
- file: Wylie.png
  didascalia: ''
- file: Program to run.png
  didascalia: ''
- file: Pin 1.png
  didascalia: ''
- file: Detect.png
  didascalia: ''
- file: Chip detected.png
  didascalia: ''
- file: Chip info.png
  didascalia: ''
- file: Rom Loaded.png
  didascalia: ''
- file: Write.png
  didascalia: ''
- file: Write ok.png
  didascalia: ''
---

# How to reprogram the CD32 ROM with Wylie SPI Programmer

> Fonte: [How to reprogram the CD32 ROM with Wylie SPI Programmer — repair.wiki](https://repair.wiki/w/How_to_reprogram_the_CD32_ROM_with_Wylie_SPI_Programmer), CC BY-SA 3.0. Autori: vedi cronologia.

## Problem description
Some iPads using the CD3217 USB-C controller IC can develop a no charge, no boot, or low voltage negotiation issue. This typically happens after liquid damage or a power surge. Replacing the CD3217 alone doesn’t fix the issue, because the connected ROM IC is often corrupted or damaged.

This guide is an alternative method to flash the CD3217 ROM. It is **not** a guide on how to repair an iPad with USB-C that does not charge.

See this guide for more info: How To Program ROM Chip for iPads with CD3217

## Guide
In this guide we will use a cheaper alternative to the JCID method, this device can be found for around 15€ in websites like Aliexpress.

After downloading the file unpack the RAR and run this program.
To read the ROM, you must first desolder the old ROM from the iPad/iPhone and solder it onto the programmer.

Keep in mind that you must match **Pin 1** correctly. If you solder the IC backwards, you may permanently damage it.

After having the chip soldered, we are ready to connect the programmer to the computer.

Connect the programmer to the computer, and in the software, click **Detect**. A small window should appear. (If Nothing happens it may be a bad solder connection or a Dead ROM IC)

Click on Select 

After selecting the chip, a lot of information about it will be displayed. This is a good sign.

Download the correct ROM for your device from the link above.

After downloading the file, load it into the program.

Click **Open File** and select your file. After the file is loaded, the program will display a message similar to this:

Then Click on Write 

After the program finishes writing, which should only take a few seconds, it will show **100%**.

After writing is complete, disconnect the programmer from the computer.

Desolder the IC and solder it back onto the motherboard.

After that, the iPad should (hopefully) charge normally again.

And enjoy the fact that you just avoided paying 300€ for something that’s basically the same—just packaged in a fancy device.
