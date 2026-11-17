---
titolo: Diagnosi e rimozione corto su rail con condensatore in corto (SPKRAMP_TOP_VBOOST)
tipo: tecnica
riassunto: Conferma corto pre-boot su DCPS, localizza il condensatore in corto con
  iniezione a bassa tensione + freeze spray/termocamera, rimuovi il componente e verifica
  pre-boot e letture diode post-riparazione.
modelli:
- iPhone 14
fonti:
- raw/repairwiki/pagine/how-to-fix-an-iphone-14-that-is-shows-temperature-warning-and-does-not-charge.md
- raw/repairwiki/pagine/how-to-fix-an-iphone-8-that-has-no-power-does-not-boot.md
- raw/repairwiki/pagine/how-to-fix-iphone-x-that-does-not-power-on.md
- raw/repairwiki/pagine/ipad-pro-9-7-not-powering-on-2a-or-higher-power-draw-before-prompt-to-boot.md
- raw/repairwiki/pagine/iphone-11-not-powering-on-2a-or-higher-power-draw-after-prompt-to-boot.md
- raw/repairwiki/pagine/short-circuits-repair-basics.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Scopo
Gestire casi in cui il dispositivo mostra **warning temperatura** e **non carica quando è acceso**, con **assorbimento anomalo in pre-boot** su DCPS, riconducibile a un **corto su rail** dovuto a un **condensatore in corto**.

Nel caso riportato dalla fonte, la rail interessata è **SPKRAMP_TOP_VBOOST**.

## Sintomi tipici (da fonte)
- **Warning temperatura** dopo il boot.
- **Non carica quando è acceso**.
- **Carica correttamente quando è spento**.
- **Surriscaldamento rapido** del dispositivo mentre è acceso.
- Su DCPS: **pre-boot draw ~1 A** prima del prompt di boot; poi il device boot-a normalmente.

## Diagnosi (passo-passo)
1. **Ispezione visiva completa**
   - Controllare corrosione/ossidazione e danni da liquidi.
   - Se presenti segni di liquido, valutare anche le aree sotto adesivi/sticker e attorno a connettori.
   - Se **non** ci sono danni da liquidi, la fonte indica che è **molto probabile** un **condensatore in corto**.

2. **Conferma elettrica del corto in pre-boot con DCPS**
   - Collegare il dispositivo a **DCPS** e osservare la corrente.
   - Obiettivo: verificare **assorbimento anomalo prima del prompt di boot** (nel caso fonte: pre-boot ~1 A).

3. **Localizzazione del componente che scalda**
   - Usare **termocamera** per individuare la zona/componentistica che scalda rapidamente.

4. **Individuazione della rail da controllare (short “before prompt to boot”)**
   - La fonte elenca le linee più probabili da controllare per corto **prima** del prompt di boot:
     - **PP_VCC_MAIN** (più probabile)
     - **PP_BATT_VCC**
     - **PPSTROBE_LX**
     - **PPVCC_HIGH**
   - Nota: la pagina corrente (iPhone 14) riporta anche **PP_SPKRAMP_TOP_VBOOST / SPKRAMP_TOP_VBOOST** come rail nel caso specifico.

5. **Ricerca del condensatore in corto con iniezione tensione + freeze spray / termocamera**
   - La fonte indica di:
     - **iniettare 4 V / 2 A** direttamente sulla **linea misurata come short**
     - usare **freeze spray** o **termocamera** per individuare il condensatore che sta dissipando.

6. **Conferma elettrica (resistenza bassa)**
   - Nel caso riportato, la fonte indica che la misura di resistenza risulta **low resistance** a conferma del corto.

> Allineamento con la fonte “Short Circuits - Repair Basics” (criteri generali):
> - Prima di concludere “short”, verificare che la rail sia effettivamente abilitata.
> - Usare multimetro in **diode o resistenza** con riferimento a **GND**; invertire le sonde può falsare la lettura per diodi interni.
> - Se la misura è **0Ω (o 0V)** verso GND (tenendo conto della resistenza puntali, tipicamente ~0.4Ω), la presenza di corto è “inequivocabile”.
> - Se non si identifica il componente, si può procedere con **iniezione di tensione** sulla linea shorted, **con estrema cautela**: non superare i valori nominali di tensione/corrente della rail e **partire da 1V**.

## Riparazione (rimozione corto)
1. **Rimuovere la motherboard**.
2. **Accedere alla rail**
   - La fonte descrive di separare/splittare il layer secondo procedura di lavoro del banco.
3. **Rimuovere il condensatore in corto**
   - Nel caso di questa pagina: rimuovere il condensatore in corto sulla rail **SPKRAMP_TOP_VBOOST**.
4. **Rimisura resistenza sulla rail**
   - Obiettivo: verificare che il corto sia stato rimosso.

> Nota (da fonte): se il corto è su un **decoupling capacitor**, la fonte indica che **si può rimuovere il condensatore shorted e non sostituirlo**; la capacitance non scenderebbe abbastanza da impattare la funzione del dispositivo.

## Verifica post-riparazione
1. **Test boot con DCPS**
   - Obiettivo: assicurarsi che il **pre-boot current draw** torni normale (nel caso fonte: non resti anomalo come ~1 A).
2. **Verifica carica con telefono acceso**
   - Atteso dalla fonte: **carica normalmente** e **warning temperatura sparisce**.
3. **Diode reading della rail (VCC_MAIN)**
   - La fonte indica: dopo la rimozione del componente in corto, fare una **diode reading** della linea.
   - Valore atteso (fonte): un **VCC Main sano** deve avere una **vault tra 0.400 e 0.500**.
4. **Test di stabilità sotto carico**
   - La fonte indica di testare **charging + usage** prima di chiudere.

## Precauzioni importanti (da fonte)
- Se si inietta tensione tramite **battery connector** (es. iPower Pro / DT880), la fonte segnala che **Yangtze** può **scaldare istantaneamente**.
  - Motivo riportato: la linea **PP_BATT_VCC** del battery connector collega **PP_VDD_MAIN** tramite il componente indicato nella fonte (testo: “it connects to PP_VDD_MAIN through it”), creando molta dissipazione.
  - La fonte aggiunge che in questi casi il corto è spesso un **cap shorted**, ma in rari casi può essere lo stesso componente (testo: “In rare cases, it's Yangtze itself”).

## Collegamenti utili
- Condensatori (MLCC/elettrolitici/tantalio): [condensatori-mlcc-elettrolitici-tantalio](../componenti/condensatori-mlcc-elettrolitici-tantalio.md)
- DCPS: [alimentatore-da-banco](../strumenti/alimentatore-da-banco.md)
- Termocamera: [termocamera](../strumenti/termocamera.md)

## Su iPhone 14 (caso fonte)
- Sintomi: **temperature warning** e **non carica quando è acceso**.
- DCPS: **pre-boot draw ~1 A** prima del prompt di boot.
- Localizzazione: **termocamera**.
- Corto: **condensatore shorted** su **SPKRAMP_TOP_VBOOST**.
- Esito atteso: normalizzazione del pre-boot, ripristino carica e scomparsa warning temperatura.
