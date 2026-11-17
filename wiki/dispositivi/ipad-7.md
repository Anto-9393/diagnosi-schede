---
titolo: iPad 7
tipo: dispositivo
riassunto: 'iPad 7 (A2197/A2198/A2199/A2200): non carica; circuito tipicamente coinvolge
  porta di ricarica, filtri F3700/F3750, mosfet Q8550, DZ8550/R8550 e Tristar U1700
  (610A3B).'
modelli:
- iPad 7
fonti:
- raw/repairwiki/pagine/ipad-7.md
- raw/repairwiki/pagine/ipad-7-not-charging.md
aggiornato: '2026-11-17'
categoria: tablet
codici_modello: []
componenti_chiave:
- Tristar U1700 (610A3B)
- Q8550
- DZ8550
- R8550
- F3700
- F3750
casi: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# iPad 7 (A2197/A2198/A2199/A2200) — non carica

## Guasti tipici
- L’iPad **non carica la batteria**.

## Componenti chiave (da controllare)
- **Porta di ricarica / charge port flex**: se non arriva tensione ~5 V dalla sorgente di ricarica alla mainboard, può essere necessario sostituire il flex della porta.
- **Tristar — U1700 (610A3B)**: componente “common to fail” su iPad 7, spesso associato a **cavi di bassa qualità**.
- **Mosfet Q8550**: se la tensione in uscita non è corretta, Q8550 può essere guasto.
- **DZ8550**: se la tensione non è corretta (o non si ottiene la caduta attesa), può essere guasto.
- **R8550**: se la tensione non è corretta (o non si ottiene la caduta attesa), può essere guasto.
- **Filtri F3700 e F3750**: se dopo la porta non si misura tensione (o si misura molto meno di 5 V, es. ~2 V), i filtri possono essere guasti e vanno sostituiti.

## Sintomi che indirizzano verso Tristar
- **Carica solo quando l’iPad è spento**.
- **Carica solo in una posizione** (problema meccanico/elettrico legato al circuito di ricarica, indicato come correlato a Tristar).

## Diagnosi (ordine consigliato)
1. **Verifica batteria (se possibile)**: su iPad che non caricano, le 3 cause più comuni indicate sono **batteria**, **charge port**, **Tristar**.
2. **Ispezione porta di ricarica**: controllare **detriti**, **danni fisici** e **danni da liquido**.
3. **Controllo circuito di carica — arrivo 5 V**:
   - Misurare sulla mainboard che la tensione **~5 V** dal caricatore arrivi effettivamente.
   - La fonte indica che il punto di misura “filter” dovrebbe essere **~5 V**.
4. **Se non c’è tensione ~5 V** con caricatore inserito:
   - Sostituire il **charge port flex**.
5. **Se la tensione è presente ma bassa** (esempio riportato: **~2 V**):
   - Sostituire i **filtri F3700 e F3750**.
6. **Verifica mosfet Q8550**:
   - Se la tensione in uscita non è corretta, la fonte indica che possono essere guasti **Q8550**, **DZ8550** o **R8550**.
7. **Test Tristar U1700 (610A3B) — misura caduta in diode scale**:
   - La fonte indica che il Tristar **riduce la caduta** da **600 mV a 30 mV (o meno)**.
   - Se **non** si ottiene la riduzione attesa, **sostituire U1700**.

## Riparazione (alto livello)
### Porta di ricarica
- La fonte specifica che la **charge port è saldata a un flex** sulla mainboard.
- Per la sostituzione: **flux**, **saldatore** e **microscopio** (consigliato).
- La fonte rimanda a una guida video (da seguire):
  - https://www.youtube.com/watch?v=p10B2fW9zOI

### Sostituzione Tristar U1700 (610A3B)
- La fonte indica che su iPad 7 il Tristar è **non underfilled**, quindi la sostituzione è “non that bad”.
- Procedura indicata:
  - **stazione ad aria calda** per dissaldare il Tristar;
  - **pulizia pad** sulla mainboard;
  - **reball** del nuovo Tristar se non è pre-balled;
  - risaldatura con hot air.
- La fonte rimanda a una guida video:
  - https://www.youtube.com/watch?v=YIoUyNI3ajE

## Test finale
- Se sostituisci la **charge port**:
  - verificare che **carica** e che funzioni anche **data transfer**;
  - testare che funzionino **entrambi gli speaker**.
- Se sostituisci il **Tristar**:
  - verificare che l’iPad **carichi** e che sia in grado di **trasferire dati**.

## Note
- Valori e componenti sono quelli riportati dalla fonte esterna; eventuali dettagli su punti di misura esatti e procedure di test strumentali “passo-passo” sono **da verificare** (la fonte fornisce solo l’ordine logico e i valori attesi principali: ~5 V, ~2 V, caduta 600 mV → 30 mV).

---

Fonte: [IPad 7 Not Charging — repair.wiki](https://repair.wiki/w/IPad_7_Not_Charging), CC BY-SA 3.0.
