---
titolo: iPhone 11 Pro
tipo: dispositivo
riassunto: 'iPhone 11 Pro: dopo prompt to boot assorbe ≥2A da DCPSU; probabile corto
  su PP_VDD_MAIN/PP_VDD_BOOST o (in alcuni casi) U_NFC.'
modelli:
- iPhone 11 Pro
- iPhone 11 Pro Max
fonti:
- raw/repairwiki/pagine/iphone-11-pro.md
- raw/repairwiki/pagine/iphone-11-pro-and-iphone-11-pro-max-not-powering-on-2a-or-higher-power-draw-after-prompt-to-boot.md
aggiornato: '2026-11-17'
categoria: phone
codici_modello: []
componenti_chiave:
- U_NFC
casi: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# iPhone 11 Pro

## Codici modello
- da verificare (non indicati nella fonte)

## Guasto tipico (da fonte)
**Sintomo:** iPhone 11 Pro / 11 Pro Max **non si accende** e mostra **assorbimento ≥2A** da **DCPSU** **prima del prompt to boot**.

### Cause più probabili (ordine dalla fonte)
1. **Corto su condensatore (capacitor shorted)** su una delle linee indicate.
2. **Corto su U_NFC**: in alcuni casi il chip può **crackarsi** e creare un corto sulla bottom board.
3. **Danni da liquidi/corrosione** (se presenti): il corto può essere anche **sotto IC** o in zone con corrosione.

### Rail/linee sospette (dalla fonte)
- **PP_VDD_MAIN** — *la più probabile*.
- **PP_VDD_BOOST** — di solito corta quando non è VDD MAIN.
- **U_NFC** — in alcuni casi il chip stesso può crackarsi e causare corto.

## Diagnosi rapida (flusso dalla fonte)
1. **Ispezione visiva completa** della scheda.
2. Controllo **danni da acqua** sotto gli adesivi sul retro.
3. Rimuovere la **schiuma/foam** attorno ai connettori per vedere meglio.
4. Cercare **corrosione** su componenti/IC.

### Se NON c’è danno da acqua
- È “**più probabile**” un **condensatore in corto** su una delle linee sopra.
- Procedere con **iniezione di tensione**:
  - **4 V / 2 A** **direttamente** sulla linea che hai misurato come corta.
- Usare **freeze spray** o **termocamera** per individuare il componente che scalda (capacitor shorted).
- **Intervento consigliato dalla fonte:** rimuovere il **solo condensatore corto** e **non sostituirlo** (il device funziona normalmente senza effetti negativi).
  - Motivazione dalla fonte: sostituire significa aggiungere calore e aumenta il rischio.

### Se c’è danno da acqua
- Prestare attenzione alle aree con **segni di corrosione**.
- La fonte indica che spesso trovi corrosione su **condensatori** ma anche **sotto IC**.
- La scheda è descritta come **2 layer** (“sandwich”):
  1. Separare in **top board** e **bottom board**.
  2. Verificare se il corto resta presente collegando **solo** la top board al DCPSU.
     - Se il corto resta: colpevole sulla **top board**.
     - Se il corto si elimina: colpevole sulla **bottom board**.
  3. In quel caso, iniettare tensione sulla **bottom board** per localizzare il corto.

## Nota specifica su iniezione via connettore batteria (da fonte)
Se inietti tramite DCPSU attraverso il **connettore batteria** (es. iPower Pro / DT880):
- può scaldarsi **Yangtze** **istantaneamente**.
- La fonte spiega che **PP_BATT_VCC** (linea del connettore batteria) collega **PP_VDD_MAIN** tramite Yangtze, creando molta dissipazione.
- In molti casi il corto non è l’IC ma un **condensatore in corto**.
- In casi rari il problema può essere **Yangtze**:
  - prova a **rimuovere Yangtze** e controllare se ci sono **corti sotto**.

## Collegamenti utili (wiki)
- Linee/rail e ricerca corto con termocamera/freeze spray: [tecniche/ricerca-corto-iniezione-bassa-tensione-e-termocamera.md](../tecniche/ricerca-corto-iniezione-bassa-tensione-e-termocamera.md)
- Componenti citati dalla fonte:
  - [componenti/c4005.md](../componenti/c4005.md)
  - [componenti/condensatori-mlcc-elettrolitici-tantalio.md](../componenti/condensatori-mlcc-elettrolitici-tantalio.md)
  - [componenti/u-nfc.md](../componenti/u-nfc.md)

## Casi reali
- da verificare (non presenti nella fonte fornita)

---

Fonte usata per questa pagina: raw/repairwiki/pagine/iphone-11-pro-and-iphone-11-pro-max-not-powering-on-2a-or-higher-power-draw-after-prompt-to-boot.md (CC BY-SA 3.0).
