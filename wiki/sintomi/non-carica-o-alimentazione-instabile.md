---
titolo: Non carica o alimentazione instabile — salto di corrente al prompt to boot
  (DCPS) / iPhone XS (≥2A prima del prompt)
tipo: sintomo
riassunto: 'Su DCPS, iPhone XS può assorbire ≥2A prima del prompt to boot: pattern
  da corto su rail (PP_VDD_MAIN/PP_VDD_BOOST, raramente U4902/U5002) e distinzione
  tramite split sandwich 2-layer.'
modelli:
- iPhone XS
fonti:
- raw/repairwiki/pagine/capacitors-repair-basics.md
- raw/repairwiki/pagine/diodes-repair-basics.md
- raw/repairwiki/pagine/how-to-diagnose-fix-an-iphone-7-that-does-not-charge-takes-0-006a-via-usb.md
- raw/repairwiki/pagine/how-to-fix-an-ipad-air-that-will-not-charge-or-power-on.md
- raw/repairwiki/pagine/how-to-fix-an-ipad-pro-11in-4th-gen-that-does-not-charge-cd3217-solution.md
- raw/repairwiki/pagine/how-to-fix-an-ipad-that-will-charge-when-powered-off-but-not-when-powered-on.md
- raw/repairwiki/pagine/how-to-fix-an-iphone-8-plus-boot-looping-on-apple-logo-and-random-charging.md
- raw/repairwiki/pagine/how-to-fix-an-iphone-8-that-has-no-power-does-not-boot.md
- raw/repairwiki/pagine/how-to-fix-iphone-7-that-does-not-turn-on-hangs-at-0-020-0-030-a-after-you-prompt-to-boot-on-dc-power-supply.md
- raw/repairwiki/pagine/how-to-fix-iphone-x-that-does-not-charge.md
- raw/repairwiki/pagine/how-to-fix-iphone-x-that-does-not-power-on.md
- raw/repairwiki/pagine/how-to-repair-ipad-6-no-power.md
- raw/repairwiki/pagine/how-to-repair-iphone-11-dead-not-charging.md
- raw/repairwiki/pagine/iphone-11-not-powering-on-2a-or-higher-power-draw-after-prompt-to-boot.md
- raw/repairwiki/pagine/iphone-11-not-powering-on-after-prompt-to-boot-current-jumps-back-and-forth-from-0-a-to-320-ma-then-0-a-to-1-4-a-then-0-a-to-500-ma-and-so-on.md
- raw/repairwiki/pagine/iphone-11-pro-and-iphone-11-pro-max-not-powering-on-2a-or-higher-power-draw-after-prompt-to-boot.md
- raw/repairwiki/pagine/iphone-xs-not-powering-on-pulls-2a-or-more-before-promt-to-boot.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Sintomo
**Non si accende / nessun boot** con assorbimento anomalo misurabile su **DC power supply (DCPS)**.

### iPhone XS — assorbimento elevato prima del prompt to boot
- Su DCPS, l’iPhone XS **non si accende** e **assorbe 2 A o più** **prima** del *prompt to boot*.

> Fonte: [IPhone XS Not Powering On, Pulls 2A or More Before Promt to Boot](../../raw/repairwiki/pagine/iphone-xs-not-powering-on-pulls-2a-or-more-before-promt-to-boot.md)

## Cause possibili (ordine probabilità)
Se **non** ci sono danni da liquidi, la fonte indica come causa più probabile un **condensatore in corto** su una delle linee sotto.

1. **Short su PP_VDD_MAIN** (più probabile)
2. **Short su PP_VDD_BOOST** (di solito quando non è VDD MAIN)
3. **Speaker Amp**: **U4902 o U5002** (più raro)

> Fonte: [IPhone XS Not Powering On, Pulls 2A or More Before Promt to Boot](../../raw/repairwiki/pagine/iphone-xs-not-powering-on-pulls-2a-or-more-before-promt-to-boot.md)

## Diagnosi rapida (workflow da fonte iPhone XS)
1. **Ispezione visiva completa** della board.
2. **Controllo danni da acqua** sotto gli sticker sul retro.
3. **Rimozione della schiuma** attorno ai connettori per migliorare l’ispezione.
4. Se **non** c’è danno da liquidi: cercare un **condensatore in corto** sulle linee indicate.

