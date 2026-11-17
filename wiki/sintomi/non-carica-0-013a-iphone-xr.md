---
titolo: Non carica con assorbimento ~82mA su DCPS e carica ~0.013A — iPhone XR
tipo: sintomo
riassunto: 'Pattern tipico su iPhone XR: non fa boot e/o non carica; su caricatore
  ~0.013A e su DCPS ~82mA prima del prompt to boot; causa più probabile Yangtze/U3300.'
modelli:
- iPhone XR
fonti:
- raw/repairwiki/pagine/iphone-xr-not-charging.md
- raw/repairwiki/pagine/iphone-xr-not-powering-on-not-charging.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Pattern / sintomi
- Il telefono **non fa boot** (tasto power) e/o **non carica**.
- Con **caricatore**: corrente di carica circa **0.013 A** (low amperage draw).
- Con **DC Power Supply (DCPS)**: assorbimento circa **82 mA** **prima del prompt to boot**.
- La fonte riporta anche: **nessun corto a massa** su **VDD Main**, **VDD Boost** o **PP3V0_NAND**.

> Nota: la pagina esistente parla esplicitamente di “prima del prompt to boot”. La fonte esterna conferma “low amperage draw da DCPSU” ma non riporta il valore numerico 82 mA/0.013 A nel testo fornito: **da verificare** se i numeri sono coerenti con la revisione della fonte.

## Cause probabili (in ordine)
1) **Yangtze — U3300 (Charging IC)**
- La fonte indica che su **iPhone XR** l’IC che fallisce più spesso è **Yangtze (U3300)**.

2) **Ear speaker flex danneggiato da liquido** (alternativa)
- La pagina esistente include come alternativa un **ear speaker flex** danneggiato da liquido.
- La fonte esterna fornita **non** menziona questa alternativa: **da verificare** se è un’ipotesi derivata da altri casi.

## Verifiche pratiche (misure/condizioni)
- **Con DCPS**: misurare l’assorbimento **prima del prompt to boot**; riscontro atteso del pattern: **~82 mA** (**da verificare** rispetto alla fonte esterna).
- **Con caricatore**: misurare la corrente di carica; riscontro atteso del pattern: **~0.013 A** (**da verificare** rispetto alla fonte esterna).
- **Corti su rail**: verificare che non ci sia corto a massa su **VDD Main**, **VDD Boost**, **PP3V0_NAND** (la fonte riporta “no short to ground” su questi punti).
- **Ear speaker flex test** (solo se si segue la pagina esistente): ripetere la prova di carica/boot con **ear speaker flex scollegato** (se disponibile) per distinguere un problema da liquido.

## Componenti correlati
- [Yangtze U3300](../componenti/yangtze-u3300.md)

## Note operative (rimozione shield su Yangtze)
- La fonte esterna indica che l’IC **Yangtze (U3300)** è **sotto la bottom back shield**.
- Per rimuovere la shield: usare **max heat**, **max air** e **largest nozzle**.
- La rimozione richiede **molto calore** o **taglio della shield** (es. tin snips).
- Precauzioni: **estremamente attento** a non “floatare” componenti/parti e a non urtare o staccare componenti.
- La fonte avverte anche di evitare troppa forza: una flessione eccessiva può danneggiare **tracce interne**.

## Su iPhone XR
- Questo pattern è riportato specificamente per **iPhone XR**.
