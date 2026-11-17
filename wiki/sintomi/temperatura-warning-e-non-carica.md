---
titolo: Temperatura warning e non carica — pattern dopo boot
tipo: sintomo
riassunto: 'Warning temperatura che compare dopo il boot: carica solo da spento, surriscaldamento
  rapido e assorbimento anomalo ~1A su DCPS prima del prompt di avvio.'
modelli:
- iPhone 14
fonti:
- raw/repairwiki/pagine/how-to-fix-an-iphone-14-that-is-shows-temperature-warning-and-does-not-charge.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Sintomi riconoscibili (pattern)
- **Warning temperatura** che **compare dopo il boot**.
- Il dispositivo **carica quando è spento**, ma **non carica quando è acceso**.
- **Surriscaldamento rapido** una volta che il telefono ha completato l’avvio.
- Su **DCPS**: **pre-boot draw ~1A** prima del prompt di avvio; poi il device **boota normalmente**.

## Cause possibili (in ordine di probabilità)
1. **Corto su rail SPKRAMP_TOP_VBOOST** dovuto a **condensatore in corto** (la fonte indica esplicitamente un “shorted capacitor” su quella linea).
2. **Componente che va in surriscaldamento** durante/seguendo il boot (da localizzare con termocamera), con conseguente comportamento “carica da spento ma non da acceso”.

> Nota: la fonte descrive la diagnosi/repair come mirata al **corto su SPKRAMP_TOP_VBOOST** tramite identificazione del **condensatore in corto**.

## Misure e verifiche utili
### 1) Verifica assorbimento con DCPS (pre-boot)
- **Condizione**: telefono collegato a **DCPS**.
- **Osservazione attesa dalla fonte**: **corrente pre-boot ~1A** prima del prompt di boot; successivamente il device **boota normalmente**.

### 2) Localizzazione del punto caldo
- **Strumento**: [termocamera](../strumenti/termocamera.md).
- **Obiettivo**: identificare il componente che **si scalda rapidamente** durante la fase in cui compare il warning/il surriscaldamento.

### 3) Verifica resistenza sul rail indicato
- **Rail**: **SPKRAMP_TOP_VBOOST**.
- **Procedura (da fonte)**: rimozione e split layer, poi **misurazione resistenza** sul rail.
- **Esito atteso**: **bassa resistenza** che indica **corto**.

## Riparazione (diagnosi → intervento)
1. Rimuovere la scheda madre, **split layer**.
2. Misurare **resistenza** su **SPKRAMP_TOP_VBOOST**.
3. **Confermare** il corto (resistenza bassa).
4. **Identificare** e **rimuovere** il **condensatore in corto** sulla linea.
5. **Rimisurare** la resistenza per confermare che il corto è stato rimosso.
6. Rimontare e testare su **DCPS**: verificare che il **pre-boot current draw** torni normale.
7. Verificare comportamento di carica: **dopo l’intervento dovrebbe caricare normalmente** senza warning temperatura.

## Collegamenti utili
- [DCPS](../strumenti/alimentatore-da-banco.md)
- [termocamera](../strumenti/termocamera.md)
- [condensatori MLCC/elettrolitici/tantalio](../componenti/condensatori-mlcc-elettrolitici-tantalio.md)
- [batteria](../componenti/batteria.md)

## Su iPhone 14
### iPhone 14 — warning temperatura dopo boot + non carica
- **Sintomi**: warning temperatura dopo boot; carica solo da spento; surriscaldamento rapido; DCPS pre-boot ~**1A**.
- **Diagnosi indicata**: corto su **SPKRAMP_TOP_VBOOST** causato da **condensatore in corto**.
- **Intervento indicato**: rimozione del condensatore in corto e verifica resistenza/assorbimento pre-boot su DCPS.

## Fonti
- [How To Fix an iPhone 14 that is shows temperature warning and does not charge — repair.wiki](../fonti/how-to-fix-an-iphone-14-that-is-shows-temperature-warning-and-does-not-charge.md)
