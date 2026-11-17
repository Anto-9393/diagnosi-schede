---
titolo: iPhone 11
tipo: dispositivo
riassunto: 'iPhone 11 non si accende: su DCPS la corrente sale e si blocca dopo prompt;
  fonte aggiunge anche caso “2 A o più prima del prompt” con probabile corto su PP_VDD_MAIN/PP_VDD_BOOST
  e ricerca con iniezione 4 V/2 A + freeze spray/termocamera.'
modelli:
- iPhone 11
fonti:
- raw/repairwiki/pagine/iphone-11.md
- raw/repairwiki/pagine/how-to-repair-iphone-11-dead-not-charging.md
- raw/repairwiki/pagine/iphone-11-not-powering-on-2a-or-higher-power-draw-after-prompt-to-boot.md
aggiornato: '2026-11-17'
categoria: phone
codici_modello: []
componenti_chiave: []
casi: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# iPhone 11

- Uscita: 2019-09-20
- Codici modello: da verificare (non indicati nella fonte)

## Guasti tipici e casi

### Dead / non carica (stuck su DCPS dopo prompt)
**Sintomi (fonte):**
- Il telefono **non si accende**.
- Collegato a **alimentatore DC (DC power supply)**: dopo il prompt di avvio, la **corrente sale a 0.140–0.150 A** e **rimane bloccata**.
- Se si **separa lo split della logica** (lower/upper layer), il device **boota** normalmente.
- Il problema **si ripresenta** se si rimonta il board in modo completo, finché non si esegue il **reball della CPU**.

**Causa probabile (fonte):**
- **Cold solder issues sotto la CPU**, legate a stress termico e/o flessioni/urti; la CPU perde contatto in modo intermittente con la logic board.

**Diagnosi (fonte):**
1. Collegare il telefono a una **DC power supply** e osservare il comportamento: dopo prompt, la corrente **si assesta a ~0.140–0.150 A** e non prosegue.
2. Eseguire lo **split del logic board** (lower e upper layer): se il telefono boota normalmente con le due parti separate, la diagnosi punta a **problema di contatto/saldatura fredda sotto CPU**.
3. Rimontare: il device torna allo **stesso stuck state** (conferma).

**Riparazione / risoluzione (fonte):**
1. Rimuovere la logica e **split board**.
2. Ispezionare le **saldature/ball della CPU** sotto microscopio (possibili segni di cracked/cold joints).
3. Eseguire **reball CPU**: rimozione residui di stagno dai pad, applicazione nuove **solder balls** con stencil, reflow con profilo controllato.
4. Rimontare i layer e reinstallare la CPU.
5. Test su **DC power supply**: il device dovrebbe **boottare normalmente**.

**Avvertenze (fonte):**
- La procedura è indicata **solo per data recovery**.
- Dopo il reball, l’**underfill/glue di fabbrica sotto la CPU non è più presente**, rendendo la scheda **molto più vulnerabile**: anche una piccola caduta o flessione può causare ulteriori guasti o perdita totale di funzionalità.
- Non garantire affidabilità oltre l’estrazione dati riuscita.

**Link utili (piano):**
- Tecnica: [sandwich-board-separation-e-reball-bb-pmu](../tecniche/sandwich-board-separation-e-reball-bb-pmu.md)

---

### Dead / non carica (assorbimento ≥2 A da DCPS prima del prompt to boot)
Questa sezione integra una fonte specifica per iPhone 11 con comportamento diverso dal “0.140–0.150 A dopo prompt”.

**Sintomi (fonte):**
- iPhone 11 **non si accende**.
- Su **DCPS** assorbe **2 A o più** prima del **prompt to boot**.

**Causa probabile (fonte):**
Se non c’è danno da liquidi, è **più probabile un condensatore in corto** su una delle linee:
- **PP_VDD_MAIN** (la più probabile)
- **PP_VDD_BOOST** (di solito corta quando non è VDD MAIN)
- **U_NFC** (in alcuni casi il chip può crackarsi e causare un corto sul bottom board)
- **Rigel (U4400)** (più raro)

**Diagnosi / verifica (fonte):**
1. **Ispezione visiva completa** della board.
2. Controllo per **danno da acqua** sotto le sticker sul retro.
3. Rimozione della **foam** attorno ai connettori per migliorare l’ispezione.
4. Cercare **corrosione** su/attorno a componenti e IC.
5. Se **non** c’è danno da acqua: trattare come **short su rail** e procedere con ricerca del componente in corto.

**Ricerca del corto (fonte):**
- Serve **iniezione di tensione 4 V / 2 A** direttamente sulla **linea** dove è stato misurato il corto.
- Usare **freeze spray** o **termocamera** per individuare il condensatore che si scalda (quindi in corto).

**Riparazione (fonte):**
- In questi casi puoi **rimuovere il condensatore in corto** e **non sostituirlo**: il device dovrebbe funzionare normalmente.
- Motivo (fonte): sostituire aggiunge calore e aumenta il rischio di peggiorare la scheda.

**Caso con danno da liquidi (fonte):**
- Prestare attenzione alle aree con segni di corrosione.
- Spesso la corrosione è su condensatori, ma anche **sotto IC**.

**Uso dello split board (fonte):**
- La board è descritta come **2 layer**: si può separare in **top board** e **bottom board**.
- Collegando il **top layer** alla DCPS da solo:
  - se lo **short resta**, il colpevole è sul **top board**
  - se lo **short si elimina**, il corto è sul **bottom board**
- In quest’ultimo caso si procede con iniezione sulla **bottom board**.

**Nota importante su iniezione via connettore batteria (fonte):**
- Se si inietta tensione tramite il **battery connector** (es. iPower Pro o DT880), attenzione: la linea **PP_BATT_VCC** collega **PP_VDD_MAIN** e può causare **riscaldamento istantaneo** (“Yangtze may heat up instantly”).
- In molti casi il corto non è l’IC ma un **condensatore in corto**.
- In rari casi il problema può essere la **Yangtze**: in tal caso controllare corti sotto la Yangtze e, se necessario, sostituirla.

---

## Note
- Valori “stuck” dopo prompt: **0.140–0.150 A** (fonte: pagina già presente in questa voce).
- Valori “prima del prompt”: **≥2 A** (fonte: raw/repairwiki/pagine/iphone-11-not-powering-on-2a-or-higher-power-draw-after-prompt-to-boot.md).
- Codici modello: **da verificare** (non presenti nelle fonti fornite).
