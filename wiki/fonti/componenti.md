---
titolo: fonti/componenti.md
tipo: fonte
riassunto: 'Caso iPhone 15 Pro Max: assorbimento DCPS 0.105–0.130 A pre-boot e heating
  del charging IC; da mappare su componenti di ricarica e sintomo correlato (sigla
  IC e net: da verificare).'
modelli:
- iPhone 15 Pro Max
fonti:
- raw/repairwiki/pagine/iphone-15-pro-max-dead-and-not-charging.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# Fonte → componenti/sintomi (iPhone 15 Pro Max)

## Contesto del caso (da fonte)
- Dispositivo: **iPhone 15 Pro Max**.
- Sintomo principale: **dead** (nessuna risposta a power button/charger) e **non carica** quando è alimentato “da batteria”.
- Comportamento con alimentatore da banco (DC Power Supply, DCPS):
  - **0.105–0.130 A** di assorbimento **prima** del prompt di boot.
  - Dopo il prompt di boot, il telefono **boota normalmente**.
- Evidenza diagnostica:
  - **Thermal imaging**: il **charging IC** (IC di ricarica) **si scalda in modo anomalo**.

## Cosa manca per collegare con precisione (da verificare)
La fonte non riporta:
- **sigla esatta** del charging IC;
- **net** coinvolti (es. linee di alimentazione/ricarica) e punti di misura.

Quindi, per ora, l’associazione a componenti specifici della wiki è **parziale** e va completata con misure/lettura schema o con un dump/annotazione aggiuntiva.

## Mappatura utile per la wiki

### Sintomo da creare/aggiornare
- **“Dead / non carica” con heating del charging IC**.
  - La fonte supporta direttamente: *dead + non carica* e *charging IC che scalda*.
  - Linkare/collegare a una pagina sintomo esistente solo se la descrizione combacia (qui: da verificare).

Pagine sintomo già presenti che potrebbero essere correlate (da verificare compatibilità):
- [non-carica-0-01-0-15a](../sintomi/non-carica-0-01-0-15a.md) (range corrente pre-boot potrebbe rientrare, ma la fonte parla di 0.105–0.130 A e di heating charging IC: da verificare).
- [temperatura-warning-e-non-carica](../sintomi/temperatura-warning-e-non-carica.md) (la fonte parla di heating via termocamera, non di “warning” a schermo: da verificare).

### Componenti da creare/aggiornare
Dato che la fonte parla esplicitamente di **charging IC**, servono pagine componente per:
- **Charging IC (sigla da verificare)**: funzione, sintomi, misure attese.

Al momento non posso indicare una sigla tra quelle già presenti (es. [Tristar](../componenti/tristar.md], [CD3217](../componenti/cd3217.md], [CD3215C00](../componenti/cd3215c00.md], [Kraken](../componenti/kraken-ic-usb.md], ecc.) perché la fonte non la nomina.

## Azioni consigliate per completare l’ingest (da verificare)
1. Identificare la **sigla del charging IC** sul board dell’iPhone 15 Pro Max del caso (foto/annotazione o lettura BOM).
2. Identificare almeno 1–2 **net** di ricarica/ingresso (es. rail DCPS → charging IC) per collegare misure e sintomi a pagine esistenti.
3. Verificare se il caso rientra in una pagina sintomo già presente (range corrente e descrizione “dead/non carica”).

## Collegamenti da fare nella wiki (con link solo dove possibile)
- Sintomo: creare/aggiornare una pagina sintomo dedicata a **dead/non carica con heating del charging IC** (link a componenti di ricarica quando la sigla sarà nota).
- Componenti: creare pagina per **charging IC — sigla da verificare**.

## Dati tecnici estratti (solo quelli presenti in fonte)
- DCPS: **0.105–0.130 A** di assorbimento **pre-prompt di boot**.
- Diagnosi: **thermal imaging** → **charging IC heating anomalo**.
- Riparazione (alto livello): sostituzione charging IC con hot air + reball, pulizia pad, test di boot/charging.

> Nota: valori e procedura sono riportati dalla fonte, ma senza sigla IC e senza net: per misure “attese” su rail specifici serve integrazione (da verificare).
