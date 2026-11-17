---
variante: senza wiki (prompt da tecnico + PassoDiagnosi, nessuna fonte)
data: 2026-11-16
provider: openai
modello: gpt-5.4-nano
script: scripts/passo_strutturato.py
token: 1164 in / 985 out
---

# A2316 — risposta SENZA wiki

## Input
La situazione `SITUAZIONE` di `scripts/passo_strutturato.py`: caffè, ha caricato fino a ~60% dopo la pulizia,
poi niente fulmine, PC non lo rileva, da spento si accende col cavo ma non carica; diode mode porta (CC ok,
D+/D− lato A instabili, RX1+ a 0.00 intermittente); senza batteria 5.2 V / 0.11–0.20 A, niente PD;
con batteria e acceso 0.002 A.

## Output
**Ipotesi**
1. [media] Circuito di ricarica/PMIC o linea di abilitazione carica — si accende col cavo ma prende ~2 mA: tipico se il PMIC non abilita la carica o una linea di sensing/enable è interrotta.
2. [alta] Controller USB-C/PD ("Uxxxx vicino alla porta") — niente PD, dati instabili; se danneggiato da liquido: CC ok ma nessuna negoziazione né enumerazione.
3. [alta] Connettore USB-C o microsaldature sui pad — ossido/contatto intermittente su pin dati o massa.

**Prossima misura:** porta USB-C, D+ e D− verso GND, in **resistenza** (ohm). Condizioni: iPad spento, "batteria scollegata? (se non vuoi aprire: lascia batteria presente)", cavo non necessario.
Valore atteso: > 100 kΩ. Se basso (< 10–20 kΩ): contaminazione/short → pulizia e rework pad; se alto: IC USB-C/PD o RX1/TX1.

**Sicurezza:** non cortocircuitare i pin dati; non alimentare/riscaldare finché non escludi corti; ESD; scollegare la batteria prima di lavorare in zona porta/PMIC.

**Domande:** resistenza D+/D− verso GND? RX1+ misurato sul lato scheda? Caricatore PD e più cavi provati?

**Fonti:** nessuna.

## Valutazione (confronto con la diagnosi reale: X3 343S00264 n.1, CD3217 n.2)
| Aspetto | Esito |
|---|---|
| Direzione generale | ✅ USB-C/PD controller tra le ipotesi alte: è il n.2 reale |
| Specificità | ❌ nessuna sigla del modello ("Uxxxx", "PMIC"): non sa cosa c'è sull'A2316 (CD3217, 343S00264) |
| Ordine delle ipotesi | ❌ la n.1 è [media] davanti a due [alta]: viola "ordinate dalla più probabile" |
| Connettore | ⚠️ dato [alta], ma nel caso reale con letture pulite non caricava comunque: corrosione presente ma non causa |
| Prossima misura | ❌ ripete in resistenza ciò che è già stato misurato in diode mode sulle stesse linee; non propone il percorso VBUS dopo il controller (uscita CD3217 → ingresso IC di carica), che è la misura decisiva |
| Condizioni | ❌ incerte ("batteria scollegata?"); non coglie la differenza con/senza batteria (modalità *dead battery* del CD3217) |
| Domanda sul caricatore PD | ✅ sensata |
| Fonti | ❌ nessuna: impossibile verificare da dove viene il ragionamento |

**In sintesi:** ragionamento plausibile ma generico. Mancano conoscenza specifica del modello, la regola
"misurare sempre nelle stesse condizioni" e la misura che discrimina. È esattamente ciò che la wiki deve aggiungere.

**Valutazione del tecnico (Antonino):**
- 
