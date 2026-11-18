---
licenza: CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
lingua: it
originale: raw/repairwiki/pagine/ipad-air-4-not-reading-touch.md
tradotto: '2026-11-18'
---

# iPad Air 4 Non legge il touch

> Fonte: [IPad Air 4 Not Reading Touch — repair.wiki](https://repair.wiki/w/IPad_Air_4_Not_Reading_Touch), CC BY-SA 3.0. Autori: vedi cronologia.
> Traduzione automatica in italiano (2026-11-18): opera modificata, stessa licenza CC BY-SA 3.0.


## Descrizione del problema
iPad Air 4 si avvia e funziona normalmente tranne per il fatto che non legge il touch

## Sintomi
- Non legge il touch

### Passi di diagnostica
- La prima cosa che vorrai provare è uno schermo sicuramente funzionante per assicurarti che non sia un problema di display. Ricorda di usare uno schermo sicuramente funzionante che avesse il touch funzionante su un altro iPad, perché i display nuovi possono avere problemi abbastanza comunemente.
- Esegui un’ispezione fisica del connettore FPC del display centrale per assicurarti che non sia rotto e che tutti i pin siano ben saldi.  
- Stacca il nastro nero che copre le shield al centro della board. Questo dovrebbe scoprire una sagoma a “J” nella shield come in Figura 1. Imposta il multimetro in diode mode e, con la sonda rossa su ground, usa la sonda nera per controllare entrambi i lati di tutti i capacitori nella grande apertura orizzontale della “J”
- Probabilmente troverai che uno o più dei capacitori in alto a sinistra o al centro della grande apertura orizzontale sono in corto verso ground su entrambi i lati.

### Passi di riparazione
Sopra i capacitori che abbiamo appena controllato ci sono due IC che controllano il touch; se uno dei capacitori è in corto verso ground su una delle linee di alimentazione di questi IC allora il circuito touch non funzionerà e avrai un iPad senza touch anche con uno schermo sicuramente funzionante. Ora devi trovare il capacitore in corto e rimuoverlo.

- Per trovare il capacitore in corto dovrai usare una DCPSU per iniettare tensione sulla linea e, con una thermal camera o spray refrigerante, possiamo determinare quale cap sta scaldando. Poiché la maggior parte dei software di boardview non elenca i nomi delle power rails per l’iPad Air 4, non sappiamo a che tipo di tensione lavorano queste linee, quindi per sicurezza impostiamo la DCPSU a 1v/1a che è una quantità sicura di potenza da iniettare su quasi qualsiasi power rail di iPad.
- Boardview ci dice almeno dove va ciascuna power rail e in questo caso scopriamo che la power rail si collega principalmente a molti caps lungo il perimetro o alle due touch IC come in Figura 2, tuttavia vediamo anche che tramite un filtro si collega a un’altra “riga” di caps sotto la shield accanto a dove stiamo facendo le prove, come si vede in Figura 3.
- Con la tua DCPSU impostata a 1v/1a come sopra, posiziona la sonda nera su ground e la sonda rossa sul lato non-ground di uno dei capacitori della power rail che risulta in corto. Usando una thermal camera o spray refrigerante, osserva dove inizia a scaldarsi la board.
- Potresti avere fortuna e trovare uno dei capacitori esposti che scalda; se succede, rimuovi il cap in corto e testa per vedere se il touch funziona.
- se il calore sembra provenire dai caps sotto la neighboring shield, allora dovrai rimuovere tutta la shield con heat oppure usare una smerigliatrice e/o un utensile da taglio per esporre la “riga” di caps. Nel mio caso ho usato una smerigliatrice per tagliare una piccola linea nell’angolo della shield e poi delle pinze (snips) per tagliare e sollevare indietro il resto dell’area come in Figura 4.
- Ora inietta di nuovo tensione e verifica se uno dei caps appena esposti sta scaldando. Nel mio caso ne ho trovato uno che scaldava, come si vede in Figura 5
- Rimuovi il cap difettoso e testa per vedere se il touch funziona. Poiché i caps su questa power rail sono capacitori di smoothing e ce ne sono molti di più sulla stessa power rail, non dobbiamo preoccuparci di sostituirlo.
