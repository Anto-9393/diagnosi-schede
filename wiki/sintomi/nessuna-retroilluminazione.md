---
titolo: Nessuna retroilluminazione — cause e diagnosi (diodi)
tipo: sintomo
riassunto: 'Assenza di retroilluminazione: possibili cause legate a diodi (aperto/corto,
  perdite, protezioni) e test base per distinguere guasti di alimentazione/protezione.'
modelli: []
fonti:
- raw/repairwiki/pagine/diodes-repair-basics.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Sintomo: nessuna retroilluminazione

> Nota: la fonte fornita è generale sui diodi e non parla specificamente di retroilluminazione. Le cause sotto sono quindi **da verificare** e vanno interpretate come “possibili” quando il guasto porta a **mancanza di alimentazione o protezioni**.

## Cause possibili (in ordine di probabilità)

1. **Diodo guasto in corto (o percorso di corrente indesiderato)**
   - I diodi tendono a guastarsi in **stato completamente aperto o completamente in corto**. Un corto può alterare le tensioni e far scattare protezioni o impedire l’avvio di sotto-sistemi che alimentano la retroilluminazione. (da fonte: guasti tipici dei diodi)
   - Misura/controllo: test diodo **fuori circuito** in modalità “diode” del multimetro; se in una direzione risulta “OL”/basso valore o comunque non rispetta la polarità attesa, il componente è sospetto. (da fonte: test diodo)

2. **Diodo guasto in aperto (nessun passaggio di corrente)**
   - Se il diodo va in **aperto**, la sezione di circuito che deve condurre in una direzione potrebbe non alimentarsi correttamente.
   - Misura/controllo: test diodo fuori circuito; in conduzione diretta il multimetro deve mostrare una caduta tipica (per silicio) e **non** deve leggere correttamente anche invertendo i puntali. (da fonte: test diodo e attenzione alla polarità)

3. **Zener/TVS in perdita o con breakdown alterato (protezione e clamp)**
   - Zener e TVS sono progettati per lavorare in reverse breakdown; se il comportamento è alterato (es. **abbassamento della reverse breakdown voltage** o **aumento della resistenza/leakage**), possono causare clamp anomali o comportamenti da “resistenza” in reverse sotto breakdown, con conseguenze su alimentazioni e avvii. (da fonte: failure/degradation modes e funzione Zener/TVS)
   - Misura/controllo: per Zener serve identificare la tensione Zener con alimentatore da banco e resistenza in serie (metodo descritto in fonte). (da fonte: “Identifying a Zener diode's Zener voltage”)

4. **Diodo “leaky” (perdita in reverse) / aumento resistenza**
   - La fonte indica che tra i modi di guasto ci sono **reverse leakage current** e **aumentata resistenza** (che può causare surriscaldamento e spreco di potenza). (da fonte: failure/degradation modes)
   - Misura/controllo: test diodo fuori circuito e verifica della lettura corretta solo in polarità diretta; se la lettura compare anche invertendo i puntali, è indicativo di guasto. (da fonte: polarità e letture)

## Test rapidi consigliati (generici)

1. **Ispezione fisica prima di misurare**
   - La fonte raccomanda di verificare prima danni fisici (es. **liquid damage/corrosion**), perché è il modo più rapido per identificare un diodo guasto. (da fonte: “Make sure the diode does not have any physical damage…”) 

2. **Test diodo con multimetro in modalità “diode” (fuori circuito)**
   - Testare **fuori dal circuito**. (da fonte)
   - Caduta attesa per diodi al silicio: circa **0.2–0.7 V** in conduzione diretta. (da fonte)
   - Se mostra **OL** o meno di **0.2 V**, il diodo è “likely faulty”. (da fonte)
   - **Attenzione alla polarità**: se il diodo dà lettura anche invertendo i puntali, è guasto. (da fonte)

3. **Se sospetti Zener: identificazione della tensione Zener**
   - Metodo in fonte: rimuovere il diodo, mettere **1 kΩ** in serie, alimentare in reverse con alimentatore da banco (positivo al catodo, negativo all’altro capo della resistenza), misurare in DC ai capi del diodo e aumentare gradualmente la tensione. (da fonte)
   - Valori/step: **da verificare** perché la fonte fornita si interrompe nella parte successiva (“until the …”).

## Collegamenti utili
- [diode.md](../componenti/diode.md)
- [tecniche/test-diodi.md](../tecniche/test-diodi.md)
