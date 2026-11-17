---
titolo: Fonte esterna — iPad Pro 11" 4th Gen non carica (CD3217)
tipo: fonte
riassunto: 'Riassunto della fonte esterna: diagnosi e riparazione del mancato charging
  su iPad Pro 11" 4th gen dovuto a CD3217, con controllo corti e swap anche del ROM
  abbinato (es. U3890).'
modelli:
- iPad Pro 11in 4th gen (A2759, A2761, A2435, A2762)
fonti:
- raw/repairwiki/pagine/how-to-fix-an-ipad-pro-11in-4th-gen-that-does-not-charge-cd3217-solution.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# Fonte esterna: How To Fix an iPad Pro 11in 4th Gen That Does Not Charge, CD3217 Solution

> URL: https://repair.wiki/w/How_To_Fix_an_iPad_Pro_11in_4th_Gen_That_Does_Not_Charge%2C_CD3217_Solution  
> Cronologia: https://repair.wiki/w/How_To_Fix_an_iPad_Pro_11in_4th_Gen_That_Does_Not_Charge%2C_CD3217_Solution?action=history  
> Revisione: 2024-02-04T13:59:31Z  
> Licenza: CC BY-SA 3.0

## Contesto / problema
- iPad Pro 11" 4th Generation non carica.
- La fonte indica che il problema è **normalmente causato da un CD3217 difettoso**.
- Nota importante della fonte: quando si sostituisce CD3217, è necessario usare un **CD3217 “matching”** da una motherboard donatrice e **trasferire anche il ROM abbinato** (nella fonte: **U3890**).

## Modelli interessati (da fonte)
- **A2759**
- **A2761**
- **A2435**
- **A2762**

## Sintomi tipici (da fonte)
- iPad che **non carica**.
- Se la batteria è scarica, il dispositivo può sembrare “senza alimentazione”.
- Se la batteria ha ancora carica:
  - **nessun simbolo di charging** quando si collega il caricatore
  - **percentuale batteria non aumenta**
- Con **USB meter** la fonte riporta lettura: **5V 0.620A**.
- Con CD3217 guasto, la fonte descrive che l’iPad resta “stuck” a **5V**, mentre in condizioni corrette dovrebbe arrivare a **15V**.

## Diagnosi (da fonte)
1. Verificare che sia un problema di charging e non un problema di “no power”:
   - usare una **batteria completamente carica** oppure
   - provare a **bootare da alimentazione**.
2. Escludere la porta di ricarica:
   - test con **charging port/part buona** (good known part).
3. Controllo in **diode mode** attorno a **CD3217** per individuare componenti in corto.
   - La fonte indica di concentrarsi sulle **3 grosse capacità** adiacenti al chip:
     - **PP_LDO_CORE**
     - **PP3V3_ACE_LDO** (indicato come “tipicamente shorted”)
     - **PP3V3_S2_ACE**
   - Se queste linee/capacità risultano in **short**, la fonte conclude che il problema è un **CD3217 charging IC difettoso**.

## Riparazione (da fonte)
1. Rimuovere il CD3217 difettoso.
2. Con il chip rimosso, **verificare e rimuovere i corti** nell’area.
3. Installare un **CD3217 di ricambio** da una scheda simile (iPad Pro con USB-C).
4. Trasferire anche il **ROM abbinato** dal donor:
   - la fonte specifica che in questo esempio il ROM è **U3890**.
   - la fonte aggiunge che spesso il ROM è etichettato come **8NXXXX** (esempi riportati: **8N150**, **8N030**, ecc.).
5. La fonte sottolinea che **senza lo swap del secondo chip (ROM abbinato)** il nuovo charging IC **non funzionerà**.
6. Importante: usare il ROM **dalla stessa scheda** da cui è stato prelevato il CD3217.

## Collegamenti utili in wiki (da fonte)
- CD3217: [CD3217](../componenti/cd3217.md)
- Tecnica di test/ricerca corti (generale): [tecniche/test-cd3217-e-ricerca-corti.md](../tecniche/test-cd3217-e-ricerca-corti.md)
- Sintomo “non carica o alimentazione instabile”: [sintomi/non-carica-o-alimentazione-instabile.md](../sintomi/non-carica-o-alimentazione-instabile.md)
- Dispositivo: [iPad Pro 11in 4th gen](../dispositivi/ipad-pro-11in-4th-gen.md)
