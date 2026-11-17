---
titolo: Fonte — iPad Pro 12.9 3rd Gen Not Charging Repair (repair.wiki)
tipo: fonte
riassunto: 'Diagnosi e riparazione iPad Pro 12.9 3rd Gen che non carica: assorbimento
  0.01–0.15 A, ispezione porta USB‑C, verifica corti su CD3215C00/Tristar/343S00235
  e sostituzione flex porta se danneggiata/corrotta.'
modelli:
- iPad Pro 12.9 3rd Gen
fonti:
- raw/repairwiki/pagine/ipad-pro-12-9-3rd-gen-not-charging-repair.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# Fonte: IPad Pro 12.9 3rd Gen Not Charging Repair

Link: https://repair.wiki/w/IPad_Pro_12.9_3rd_Gen_Not_Charging_Repair  
Licenza: CC BY-SA 3.0 (vedi fonte)

## Problema
iPad Pro 12.9 3rd Gen che **non carica**.

## Sintomi riportati
- Il dispositivo assorbe dal caricatore **zero o pochissimi** (range **0.01–0.15 A**).
- L’iPad **può o non può** avviarsi.

## Diagnosi (passi chiave)
1. **Porta di ricarica (USB‑C) spesso guasta** per **danno fisico o liquidi**.
   - Ispezionare visivamente i **pin** che fanno contatto con il cavo USB‑C.
   - Se i pin sono danneggiati: **sostituire la porta di ricarica**.
2. Componenti motherboard “più comuni” che possono impedire la ricarica (da verificare):
   - [CD3215C00](../componenti/cd3215c00.md)
   - [Tristar 610A3C](../componenti/tristar.md)
   - [343S00235](../componenti/343s00235.md)
3. **Controllare corti** attorno a ciascuno dei componenti sopra.

## Riparazione (azioni riportate)
- **Porta USB‑C danneggiata/corrotta**: sostituire il **flex cavo della porta di ricarica**.
- **Corto vicino ai controller di ricarica**:
  - Iniettare una **bassa tensione** sulla linea in corto.
  - Usare **termocamera** o **isopropanolo** per individuare il componente che genera il corto.
  - Rimuovere e testare finché il corto risulta eliminato.
  - Chip indicato come più comune da guasto su questo modello: **CD3215C00**.

## Note operative (da fonte)
- Per la ricerca del corto: combinazione **iniezione bassa tensione + termocamera** (o isopropanolo).
- Strumento citato: [termocamera](../strumenti/termocamera.md).

## Pagine wiki collegate (da questa fonte)
- [CD3215C00](../componenti/cd3215c00.md)
- [Tristar](../componenti/tristar.md)
- [343S00235](../componenti/343s00235.md)
- [termocamera](../strumenti/termocamera.md)
- Sintomo correlato (range assorbimento): [non-carica-0-01-0-15a](../sintomi/non-carica-0-01-0-15a.md)
