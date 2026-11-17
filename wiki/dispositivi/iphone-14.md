---
titolo: iPhone 14
tipo: dispositivo
riassunto: 'iPhone 14: warning temperatura dopo boot e non carica acceso, ma carica
  da spento; causa identificata come condensatore in corto su rail SPKRAMP_TOP_VBOOST.'
modelli:
- iPhone 14
fonti:
- raw/repairwiki/pagine/iphone-14.md
- raw/repairwiki/pagine/how-to-fix-an-iphone-14-that-is-shows-temperature-warning-and-does-not-charge.md
aggiornato: '2026-11-17'
categoria: phone
codici_modello: []
componenti_chiave: []
casi: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# iPhone 14

- Uscita: September 7, 2022,
- Codici modello: da verificare (non indicati nella fonte)

## Guasti tipici e casi

### Carica solo da spento + warning temperatura dopo boot
**Sintomi (da fonte):**
- All’accensione compare **warning temperatura dopo il boot**.
- Il telefono **carica quando è spento**, ma **non carica quando è acceso**.
- **Surriscaldamento rapido** una volta che il telefono ha fatto boot.
- Su **DCPS**: **pre-boot draw ~1A** prima del prompt di boot, poi il device **boota normalmente**.

**Diagnosi (da fonte):**
1. Collegare il device a **DCPS** e osservare la corrente: confermare l’anomalia del **~1A pre-boot**.
2. Usare **termocamera** per localizzare il componente che scalda rapidamente.
3. Identificare un **condensatore in corto** sulla linea/rail **SPKRAMP_TOP_VBOOST**.

**Riparazione (da fonte):**
1. Rimuovere la motherboard dal housing e **separare gli strati**.
2. Eseguire **misura di resistenza** sulla rail **SPKRAMP_TOP_VBOOST**.
3. Confermare **bassa resistenza** (indicativa di corto).
4. Identificare e **rimuovere il condensatore in corto** dalla rail.
5. Ricontrollare la resistenza per verificare che il corto sia stato rimosso.
6. Rimontare e testare il boot con **DCPS**: verificare che il **pre-boot current draw** torni normale.
7. Verificare il comportamento di carica: **dopo la riparazione dovrebbe caricare normalmente** e senza warning temperatura.
8. Verificare stabilità sotto carico (carica + uso) prima di chiudere.

**Link utili:**
- Sintomo correlato: [temperatura-warning-e-non-carica](../sintomi/temperatura-warning-e-non-carica.md)
- Tecnica correlata (ricerca corto su rail con condensatore): [diagnosi-e-rimozione-corto-su-rail-con-capacitore-in-corto](../tecniche/diagnosi-e-rimozione-corto-su-rail-con-capacitore-in-corto.md)
- Componenti correlati (famiglia condensatori): [condensatori-mlcc-elettrolitici-tantalio](../componenti/condensatori-mlcc-elettrolitici-tantalio.md)

## Note
- **Codici modello**: da verificare (non presenti nella fonte fornita).
- Sigla esatta del condensatore su **SPKRAMP_TOP_VBOOST**: da verificare (la fonte indica solo “shorted capacitor” sulla rail, senza part number).
