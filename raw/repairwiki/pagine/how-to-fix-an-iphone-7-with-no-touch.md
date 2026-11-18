---
titolo: How To Fix an iPhone 7 With No Touch
tipo: fonte_esterna
url: https://repair.wiki/w/How_To_Fix_an_iPhone_7_With_No_Touch
cronologia: https://repair.wiki/w/How_To_Fix_an_iPhone_7_With_No_Touch?action=history
revisione: '2024-01-22T08:59:25Z'
categorie: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
figure:
- file: IP7 No Touch Fix.jpg
  didascalia: How To Fix No Touch on iPhone 7
---

# How To Fix an iPhone 7 With No Touch

> Fonte: [How To Fix an iPhone 7 With No Touch — repair.wiki](https://repair.wiki/w/How_To_Fix_an_iPhone_7_With_No_Touch), CC BY-SA 3.0. Autori: vedi cronologia.

## Problem description
No Touch — Phone turns on but touch doesn't work
## Symptoms
- Turns on but no touch

## Solution
- Diode mode the LCD connector (J4502) and check for any lines that are OL or 0.000V (shorted).
- In most cases, you'll find pry damage near the connector, causing damage to a filter or resistor. Commonly damaged:
  - FL3917
  - FL3910
  - R3923
- If you find an abnormal diode mode value, see if the name of the line mentions the word "touch. This will help assure you that you're looking at the right spot
- Follow the path of the abnormal value by doing diode mode readings on every component in the path, to see where the correct diode mode reading is located. That will point you towards the failed component.
  - For example, if the top side of FL3917 gives you OL, but the bottom side of it gives you 0.442, then you found your failed component.

Another solution:
- If you found the diode mode readings are all normal, then most likely it's a connector issue
- Find the 4 ground pins on the LCD and Home Button connectors and use fine tip tweezers or an Xacto blade to bend them outwards.
- Refer to the example image 
- - Usually this issue is caused from too many screens being unplugged and plugged in, causing those pins to be pushed outwards
- Or from someone plugging in a 8/8P screen into a 7/7P board.
- If still no touch, you can try replacing the LCD connector to see if that solves it.
