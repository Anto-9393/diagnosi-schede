# iPad Air 4 Wi-Fi (A2316) — non carica dopo caffè

**Stato:** in corso — X3 e flat USB-C sostituiti, ancora non carica; prossimo: CD3217 · **Periodo:** 25 ott – 17 nov 2026

## Sintomi

- Arrivato: caffè versato, si era spento e non caricava.
- Dopo pulizia con IPA della porta: ha caricato per ore (fino a ~58–67%), senza scaldare.
- Poi: smette di caricare, **nessun fulmine**, **il PC non lo rileva**.
- Da spento, inserendo il cavo, si accende (ma non carica).
- Con batteria all'1%, inserire il cavo lo faceva riavviare.

## Misure

### Porta USB-C (Mechanic T-824, diode mode)

| Pin                  | Misure nel tempo                              | Note                                                                       |
| -------------------- | --------------------------------------------- | -------------------------------------------------------------------------- |
| VBUS 4/9/16/21       | 0.00 → lato A 0.69/0.38 → di nuovo tutti 0.00 | lettura VBUS del tester bassa anche da sana; lato A instabile = corrosione |
| CC1 / CC2 (5/17)     | 0.53 / 0.63                                   | stabili                                                                    |
| D+/D− lato A (6/7)   | 0.71 → **1.00** → 0.70                        | instabile                                                                  |
| D+/D− lato B (18/19) | 0.63 → 0.61                                   | stabili                                                                    |
| SBU1 / SBU2 (8/20)   | 0.71 / 0.47                                   | asimmetrici, invariati                                                     |
| RX1+ (23)            | OL → **0.00** → OL → **0.00** → OL            | ponte verso GND (pin 24) che va e viene                                    |

Conclusione: corrosione attiva nel connettore vecchio. Flat sostituito il 15 nov → **non era la causa** della mancata carica.

### Alimentazione

- Senza batteria, USB dall'AiXun: **5,2 V, 0,11–0,20 A**, resta a 5 V (nessuna negoziazione PD).
- Con batteria e iPad acceso, cavo inserito: **0,002 A** → non prende corrente dall'USB.
- Batteria: 3,66 V → scesa a ~2,9–3,1 V → ricaricata dal banco (4,2 V, ~2–3 A) fino a **3,8 V / 45%**.

### Scheda (JC Drawing, `iPxdAir4_WIFI_A2316 motherboard copperAB`; Borneo non ha l'A2316)
Le sigle X… sono la numerazione di JC Drawing (copperAB), non i designatori Apple: indicare sempre anche il codice del chip.

- **NET205** (VBUS dal connettore flat): 5 V fino a **X5 = CD3217B12** (controller USB-C/PD TI).
- **X1548 / X1549 / X1550** (uscita CD3217 → ingresso X3):
  - **4,7 V** in una prima misura (probabilmente senza batteria / modalità "dead battery");
  - **0,026–0,186 V** con batteria + cavo → il CD3217 non chiude il passaggio verso X3.
- **X3 = 343S00264-A0** (IC di ricarica; _non_ 343S00394): **scalda subito col cavo inserito** (goccia di IPA evapora in fretta), senza cavo si asciuga lentamente.
- Bobine **X2020 / X2021** collegate a X3 (terminali sotto il corpo, non misurabili a puntale).
- **ROM del CD3217**: marcatura **8N040** (formato 8Nxxxx, come indicato da repair.wiki per la ROM abbinata al CD3217). Su JC Drawing è il chip piccolo accanto a X5, siglato **X7** (sigla JC). La ROM va in coppia con il CD3217: se si sostituisce il CD3217 da donor va trasferita la ROM dello STESSO donor, oppure riprogrammata (Wylie).
- Termocamera: CPU ~60 °C da accesa e aperta = normale. Nessun punto caldo sul CD3217.

## Interventi fatti
| Data | Intervento | Esito |
|---|---|---|
| 25 ott | Pulizia porta con IPA | carica per ore, poi smette |
| ~15 nov | **X3 sostituito** con 343S00264 nuovo | non carica |
| 15 nov | **Flat/connettore USB-C sostituito** | non carica |

## Diagnosi (aggiornata 15 nov)
1. **X5 CD3217B12** — ora sospettato n.1: con batteria non fa passare VBUS verso X3; nessun fulmine e PC che non rileva (carica + dati) sono entrambi compito suo.
2. **Alimentazioni / passivi intorno al CD3217** corrosi dal caffè — da verificare prima di toccare il chip.
3. **ROM 8N040 (X7 su JC)** — meno probabile (ha caricato dopo la pulizia), ma si sostituisce insieme al CD3217 da scheda donatrice, o si riprogramma.

## Ordine di intervento (da qui)
1. Verificare con X3 nuovo: X1548 con batteria + cavo (ancora ~0 V?), X3 scalda ancora col cavo?
2. Alimentazioni del CD3217 (≈3,3 V e 1,8 V sui condensatori intorno a X5), batteria collegata e iPad acceso; ispezione corrosione/passivi.
3. Se le alimentazioni ci sono: **CD3217 + ROM da scheda donatrice A2316** (oppure ROM 8N040 riprogrammata con Wylie).
4. Avvisare il cliente del danno da liquido.

## Lezioni utili

- I controller tipo CD3217 hanno una modalità **"dead battery"**: senza batteria lasciano passare VBUS da soli, con batteria aspettano firmware e comunicazione col SoC. Misurare **sempre nelle stesse condizioni** (con/senza batteria, acceso/spento).
- Se il PC non vede il dispositivo e non carica, sospettare ciò che è comune a carica e dati (porta, CD3217) prima dell'IC di carica. **Qui è stato cambiato prima X3 per il calore, ma non era la causa.**
- Corrente quasi nulla (0,002 A) con tensione VBUS stabile a 5 V **non** indica un corto: un corto tirerebbe corrente o manderebbe l'alimentatore in protezione.
- Su iPhone/iPad l'IC di carica è "power path": anche senza cavo tutta la corrente della batteria verso il sistema passa da lui, quindi da acceso è sempre un po' caldo.
- AiXun: "I-Range Show" cambia solo la **scala della lancetta**, non il limite di corrente; i numeri rossi in alto sono le misure reali.
- Su iPad, senza batteria la scheda non si avvia dal banco (manca il dato 1,8 V/gauge della batteria): per misurare la corrente mettere il banco **in parallelo** alla batteria.
- Pulendo con la calza, molto flussante e nessuna pressione: il mask del substrato si graffia facilmente.
- Alcune fonti (es. la guida repair.wiki iPad Pro 11 4th Gen) chiamano il CD3217 "charging IC": è impreciso, è il controller USB-C/PD.

## Riferimenti

- repair.wiki — ROM per iPad con CD3217: https://repair.wiki/w/How_To_Program_ROM_Chip_for_iPads_with_CD3217
- iFixit — caso A2316 che non carica: https://www.ifixit.com/Answers/View/765559/Charging+issue+++other+problem
- Video sostituzione CD3217B su A2316: https://www.youtube.com/watch?v=by-bExpuRbw

## Strumenti usati

Mechanic T-824 SE, alimentatore da banco AiXun, multimetro, termocamera MEGA-IDEA, microscopio, JC Drawing.
