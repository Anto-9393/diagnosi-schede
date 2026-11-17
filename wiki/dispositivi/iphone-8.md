---
titolo: iPhone 8
tipo: dispositivo
riassunto: 'iPhone 8 con batteria “Service” e livello che resta a 0–1%: spesso Q3200/Q3201
  (MOSFET I2C0) o connettore batteria; in alternativa Tigris/linee sotto Tigris-Hydra.'
modelli:
- iPhone 8
fonti:
- raw/repairwiki/pagine/iphone-8.md
- raw/repairwiki/pagine/how-to-fix-iphone-8-not-charging-after-screen-repair-stuck-at-0-battery-level.md
aggiornato: '2026-11-17'
categoria: phone
codici_modello: []
componenti_chiave:
- Q3200
- Q3201
- I2C0_SMC_BI_GG_SDA_CONN
- I2C0_SMC_TO_GG_SCL_CONN
- Tigris
- Hydra
casi: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# iPhone 8 — non carica / stuck a 0% dopo riparazione schermo

## Codici modello
- da verificare (non indicati nella fonte)

## Componenti chiave (da fonte)
- [Q3200/Q3201](#q3200q3201-mosfet-batteria-i2c0-smc-bi-gg-sda-conn-e-i2c0-smc-to-gg-scl-conn)
- Linee I2C:
  - `I2C0_SMC_BI_GG_SDA_CONN`
  - `I2C0_SMC_TO_GG_SCL_CONN`
- Connettore batteria (verifica pin centrali)
- IC citati come possibili cause:
  - Tigris (da fonte: su iPhone 8/8P è “now Tigris that fails”)
  - Hydra (da fonte: “Hydra or another line under Tigris or Hydra having an issue”)

## Sintomi tipici (da fonte)
- Il telefono si avvia e arriva alla Home, ma dopo ~3 minuti si riavvia spontaneamente.
- A volte va in bootloop anche se la batteria è “dead”.
- A volte: Home → riavvio immediato.
- Livello batteria sporadico (cambia continuamente) oppure bloccato a `0%` o `1%` anche con batteria carica.
- Non carica: su USB meter la corrente non è stabile (non un draw “1+ A via USB”), ma fluttua.
- In **Impostazioni > Batteria > Salute batteria**: “Service” e senza percentuale.
- In **3u Tools**: nessun dato batteria.

## Sezione caso/guasto (da fonte)
### Q3200/Q3201 — MOSFET batteria su linee I2C0
**Dove/come sono collegati (da fonte):**
- `I2C0_SMC_BI_GG_SDA_CONN` → collega a Q3200
- `I2C0_SMC_TO_GG_SCL_CONN` → collega a Q3201

**Part number (da fonte):**
- Q3200/3201: `RV3C002UNT2CL`

**Quando sospettarli (da fonte):**
- Se il problema è comparso **dopo una riparazione schermo**, la fonte indica che “most likely one or both battery mosfets (Q3200/Q3201) got damaged”.

**Diagnosi consigliata (da fonte):**
- Eseguire **Diode Mode** sul connettore batteria.
- Le **2 piccole pin** sono le linee dati che vanno ai MOSFET.
  - Se uno o entrambi i pin leggono **OL** → MOSFET danneggiato.
  - Se non ci sono pad strappati → sostituire il MOSFET danneggiato.
  - Dopo la sostituzione: rifare Diode Mode per verificare di nuovo una lettura “diode mode” (la fonte cita un valore indicativo `~.665v`).
  - Se ci sono **ripped pads** → servono **jumper** sui pin appropriati (da fonte: “you'll need to run jumpers for the appropriate pin(s)”).

**Note operative (da fonte):**
- La fonte rimanda a una figura/video per l’assegnazione dei jumper (pin “top” e “bottom”), ma i dettagli esatti dei punti A/B/C/D non sono riportati qui: **da verificare**.

### Connettore batteria — pin centrali piegati/danneggiati
**Quando sospettarlo (da fonte):**
- In alcuni casi il connettore batteria è “warped or damaged”.

**Diagnosi/controllo (da fonte):**
- Ispezione visiva dei **pin centrali** del connettore batteria.
  - Se sembrano “pushed out” e nascosti sotto la plastica → provare a spingerli fuori con un tool.
  - Se il connettore è “smashed” o manca plastica → sostituire il connettore.
  - In alternativa: sostituire direttamente il connettore batteria.

### Pry damage dopo riparazione schermo
**Quando sospettarlo (da fonte):**
- Se il problema è comparso dopo una riparazione schermo.

**Cosa fare (da fonte):**
- Diode Mode sul connettore batteria per verificare Q3200/Q3201 (vedi sezione sopra).
- Se non risolve: passare a Tigris/Hydra.

### Altre cause: Tigris / Hydra / linee sotto Tigris-Hydra
**Tigris (da fonte):**
- Se quanto sopra non risolve: provare a sostituire **Tigris**.
- Nota della fonte: su iPhone più vecchi Tristar causava problemi; su iPhone 8/8P e newer “that chip is now Tigris that fails & requires a replacement”.

**Hydra e linee sotto Tigris/Hydra (da fonte):**
- Se ancora non risolve: può essere Hydra o un’altra linea sotto Tigris/Hydra.
- Procedura indicata (da fonte):
  - Diode mode su **ogni pad** sotto Tigris e Hydra per trovare **OL** o **short**.
  - Se trovi una linea in **short**: “track down the shorted capacitor by injecting voltage”.
  - Se trovi **OL** dove dovrebbe esserci lettura: seguire il percorso della linea e fare diode mode punto per punto finché la lettura “reappears”; quel punto indica dove la linea è scollegata e di solito va sostituito il componente che ha scollegato la linea (spesso un “filter”).

## Test finale (da fonte)
- Avviare **Stopwatch** e verificare che funzioni più di ~3 minuti (prima si riavviava a ~3 minuti).
- Riprodurre un video YouTube per ~1 ora per verificare continuità.
- Controllare la **corrente di carica USB**.
- Controllare la **Battery Health** in Impostazioni.
- Verificare che il livello batteria mostri valori accurati.

## Link utili (pagine wiki)
- [i2c-line-battery-connector](../componenti/i2c-line-battery-connector.md)
- [test-i2c-battery-connector-ol-diodes-mode](../tecniche/test-i2c-battery-connector-ol-diodes-mode.md)
- [Tristar](../componenti/tristar.md) (nota: la fonte parla di Tigris su iPhone 8/8P; pagina Tristar utile per contesto)
- [pmic](../componenti/pmic.md)
- [batteria](../componenti/batteria.md)
