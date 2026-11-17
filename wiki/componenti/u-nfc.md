---
titolo: U_NFC — chip NFC (possibile causa di corto su bottom board)
tipo: componente
riassunto: 'In alcuni casi U_NFC crackato può causare un corto nella bottom board:
  iPhone 11 Pro/Pro Max con assorbimento ≥2 A da DCPSU prima del prompt di boot.'
modelli:
- iPhone 11 Pro
- iPhone 11 Pro Max
fonti:
- raw/repairwiki/pagine/iphone-11-not-powering-on-2a-or-higher-power-draw-after-prompt-to-boot.md
- raw/repairwiki/pagine/iphone-11-pro-and-iphone-11-pro-max-not-powering-on-2a-or-higher-power-draw-after-prompt-to-boot.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Funzione
Da fonte: **U_NFC** è citato come possibile componente che, in alcuni casi, può **crackare** e causare un **corto “within the bottom board”** (bottom board).

> Nota: la fonte non descrive ulteriori funzioni elettriche/di controllo di U_NFC in questo contesto. **Da verificare**.

## Dove si trova
Da fonte: il corto può essere presente **nella bottom board**. La posizione precisa di U_NFC sulla scheda non è indicata nella fonte. **Da verificare**.

## Sintomi tipici quando si guasta
Scenario da fonte (per iPhone 11 Pro/11 Pro Max):
- **non si accende**
- **assorbimento ≥ 2 A** da **DCPSU** **prima** del **prompt di boot**.

## Cause / modalità guasto (da fonte)
- **U_NFC crackato**: in alcuni casi il chip può crackare e causare un **corto nella bottom board**.

## Misure utili (diagnosi)
### 1) Ispezione visiva completa e controllo danni da liquidi
Da fonte:
- Ispezione completa della board.
- Controllo **water damage sotto le sticker sul retro**.
- Rimozione della **foam attorno ai connettori** per vedere meglio corrosione su componenti/IC.

### 2) Se non c’è water damage: ricerca corto su rail con iniezione
Da fonte: se non c’è water damage, il problema è **più spesso** un **condensatore cortocircuitato** su una delle linee indicate.

Linee citate dalla fonte:
- **PP_VDD_MAIN** (più probabile)
- **PP_VDD_BOOST** (di solito corto quando non è VDD MAIN)
- **U_NFC** (in alcuni casi, come origine rara del corto nella bottom board)

Procedura (da fonte):
- Misura quale linea risulta **in corto** (metodo di misura non specificato dalla fonte; **da verificare**).
- **Inietta 4 V / 2 A** **direttamente** sulla **linea misurata come short**.
- Usa **freeze spray** o **termocamera** per individuare il componente che si scalda (tipicamente il **condensatore in corto**).

Valutazione da fonte:
- In questi casi spesso **si rimuove il condensatore corto** e **non si sostituisce**.
- La fonte motiva la scelta con la riduzione del rischio legato a ulteriore calore sulla board.

### 3) Caso “2 layer board”: separazione top/bottom board
Da fonte: la scheda è descritta come **2 layer board**.
- Separare la sandwich in **top board** e **bottom board**.
- Collegare **solo la top board** al **DC Power Supply**.
  - Se il corto **rimane**: colpevole sulla **top board**.
  - Se il corto **sparisce**: colpevole sulla **bottom board**.
- In quel caso, la fonte indica di **iniettare sulla bottom board** per localizzare il corto.

### 4) Attenzione all’iniezione via connettore batteria (PP_BATT_VCC / PP_VDD_MAIN)
Da fonte:
- Se si inietta tramite **battery connector** (es. iPower Pro / DT880), può scaldarsi **Yangtze** **istantaneamente**.
- Motivo da fonte: **PP_BATT_VCC** collega **PP_VDD_MAIN** e crea molta dissipazione.
- Da fonte: spesso il corto non è il chip, ma un **condensatore corto**; in rari casi può essere **Yangtze**.
- Da fonte: provare a rimuovere **Yangtze** e controllare eventuali short sotto.

## Valori attesi / condizioni (da fonte)
- **DCPSU**: assorbimento **≥ 2 A** **prima** del **prompt di boot**.
- **Iniezione**: **4 V / 2 A** sulla **linea misurata come short**.

## Su iPhone 11 Pro
- Scenario da fonte: **non powering on** con **≥2 A** da **DCPSU** prima del **prompt di boot**.
- **U_NFC**: citato come possibile causa rara (crack → corto nella bottom board).

## Su iPhone 11 Pro Max
- Scenario da fonte: **non powering on** con **≥2 A** da **DCPSU** prima del **prompt di boot**.
- **U_NFC**: citato come possibile causa rara (crack → corto nella bottom board).

## Collegamenti utili
- [tecniche/ricerca-corto-iniezione-bassa-tensione-e-termocamera.md](../tecniche/ricerca-corto-iniezione-bassa-tensione-e-termocamera.md)
- [tecniche/diagnosi-e-rimozione-corto-su-rail-con-capacitore-in-corto.md](../tecniche/diagnosi-e-rimozione-corto-su-rail-con-capacitore-in-corto.md)
- [componenti/rigel-u4400.md](../componenti/rigel-u4400.md) (citato dalla fonte come raro)
