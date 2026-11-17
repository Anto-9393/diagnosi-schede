---
titolo: How To Fix iPhone X That Does Not Power On — riassunto fonte
tipo: fonte
riassunto: 'Procedura e logica diagnostica per iPhone X “no power/no boot”: ispezione
  liquidi, ricerca corto su rail (PP_VDD_MAIN/PP_VDD_BOOST/PP_SPKRAMP_TOP_VBOOST),
  iniezione 4 V/2 A e localizzazione del condensatore in corto; note su sandwich board
  e falsi positivi di calore (Q3350/PMIC).'
modelli:
- iPhone X
fonti:
- raw/repairwiki/pagine/how-to-fix-iphone-x-that-does-not-power-on.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Scopo della fonte
Riparare un **iPhone X** che **non si accende / non fa boot / non mostra segni di vita** (anche “does not charge”). La fonte descrive una sequenza: ispezione visiva (in particolare danni da liquidi), poi diagnosi di **corto su rail** tramite misure di assorbimento e **iniezione di tensione** per localizzare il componente in corto.

## Sintomi riportati
- **No Power / does not turn on / no signs of life / does not boot**
- **Does not charge**
- Comportamento corrente (quando si tenta il boot):
  - “Pulls **2A or more** beyond you prompt to boot”
  - “No current draw before prompt to boot”, poi dopo il tentativo: salto rapido tra **0 A** e valori diversi (es. **0 A > 320 mA > 0 A > 1.4 A > 0 A > 500 mA**)

## Diagnosi: ispezione e causa più probabile
1. **Ispezione visiva completa** della scheda.
2. Controllo specifico di **danni da acqua** sotto gli adesivi sul retro.
3. Rimozione della **schiuma attorno ai connettori** per migliorare la visibilità.
4. Ricerca di **corrosione** su componenti e IC.

Se **non** c’è danno da acqua, la fonte indica che la causa più probabile è un **condensatore in corto**.

## Diagnosi corto: “Short Before Prompt To Boot”
Quando il corto è presente **prima** del tentativo di boot, la fonte indica di controllare queste linee:
- **PP_VDD_MAIN** (la più probabile)
- **PP_VDD_BOOST** (di solito corta se non è VDD MAIN)
- **PP_SPKRAMP_TOP_VBOOST** (più raro)

### Localizzazione del componente in corto
- La fonte richiede **iniezione di tensione 4 V / 2 A** direttamente sulla linea misurata come in corto.
- Per individuare il condensatore in corto si usano:
  - **freeze spray**
  - oppure **termocamera**

### Azione correttiva
- In questi casi, la fonte afferma che si può **rimuovere il condensatore in corto** **senza sostituirlo** e il dispositivo dovrebbe funzionare normalmente.
- Motivazione della fonte: sostituire significa aggiungere calore e aumentare il rischio di ulteriori problemi.

## Diagnosi corto: “Short After Prompt To Boot”
Se il comportamento da corto appare **dopo** il tentativo di boot:
- Controllare corti **intorno alla NAND**.
- La fonte elenca rail che spesso risultano coinvolti quando c’è un condensatore in corto:
  - **PP3V0_NAND**
  - **PP0V9_NAND**
  - **PP1v8_IO**

### Localizzazione del componente in corto
- Anche qui: **iniezione di tensione** per trovare il condensatore responsabile.

### Nota su calore di PMIC (falso indizio)
- La fonte avverte che il **PMIC (U2700)** può scaldarsi molto durante test con **DCPS collegato tramite connettore batteria**, ma **non** è necessariamente la causa del corto.
- Spiegazione della fonte: il corto è “al condensatore vicino a NAND”, ma connessi alla batteria il percorso di corrente può far scaldare il PMIC.

## Caso alternativo: corto RAM
La fonte riporta un comportamento simile anche quando è corto:
- **PP1V8_S2** oppure **PP1V1_S2**

### Come distinguerlo
- Controllare **calore sopra la CPU**.
- Se si trova corto su **PP1V8_S2 / PP1V1_S2** e **calore sopra la CPU**, la fonte conclude che può trattarsi di **RAM short**.

### Azione correttiva (molto avanzata)
- La fonte indica che serve **sostituire la RAM**.
- Avviso: riparazione **molto avanzata**, facile danneggiare la CPU; solo per chi ha “mastered this repair”.

## Note operative importanti (sandwich board / Q3350)
- Per iPhone X e modelli più recenti, la fonte dice che spesso è necessario **split della sandwich board** per accedere/diagnosticare correttamente.
- Avviso: farlo in modo errato può causare **danni permanenti**.

### Nota su iniezione tramite connettore batteria e Q3350
- Se si usa un alimentatore DC per iniettare tensione attraverso il connettore batteria (es. iPower Pro o DT880), la fonte segnala che il **Tigris Mosfet Q3350** si scalda **istantaneamente**.
- Motivo (come riportato dalla fonte): la linea **PP_BATT_VCC** collega **PP_VDD_MAIN** tramite **Q3350**, creando molta dissipazione; inoltre **Q3350 non ha connessione a massa**, quindi “è impossibile” che sia lui in corto.

## Collegamenti interni consigliati (da wiki)
- [iPhone X](../dispositivi/iphone-x.md)
- [Tristar](../componenti/tristar.md)
- [PMIC](../componenti/pmic.md)
- [Batteria](../componenti/batteria.md)
- [Tecniche: test CD3217 e ricerca corti](../tecniche/test-cd3217-e-ricerca-corti.md) (utile come riferimento generale su ricerca corto)
- [Tecniche: test diodi](../tecniche/test-diodi.md) (solo se serve escludere altri guasti)

> Nota: la fonte specifica rail e componenti (PP_VDD_MAIN, PP_VDD_BOOST, PP_SPKRAMP_TOP_VBOOST, PP3V0_NAND, PP0V9_NAND, PP1v8_IO, PP1V8_S2, PP1V1_S2, U2700, Q3350) ma non fornisce sigle/part number dei condensatori; quindi i riferimenti a componenti specifici restano “da verificare” a livello di mappatura scheda.
