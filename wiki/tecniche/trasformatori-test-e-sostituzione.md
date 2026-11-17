---
titolo: Trasformatori — test e sostituzione
tipo: tecnica
riassunto: Tecnica generale per ispezionare, verificare continuità/resistenza/induttanza
  e, se necessario, riparare o sostituire un trasformatore (con attenzione al rapporto
  spire).
modelli: []
fonti:
- raw/repairwiki/pagine/transformers-repair-basics.md
aggiornato: '2026-11-17'
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
---

## Scopo
Questa tecnica descrive come **testare un trasformatore** (o induttore con più avvolgimenti) e come procedere alla **riparazione/sostituzione** quando risulta guasto.

> Nota: in riparazione schede, spesso il trasformatore è un **componente “a valle”**: può guastarsi come **sintomo** di problemi su altri componenti/rail. La fonte indica che i trasformatori “raramente falliscono” se il resto del circuito è corretto.

## 1) Ispezione visiva (prima di misurare)
1. Scollega alimentazione e batteria.
2. Ispeziona il trasformatore per:
   - segni di bruciatura,
   - rottura/cedimento dell’isolamento,
   - deformazioni del componente.

Se trovi danni evidenti (burn marks, isolamento rotto, deformazioni), tratta il componente come sospetto principale e passa ai test elettrici.

## 2) Preparazione: rimozione per misure affidabili
La fonte consiglia che è difficile misurare il trasformatore **in circuito** (a meno che non sia già “aperto/blown”).

**Procedura consigliata: desaldare il trasformatore** prima di misurare.

## 3) Identificazione avvolgimenti (primario/secondario)
1. Identifica i terminali degli avvolgimenti tramite:
   - schema elettrico,
   - serigrafia/etichettatura sul PCB.
2. Determina **primario** e **secondario** (o più secondari) prima di fare continuità/resistenza.

## 4) Test continuità (multimetro)
1. Imposta il multimetro in modalità **continuity**.
2. Verifica che **ogni avvolgimento** sia elettricamente continuo.

**Interpretazione (fonte):**
- **Circuito aperto** su un avvolgimento → possibile **taglio** del filo dell’avvolgimento.

## 5) Test resistenza DC (ohmmetro)
1. Misura la **resistenza DC** del primario e del secondario.

**Interpretazione (fonte):**
- **Resistenza estremamente bassa** → possibile **avvolgimento in corto**.
- **Resistenza anormalmente alta** → possibile **interruzione interna** o **connessioni degradate**.

> La fonte specifica anche che è “difficile” misurare la resistenza “bassa” senza un riferimento: in alternativa, è preferibile misurare l’induttanza con un LCR meter se disponibile.

## 6) Test induttanza (LCR meter) — quando disponibile
Se hai un **LCR meter** e un **datasheet/trasformatore di riferimento**, misura l’**induttanza** di ciascun avvolgimento.

**Motivo (fonte):** la resistenza DC può essere poco informativa senza riferimento; l’induttanza aiuta a capire se l’avvolgimento è degradato.

Valori attesi: **da verificare** (la fonte non fornisce numeri specifici).

## 7) Quando “riparare” vs “sostituire”
La fonte afferma che:
- in **9/10 casi** non è possibile comprare un trasformatore sostitutivo “standard”
- spesso i trasformatori sono **scelti/progettati specificamente** per quel circuito
- quindi la sostituzione diretta è rara; la via principale è **rewiring/rifacimento dell’avvolgimento**.

## 8) Riparazione/rifacimento avvolgimento (rewind)
Questa è la procedura descritta dalla fonte.

### 8.1 Apertura del trasformatore
1. Apri il trasformatore: tipicamente il **core è diviso in due parti** e tenuto insieme con **colla**.
2. Cerca di **non rompere** il core: la fonte avverte che rompere/degradare il core può peggiorare le prestazioni.

### 8.2 Smontaggio avvolgimenti
1. Svolgi **ogni avvolgimento individualmente**.
2. Tieni traccia di:
   - **numero di spire**,
   - **ordine** degli avvolgimenti.

> La fonte sottolinea che è “really important” mantenere **ordine e numero di spire**.

### 8.3 Riutilizzo isolamento
- Se l’isolamento **non è danneggiato**, può essere **riutilizzato**.

### 8.4 Sostituzione filo (wire) e diametro
1. Misura il **diametro** del/i avvolgimento/i difettoso/i (o di tutti se devi rifare più avvolgimenti).
2. Usa lo stesso diametro di filo **enameled** (smaltato) per ricostruire.

### 8.5 Ricostruzione avvolgimenti
1. Crea lo **stesso numero di spire** sul core.
2. Rispetta **l’ordine** degli avvolgimenti come prima.
3. Incolla/rimetti il core in posizione.

## 9) Rischi principali (attenzione al rapporto spire)
La fonte chiude con un punto critico:
- **rapporto spire errato** può **danneggiare i circuiti**.

Quindi, prima di richiudere e rimontare:
- ricontrolla numero spire e ordine,
- verifica che il filo e l’isolamento siano corretti.

## Collegamenti utili
- Per test su induttori/avvolgimenti in generale: [induttori](../componenti/induttori.md)
- Per basi su corti/diagnosi: [short-circuits-repair-basics](../fonti/short-circuits-repair-basics.md) (pagina fonte già presente)
