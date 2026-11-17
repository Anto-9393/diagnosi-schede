---
titolo: iPhone 15 Pro Max
tipo: dispositivo
riassunto: 'iPhone 15 Pro Max morto e non carica: con DCPS assorbe 0.105–0.130 A pre-boot;
  termocamera mostra heating anomalo del charging IC; riparazione con sostituzione
  charging IC (sigla da verificare).'
modelli:
- iPhone 15 Pro Max
fonti:
- raw/repairwiki/pagine/iphone-15-pro-max.md
- raw/repairwiki/pagine/iphone-15-pro-max-dead-and-not-charging.md
aggiornato: '2026-11-17'
categoria: phone
codici_modello:
- A2849
- A3105
- A3106
- A3108
componenti_chiave: []
casi: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# iPhone 15 Pro Max — dead / non carica (charging IC scalda)

## Sintomi (caso)
- iPhone 15 Pro Max appare **dead**: nessuna risposta al tasto power e **nessuna carica** quando è alimentato dalla batteria.
- Collegandolo a **DC Power Supply (DCPS)**: il dispositivo **consuma 0.105–0.130 A** prima del prompt di boot, poi **boota normalmente** dopo il prompt.
- Con **termocamera**: il **charging IC** scalda in modo anomalo.

Fonte: raw/repairwiki/pagine/iphone-15-pro-max-dead-and-not-charging.md

## Diagnosi (misure utili)
1. **Test con DCPS**
   - Collegare l’iPhone alla DCPS.
   - Misurare la **corrente assorbita pre-boot**: valore atteso nel caso **0.105–0.130 A**.
   - Premere power per ottenere il **prompt di boot** e verificare che, dopo il prompt, il telefono **booti normalmente**.

2. **Verifica termica**
   - Usare **termocamera** (o metodo Rosin indicato nella fonte) per localizzare la sorgente di calore.
   - Nel caso, il **charging IC** mostra **heating** anomalo → indicazione di guasto del charging IC.

Fonte: raw/repairwiki/pagine/iphone-15-pro-max-dead-and-not-charging.md

## Riparazione (board-level)
> Nota: la fonte non riporta la **sigla esatta** del charging IC né i **codici componenti**; da verificare.

1. **Smontaggio**
   - Rimuovere display.
   - Scollegare la batteria.
   - Rimuovere la motherboard dall’alloggiamento.

2. **Isolamento area charging IC**
   - Separare gli strati (“split layers”).
   - Isolare l’area del charging IC usando **thermal shielding**.

3. **Sostituzione charging IC**
   - Rimuovere l’IC guasto con **hot air + flux**, sollevando con cautela.
   - Pulire le piazzole: **wick** dello stagno residuo e ispezione per danni pad.
   - Installare IC nuovo: **reball**, allineamento e re-install.

4. **Test post-riparazione**
   - Collegare a DCPS e verificare che la lettura **prima del prompt di boot** torni “normale” (la fonte non dà un valore numerico post-riparazione).
   - Verificare la **funzionalità di carica batteria**.

5. **Rimontaggio**
   - Richiudere solo dopo conferma del corretto funzionamento.

Fonte: raw/repairwiki/pagine/iphone-15-pro-max-dead-and-not-charging.md

## Componenti correlati (da collegare)
- Charging IC: **sigla da verificare** (la fonte non la specifica).
- Per procedure di ricerca corti/diagnosi su rail e termocamera: vedi [tecniche/ricerca-corto-iniezione-bassa-tensione-e-termocamera.md](../tecniche/ricerca-corto-iniezione-bassa-tensione-e-termocamera.md).

## Note / contraddizioni
- La pagina dispositivo esistente per iPhone 15 Pro Max non contiene ancora i dettagli del caso; questo contenuto va aggiunto come sezione “casi”/“guasti tipici” nella pagina dispositivo.
- Sigla del charging IC e componenti esatti: **da verificare** dalla fonte originale o da misure/identificazione sul PCB.
