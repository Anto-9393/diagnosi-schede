---
titolo: Fonte — How To Fix an iPhone 14 that is shows temperature warning and does
  not charge
tipo: fonte
riassunto: 'iPhone 14 con warning temperatura dopo il boot e mancata carica: da riparare
  un corto su rail SPKRAMP_TOP_VBOOST (capacitore MLCC in corto).'
modelli:
- iPhone 14
fonti:
- raw/repairwiki/pagine/how-to-fix-an-iphone-14-that-is-shows-temperature-warning-and-does-not-charge.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# Fonte: How To Fix an iPhone 14 that is shows temperature warning and does not charge

> Link: https://repair.wiki/w/How_To_Fix_an_iPhone_14_that_is_shows_temperature_warning_and_does_not_charge  
> Cronologia: https://repair.wiki/w/How_To_Fix_an_iPhone_14_that_is_shows_temperature_warning_and_does_not_charge?action=history  
> Revisione: 2025-09-08T22:23:30Z  
> Licenza: CC BY-SA 3.0

## Descrizione problema
- iPhone 14 mostra **warning temperatura** quando acceso.
- Il dispositivo **carica normalmente da spento**, ma **non carica quando è acceso**.
- Una volta completato il boot, si verifica **surriscaldamento rapido**.
- Su **DCPS**: **pre-boot draw ~1A** prima del prompt di boot; poi il dispositivo avvia normalmente.

## Sintomi (riassunto)
- Compare warning temperatura **dopo il boot**.
- **Carica quando è spento**, ma **non carica quando è acceso**.
- **Surriscaldamento rapido** mentre il telefono è acceso.
- Su DCPS: **corrente pre-boot anomala ~1A** prima del prompt di boot.

## Diagnosi (passi della fonte)
1. Collegare il telefono a **DCPS** e osservare la **corrente assorbita** per confermare l’**anomala ~1A** pre-boot.
2. Usare **termocamera** per localizzare il componente che si scalda rapidamente.
3. Identificare un **capacitore in corto** sulla linea **SPKRAMP_TOP_VBOOST**.

## Riparazione (passi della fonte)
1. Rimuovere la motherboard dall’alloggiamento e **separare lo stack/layer**.
2. Eseguire una **misura di resistenza** sulla rail **SPKRAMP_TOP_VBOOST**.
3. Confermare **bassa resistenza** → indicazione di **corto**.
4. Identificare e **rimuovere il condensatore** in corto dalla rail.
5. Rifare la misura di resistenza per confermare che il corto è stato rimosso.
6. Rimontare e testare il boot con **DCPS**, verificando che la **corrente pre-boot** torni normale.
7. Accendere il telefono e verificare che la **carica** riprenda normalmente e che **non compaia più il warning temperatura**.
8. Verificare stabilità sotto carico (carica + utilizzo) prima di chiudere.

## Componenti/rail citati
- **SPKRAMP_TOP_VBOOST** (rail di alimentazione)
- **Capacitore in corto** sulla rail **SPKRAMP_TOP_VBOOST** (tipologia: da verificare nella fonte; la pagina indica “shorted capacitor”).

## Collegamenti utili (wiki)
- Sintomo correlato: [temperatura-warning-e-non-carica](../sintomi/temperatura-warning-e-non-carica.md)
- Tecnica correlata (corto su rail): [diagnosi-e-rimozione-corto-su-rail-con-capacitore-in-corto](../tecniche/diagnosi-e-rimozione-corto-su-rail-con-capacitore-in-corto.md)
- Componente correlato (capacitori MLCC/elettrolitici/tantalio): [condensatori-mlcc-elettrolitici-tantalio](../componenti/condensatori-mlcc-elettrolitici-tantalio.md)
- Dispositivo: [iPhone 14](../dispositivi/iphone-14.md)
