---
titolo: How To Fix an iPhone 16 with NO IMEI due to shorted baseband
tipo: fonte_esterna
url: https://repair.wiki/w/How_To_Fix_an_iPhone_16_with_NO_IMEI_due_to_shorted_baseband
cronologia: https://repair.wiki/w/How_To_Fix_an_iPhone_16_with_NO_IMEI_due_to_shorted_baseband?action=history
revisione: '2025-11-03T12:00:24Z'
categorie: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
figure:
- file: 16 masked pad.png
  didascalia: iPhone 16 PP_3V1_LDO10 pad masked on logic board.
- file: 16 masked pad on boardview.png
  didascalia: PP_3V1_LD010 pad on board view.
---

# How To Fix an iPhone 16 with NO IMEI due to shorted baseband

> Fonte: [How To Fix an iPhone 16 with NO IMEI due to shorted baseband — repair.wiki](https://repair.wiki/w/How_To_Fix_an_iPhone_16_with_NO_IMEI_due_to_shorted_baseband), CC BY-SA 3.0. Autori: vedi cronologia.

## Problem description
An iPhone 16 powers on normally but shows “No IMEI” or “Modem Firmware Missing” under Settings → General → About. Upon board-level diagnosis, PP_3V1_LDO10, a key baseband power rail, is found shorted to ground under the Baseband CPU.

## Symptoms
- “No IMEI” or “Modem Firmware Missing” displayed in settings.
- Restore completes successfully but no modem detected.
- PP_3V1_LDO10 line measures 0 Ω (hard short) or very low resistance to ground.
- Short disappears when BB_CPU is removed from the board.

## Solution
The short originates beneath the Baseband CPU due to internal pad failure or solder bridge on PP_3V1_LDO10.

The fix is to:

1. Remove the Baseband CPU (BB_CPU).
1. Mask (insulate) the PP_3V1_LDO10 pad on the board.
1. Reball and reattach the Baseband CPU to restore normal baseband function. This isolates the faulty shorted pad while maintaining all functional interconnects.
### Diagnostic Steps
1. Visual Inspection
1. * Inspect baseband area for rework signs or water damage.
1. * Confirm clean, undamaged board and intact shield.
1. Resistance Check (Multimeter, Diode Mode)
1. * Measure PP_3V1_LDO10 (typically found near U_BB_CPU).
1. * Faulty: near 0 Ω → short to ground.
1. Thermal / Freeze Spray Test
1. * Inject 1.0 V–3 V into PP_3V1_LDO10 with current limit.
1. * Observe heat spot — shorted region will reveal as the Baseband CPU heating.
1. Confirmation
1. * Lift BB_CPU using controlled heat.
1. * Recheck PP_3V1_LDO10 line — if short clears → short was under the chip.

### Repair Steps
1. Preparation
1. * Remove underfill around BB_CPU carefully.
1. * Preheat board evenly to avoid warping.
1. Chip Removal
1. * Heat BB_CPU area.
1. * Gently lift the CPU once solder balls reflow.
1. Short Check
1. * Test PP_3V1_LDO10 to ground again — short should now be gone.
1. Pad Masking
1. * Apply UV mask or polyimide tape dot over the PP_3V1_LDO10 pad on the board side.
1. * Cure UV mask properly.
1. Reballing
1. * Clean chip, remove all solder residues.
1. * Reball with IC.
1. * Inspect under microscope for even joints.
1. Reinstallation
1. * Align BB_CPU precisely using microscope or positioning template.
1. * Reflow until proper seating observed.
1. Testing
1. * Allow board to cool.
1. * Check PP_3V1_LDO10 resistance — should now read normal.
1. * Assemble and power on.
1. * Confirm IMEI and baseband version now visible.
