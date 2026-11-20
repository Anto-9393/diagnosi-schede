---
titolo: Pulizia della scheda dopo liquidi — IPA, mai acqua, mai con tensione
tipo: tecnica
riassunto: 'Metodo del tecnico per una scheda bagnata (acqua, caffè, bibite): batteria e cavo scollegati, mappatura
  della corrosione al microscopio, pulizia con alcol isopropilico 99% (mai acqua), ultrasuoni alla fine, asciugatura
  completa prima di ridare tensione.'
modelli: []
fonti:
- raw/banco/pulizia-dopo-liquidi.md
- raw/repairwiki/pagine/visual-inspection-repair-basics.md
aggiornato: '2026-11-20'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Regola di sicurezza (prima di tutto)
**Mai liquidi su una scheda alimentata.** Prima di qualsiasi pulizia: cavo USB/caricatore staccato e **batteria scollegata**.
Un liquido su una scheda sotto tensione crea corti tra le linee e brucia componenti (controller di carica, PMIC, condensatori).

## Cosa usare
- **Alcol isopropilico (IPA) 99%** con pennello antistatico: scioglie i residui, evapora in fretta e non lascia aloni.
- **Niente acqua** per pulire la scheda: è la scelta del tecnico al banco (l'acqua del rubinetto, poi, lascia sali che
  conducono e corrodono).
- Caffè e bibite lasciano **residui zuccherini appiccicosi**: insistere sotto i connettori (es. porta USB-C) e attorno ai passivi.

## Ordine di lavoro
1. Scollega cavo e batteria.
2. **Mappa il danno prima di pulire**: microscopio, foto delle zone con ossido, aloni e "polvere verde". La guida
   *Visual Inspection – Repair Basics* consiglia di lasciare gli ultrasuoni **alla fine**: dopo la pulizia i segni del
   liquido diventano difficili da trovare.
3. Pulisci con IPA 99% e pennello le zone mappate; ripeti finché non restano residui.
4. Ultrasuoni (se servono) solo alla fine.
5. **Asciugatura completa** prima di ridare tensione.
6. Solo dopo: misure (diode mode, alimentatore con limite di corrente). Con i residui le letture non sono affidabili.

## Collegamenti
- [Analisi visiva e ispezione della logic board](analisi-visiva-e-ispezione-logic-board.md)
- [Test CD3217 e ricerca corti](test-cd3217-e-ricerca-corti.md)
- [Caso: iPad Air 4 A2316 non carica dopo caffè](../casi/ipad-air-4-a2316-non-carica.md)
