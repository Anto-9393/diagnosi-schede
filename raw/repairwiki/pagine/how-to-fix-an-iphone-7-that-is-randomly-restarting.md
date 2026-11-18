---
titolo: How To Fix an iPhone 7 That Is Randomly Restarting
tipo: fonte_esterna
url: https://repair.wiki/w/How_To_Fix_an_iPhone_7_That_Is_Randomly_Restarting
cronologia: https://repair.wiki/w/How_To_Fix_an_iPhone_7_That_Is_Randomly_Restarting?action=history
revisione: '2024-01-25T06:39:16Z'
categorie: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
figure:
- file: Placeholder image.jpg
  didascalia: Example image (Figure 1) -- No image yet. Help expand this page by uploading
    it!
---

# How To Fix an iPhone 7 That Is Randomly Restarting

> Fonte: [How To Fix an iPhone 7 That Is Randomly Restarting — repair.wiki](https://repair.wiki/w/How_To_Fix_an_iPhone_7_That_Is_Randomly_Restarting), CC BY-SA 3.0. Autori: vedi cronologia.

## Problem description
How to fix an iPhone 7 that is randomly restarting. This typically happens after opening the phone or replacing the battery.

And typically it will restart every 3 minutes.

## Symptoms
- Phone will fully boot up and get to the home screen but after about 3 minutes, it will just spontaneously restart
- You'll notice the battery level is sporadic (value constantly changes) or stays at 0% or 1%, even if battery is fully charged

- You see it's not charging, where USB meter charging current is jumping all over the place, instead of a 1+A current draw via USB.
- In Settings > Battery > Battery Health, it says "Service" and no battery health percentage.
- In 3u Tools, it shows no battery data.
If you see any or all of the symptoms above, it is usually a sign the phone cannot "talk" to the battery.

TIGRIS_BATTERY_SWI_CONN is responsible for transmitting data from the battery to Tigris to the CPU.

## Solution
- Check the panic log. If you see "Missing Sensors: TG0B", it's the battery connector issue. Read below solutions.
- In most cases, the battery connector is warped or damaged
  - You can visually inspect the small center pins of the battery connector. If they look like they're "pushed out" and hidden under the plastic of the connector, you can try pushing them back out with a tool
  - Or you can replace the battery connector itself.
- Sometimes, Tigris has an issue and needs to be replaced.
- If this also doesn't solve it, it could be Tristar or another line under Tigris or Tristar having an issue.
  - You'll need to diode mode each pad under Tigris and Tristar to see if you can find an OL or a short, causing the issue.
    - If you find a shorted line, track down the shorted capacitor by injecting voltage
    - If you find an OL where there should be a reading, follow the path of the line and diode mode every at every point. Find the point where the diode mode reading reappears. That should be where the line is disconnected and you'll need to replace the component that disconnected the line, usually a filter.
### Final Testing
- Run the stopwatch and see if it can run for longer than the 3 minutes that it was rebooting at
- Play a 1hr Youtube video to see if it can play it continuously
- Check the USB charging current
- Check the Battery Health in the Settings
- Check if the battery level is showing accurate battery levels.
