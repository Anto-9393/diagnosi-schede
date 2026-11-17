---
titolo: Caso — iPad Air 4 (A2316) non carica dopo caffè
tipo: caso
riassunto: 'Dopo versamento di caffè: iniziale ripresa dopo pulizia, poi nessun fulmine
  e PC non rileva; misure su USB-C e rail indicano CD3217B12 come sospetto principale
  (X3 nuovo non risolve).'
modelli:
- iPad Air 4 (A2316)
fonti:
- raw/casi_demo/ipad-air-4-a2316-non-carica.md
aggiornato: '2026-11-17'
---

## Sintomi (caso reale)
- iPad Air 4 Wi‑Fi **A2316** spento dopo versamento di caffè.
- Dopo pulizia porta USB‑C con IPA: carica per ore (fino a ~**58–67%**), senza scaldare.
- Poi: **non carica** con **nessun fulmine** e **PC non lo rileva**.
- Da spento: inserendo il cavo si accende, ma **non carica**.
- Con batteria all’**1%**: inserendo il cavo riavvia.

## Misure chiave
### Porta USB‑C (Mechanic T‑824, diode mode)
- **VBUS (pin 4/9/16/21)**: lettura bassa e instabile; lato A instabile (corrosione nel connettore vecchio).
- **CC1/CC2 (pin 5/17)**: **0,53 / 0,63** (stabili).
- **D+/D− lato A (pin 6/7)**: **0,71 → 1,00 → 0,70** (instabile).
- **D+/D− lato B (pin 18/19)**: **0,63 → 0,61** (stabili).
- **SBU1/SBU2 (pin 8/20)**: **0,71 / 0,47** (asimmetrici, invariati).
- **RX1+ (pin 23)**: **OL → 0,00 → OL → 0,00 → OL**; ponte verso GND (pin 24) che va e viene.

**Conclusione dal connettore:** corrosione attiva nel connettore vecchio. La sostituzione del flat/connettore (15 nov) **non ha risolto** la mancata carica.

### Alimentazione / corrente
- **Senza batteria** (AiXun, USB): **5,2 V**, **0,11–0,20 A**, resta a 5 V (**nessuna negoziazione PD**).
- **Con batteria + iPad acceso**, cavo inserito: **0,002 A** → non prende corrente dall’USB.
- Batteria: **3,66 V** → scesa a ~**2,9–3,1 V**; ricaricata dal banco a **4,2 V** con ~**2–3 A** fino a **3,8 V / 45%**.

### Scheda (JC Drawing)
- **NET205** (VBUS dal flat) arriva a **X5 = CD3217B12** (controller USB‑C/PD TI).
- Uscite CD3217 verso **X3**:
  - **X1548 / X1549 / X1550**: in una prima misura **~4,7 V** (probabilmente condizione “dead battery”/senza batteria).
  - Con **batteria + cavo**: **0,026–0,186 V** → il CD3217 **non chiude il passaggio** verso X3.
- **X3 = 343S00264‑A0** (IC di ricarica):
  - con cavo inserito **scalda subito** (goccia di IPA evapora in fretta).
  - senza cavo si asciuga lentamente.
- **ROM CD3217**: marcatura **8N040** (chip piccolo accanto a X5, su JC Drawing siglato **X7**). La ROM va in coppia con il CD3217: se si sostituisce il CD3217 da donor va trasferita la ROM dello **stesso donor** o riprogrammata (Wylie).
- Termocamera: CPU ~**60 °C** (normale). Nessun punto caldo sul **CD3217**.

## Componenti coinvolti (come da caso)
- [CD3217](../componenti/cd3217.md) — **X5 = CD3217B12** (sospetto principale).
- [343S00235](../componenti/343s00235.md) — **non**: nel caso l’IC di ricarica è indicato come **343S00264‑A0** (da verificare se esiste pagina specifica per 343S00264).
- [CD3217](../componenti/cd3217.md) — **ROM 8N040** (X7 su JC Drawing).

## Interventi fatti e risultati
| Data | Intervento | Esito |
|---|---|---|
| 25 ott | Pulizia porta con IPA | carica per ore, poi smette |
| ~15 nov | **X3 sostituito** con 343S00264 nuovo | non carica |
| 15 nov | **Flat/connettore USB‑C sostituito** | non carica |

## Diagnosi (aggiornata al 15 nov)
1. **X5 CD3217B12** — sospetto n.1: con batteria **non fa passare VBUS verso X3**. Il quadro “**nessun fulmine** + **PC non rileva**” è coerente con un problema comune a carica e dati.
2. **Alimentazioni / passivi attorno al CD3217** corrosi dal caffè — da verificare prima di toccare il chip.
3. **ROM 8N040 (X7 su JC)** — meno probabile (ha caricato dopo la pulizia), ma possibile: in caso di sostituzione CD3217 usare ROM abbinata o riprogrammare.

## Prossimi step (ordine operativo)
1. Verificare con **X3 nuovo**:
   - misure su **X1548** con **batteria + cavo** (nel caso era **~0 V / molto bassa**: da confermare).
   - controllare se **X3 scalda ancora** con cavo inserito.
2. Ispezione e misure delle **alimentazioni del CD3217** (nel caso: “≈3,3 V e 1,8 V sui condensatori intorno a X5”) con batteria collegata e iPad acceso; cercare corrosione su passivi.
3. Se le alimentazioni sono presenti:
   - sostituire **CD3217 + ROM** usando una scheda donatrice A2316 (o riprogrammare ROM **8N040** con Wylie).
4. Avvisare il cliente del danno da liquido.

## Lezioni utili (da questo caso)
- Controller tipo **CD3217**: modalità **"dead battery"**. Senza batteria può lasciare passare VBUS; con batteria può aspettare firmware/comunicazione col SoC.
- Se **PC non vede** e **non carica**, prima sospettare ciò che gestisce insieme carica e dati (porta/CD3217), non solo l’IC di ricarica.
- Corrente quasi nulla (**0,002 A**) con VBUS stabile a 5 V **non** indica automaticamente corto (un corto tirerebbe corrente o farebbe intervenire protezioni).

## Strumenti usati (come nel caso)
- Mechanic **T‑824 SE**
- Alimentatore da banco **AiXun**
- Multimetro
- Termocamera **MEGA‑IDEA**
- Microscopio
- JC Drawing

## Link utili
- [CD3217](../componenti/cd3217.md)
- [343S00235](../componenti/343s00235.md)
- [iPad Air 4](../dispositivi/ipad-air-4.md)
- Tecnica correlata: [test-cd3217-e-ricerca-corti](../tecniche/test-cd3217-e-ricerca-corti.md)
