---
titolo: Test Tristar e diagnosi “non carica” (USB ~0.006–0.007A) + corto su PP_VDD_MAIN/PP_VDD_BOOST
  — tecnica generale
tipo: tecnica
riassunto: 'Flusso troubleshooting “non carica” con draw USB molto basso: split sandwich
  e verifica Tristar/Yangtze; se invece hai corto/assorbimento alto su iPhone XS,
  cerca corto su PP_VDD_MAIN/PP_VDD_BOOST con iniezione e termica.'
modelli: []
fonti:
- raw/repairwiki/pagine/how-to-diagnose-fix-an-iphone-7-that-does-not-charge-takes-0-006a-via-usb.md
- raw/repairwiki/pagine/how-to-fix-an-ipad-air-that-will-not-charge-or-power-on.md
- raw/repairwiki/pagine/how-to-fix-an-ipad-pro-11in-4th-gen-that-does-not-charge-cd3217-solution.md
- raw/repairwiki/pagine/how-to-fix-an-ipad-that-will-charge-when-powered-off-but-not-when-powered-on.md
- raw/repairwiki/pagine/how-to-fix-iphone-7-that-does-not-turn-on-hangs-at-0-020-0-030-a-after-you-prompt-to-boot-on-dc-power-supply.md
- raw/repairwiki/pagine/how-to-fix-iphone-x-that-does-not-charge.md
- raw/repairwiki/pagine/how-to-repair-ipad-pro-10-5-not-charging-or-not-detected-by-pc.md
- raw/repairwiki/pagine/iphone-xs-not-charging.md
- raw/repairwiki/pagine/iphone-xs-not-powering-on-pulls-2a-or-more-before-promt-to-boot.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Scopo
Diagnosi e riparazione di iPhone/iPad con sintomo **“non carica”** dove:
- il dispositivo **si accende** ma **non carica**;
- il **USB meter** mostra **0.006–0.007 A** (draw molto basso) oppure **0.000 A**.

In parallelo, per iPhone XS (caso fonte): se il problema è **“non si accende”** e il DCPSU vede **2 A o più prima del prompt**, la fonte indica un possibile **corto su rail** (PP_VDD_MAIN / PP_VDD_BOOST) da localizzare con iniezione.

> Nota: la fonte “non carica ~0.006–0.007A” è generale; la parte PP_VDD_MAIN/PP_VDD_BOOST è specifica per iPhone XS “non powering on”. Da verificare eventuali contraddizioni tra i due flussi sullo stesso identico sintomo (carica vs no power).
