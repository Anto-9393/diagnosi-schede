---
titolo: iPad Pro 11in 4th Gen
tipo: dispositivo
riassunto: 'iPad Pro 11in 4th Gen (A2759/A2761/A2435/A2762): no charge spesso dovuto
  a CD3217 con ROM abbinata (U3890).'
modelli:
- iPad Pro 11in 4th Gen
fonti:
- raw/repairwiki/pagine/ipad-pro-11in-4th-gen.md
- raw/repairwiki/pagine/how-to-fix-an-ipad-pro-11in-4th-gen-that-does-not-charge-cd3217-solution.md
aggiornato: '2026-11-17'
categoria: tablet
codici_modello:
- A2759
- A2761
- A2435
- A2762
componenti_chiave:
- CD3217
casi: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# iPad Pro 11in 4th Gen

- Uscita: 2022
- Codici modello: **A2759 / A2761 / A2435 / A2762** (da fonte)

## Guasti tipici e casi

### Non carica (spesso “nessuna alimentazione” apparente)
**Sintomi tipici (da fonte):**
- L’iPad **non carica**.
- Se la batteria è **scarica**, il dispositivo può sembrare **“senza alimentazione”**.
- Se la batteria ha ancora carica, **non compare il simbolo di ricarica** e la **percentuale batteria non aumenta**.
- Con un **USB meter**: lettura indicata **5V 0.620A**.
- Con CD3217 guasto, l’iPad può rimanere **“stuck” a 5V** (indicazione di problema di charging).

**Diagnosi mirata (da fonte):**
1. Verificare che sia un problema di **charging** e non un problema di **no power** (es. usare **batteria completamente carica** o **power supply**/boot da alimentazione).
2. Escludere un problema del **connettore/charging port** testando con una **parte nota buona**.
3. Controllo in **diode mode** attorno a **CD3217** per individuare componenti in **corto**.
4. La fonte indica di concentrarsi su **3 grossi condensatori** vicino al chip:
   - **PP_LDO_CORE**
   - **PP3V3_ACE_LDO** (tipicamente la linea in corto)
   - **PP3V3_S2_ACE**

**Criterio (da fonte):**
- Se questi componenti risultano **in corto**, la fonte conclude che il problema è un **CD3217 charging IC difettoso**.

**Riparazione (da fonte):**
- Rimuovere il **CD3217** guasto.
- Con chip rimosso, verificare e rimuovere eventuali **short** residui nell’area.
- Installare un **CD3217 compatibile** preso da una **motherboard donatrice**.
- Insieme al CD3217, trasferire anche la **ROM abbinata** per questo modello: **U3890**.
  - La fonte specifica che **senza** lo swap della seconda memoria, il nuovo CD3217 **non funzionerà**.
  - La ROM deve provenire dalla **stessa scheda** da cui è stato prelevato il CD3217.
  - Esempi di etichettatura ROM riportati: **8N150**, **8N030**, ecc. (da fonte).

## Componenti chiave coinvolti
- [CD3217](../componenti/cd3217.md) — controller/IC di charging (fonte: causa tipica del no charge).

> Nota: la fonte cita anche la **ROM chip U3890** (da trasferire in coppia con CD3217), ma non è presente una pagina componente dedicata nella struttura attuale: **da verificare** se creare/agganciare una pagina per U3890.

## Collegamenti utili
- Sintomo correlato: [non-carica-o-alimentazione-instabile](../sintomi/non-carica-o-alimentazione-instabile.md)
- Tecnica correlata (CD3217): [test-cd3217-e-ricerca-corti](../tecniche/test-cd3217-e-ricerca-corti.md)
- Tecnica correlata (CD3217 no charge, iPhone): [test-tristar-e-diagnosi-non-carica-iphone](../tecniche/test-tristar-e-diagnosi-non-carica-iphone.md)
