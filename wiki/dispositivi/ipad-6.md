---
titolo: iPad 6
tipo: dispositivo
riassunto: Se iPad 6 è completamente morto e su DCPS va in corto ( >1 A) o in ciclo
  a ~0.150 A, la fonte indica controlli su batteria (3.7–4.2 V), corto VCC_MAIN, Tristar
  e sezioni WiFi/PMU.
modelli:
- iPad 6
fonti:
- raw/repairwiki/pagine/ipad-6.md
- raw/repairwiki/pagine/how-to-repair-ipad-6-no-power.md
aggiornato: '2026-11-17'
categoria: tablet
codici_modello:
- A1893
- A1954
componenti_chiave: []
casi: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# iPad 6 — no power (DCPS: corto o ciclo a ~0.150 A)

## Sintomi tipici (da fonte)
- Nessun segno di vita: nessun boot, nessun display, nessuna vibrazione, nessuna icona di ricarica.
- Collegato a DC Power Supply (DCPS):
  - **corrente che sale istantaneamente oltre 1 A** → possibile **dead short**
  - oppure **salta subito a ~0.150 A e poi resetta** (boot parziale ma fallisce)
- Possibile **calore localizzato** solo vicino al componente in corto.

> Nota fonte: una sequenza di boot “corretta” dovrebbe essere **0.050 → 0.060 → 0.100 →** crescita fino a **~1.00 A**.

## Diagnosi guidata (da fonte)

### 1) Verifica tensione batteria
- Misura batteria: **valore atteso sano: 3.7–4.2 V**.
- Se batteria è **0 V**, l’iPad può apparire “morto”.

Collegamenti utili:
- [batteria](../componenti/batteria.md)
- [i2c-line-battery-connector](../componenti/i2c-line-battery-connector.md)

### 2) Test avvio con DC Power Supply (DCPS)
- Collegare **direttamente alla board**.
- Osservare il comportamento della corrente:
  - **spike istantaneo > 1.00 A** → possibile corto su **VCC_MAIN**, **WiFi IC** o **PMIC**
  - **spike istantaneo a ~0.150 A e reset/ciclo** → indicato come **Tristar failure**

Collegamenti utili:
- [tristar](../componenti/tristar.md)
- [pmic](../componenti/pmic.md)

### 3) Ricerca corto su VCC_MAIN
- Multimetro in **diode mode**.
- Probing come da fonte:
  - **rosso a massa (ground)**
  - **nero sui condensatori di VCC_MAIN**
- Interpretazione:
  - lettura **vicina a 0.000** → **corto**

Collegamenti utili:
- [condensatori-mlcc-elettrolitici-tantalio](../componenti/condensatori-mlcc-elettrolitici-tantalio.md)
- [c4005](../componenti/c4005.md)

### 4) Ispezione area Charging IC (termica/rosin)
- Controllare sotto **termocamera** o con **rosin flux** per individuare un **Charging IC** guasto.

Collegamenti utili:
- [hydra-ic](../componenti/hydra-ic.md)
- [bb-pmu](../componenti/bb-pmu.md)

### 5) Controllo sezione WiFi
- Controllare sotto **termocamera/rosin flux** per un **WiFi IC in corto**.

Collegamenti utili:
- [pmic](../componenti/pmic.md)

## Riparazione (da fonte)

### 1) Rimozione board
- Separare **prima la batteria**, poi rimuovere la board dal telaio/chassis.

### 2) Identificazione guasto (in base a DCPS + termica/rosin)
- Se si trova **corto su condensatore** → sostituire il condensatore.
- Se un **chip WiFi è caldo** → sostituire il WiFi IC.
- Se il comportamento DCPS indica **Tristar short** → sostituire **Tristar**.

Collegamenti utili:
- [tristar](../componenti/tristar.md)
- [condensatori-mlcc-elettrolitici-tantalio](../componenti/condensatori-mlcc-elettrolitici-tantalio.md)
- [hydra-ic](../componenti/hydra-ic.md)

### 3) Fix del corto
- Sostituire il componente **bruciato/shortato**:
  - condensatore in corto
  - WiFi IC
  - **Hydra charging IC**

Collegamenti utili:
- [hydra-ic](../componenti/hydra-ic.md)

### 4) Riassemblaggio e test
- Confermare **pattern di corrente corretto** (sequenza di boot come da nota fonte).
- Confermare **ricarica**.
- Confermare **boot riuscito**.
- Eseguire test **WiFi**.
- Collegare a **iTunes/PC** per riconoscimento.

## Note operative / rischi
- La fonte non specifica ulteriori dettagli di sicurezza (da verificare). In generale, su “no power” con **dead short** è fondamentale evitare alimentazioni prolungate che possono danneggiare ulteriormente rail e componenti.

## Componenti coinvolti (da fonte)
- **VCC_MAIN** (corto rail)
- **Tristar**
- **WiFi IC**
- **PMU/PMIC**
- **Charging IC / Hydra charging IC**

Collegamenti:
- [tristar](../componenti/tristar.md)
- [pmic](../componenti/pmic.md)
- [hydra-ic](../componenti/hydra-ic.md)
- [bb-pmu](../componenti/bb-pmu.md)
