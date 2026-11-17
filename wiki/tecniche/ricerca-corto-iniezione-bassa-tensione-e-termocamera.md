---
titolo: Ricerca corto — iniezione bassa tensione e termocamera
tipo: tecnica
riassunto: Localizza un corto su rail iniettando 1–4 V (partendo da 1 V) e usando
  termocamera/freeze spray per identificare il componente che scalda (spesso un condensatore),
  gestendo anche OCP/power cycling.
modelli: []
fonti:
- raw/repairwiki/pagine/ipad-pro-12-9-3rd-gen-not-charging-repair.md
- raw/repairwiki/pagine/ipad-pro-12-9-4th-gen-not-charging-repair.md
- raw/repairwiki/pagine/ipad-pro-12-9-5th-gen-not-powering-on-due-to-long-screw-damage.md
- raw/repairwiki/pagine/ipad-pro-9-7-not-powering-on-2a-or-higher-power-draw-before-prompt-to-boot.md
- raw/repairwiki/pagine/iphone-11-not-powering-on-2a-or-higher-power-draw-after-prompt-to-boot.md
- raw/repairwiki/pagine/iphone-11-not-powering-on-after-prompt-to-boot-current-jumps-back-and-forth-from-0-a-to-320-ma-then-0-a-to-1-4-a-then-0-a-to-500-ma-and-so-on.md
- raw/repairwiki/pagine/iphone-11-pro-and-iphone-11-pro-max-not-powering-on-2a-or-higher-power-draw-after-prompt-to-boot.md
- raw/repairwiki/pagine/iphone-15-pro-max-dead-and-not-charging.md
- raw/repairwiki/pagine/iphone-15-series-no-touch-no-charging.md
- raw/repairwiki/pagine/iphone-xr-not-powering-on-with-heat-above-the-cpu.md
- raw/repairwiki/pagine/iphone-xs-not-powering-on-pulls-2a-or-more-before-promt-to-boot.md
- raw/repairwiki/pagine/short-circuits-repair-basics.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Scopo
Localizzare rapidamente quale componente sta causando un **corto** su una **linea di alimentazione/ricarica (rail)** usando:
- **iniezione di bassa tensione** sulla rail sospetta
- **osservazione termica** con **termocamera** e/o **freeze spray** (o aria compressa capovolta)

La logica di base è: nella zona del corto scorre più corrente → il componente/area interessata scalda prima degli altri.

> Fonte: Short Circuits - Repair Basics (repair.wiki) + tecnica esistente (iniezione 4 V/2 A e freeze/termocamera).

## Quando usarla
- Hai una rail che **non raggiunge** la tensione attesa o resta a **0 V** (o comunque hai evidenza di corto su rail).
- Hai già fatto (o puoi fare) una verifica con **multimetro in diode/resistenza** verso GND per confermare che la rail è effettivamente in corto.

> Fonte: Short Circuits - Repair Basics.

## Pre-check: conferma corto e ispezione
1. **Ispezione visiva** (sempre prima): cerca corrosione, componenti bruciati/danneggiati, discolorazioni, **solder bridge** (specie dopo riparazioni precedenti).
2. Se non trovi nulla, misura con multimetro in **diode o resistenza**:
   - puntale nero su **GND** (lato massa della rail)
   - attenzione: invertire i puntali può dare letture basse per **diodi di protezione interni** anche senza corto.
3. Se misuri **0 Ω / 0 V** (tenendo conto della resistenza puntali, tipicamente ~0,4 Ω secondo fonte), allora è **corto**.

> Fonte: Short Circuits - Repair Basics.

## Procedura: localizzazione con iniezione + termica
### 1) Iniezione “a bassa tensione” (parti basso)
- Se devi iniettare tensione per localizzare, la fonte consiglia di **partire da 1 V** (di solito “safe” per quasi tutte le rail) e **non superare** mai la tensione/corrente nominale della rail.
- Tecnica esistente (pagina già presente): iniettare **4 V / 2 A** sulla linea che risulta in corto e osservare la risposta termica.

> Fonte: Short Circuits - Repair Basics (partire da 1 V, non superare rating) + pagina tecnica esistente (4 V/2 A).

### 2) Osservazione termica durante l’iniezione
Durante l’iniezione, usa:
- **termocamera** per vedere quale componente/area sale di temperatura più velocemente
- oppure **freeze spray** (o aria compressa capovolta / isopropyl alcohol secondo fonte) per “marcare” il punto che scalda

> Fonte: Short Circuits - Repair Basics.

### 3) Interpretazione e rimozione
- La fonte indica che il componente in corto spesso **scalda molto più velocemente** del resto.
- Una volta identificato il componente “hot”, rimuovilo e verifica se il corto **persiste**.

> Fonte: Short Circuits - Repair Basics.

## Variante: se non trovi nulla con termica
Se non riesci a identificare il componente:
- può essere un corto a **bassissima resistenza** (es. **solder bridge** o componenti di potenza come MOSFET/diode/condensatori grandi)
- oppure il corto “apparente” è generato da un’altra rail che deriva dalla tua rail sospetta
- in caso di “dead short” spesso la causa è **solder bridge** o componenti di potenza

> Fonte: Short Circuits - Repair Basics.

## OCP / power cycling: cosa aspettarsi durante la diagnosi
Molti generatori di rail includono **overcurrent protection (OCP)**. Quando rileva un corto:
- può **ridurre** la tensione o **spegnere** la rail
- poi può **riattivare** dopo un tempo
- se il corto non è rimosso, la rail può ripetere il ciclo → in pratica vedi **power cycling** (anche come “clicking” e tensione instabile su voltmetro)

> Fonte: Short Circuits - Repair Basics.

### Implicazione pratica per la localizzazione
Se durante l’iniezione/diagnosi vedi instabilità (spegnimenti/riaccensioni), non significa automaticamente che il corto sia “sparito”: può essere solo l’OCP che sta proteggendo la rail.

> Fonte: Short Circuits - Repair Basics.

## Collegamenti (wiki)
- [strumenti/termocamera](../strumenti/termocamera.md)
- [tecniche/diagnosi-e-rimozione-corto-su-rail-con-capacitore-in-corto.md](../tecniche/diagnosi-e-rimozione-corto-su-rail-con-capacitore-in-corto.md)
- [componenti/condensatori-mlcc-elettrolitici-tantalio](../componenti/condensatori-mlcc-elettrolitici-tantalio.md)
- [componenti/diode](../componenti/diode.md)
- [fonti/short-circuits-repair-basics.md](../fonti/short-circuits-repair-basics.md)
