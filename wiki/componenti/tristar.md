---
titolo: Tristar — controller USB/charging (U3500/610A3C)
tipo: componente
riassunto: 'Aggiorna Tristar includendo la variante 610A3C: su iPad Pro 12.9 3rd Gen
  è tra le cause di non carica (0.01–0.15 A assorbiti) e va verificato con ricerca
  corto attorno all’IC.'
modelli:
- iPad Pro 10.5
- iPad Pro 11in 1st gen
- iPad Pro 12-9 3rd gen
- iPad 7
fonti:
- raw/repairwiki/pagine/how-to-diagnose-fix-an-iphone-7-that-does-not-charge-takes-0-006a-via-usb.md
- raw/repairwiki/pagine/how-to-fix-an-ipad-air-that-will-not-charge-or-power-on.md
- raw/repairwiki/pagine/how-to-fix-an-iphone-8-plus-boot-looping-on-apple-logo-and-random-charging.md
- raw/repairwiki/pagine/how-to-fix-iphone-7-that-does-not-turn-on-hangs-at-0-020-0-030-a-after-you-prompt-to-boot-on-dc-power-supply.md
- raw/repairwiki/pagine/how-to-fix-iphone-x-that-does-not-charge.md
- raw/repairwiki/pagine/how-to-fix-iphone-x-that-does-not-power-on.md
- raw/repairwiki/pagine/how-to-repair-ipad-6-no-power.md
- raw/repairwiki/pagine/how-to-repair-ipad-pro-10-5-not-charging-or-not-detected-by-pc.md
- raw/repairwiki/pagine/ipad-7-not-charging.md
- raw/repairwiki/pagine/ipad-pro-11in-1st-gen-not-recognized-by-pc-in-recovery-mode-or-charging-issues.md
- raw/repairwiki/pagine/ipad-pro-12-9-3rd-gen-not-charging-repair.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Funzione
Il **Tristar** (IC USB/charging) gestisce la parte di **charging** e la **negoziazione/riconoscimento USB** verso PC.

- Su iPad Pro 10.5 la pagina esistente collega il guasto spesso a **U3500 (Tristar)**.
- La fonte esterna aggiunge che su alcuni iPad Pro esiste una variante **speciale “A3C”**: **Tristar 610A3C**, usata per gestire principalmente **5V USB-A** e non retrocompatibile con altri Tristar. (da verificare per iPad Pro 12.9 3rd Gen: la fonte esterna la cita come possibile causa di non carica, ma non specifica la logica 5V/PD)

## Dove si trova
### iPad Pro 10.5
- Da verificare (la pagina esistente non riporta posizione/sigla di layer; indica solo che è coperto da shield/armour).

### iPad Pro 11in 1st gen
- La fonte esterna indica che il **Tristar 610A3C** è nascosto sotto una parte dello shield sopra i **screen FPC connectors** in **mezzo alla board**.
- Per accedere serve rimuovere abbastanza shield (la fonte suggerisce grinding tool o snips).

### iPad Pro 12-9 3rd gen
- Da verificare (la fonte esterna non descrive posizione fisica del Tristar sulla board).

### iPad 7
- Da verificare (la pagina esistente non riporta posizione/sigla di layer; indica solo che è sostituibile con hot air).

## Sintomi tipici quando si guasta
### iPad Pro 10.5 — non carica e non rilevato da PC
Condizioni (pagina esistente):
- iPad **non carica**
- **nessuna icona di carica**
- **PC non rileva** il dispositivo (nessun suono di riconoscimento USB)
- nessuna comunicazione dati
- cavo/brick nuovi non risolvono
- il dispositivo può comunque accendersi se la batteria ha carica

### iPad 7 — non carica (e casi correlati)
Condizioni (pagina esistente):
- “The iPad does not charge the battery”
- se presenti: **iPad charges but only turned off**
- se presenti: **iPad only charges in one position**
- la pagina esistente collega questi comportamenti al **Tristar**

### iPad Pro 12-9 3rd gen — assorbimento quasi nullo (0.01–0.15 A)
Condizioni (fonte esterna):
- Il dispositivo **pulls zero or very few (0.01–0.15) amps** dal caricatore.
- L’iPad **può o non può** boot.

### iPad Pro 11in 1st gen — carica solo in un caso (PD 15V vs USB-A 5V) e/o mancato collegamento a PC
Condizioni (pagina esistente + fonte esterna):
- La fonte esterna descrive che la variante **610A3C** è legata a **5V USB-A** e che può esserci comportamento “solo su una tipologia di alimentatore”.
- La pagina esistente riporta anche casi di mancato riconoscimento/negoziazione verso PC.

## Criteri diagnostici (misure utili)
### iPad Pro 10.5 — conferma fault U3500 (Tristar)
La pagina esistente propone la sostituzione di **U3500 (Tristar)** se (pagina esistente):
- assorbimento **abnorme**
- “dock test” passa (dock flex noto-good non ripristina charging/detection)
- **nessuna rilevazione PC**
- **nessuna negoziazione di charging USB**

