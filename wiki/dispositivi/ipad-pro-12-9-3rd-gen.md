---
titolo: iPad Pro 12.9 3rd Gen
tipo: dispositivo
riassunto: 'iPad Pro 12.9 3rd Gen (A1876/A1895/A1983/A2014) che non carica: ispezione
  porta USB-C, verifica CD3215C00/Tristar 610A3C/343S00235 e ricerca corto con iniezione
  bassa tensione + termocamera.'
modelli:
- iPad Pro 12.9 3rd Gen
fonti:
- raw/repairwiki/pagine/ipad-pro-12-9-3rd-gen.md
- raw/repairwiki/pagine/ipad-pro-12-9-3rd-gen-not-charging-repair.md
aggiornato: '2026-11-17'
categoria: tablet
codici_modello: []
componenti_chiave:
- CD3215C00
- Tristar 610A3C
- 343S00235
casi: []
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

# iPad Pro 12.9 3rd Gen

- Uscita: 2018-11-07
- Codici modello: A1876, A1895, A1983, A2014

## Guasti tipici e casi

### Sintomi (da fonte)
- Il dispositivo assorbe **0.01–0.15 A** (zero o pochissimo) dal caricatore.
- L’iPad **può** o **non** avviarsi.

### Diagnosi mirata (da fonte)
1. **Ispezione porta USB-C**
   - La porta di ricarica su questo modello spesso fallisce per **danno fisico** o **danno da liquidi**.
   - Ispezionare visivamente i **pin** che fanno contatto con il cavo USB-C.
   - Se i pin sono danneggiati: **sostituire la porta / flex della porta di ricarica**.

2. **Componenti tipici che possono impedire la ricarica (da fonte)**
   Verificare e cercare **corti** attorno a:
   - [CD3215C00](../componenti/cd3215c00.md)
   - [Tristar 610A3C](../componenti/tristar.md)
   - [343S00235](../componenti/343s00235.md)

3. **Ricerca corto su rail di ricarica (da fonte)**
   - Se c’è un corto vicino ai controller di carica, **iniettare una bassa tensione** nella linea in corto.
   - Usare **termocamera** (o, in alternativa, **isopropyl alcohol** per evidenziare la zona calda/reattiva) per individuare il componente che causa il corto.
   - Rimuovere e testare finché il corto risulta eliminato.

### Riparazione (da fonte)
- **Porta USB-C danneggiata/corrotta**: sostituire il **flex della porta di ricarica**.
- **Corto vicino ai controller di carica**: individuare il componente in corto con iniezione bassa tensione + termocamera e rimuovere/sostituire il componente responsabile.
- Nota della fonte: il chip di carica più comune da guastare su questo modello è **CD3215C00**.

## Componenti chiave (da fonte)
- [CD3215C00](../componenti/cd3215c00.md)
- [Tristar 610A3C](../componenti/tristar.md)
- [343S00235](../componenti/343s00235.md)

## Note
- Valori e passaggi sopra sono riportati dalla fonte esterna indicata in pagina.
- Per misure elettriche aggiuntive (tensioni rail, resistenze attese, punti di test specifici) **da verificare**: non presenti nella fonte fornita.

Fonte: [IPad Pro 12.9 3rd Gen — repair.wiki](https://repair.wiki/w/IPad_Pro_12.9_3rd_Gen), CC BY-SA 3.0.

Fonte specifica: [IPad Pro 12.9 3rd Gen Not Charging Repair — repair.wiki](https://repair.wiki/w/IPad_Pro_12.9_3rd_Gen_Not_Charging_Repair), CC BY-SA 3.0.
