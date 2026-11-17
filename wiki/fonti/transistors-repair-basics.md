---
titolo: Transistors — Repair Basics (fonte esterna)
tipo: fonte
riassunto: 'Riassunto della fonte: funzioni e tipi di transistor, ispezione guasti,
  test con multimetro in diode mode (BJT/FET/IGBT) e criteri/rischi di sostituzione.'
modelli: []
fonti:
- raw/repairwiki/pagine/transistors-repair-basics.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# Transistors - Repair Basics (riassunto fonte)

Fonte esterna: [Transistors - Repair Basics — repair.wiki](https://repair.wiki/w/Transistors_-_Repair_Basics) (CC BY-SA 3.0).

## Funzione dei transistor
Un transistor è un dispositivo a semiconduttore usato per:
- **Amplificazione** di segnali deboli.
- **Switching** (interruttore elettronico) in logiche/digitali e circuiti di controllo.
- **Regolazione di tensione** (lineare o in **switch-mode** tramite commutazione rapida).
- **Controllo motori** (es. IGBT in applicazioni di potenza).

## Tipi principali (come in fonte)
- **BJT (Bipolar Junction Transistor)**: NPN e PNP.
- **FET**: JFET e **MOSFET**; in fonte si descrivono N-channel e P-channel.
- **IGBT**: combinazione di caratteristiche BJT e MOSFET, per commutazioni ad alta potenza.
- **Phototransistor**: sensibile alla luce, usato in rilevazione/isolamento (es. optocoupler).

## Come riconoscerli (indicazioni generali)
- Spesso indicati come **Qxx**.
- Transistor discreti con **3 o 4 terminali** (package plastico/metallo).

## Guasti tipici (ispezione visiva)
Prima di misurare: **ispezione**.
Segni di possibile guasto:
- **Corrosione** dei pin o della shell metallica.
- **Pin rotti** (corrosione o fatica meccanica).
- **Scolorimento** del componente o dell’area circostante (surriscaldamento).
- **Bruciature**, fori o **crepe** nel package.

La fonte segnala che spesso i transistor falliscono in **corto** (uno o più pin in corto tra loro). In caso di corto può essere necessario controllare anche altri componenti danneggiati o la causa del corto.

Possibili guasti anche **in aperto** (rottura di bond interni per sovracorrente o fatica) e **leakage resistivo** tra elettrodi (degrado/aria/umidità).

## Test con multimetro (diode mode)
> La fonte descrive test “di base” in **diode mode** e criteri di lettura.

### BJT (NPN/PNP)
**Obiettivo:** verificare che le giunzioni PN interne siano “come due diodi” con un terminale comune.

1. **Identificare pinout** (base/emettitore/collettore).
   - Se non disponibile da documentazione o inferibile dal circuito: provare combinazioni in **diode mode** cercando la configurazione “due diodi con terminale comune”.
   - Nota fonte: se il transistor è guasto, potrebbe non essere possibile ricavare il pinout con questo metodo.
   - Nota fonte: nei BJT con shell metallica può esserci una **tab** o un **punto verniciato** vicino all’emettitore; la base è il pin più vicino all’emettitore.
   - Nota fonte: alcuni power BJT hanno una **flyback diode** interna tra emettitore e collettore.

2. **Controllo corto/leakage**
   - Multimetro su **scala resistenza più alta** (o autoscale).
   - Misura tra **C (collector)** e **E (emitter)**.
   - Se < **100 Ω** → BJT **in corto**.
   - Valori da decine di kΩ fino a MΩ → possibile **leaky** (non necessariamente inutilizzabile: dipende dal circuito).
   - Inversione puntali: può evidenziare una **flyback diode** (basso in una direzione, alto nell’altra).

3. **Test giunzioni in diode mode**
   - Multimetro in **diode mode**.
   - **NPN**: puntale rosso su **B**, nero su **E** e poi su **C** → atteso **drop diodo**.
     - Tipico: **0.6–0.7 V**
     - Per Germanio vecchi: **0.2–0.5 V**
   - **PNP**: ripetere invertendo i puntali (nero su base) → stesso valore diodo.
   - Se lettura molto **più alta**, **più bassa** o **OL** → transistor **difettoso**.

### FET (N-channel / P-channel)
**Obiettivo:** verificare che il gate possa “abilitare” conduzione tra drain e source tramite carica/scarica del gate.

1. **Verifica corto D-S**
   - Prima: assicurarsi che il FET **non sia in corto**.
   - Misura resistenza tra **D (drain)** e **S (source)**.
   - Se < **100 Ω** → FET **in corto**.

2. **Test in diode mode**
   - Multimetro in **diode mode**.
   - **N-channel**:
     - rosso su **G (gate)**, nero su **S**.
     - poi passare rapidamente il rosso su **D**.
     - atteso: **bassissimo drop** (vicino a **0 V**) → conferma funzionamento.
   - **P-channel**: stessa logica ma invertendo i puntali (nero su gate).
   - Se drop alto o **OL** → FET **difettoso**.

3. Alternativa (se disponibile LCR meter)
   - Misurare **capacitance** tra **G** e **S**.
   - Valore da confrontare con **datasheet** o FET simile.

### IGBT
**Obiettivo:** in molti casi l’IGBT include una “freewheeling diode” in reverse parallel; quindi il test può ridursi a verificare la diode.

1. In **diode mode**:
   - Identificare pin: **G (gate)**, **E (emitter)**, **C (collector)**.
   - La fonte indica che spesso c’è una diode in reverse parallel; quindi si controlla che la diode sia ancora funzionale.

2. Misura consigliata dalla fonte:
   - rosso su **E**, nero su **C**.
   - atteso: drop diode tipico **0.4–0.7 V**.
   - Se drop alto/basso o **OL** → IGBT **difettoso**.

3. Alternativa (se disponibile LCR meter)
   - Misurare capacitance **G** vs **E** e confrontare con datasheet o IGBT simile.

## Criteri di sostituzione e rischi
La fonte enfatizza due punti:
1) **MAKE SURE THE PIN OUT MATCHES**: se il pinout non coincide, si rischia di danneggiare tutto ciò che è collegato.
2) Oltre al pinout, rispettare specifiche elettriche.

