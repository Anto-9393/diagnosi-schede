---
titolo: 'Fonti — iPhone 11 Pro / 11 Pro Max: non si accende, assorbimento ≥2A prima
  del prompt di boot'
tipo: fonte
riassunto: 'Riassunto della fonte esterna: diagnosi di corto su linee PP_VDD_MAIN/PP_VDD_BOOST
  (e casi su U_NFC) in iPhone 11 Pro/Pro Max con assorbimento ≥2A prima del prompt
  di boot.'
modelli:
- iPhone 11 Pro
- iPhone 11 Pro Max
fonti:
- raw/repairwiki/pagine/iphone-11-pro-and-iphone-11-pro-max-not-powering-on-2a-or-higher-power-draw-after-prompt-to-boot.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Fonte
- Pagina sorgente: [IPhone 11 Pro and iPhone 11 Pro Max Not Powering on, 2a or Higher Power Draw After Prompt to Boot — repair.wiki](https://repair.wiki/w/IPhone_11_Pro_and_iPhone_11_Pro_Max_Not_Powering_on%2C_2a_or_Higher_Power_Draw_After_Prompt_to_Boot)
- Licenza: CC BY-SA 3.0

## Descrizione problema (da fonte)
- iPhone 11 Pro / iPhone 11 Pro Max **non si accende**.
- Con **alimentatore DCPSU** si osserva **assorbimento di 2A o superiore** **prima** del prompt di boot.

## Soluzione / flusso diagnostico (da fonte)
1. **Ispezione visiva completa** della scheda.
   - Controllare **danni da liquidi** sotto gli adesivi sul retro.
   - Rimuovere la **schiuma/foam** attorno ai connettori per vedere meglio.
   - Cercare **corrosione** su componenti e IC.

2. Se **non** ci sono danni da acqua:
   - La fonte indica come causa più probabile un **condensatore in corto** su una delle seguenti linee:
     - **PP_VDD_MAIN** (più probabile)
     - **PP_VDD_BOOST** (di solito corto quando non è VDD MAIN)
     - **U_NFC** (in alcuni casi il chip può creparsi e causare un corto “dentro” la bottom board)

3. **Localizzazione del condensatore in corto**
   - La fonte propone:
     - **iniezione di tensione 4 V / 2 A** direttamente sulla **linea** che risulta in corto (secondo la misura).
     - usare **freeze spray** o **termocamera** per individuare il componente che si scalda.

4. **Intervento**
   - In questi casi (corto da condensatore) la fonte afferma che spesso è sufficiente **rimuovere il condensatore in corto** senza sostituirlo.
   - Motivazione da fonte: sostituire significa aggiungere calore e aumentare il rischio.
   - La fonte dichiara che il dispositivo **funziona normalmente** senza effetti negativi (da verificare sul singolo caso).

5. Se c’è **danno da liquidi**:
   - Prestare attenzione alle zone con segni di corrosione.
   - La fonte riporta che spesso la corrosione si trova:
     - su condensatori
     - **anche sotto gli IC**.

6. Approccio “sandwich” (scheda 2 layer) per isolare la posizione del corto (da fonte)
   - La fonte suggerisce di separare la scheda in **top board** e **bottom board**.
   - Verificare se il corto è ancora presente alimentando/collegando **solo** lo strato superiore:
     - se il corto **rimane** → colpevole sul **top board**
     - se il corto **sparisce** → colpevole sulla **bottom board**
   - In quest’ultimo caso, la fonte consiglia di fare l’iniezione per trovare il corto **sulla bottom board**.

## Nota importante su iniezione tramite connettore batteria (da fonte)
- Se si inietta tensione attraverso il connettore batteria (es. iPower Pro / DT880), la fonte avverte che può scaldarsi **Yangtze** **istantaneamente**.
- Motivo da fonte: la linea **PP_BATT_VCC** collega **PP_VDD_MAIN** tramite Yangtze, generando molto calore.
- La fonte consiglia:
  - provare a **rimuovere Yangtze** e controllare se ci sono **corti sotto Yangtze**.
  - se non ci sono corti sotto Yangtze → il problema era Yangtze e va **sostituito**.

## Componenti/linee citate (da fonte)
- **PP_VDD_MAIN**
- **PP_VDD_BOOST**
- **U_NFC**
- **Yangtze**
- **PP_BATT_VCC**

## Link utili presenti nella fonte (da fonte)
- Freeze spray (video): https://youtu.be/3MtLSQJvQxI
- Termocamera (video): https://youtu.be/fkd4iDjgfvc
- iPower Pro / DT880 (video): https://youtu.be/rawjB9yxe1A

## Pagine wiki collegate (per navigazione)
- [iPhone 11 Pro](../dispositivi/iphone-11-pro.md)
- [iPhone 11 Pro Max](../dispositivi/iphone-11-pro-max.md)
- [strumenti/alimentatore-da-banco.md](../strumenti/alimentatore-da-banco.md)
- [tecniche/ricerca-corto-iniezione-bassa-tensione-e-termocamera.md](../tecniche/ricerca-corto-iniezione-bassa-tensione-e-termocamera.md)
