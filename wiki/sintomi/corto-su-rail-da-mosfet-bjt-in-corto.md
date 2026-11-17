---
titolo: Corto su rail/power path causato da MOSFET/BJT in corto
tipo: sintomo
riassunto: 'Guasto transistor in corto può trascinare un corto su rail/power path:
  come distinguere corto reale da guasti diodi/flyback e cosa misurare in diode mode
  e in resistenza.'
modelli: []
fonti:
- raw/repairwiki/pagine/transistors-repair-basics.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Sintomo
Quando un **transistor (MOSFET/BJT/IGBT)** va in **corto** (alcuni o tutti i terminali tra loro), può causare un **corto su rail/power path**: l’alimentazione va in protezione, l’assorbimento sale, oppure il rail non riesce a stabilizzarsi.

> Nota: la fonte indica che “transistors usually fail in a short circuit” e che in caso di corto può essere necessario controllare anche il resto del circuito per danni a catena. (da verificare i net specifici iPhone/iPad: servono altre fonti per mappare rail e componenti Apple).

## Cause possibili (in ordine di probabilità)
1. **Transistor guasto in corto**
   - La fonte riporta che i transistor spesso falliscono in corto (alcuni o tutti i pin corti tra loro).
2. **Diodo/flyback interno o associato al transistor guasto**
   - Per **BJT**: la fonte segnala che alcuni power BJT possono avere **flyback diodi** tra emitter e collector.
   - Per **IGBT**: la fonte indica che spesso c’è un **freewheeling diode** in reverse parallel.
   - Per **FET**: la fonte descrive test in diode mode tramite gate/source e poi gate→drain per verificare il comportamento.
3. **Altro componente nel power path danneggiato dal corto**
   - La fonte suggerisce di ispezionare il resto del circuito perché il corto può danneggiare altri componenti o il transistor può essere stato “innescato” da un guasto precedente.

## Come distinguere “corto reale” vs guasto diodi/flyback
### 1) Controllo rapido: resistenza tra i terminali di potenza
- **FET**: misura **R tra D e S**.
  - Se misuri **< 100 Ω** → il FET è **shorted** (corto reale sul power path tramite D-S).
  - Se non è shorted, passa al test in diode mode.
- **BJT**: la fonte consiglia di cercare corto/leakage misurando **R tra C ed E**.
  - Se misuri **< 100 Ω** → BJT **shorted**.
  - Valori molto più alti possono indicare transistor “leaky” (dipende dal circuito).

### 2) Diode mode: verifica della giunzione attesa (e presenza di flyback/freewheeling)
#### BJT (diode mode)
- La fonte dice che un BJT “dovrebbe testare come due diodi con un terminale comune”.
- Procedura:
  - Identifica base/emitter/collector.
  - In **diode mode**:
    - **NPN**: **rosso su B**, nero su **E** e poi su **C** → atteso **drop ~0.6–0.7 V** (o **0.2–0.5 V** per Germanium vecchi).
    - **PNP**: inverti le sonde (nero su B).
- Interpretazione:
  - Se leggi **OL** o un drop **molto diverso** → transistor guasto.
- Attenzione flyback:
  - La fonte indica che misurare **C-E con polarità invertite** può evidenziare un **flyback diode** (basso in una direzione e alto nell’altra).

#### FET (diode mode)
- La fonte propone:
  - Se non è shorted, in **diode mode**:
    - **N-Channel**: **rosso su G**, **nero su S**.
    - Poi “sposta” rapidamente il rosso su **D**: atteso **bassissima caduta (vicino a 0)**.
    - **P-Channel**: inverti le sonde (nero su G).
- Interpretazione:
  - Se leggi **drop alto** o **OL** → FET faulty.

#### IGBT (diode mode)
- La fonte indica che spesso c’è un **freewheeling diode** in reverse parallel.
- Test:
  - **rosso su E**, **nero su C** → atteso **~0.4–0.7 V**.
  - Se leggi **alto/basso** o **OL** → IGBT faulty.

### 3) Segnali pratici
- Se **D-S** (FET) o **C-E** (BJT) risultano **< 100 Ω** → è molto probabile un **corto reale** del transistor.
- Se invece il transistor non è shorted ma in diode mode compaiono comportamenti “asimmetrici” (es. basso in una polarità e alto nell’altra) → può essere **flyback/freewheeling diode** (quindi non necessariamente un corto “diretto” del transistor).

## Misure utili (valori attesi dalla fonte)
- **FET**: 
  - **R(D-S) < 100 Ω** (a transistor scollegato o in condizioni di misura coerenti) → FET shorted.
- **BJT**:
  - **R(C-E) < 100 Ω** → BJT shorted.
  - In diode mode: drop atteso **0.6–0.7 V** (o **0.2–0.5 V** per Germanium vecchi).
- **IGBT**:
  - In diode mode **E→C**: atteso **0.4–0.7 V**.

> Condizioni di misura: la fonte non specifica “acceso/spento” o “con batteria scollegata”; per sicurezza operativa applicare sempre le buone pratiche di diagnosi (da verificare con altre pagine tecniche del piano).

## Collegamenti utili
- [Transistors - Repair Basics](../fonti/transistors-repair-basics.md) (fonte)
- Componenti transistor:
  - [transistor-mosfet-bjt-igbt-fet](../componenti/transistor-mosfet-bjt-igbt-fet.md)
- Tecnica di test:
  - [test-transistor-in-diode-mode](../tecniche/test-transistor-in-diode-mode.md)
- Sintomi correlati (da verificare):
  - [non-carica-o-non-rilevato-da-pc](../sintomi/non-carica-o-non-rilevato-da-pc.md)
  - [non-carica-o-alimentazione-instabile](../sintomi/non-carica-o-non-rilevato-da-pc.md)

## Limiti / da verificare
- La fonte non fornisce **net/rail specifici iPhone/iPad** né procedure “su rail X” con valori attesi per quei dispositivi: per completare la parte “power path iPhone/iPad” servono altre fonti (da verificare).