### BJTs — cosa considerare
- **Tipo**: NPN vs PNP (in base alla funzione originale).
- **Package/pinout** compatibile.
- **Ratings**: **VCE** e **IC** (match o superare).
- **Gain (hFE)**: in applicazioni di amplificazione, matchare il più possibile.
- **Power dissipation**: uguale o superiore.

### FETs — cosa considerare
- **Tipo**: N-channel vs P-channel.
- **Package/pinout** compatibile.
- **Ratings**: **VDS** e **ID** (match o superare).
- **RDSon**: scegliere un FET con **RDSon uguale o più basso**.
- **Gate capacitance / gate charge**: cercare valori vicini.
- **Switching characteristics**: attenzione a **Turn On/Off Delay Time** e **Rise/Fall Time** per switching sensibile.
- **Power dissipation**: uguale o superiore.

### IGBT — cosa considerare
- **Package/pinout** compatibile.
- **Ratings**: **VDS** e **ID** (match o superare).
- **RDSon**: uguale o più basso.
- **Gate capacitance**: vicino al guasto.
- **Switching characteristics**: attenzione a tempi di commutazione e rise/fall.
- **Power dissipation**: uguale o superiore.

## Collegamenti utili (pagine interne)
- [multimetro](../strumenti/multimetro.md)
- [diode](../componenti/diode.md)
- [tecniche/test-transistor-in-diode-mode.md](../tecniche/test-transistor-in-diode-mode.md)
- [tecniche/test-diodi.md](../tecniche/test-diodi.md)
