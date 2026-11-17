---
titolo: iPhone 11 Pro Max
tipo: dispositivo
riassunto: 'Caso iPhone 11 Pro/11 Pro Max: non si accende con assorbimento ≥2A; spesso
  corto su PP_VDD_MAIN/PP_VDD_BOOST o (raro) U_NFC; procedura con ispezione e iniezione
  4V/2A per localizzare il condensatore in corto.'
modelli:
- iPhone 11 Pro Max
fonti:
- raw/repairwiki/pagine/iphone-11-pro-max.md
- raw/repairwiki/pagine/iphone-11-pro-and-iphone-11-pro-max-not-powering-on-2a-or-higher-power-draw-after-prompt-to-boot.md
aggiornato: '2026-11-17'
categoria: phone
codici_modello: []
componenti_chiave:
- U_NFC
casi: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# iPhone 11 Pro Max

## Guasti tipici e casi

### Non si accende / assorbimento ≥2A dopo prompt to boot
**Sintomo (da fonte):** iPhone 11 Pro o iPhone 11 Pro Max non si accende con assorbimento **2A o superiore** dalla DCPSU **prima** del prompt to boot.

**Diagnosi (da fonte):**
1. **Ispezione visiva completa** della scheda.
2. Controllare **danni da liquidi** sotto gli adesivi sul retro.
3. Rimuovere la **schiuma attorno ai connettori** per vedere meglio.
4. Cercare **corrosione** su/attorno a componenti e IC.

**Se NON c’è danno da acqua:**
- È “più probabile” un **condensatore in corto** su una delle seguenti linee:
  - **PP_VDD_MAIN** (linea più probabile)
  - **PP_VDD_BOOST** (di solito corta quando non è VDD MAIN)
  - **U_NFC**: in alcuni casi il chip può **crackarsi** e creare un corto “nel bottom board”.

**Localizzazione del corto (da fonte):**
- Iniettare **4 V / 2 A** **direttamente** sulla linea che hai misurato come in corto.
- Usare **freeze spray** o **termocamera** per individuare il **condensatore** che si scalda.
  - (La fonte rimanda a video: freeze spray e termocamera.)

**Riparazione (da fonte):**
- In questi casi puoi **rimuovere** il condensatore in corto **senza sostituirlo**: il dispositivo dovrebbe funzionare normalmente.
- La fonte sconsiglia la sostituzione perché comporta **più calore** e quindi **più rischio**.

**Se c’è danno da acqua (da fonte):**
- Prestare attenzione alle aree con segni di liquido.
- Spesso si trova corrosione su condensatori ma anche **sotto IC**.
- La fonte suggerisce di considerare la scheda come **2 layer** (sandwich):
  - separare in **top board** e **bottom board**
  - verificare se il corto è ancora presente collegando **solo** il top layer alla DCPSU
    - se il corto resta → colpevole nel **top board**
    - se il corto scompare → colpevole nel **bottom board**
  - in quel caso iniettare tensione sul **bottom board** per localizzare il corto.

**Nota importante sulla modalità di iniezione tramite connettore batteria (da fonte):**
- Se inietti tensione tramite connettore batteria (es. iPower Pro / DT880), può scaldarsi **Yangtze** **istantaneamente**.
- Motivo (da fonte): la linea **PP_BATT_VCC** del connettore batteria collega **PP_VDD_MAIN** tramite Yangtze, creando molta dissipazione.
- La fonte consiglia:
  - provare a **rimuovere Yangtze** e controllare eventuali **corti sotto Yangtze**
  - se non ci sono corti sotto Yangtze, il problema era Yangtze e va **sostituita**.

## Collegamenti utili (wiki)
- Tecnica generale per ricerca corto con iniezione e termocamera: [ricerca-corto-iniezione-bassa-tensione-e-termocamera](../tecniche/ricerca-corto-iniezione-bassa-tensione-e-termocamera.md)
- Componenti/linee citate nella fonte:
  - [condensatori-mlcc-elettrolitici-tantalio](../componenti/condensatori-mlcc-elettrolitici-tantalio.md)
  - [u-nfc](../componenti/u-nfc.md)

## Fonti
- Fonte: [IPhone 11 Pro and iPhone 11 Pro Max Not Powering on, 2a or Higher Power Draw After Prompt to Boot — repair.wiki](https://repair.wiki/w/IPhone_11_Pro_and_iPhone_11_Pro_Max_Not_Powering_on%2C_2a_or_Higher_Power_Draw_After_Prompt_to_Boot), CC BY-SA 3.0.
