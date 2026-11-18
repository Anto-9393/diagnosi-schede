---
titolo: How to fix iPhone 7 that does not turn on, hangs at 0.020–0.030 A after you
  prompt to boot on DC Power Supply
tipo: fonte_esterna
url: https://repair.wiki/w/How_to_fix_iPhone_7_that_does_not_turn_on%2C_hangs_at_0.020%E2%80%930.030_A_after_you_prompt_to_boot_on_DC_Power_Supply
cronologia: https://repair.wiki/w/How_to_fix_iPhone_7_that_does_not_turn_on%2C_hangs_at_0.020%E2%80%930.030_A_after_you_prompt_to_boot_on_DC_Power_Supply?action=history
revisione: '2024-01-09T18:08:02Z'
categorie: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# How to fix iPhone 7 that does not turn on, hangs at 0.020–0.030 A after you prompt to boot on DC Power Supply

> Fonte: [How to fix iPhone 7 that does not turn on, hangs at 0.020–0.030 A after you prompt to boot on DC Power Supply — repair.wiki](https://repair.wiki/w/How_to_fix_iPhone_7_that_does_not_turn_on%2C_hangs_at_0.020%E2%80%930.030_A_after_you_prompt_to_boot_on_DC_Power_Supply), CC BY-SA 3.0. Autori: vedi cronologia.

## Problem description
Fixing an issue where the iPhone 7 would not turn on, pulls around 20-30 mA from the DC power supply.

## Symptoms
- No Power/Doesn't boot. Just dead.
- Cannot get into DFU mode.
- When the board is connected to a DC power supply
  - You get 0 A draw before prompt to boot
  - When you prompt to boot, it jumps up to 20–40 mA and just hangs at that value. No fluctuation

## Solution
- Clean underfill above CPU
- Clear out all underfill around L1801, L1804 and L3302
- Poke those coils and see if they break off
- If any of the three break, replace the coils that broke off.
- Coil values
  - L1801 — 1 μH, 2.1 A, 0.12 Ω
  - L1804 — 1 μH, 2.1 A, 0.12 Ω
  - L3302 — 1.2 μH, 3.0 A, 0.080 Ω

**Please Note:** You cannot check for these coils if they're loose by poking them with the underfill still there. You MUST clear it all out around these coils and then poke them to see if they break off.

Also, these are pressed up right against the CPU, so be careful with your hot air, because you can accidentally "float" the CPU and cause a more significant failure.
