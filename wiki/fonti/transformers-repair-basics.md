---
titolo: Transformers — Repair Basics (fonte esterna)
tipo: fonte
riassunto: 'Riassunto della fonte: funzione dei trasformatori, tipi, guasti tipici,
  test (continuità/resistenza/induttanza) e considerazioni di sostituzione/rewiring.'
modelli: []
fonti:
- raw/repairwiki/pagine/transformers-repair-basics.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# Transformers - Repair Basics (repair.wiki)

> Fonte: [Transformers - Repair Basics — repair.wiki](https://repair.wiki/w/Transformers_-_Repair_Basics) (CC BY-SA 3.0).

## Funzione
Un trasformatore trasferisce energia tra due o più circuiti **tramite induzione elettromagnetica**, senza collegamento elettrico diretto tra avvolgimenti.

Usi principali (da fonte):
- **Conversione di tensione** (step-up/step-down) tramite rapporto spire tra **primario** e **secondario**.
- **Isolamento galvanico** tra primario e secondario (tipico nelle alimentazioni AC-DC).
- **Sensing di corrente** con trasformatore di corrente (replica scalata della corrente primaria in AC).

In schemi elettrici è spesso indicato come **T1/T2/TR1/TR2**.

## Tipi
La fonte distingue (in base a funzione/struttura):
- **Power transformers**: alta potenza/corrente, alta efficienza.
- **Isolation transformers**: isolamento tra primario e secondario, comuni nelle PSU.
- **Autotransformers**: un solo avvolgimento con prese; **non** forniscono isolamento galvanico.
- **Audio transformers**: accoppiamento/impedenza e isolamento in circuiti audio (meno usati).

## Guasti tipici
La fonte indica guasti come:
- **Avvolgimenti in corto**
- **Circuito aperto**
- **Degrado dell’isolamento**

Cause ricorrenti (da fonte): **sovracorrente**, **surriscaldamento**, **invecchiamento**.

Nota importante della fonte: i trasformatori “raramente falliscono” se il resto del circuito è progettato correttamente; spesso il guasto del trasformatore è **un sintomo** e non la causa (da verificare caso per caso).

## Test (diagnosi)
Prima di misurare: **ispezione visiva** per segni di bruciature, rotture dell’isolamento, deformazioni.

### Continuità, resistenza e induttanza
La fonte consiglia di testare il trasformatore **fuori circuito**:
1. **Desaldare** il trasformatore (in-circuit è difficile da misurare se non è già “aperto/blown”).
2. **Identificare i terminali** dei due avvolgimenti (primario/secondario) da schema o marcature.
3. **Continuità** con multimetro: verificare che ogni avvolgimento sia elettricamente continuo.
   - Un **open** indica una rottura del filo dell’avvolgimento.
4. **Resistenza DC** di primario e secondario:
   - **Resistenza estremamente bassa** → possibile avvolgimento in corto.
   - **Resistenza anormalmente alta** → possibile rottura interna o connessioni degradate.

Per la parte “bassa resistenza”: la fonte dice che è **difficile** misurare il “basso” senza un riferimento; alternativa:
- usare un **LCR meter** per misurare l’**induttanza** di ciascun avvolgimento, se si dispone di un datasheet/trasformatore di riferimento.

## Sostituzione / riparazione
La fonte afferma che in **9/10 casi** non è pratico comprare un trasformatore sostitutivo “diretto” (serve spesso un componente da **donor board/device**), perché spesso è scelto e progettato specificamente per quel circuito.

Se è un trasformatore standard:
- verificare che le **specifiche** coincidano.

### “Sostituzione” tramite rewiring (riparazione)
La fonte descrive come principale metodo di ripristino:
- Aprire il trasformatore (spesso il **core** è diviso in due parti e tenuto con colla).
- **Non rompere** il core: può degradare le prestazioni.
- **Svolgere** ogni avvolgimento singolarmente, mantenendo:
  - **numero di spire**
  - **ordine** degli avvolgimenti (la fonte sottolinea che è “really important”).
- Se l’isolamento non è danneggiato: riutilizzare l’isolante.
- Misurare il **diametro del filo** dell’avvolgimento guasto (o di tutti se serve sostituire più avvolgimenti) e usare lo stesso **filo smaltato (enameled)**.
- Ricreare lo stesso numero di spire, nello stesso ordine, e **incollare** il core.

Avvertenza finale della fonte: un **rapporto spire errato** può danneggiare i circuiti.

## Collegamenti utili (wiki)
Per diagnosi e riparazione su componenti di potenza/induttivi, vedi:
- [induttori](../componenti/induttori.md)
- [tecniche/test-induttori.md](../tecniche/test-induttori.md)
- [sintomi/induttore-danneggiato-o-aperto.md](../sintomi/induttore-danneggiato-o-aperto.md)

(Nota: la fonte è specifica per “transformers”; in ambito iPhone/iPad spesso i guasti su induttivi/trasformatori si gestiscono con logiche simili di continuità/induttanza, ma i dettagli di misura e i componenti esatti vanno verificati sul caso e sulla board.)
