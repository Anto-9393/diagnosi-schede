---
titolo: IPhone 11 with half backlight on display
tipo: fonte_esterna
url: https://repair.wiki/w/IPhone_11_with_half_backlight_on_display
cronologia: https://repair.wiki/w/IPhone_11_with_half_backlight_on_display?action=history
revisione: '2025-05-31T14:29:37Z'
categorie: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# IPhone 11 with half backlight on display

> Fonte: [IPhone 11 with half backlight on display — repair.wiki](https://repair.wiki/w/IPhone_11_with_half_backlight_on_display), CC BY-SA 3.0. Autori: vedi cronologia.

## Problem description
The device turns on and works but there is a dark spot on one of the bottom corners.

## Symptoms
- There is a dark spot on the bottom left side of the screen 
- There is a dark spot on the bottom right side of the screen 

### Diagnostic Steps
The first step is to try to swap parts before assuming there is a problem with the motherboard, so start by trying a new display.

If a new display doesn't fix the issue the next step is to diagnose the motherboard.

Why this issue even happens in the first place? Well, because on the iPhone 11 motherboard there are actually 2 backlight circuits for the display.

Start by taking diode readings of the LCD FPC especially the backlight lines and compare with the image below. If a line that should have 0.500 measures 0.000, you know there is a short. If it measures OL or nothing at all, it means that the circuit is open.

After taking diode readings of the FPC, you will probably already find the line that is faulty, use a program like ZXW to trace where it goes.

The backlight circuits are located under a shield on the top board, so if you're skilled enough, you may not need to split the boards.

As we said before, there are 2 backlight circuits, so if you have a dark spot on the left side of the screen, you should focus your attention there.

The most common issue is for the output resistor to be blown, if you already took diode measurements of the FPC you saw that.

A common issue is also a short on PP_DISPLAY_BL12_ANODE or PP_DISPLAY_BL34_ANODE, a short on these lines can destroy the entire circuit. Coils, backlight IC, Caps, and diodes.

Here is also a schematic of how one IC works in detail.

### Repair Steps
Replacing the output resistors is easy, find them on a donor board or use any with 0.000 ohm resistance and foot size of 0201.

The backlight IC U5650 or U5660 is an LM3539A1 and can be easily found.

If you have a short on, for example, a capacitor PP_DISPLAY_BL12_ANODE or PP_DISPLAY_BL34_ANODE, it is recommended to remake that circuit.
