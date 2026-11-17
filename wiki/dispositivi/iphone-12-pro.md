---
titolo: iPhone 12 Pro
tipo: dispositivo
riassunto: 'iPhone 12 Pro con non carica e touch assente: spesso legato a Kraken IC;
  diagnosi con DCPS e riparazione con sostituzione/reball del Kraken.'
modelli:
- iPhone 12 Pro
fonti:
- raw/repairwiki/pagine/iphone-12-pro.md
- raw/repairwiki/pagine/how-to-fix-an-iphone-12-pro-that-is-not-charging-and-touch-not-working.md
aggiornato: '2026-11-17'
categoria: phone
codici_modello: []
componenti_chiave:
- Kraken IC
casi: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# iPhone 12 Pro

- Uscita: 2020-10-23
- Codici modello: da verificare (non indicati nella fonte)

## Guasti tipici e casi

### Caso: non carica + touch non funziona (spesso Kraken IC)

**Sintomi riportati (da fonte):**
- iPhone non carica.
- Nessuna risposta quando si collega il caricatore.
- Touchscreen non funziona.
- Il dispositivo può accendersi usando [DCPS](../strumenti/alimentatore-da-banco.md), ma **non rileva la connessione USB**.
- Possibile **assorbimento di corrente anomalo** su DCPS quando si tenta il boot (picco/andamento irregolare).

**Cause più probabili (da fonte):**
- Guasto del **USB IC**, noto come **Kraken IC**.
- Trigger frequente: uso di caricabatterie aftermarket o di scarsa qualità; in alternativa può guastarsi anche “spontaneamente”.

#### Diagnosi (da fonte)
1. **Test con parti note buone**
   - Provare con **charging port flex** e **batteria** funzionanti.
   - Se il problema persiste, passare a sospetto di guasto a livello scheda.
2. **Ispezione visiva**
   - Controllare danni di scheda, corrosione o segni di **liquid ingress** vicino all’area USB / IC di ricarica.
3. **Test con DC power supply (DCPS)**
   - Collegare il dispositivo alla DCPS.
   - Se la corrente assorbita è **anomala** (andamento irregolare/picco quando “prompt to boot”) → **probabile Kraken IC**.

> Nota: la fonte non riporta valori numerici di corrente/tensione; per i settaggi e le modalità operative fare riferimento a [tecniche/test-dcps-e-diagnosi-kraken-ic.md](../tecniche/test-dcps-e-diagnosi-kraken-ic.md).

#### Riparazione (da fonte)
1. **Accesso scheda**
   - Rimuovere la logic board con attenzione.
   - Separare lo “sandwich layer”.
   - Isolare l’area dell’IC di ricarica (Kraken).
2. **Preparazione**
   - Applicare flux attorno al Kraken IC.
   - Usare hot air con flusso/temperatura controllati.
3. **Sostituzione IC**
   - Rimuovere il Kraken IC difettoso.
   - Pulire i pad con solder wick e flux.
   - Eseguire **reball** oppure usare un IC nuovo.
   - Allineare e reflow del Kraken IC sostitutivo.
4. **Test**
   - Rimontare.
   - Collegare a caricatore e verificare la funzione di ricarica.
   - Verificare che il touch sia **completamente ripristinato**.

#### Collegamenti utili
- Componente: [Kraken IC USB](../componenti/kraken-ic-usb.md)
- Sintomo correlato: [non carica e touch non funziona](../sintomi/non-carica-e-touch-non-funziona.md)
- Tecnica/diagnosi con DCPS: [test-dcps-e-diagnosi-kraken-ic](../tecniche/test-dcps-e-diagnosi-kraken-ic.md)
- Strumento: [DC power supply (DCPS)](../strumenti/alimentatore-da-banco.md)

## Componenti chiave (da completare)
- Kraken IC (da verificare sigla/part number specifico per iPhone 12 Pro: la fonte parla di “Kraken IC” senza sigla).

## Codici modello (da completare)
- da verificare (non indicati nella fonte).
