---
titolo: Fonte — iPad Pro 9.7 Not Powering on, 2a or Higher Power Draw before Prompt
  to Boot
tipo: fonte
riassunto: 'Caso esterno: iPad Pro 9.7 che assorbe ≥2A da DCPS prima del prompt di
  boot → indicazione di corto su linee PP_VCC_MAIN/PP_BATT_VCC/PPSTROBE_LX/PPVCC_HIGH;
  ricerca con iniezione 4V/2A e localizzazione (freeze spray/termocamera).'
modelli:
- iPad Pro 9.7
fonti:
- raw/repairwiki/pagine/ipad-pro-9-7-not-powering-on-2a-or-higher-power-draw-before-prompt-to-boot.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# IPad Pro 9.7 Not Powering on, 2a or Higher Power Draw before Prompt to Boot (repair.wiki)

> Fonte: [IPad Pro 9.7 Not Powering on, 2a or Higher Power Draw before Prompt to Boot — repair.wiki](https://repair.wiki/w/IPad_Pro_9.7_Not_Powering_on%2C_2a_or_Higher_Power_Draw_before_Prompt_to_Boot), CC BY-SA 3.0. Autori: vedi cronologia.

## Descrizione problema
- iPad Pro 9.7 **non si accende**.
- Con alimentatore da banco (DCPS) la scheda **assorbe 2A o più** **prima** del “prompt to boot”.

## Soluzione / logica diagnostica (da fonte)
1. **Ispezione** della motherboard per:
   - componenti bruciati
   - danni da liquidi
2. Se **non** ci sono danni da liquidi, la fonte indica che è **molto probabile** un **corto** su una delle seguenti linee:
   - **PP_VCC_MAIN**
   - **PP_BATT_VCC**
   - **PPSTROBE_LX**
   - **PPVCC_HIGH**
3. La fonte segnala che la linea **più comune** con corto è **VCC_MAIN** (quindi tipicamente **PP_VCC_MAIN**).

## Localizzazione del corto (da fonte)
- Per rilevare il corto: **iniettare tensione 4 V / 2 A** **direttamente** sulla linea che risulta in corto.
- Usare:
  - **freeze spray** (link video nella fonte) oppure
  - **termocamera** (link video nella fonte)
- La fonte specifica un comportamento osservato su questo iPad:
  - con corto su **VCC_MAIN**, **U8500** può scaldarsi.
  - **Non** assumere automaticamente che **U8500** sia la causa: controllare altri hot spot sulla board.

## Cosa fare dopo aver identificato il componente (da fonte)
- Se il corto è su un **chip**: **sostituire** il componente.
- Se il corto è su un **condensatore di disaccoppiamento**: spesso si può **rimuovere** dal PCB (la fonte afferma che la capacità potrebbe non scendere abbastanza da compromettere il funzionamento).
- Se c’è **danno da liquidi**:
  - la corrosione può causare il corto
  - a volte la pulizia della corrosione è sufficiente a ripristinare
  - se si vedono segni di liquido sotto un IC: probabilmente serve rimozione/pulizia e **reball** o **sostituzione** del chip.

## Verifica finale (da fonte)
- Dopo la rimozione del componente in corto, eseguire una **diode reading** della linea.
- La fonte riporta che una **VCC Main sana** dovrebbe avere una lettura “**vault**” tra **0.400 e 0.500**.
  - Nota: il termine “vault” è riportato così nella fonte; **da verificare** il significato esatto nel contesto del multimetro/lettura.

## Collegamenti utili (da wiki)
- Sintomo correlato (assorbimento anomalo / ciclo di accensione): [non-si-accende-ciclo-assorbimento-0-0-3a-schermo-lampeggia](../sintomi/non-si-accende-ciclo-assorbimento-0-0-3a-schermo-lampeggia.md) (pagina esistente; contenuto da verificare rispetto a questo caso specifico).
- Tecnica di ricerca corto con iniezione bassa tensione e termocamera: [ricerca-corto-iniezione-bassa-tensione-e-termocamera](../tecniche/ricerca-corto-iniezione-bassa-tensione-e-termocamera.md).
- Tecnica generale di diagnosi/rimozione corto su rail: [diagnosi-e-rimozione-corto-su-rail-con-capacitore-in-corto](../tecniche/diagnosi-e-rimozione-corto-su-rail-con-capacitore-in-corto.md).

## Note di compatibilità con la wiki
- Le linee indicate (**PP_VCC_MAIN**, **PP_BATT_VCC**, **PPSTROBE_LX**, **PPVCC_HIGH**) sono riportate dalla fonte; **da verificare** eventuali corrispondenze con sigle/rail presenti nelle pagine componenti esistenti.
- La fonte cita **U8500** come possibile hot spot su VCC_MAIN; **da verificare** la sigla componente equivalente nella nostra mappatura (se presente in componenti/...).
