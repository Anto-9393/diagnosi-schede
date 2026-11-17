---
titolo: Fonte — iPhone 15 Pro Max not charging and no touch (U9500/U9720, vincoli
  donor)
tipo: fonte
riassunto: 'Fonte esterna su iPhone 15 Pro Max che non carica e non ha touch: diagnosi
  su U9500 (5V pad) e verifica Tigris con wireless; riparazione richiede sostituzione
  accoppiata U9500+U9720 da donor iPhone 15 Pro Max.'
modelli:
- iPhone 15 Pro Max
fonti:
- raw/repairwiki/pagine/iphone-15-pro-max-not-charging-and-no-touch.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# iPhone 15 Pro Max Not Charging and no Touch — repair.wiki (CC BY-SA 3.0)

> Fonte: [IPhone 15 Pro Max Not Charging and no Touch — repair.wiki](https://repair.wiki/w/IPhone_15_Pro_Max_Not_Charging_and_no_Touch)  
> Cronologia: https://repair.wiki/w/IPhone_15_Pro_Max_Not_Charging_and_no_Touch?action=history  
> Revisione: 2025-05-27T17:42:14Z  
> Licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)

## Contesto / problema
- Il dispositivo **non carica**.
- In aggiunta, **touch non funziona**.

## Sintomi riportati
- “Device doesn't charge.”
- “Device doesn't charge and touch is also not working.”

## Diagnosi (punti chiave)
1. **Regola prima i componenti “facili”**: test con **display e batteria nuovi**.
2. Se non carica, **non è detto** che sia U9500.
   - La fonte indica che la causa può essere anche un **Tigris IC**.
   - Test suggerito: **provare un wireless charger**.
     - Se **carica via wireless**, allora **Tigris è considerato funzionante**.
3. Per verificare U9500:
   - U9500 deve avere **5V sul pad sotto**.
   - Misura: serve **separare la motherboard**, collegare la **charging port**, poi collegare a un **charger**.
   - Interpretazione:
     - Se misuri **5V all’ingresso**, significa che U9500 **riceve alimentazione** e “should be functioning”.

## Soluzione / riparazione (vincoli donor)
- La fonte collega il problema a un **U9500 difettoso** (chip che “detects what is connected in the USB C port”).
- U9500 **non lavora da solo**: funziona in associazione con un **ROM IC (U9720)**.
- Vincolo sostituzione:
  - **Non è possibile sostituire solo U9500**.
  - Per sostituire U9500 serve sostituire anche **U9720**.
  - Entrambi devono provenire da un **donor iPhone 15 Pro Max**.
  - Vincolo esplicito: **non possono essere presi da iPhone 15 o iPhone 15 Pro**.

## Procedura di sostituzione (come riportata)
- Usare hot air per:
  - desaldare il vecchio **U9500**.
  - mentre è ancora caldo, desaldare anche il **ROM IC U1030** (nota: la fonte cita U1030 in questa fase).
- Pulizia pads della motherboard.
- Reball:
  - Reball U9500 se non pre-balled.
  - Reball U9720.
- Saldatura:
  - hot air per saldare il nuovo U9500.
  - saldare il nuovo U9720.

## Verifiche dopo la sostituzione
- Testare **carica** e **touch**.
- Collegamenti per test (come riportato):
  - collegare **charging port, screen e battery** al **top board**.
  - La fonte afferma che l’iPhone 15 Pro Max può **power on con solo top board**.
- Misura corrente:
  - collegare a un charger.
  - usare un **amp meter** per misurare la corrente assorbita.

## Final testing (come riportato)
- Dopo rimontaggio: verificare **tutte le funzioni**, non solo la charging circuit.
- Fast charge:
  - collegare a un **fast charger**.
  - se fast charging: dovrebbe richiedere **9V** e **~2+ A**, “depending on battery capacity”.
- Data transfer:
  - collegare a un computer e verificare trasferimento dati.
- Audio:
  - collegare **USB-C headphones** e confermare audio.

## Componenti citati (mappatura wiki)
- [U9500](../componenti/u9500.md) — controller/detect USB-C port; richiede **5V sul pad sotto**.
- [U9720](../componenti/u9720.md) — ROM IC associato a U9500 (sostituzione accoppiata).
- [Tigris IC](../componenti/rigel-u4400.md) — la fonte lo cita come possibile causa; test con wireless charger.

## Note / incongruenze da verificare
- La fonte dice “ROM IC (U9720)”, ma nella fase di desolder durante la sostituzione cita anche **“ROM IC U1030”**. Da verificare se U1030 sia un refuso o un riferimento corretto nel contesto della procedura.
