---
titolo: Short Circuits — Repair Basics (repair.wiki)
tipo: fonte
riassunto: 'Guida di base per riconoscere, misurare e localizzare corti su rail: ispezione,
  misure in diode/resistenza verso GND, ricerca con calore e iniezione controllata,
  cenni a OCP.'
modelli: []
fonti:
- raw/repairwiki/pagine/short-circuits-repair-basics.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# Short Circuits - Repair Basics (riassunto fonte)

> Fonte: [Short Circuits - Repair Basics — repair.wiki](https://repair.wiki/w/Short_Circuits_-_Repair_Basics), CC BY-SA 3.0.

## Cos’è un corto circuito
Un corto è un percorso improprio verso massa (GND) con resistenza molto bassa (0/low resistance). Spesso nasce quando un componente (es. **capacitori** o **MOSFET**) fallisce creando un cammino verso GND. Cause citate: corrosione, capacitori esplosi, ecc.

## Riconoscere un corto (diagnosi iniziale)
- Se una **rail di tensione** resta a **0 V** o non raggiunge la tensione attesa, sospettare un corto sulla rail.
- Prima di concludere, verificare che la rail sia effettivamente **abilitata**: alcune rail (es. CPU/GPU) possono avere resistenza verso GND bassa tra **0 e 1 Ω** anche senza corto.
- **Ispezione visiva**: cercare corrosione, componenti bruciati/danneggiati, scolorimenti, ponti di saldatura (specie dopo riparazioni precedenti).

## Misure con multimetro (diode/resistenza)
Per confermare il corto:
- Usare il multimetro in **modalità diode** o **resistenza**.
- Collegare il puntale **nero** (negativo) verso il lato **inferiore della rail**, tipicamente **GND**.
- Attenzione: invertire i puntali **può** dare letture basse per via delle **diodi di protezione interni** negli IC, anche senza corto.
- Se la misura verso GND risulta **0 Ω** (o **0 V**) — considerando la resistenza dei puntali (la fonte cita tipicamente ~**0,4 Ω**) — la presenza di corto è considerata **inequivocabile**.
- Se non è 0 Ω, la gravità dipende da tensione e specifiche di corrente della rail (valori da verificare sul caso).

## Localizzare il corto (approccio pratico)
1. **Ispezione visiva approfondita** della zona della rail.
2. Se si trovano componenti sospetti (bruciature, scolorimenti, ponti di saldatura, componenti fisicamente danneggiati):
   - rimuoverli
   - ricontrollare se il corto persiste.
3. Se non si trovano anomalie visive:
   - alimentare con cautela e verificare se qualche componente sulla rail diventa **notevolmente caldo**.
   - rimuovere i componenti che risultano cortocircuitati/danneggiati.
   - nota della fonte: non ogni componente caldo è necessariamente in corto; come regola generale, quelli troppo caldi al tatto sono probabilmente danneggiati e spesso si scaldano più velocemente degli altri.
4. Se ancora non si identifica il componente:
   - può essere necessario **iniettare tensione** sulla motherboard/rail per aumentare la corrente nel punto di corto e quindi la generazione di calore.
   - cautela: non superare mai la **tensione** o la **corrente** nominale della rail.
   - la fonte suggerisce di iniziare da **1 V** (citato come generalmente sicuro per molte rail).
5. Tecniche alternative citate:
   - iniettare potenza sulla linea e usare **termocamera** per individuare il componente più caldo.
   - usare **freeze spray** (o aria compressa spruzzata capovolta) o **isopropanolo** per identificare il componente che si scalda più velocemente.
6. Se il corto non si localizza:
   - potrebbe essere un corto a **bassissima resistenza** o potrebbe non esistere.
   - ripercorrere i passaggi, rimuovere fili/connessioni “volanti” aggiunte e rieseguire ispezione visiva.
   - possibile che un’altra rail (generata dalla rail sospetta) sia a sua volta in corto.

### Note sulla difficoltà su rail CPU/GPU
La fonte evidenzia che “dead shorts” (impedenza molto bassa) possono essere causati da ponti di saldatura o componenti di potenza (MOSFET, diodi, grandi condensatori). Su rail CPU/GPU la misura può risultare “corta” ma è difficile identificare il componente caldo per via di resistenze equivalenti molto basse e correnti elevate (esempio concettuale: CPU 25 W a 0,8 V → resistenza equivalente ~25,6 mΩ e >30 A).

## Protezione da sovracorrente (OCP)
La fonte riassume che quasi tutte le alimentazioni/rail generator includono protezione da corto (overcurrent protection). Tre approcci citati:
1. **Resistenza di limitazione** (semplice, usata in circuiti a bassa potenza): limita la corrente ma non disconnette completamente.
2. **Fusibili**: interrompono fisicamente l’alimentazione; spesso monouso; esistono varianti resettable o PTC.
3. **Current limiting attivo** (tipico in switching power supply): il controller misura la corrente e:
   - riduce la tensione (in lab power supply) oppure
   - spegne la rail e la riattiva dopo un tempo.
   - può manifestarsi come “power cycling” (click) e come tensione instabile su voltmetro.

## Playlist YouTube (fonte)
- Video introduttivo e playlist dedicate ai corti sono linkate nella fonte.

---

### Collegamenti utili (wiki)
Questa fonte è coerente con le tecniche presenti in wiki per:
- ricerca corto con iniezione a bassa tensione e termocamera: [tecniche/ricerca-corto-iniezione-bassa-tensione-e-termocamera.md](../tecniche/ricerca-corto-iniezione-bassa-tensione-e-termocamera.md)
- diagnosi/rimozione corto su rail con condensatore in corto: [tecniche/diagnosi-e-rimozione-corto-su-rail-con-capacitore-in-corto.md](../tecniche/diagnosi-e-rimozione-corto-su-rail-con-capacitore-in-corto.md)
- componenti tipici coinvolti nei corti (es. [componenti/diode.md](../componenti/diode.md), [componenti/condensatori-mlcc-elettrolitici-tantalio.md](../componenti/condensatori-mlcc-elettrolitici-tantalio.md)).
