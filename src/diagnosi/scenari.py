"""Scenari di prova riusati da più script (stesso input = confronto onesto tra varianti)."""

A2316_PASSO1 = """\
Dispositivo: iPad Air 4 Wi-Fi (A2316).
Storia: caffè versato, si era spento e non caricava. Dopo pulizia con IPA della porta ha caricato
per ore fino a circa 60%, senza scaldare. Poi ha smesso di caricare: nessun fulmine, il PC non lo rileva.
Da spento, inserendo il cavo, si accende ma non carica.
Misure fatte:
- Porta USB-C in diode mode: CC1/CC2 0.53/0.63 stabili; D+/D- lato A instabili; RX1+ va e viene a 0.00 verso GND.
- Senza batteria, USB da alimentatore: 5.2 V, 0.11-0.20 A, resta a 5 V (nessuna negoziazione PD).
- Con batteria e iPad acceso, cavo inserito: 0.002 A dall'USB.
Qual è il prossimo passo?"""