### iPad Pro 11in 1st gen — distinzione tra CD3215 e Tristar 610A3C
La fonte esterna descrive 3 punti di failure; per la parte Tristar:

1) **CD3215 IC** (fonte esterna)
- Se CD3215 fallisce: potenzialmente si riesce a caricare via **5V USB-A**, ma **non** si negozia carica a **15V** con **USB-C PD**.

2) **Tristar 610A3C** (fonte esterna)
- La fonte esterna indica che il **Tristar 610A3C** gestisce principalmente **5V USB-A** e che è una variante **speciale “A3C”** non retrocompatibile.
- Diagnosi proposta (fonte esterna): dopo aver verificato/escluso CD3215 e il charge port, se il comportamento è coerente (es. carica solo in un verso/solo su una tipologia di alimentatore) allora il Tristar è “più che probabile” il colpevole.

3) **Test corti attorno al Tristar** (fonte esterna)
- Probing con multimetro in **diode mode** attorno al Tristar per **capacitori shorted**.
- Nota della fonte: i capacitori attorno al Tristar **non sempre** vanno in corto quando l’IC fallisce.

### iPad Pro 12-9 3rd gen — ricerca corto attorno ai controller di charging
La fonte esterna indica che su questo modello i componenti più comuni che possono fallire e impedire la carica sono:
- **CD3215C00**
- **Tristar 610A3C**
- **Charging IC 343S00235**

Criterio (fonte esterna):
- **Check for short circuits around each of these**.

## Riparazione (sostituzione) — note operative
### iPad Pro 10.5 — sostituzione U3500 (Tristar)
La pagina esistente propone (passi pagina esistente):
1. scollegare la batteria
2. rimuovere logic board
3. rimuovere protective armour/shield che copre U3500
4. applicare flux
5. rimuovere U3500 con hot air controllato
6. pulire i pad
7. installare U3500 noto-good
8. ispezionare i giunti sotto microscopio
9. riassemblare
10. test: charging e PC detection

### iPad Pro 11in 1st gen — sostituzione Tristar 610A3C
La fonte esterna propone:
- se si trova un **capacitore shorted** attorno al Tristar: seguire la stessa logica di diagnosi (iniezione di tensione + freeze spray/termocamera per vedere quale componente scalda prima), rimuovere il corto o sostituire il Tristar.
- se **non** si trova un corto ma il Tristar resta sospetto: **sostituire Tristar 610A3C** (la fonte indica che si può reperire presso distributori o da donor board).

Test post-riparazione (fonte esterna):
- assicurarsi che il corto non sia più presente (se presente)
- verificare che l’iPad:
  - carichi a **5V** con **USB-A charger**, e
  - venga riconosciuto da **iTunes/3uTools**, specialmente in **Recovery o DFU**

### iPad Pro 12-9 3rd gen — gestione corto attorno ai controller
La fonte esterna indica una logica di riparazione basata su:
- ispezione visiva del **charging port** (pins danneggiati/corrosi → sostituire il flex del connettore)
- **check e rimozione corto** attorno a:
  - **CD3215C00**
  - **Tristar 610A3C**
  - **Charging IC 343S00235**

Per i corti (fonte esterna):
- iniettare **low voltage** nella linea shorted e usare **thermal camera** o **isopropyl alcohol** per identificare il componente che causa lo short.
- rimuovere e testare se lo short è stato eliminato.

Nota (fonte esterna):
- “The most common charging chip to fail on this model is the CD3215C00.”

### iPad 7 — sostituzione U1700 (Tristar)
La pagina esistente indica:
- su iPad 7 il Tristar è **610A3B**
- sostituzione “not that bad” (fonte pagina esistente):
  1. desolder con hot air station
  2. pulire i pad
  3. se il nuovo Tristar non è pre-balled: **reball**
  4. saldare il nuovo Tristar con hot air

## Note compatibilità / varianti
- **Aggiornamento da fonte esterna:** il **Tristar 610A3C** è una variante **speciale “A3C”** e **non è backwards compatible con altri Tristars**.
- La pagina esistente (iPad Pro 10.5) menziona compatibilità “USB IC (U3500) Tristar should match” e cita **610A3B** (iPhone 7/7 Plus), ma **non** conferma la variante 610A3C per iPad Pro 10.5.
- Quindi:
  - per iPad Pro 11in 1st gen: **610A3C** (fonte esterna)
  - per iPad 7: **610A3B** (pagina esistente)
  - per iPad Pro 12-9 3rd gen: **610A3C** (fonte esterna)
  - per iPad Pro 10.5: **da verificare** la variante esatta e la compatibilità.

## Collegamenti utili
- [strumenti: DC power supply (DCPS)](../strumenti/alimentatore-da-banco.md)
- [tecniche: test DCPS e diagnosi Kraken IC](../tecniche/test-dcps-e-diagnosi-kraken-ic.md)
- [tecniche: test Tristar e diagnosi non carica iPhone](../tecniche/test-tristar-e-diagnosi-non-carica-iphone.md)
- [componenti: Tristar](../componenti/tristar.md)
- [componenti: kraken-ic-usb](../componenti/kraken-ic-usb.md)