> Fonte: [IPhone XS Not Powering On, Pulls 2A or More Before Promt to Boot](../../raw/repairwiki/pagine/iphone-xs-not-powering-on-pulls-2a-or-more-before-promt-to-boot.md)

## Misure / conferma corto su rail (iniezione + localizzazione)
### Iniezione
- La fonte indica di **iniettare tensione 4 V / 2 A** **direttamente** nella **linea** dove hai misurato lo short.

> Fonte: [IPhone XS Not Powering On, Pulls 2A or More Before Promt to Boot](../../raw/repairwiki/pagine/iphone-xs-not-powering-on-pulls-2a-or-more-before-promt-to-boot.md)

### Localizzazione condensatore in corto
- Usare **freeze spray** oppure **termocamera** per individuare il **condensatore in corto**.

> Fonte: [IPhone XS Not Powering On, Pulls 2A or More Before Promt to Boot](../../raw/repairwiki/pagine/iphone-xs-not-powering-on-pulls-2a-or-more-before-promt-to-boot.md)

## Riparazione (cosa fare con il condensatore in corto)
- In questi casi la fonte indica che puoi **rimuovere il condensatore in corto** e **non sostituirlo**.
- Motivazione della fonte: sostituire significa aggiungere calore per reinstallare e aumenta il rischio.

> Fonte: [IPhone XS Not Powering On, Pulls 2A or More Before Promt to Boot](../../raw/repairwiki/pagine/iphone-xs-not-powering-on-pulls-2a-or-more-before-promt-to-boot.md)

## Caso con danni da liquidi
Se c’è **danno da liquidi**, la fonte dice di prestare attenzione alle aree con **segni di corrosione** (spesso anche **sotto gli IC**).

> Fonte: [IPhone XS Not Powering On, Pulls 2A or More Before Promt to Boot](../../raw/repairwiki/pagine/iphone-xs-not-powering-on-pulls-2a-or-more-before-promt-to-boot.md)

## Split sandwich (board 2-layer) per capire su quale lato è il corto
La fonte specifica che l’iPhone XS è una **2-layer board** e propone:
1. **Separare il sandwich** in **top board** e **bottom board**.
2. Verificare se lo **short resta** collegando **solo** la top layer al DCPS.
   - Se lo short **rimane**: il colpevole è sulla **top board**.
   - Se lo short **si elimina**: il corto è sulla **bottom board**.\n3. In quel caso, puoi **iniettare tensione** sulla **bottom board** per trovare il componente.

> Fonte: [IPhone XS Not Powering On, Pulls 2A or More Before Promt to Boot](../../raw/repairwiki/pagine/iphone-xs-not-powering-on-pulls-2a-or-more-before-promt-to-boot.md)

## Nota importante: iniezione via battery connector (Yangtze può scaldare istantaneamente)
Se usi un DCPS per iniettare tensione **attraverso il battery connector** (es. iPower Pro / DT880), la fonte avvisa:
- **Yangtze può scaldare istantaneamente**.
- Motivo: la linea del battery connector **PP_BATT_VCC** collega **PP_VDD_MAIN** tramite **Yangtze**, creando molta dissipazione.
- Nella maggior parte dei casi lo short **non** è l’IC ma un **condensatore in corto**.
- In casi rari, lo short può essere **Yangtze**: rimuoverla/controllarla e verificare se il corto resta.

> Fonte: [IPhone XS Not Powering On, Pulls 2A or More Before Promt to Boot](../../raw/repairwiki/pagine/iphone-xs-not-powering-on-pulls-2a-or-more-before-promt-to-boot.md)

## Collegamenti utili
- [DC power supply / DCPS](../strumenti/alimentatore-da-banco.md)
- [Tecnica: ricerca corto con iniezione bassa tensione e termocamera](../tecniche/ricerca-corto-iniezione-bassa-tensione-e-termocamera.md)
- [Condensatori MLCC/elettrolitici/tantalio](../componenti/condensatori-mlcc-elettrolitici-tantalio.md)
- [Diode mode / test con connettore (se serve per escludere altri guasti)](../tecniche/test-i2c-battery-connector-ol-diodes-mode.md)
