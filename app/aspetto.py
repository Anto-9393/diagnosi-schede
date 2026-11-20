"""Aspetto dell'interfaccia: colori della scheda (solder mask verde, rame), carattere Barlow, e le funzioni che
trasformano un PassoDiagnosi in HTML.

Ogni testo che viene dal modello passa da html.escape: l'output dell'LLM è un dato NON fidato per chi lo
mostra (S15, output handling). Senza escape, un "<script>" o un link in una risposta finirebbe nella pagina.
"""
import re
from html import escape

COLORI = {"fondo": "#F2F5F2", "inchiostro": "#1A2420", "maschera": "#1E5B45", "rame": "#B5652B",
          "muto": "#5E6E66", "linea": "#C9D4CD", "rosso": "#B42318", "ambra": "#8A5A00"}

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600&family=Barlow+Semi+Condensed:wght@500;600;700&family=Share+Tech+Mono&display=swap');
/* Solo testo: NON le icone di Streamlit (sono un font a sé: cambiarlo mostra il nome dell'icona, es. "keyboard_double_…") */
html, body, .stApp, .stMarkdown, .stMarkdown p, .stMarkdown li, label, input, textarea, button p, .stCaption {
  font-family: 'Barlow', system-ui, sans-serif; }
h1, h2, h3 { font-family: 'Barlow Semi Condensed', 'Barlow', sans-serif; font-weight: 700; letter-spacing: .005em; }
h1 { font-size: 2.1rem; color: #EEF2E6; margin-bottom: .2rem; }
.block-container { max-width: 920px; }

/* Stile "scheda madre": piste di rame e via dorate lungo i bordi della pagina, fori di fissaggio */
.stApp { background-color: #12402F;
  background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='130' height='560'><g fill='none' stroke='%23B8743F' stroke-width='5' opacity='.5'><path d='M130 70 H96 L72 94 V300 L96 324 H130'/><path d='M130 420 H110 L94 436 V560'/></g><g fill='%2312402F' stroke='%23D9B25F' stroke-width='3'><circle cx='72' cy='94' r='8'/><circle cx='72' cy='300' r='8'/><circle cx='94' cy='436' r='8'/></g><circle cx='104' cy='372' r='14' fill='%230B241A' stroke='%23D9B25F' stroke-width='5'/></svg>"),
    url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='130' height='420'><g fill='none' stroke='%23B8743F' stroke-width='5' opacity='.5'><path d='M130 40 H100 L80 60 V240 L100 260 H130'/></g><g fill='%2312402F' stroke='%23D9B25F' stroke-width='3'><circle cx='80' cy='60' r='8'/><circle cx='80' cy='240' r='8'/></g><circle cx='104' cy='390' r='14' fill='%230B241A' stroke='%23D9B25F' stroke-width='5'/></svg>");
  background-repeat: no-repeat, no-repeat; background-position: right top, right bottom; background-attachment: fixed, fixed; }
[data-testid="stHeader"] { background: transparent; }
[data-testid="stSidebar"] { background: #0B2A1F; border-right: 3px dashed #2E6B54; }
[data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2 { font-family: 'Share Tech Mono', monospace; font-weight: 400; color: #EEF2E6; }
.serigrafia { font-family: 'Share Tech Mono', monospace; color: #E0A06A; font-size: .95rem; margin: 0 0 .2rem; }
[data-testid="stChatInput"] { border: 2px solid #B8743F; border-radius: 10px; }
/* la casella del messaggio partiva alta mezza pagina: una riga, cresce mentre scrivi */
[data-testid="stChatInput"] textarea { height: auto !important; }
/* riquadri informativi: niente azzurro di default, chip scuro con bordo rame come il resto */
[data-testid="stAlertContainer"], [data-testid="stAlert"] > div { background-color: #0B2A1F !important; border: 1px dashed #8E9893; color: #E6EFE9 !important; }
[data-testid="stAlert"] p { color: #CFE0D6 !important; }
/* domande di esempio nella pagina vuota */
/* pagina iniziale: logo, titolo e casella al centro, come un banco pulito */
.copertina { text-align: center; margin: 6vh 0 1.2rem; }
.copertina img { width: 110px; height: 110px; border-radius: 50%; border: 3px solid #D9B25F; background: #0B2A1F; }
.copertina h1 { font-size: 2.6rem; margin: .6rem 0 .2rem; padding: 0; }
.copertina p { color: #9DB5A8; font-size: 1.05rem; margin: 0; }
.copertina .sigla { font-family: 'Share Tech Mono', monospace; color: #E0A06A; font-size: .85rem; letter-spacing: .04em; }
.st-key-esempi button { background: #0B2A1F; border: 1px solid #B8743F; color: #E6EFE9; border-radius: 999px; }
.st-key-esempi button:hover { border-color: #E0A06A; color: #E0A06A; }
[data-testid="stExpander"] details { background: #17211D; border: 0; border-top: 4px dashed #56645E; border-bottom: 4px dashed #56645E; border-radius: 4px; }
/* Avatar della chat più grandi: il tecnico in camice e il multimetro devono riconoscersi */
[data-testid="stChatMessage"] > div:first-child:has(img), [data-testid="stChatMessageAvatarCustom"] { width: 3.2rem !important; height: 3.2rem !important; }
[data-testid="stChatMessage"] img { width: 3.2rem !important; height: 3.2rem !important; border-radius: 50%; }

/* "Mi serve sapere": riquadro a chip con un campo per domanda */
[data-testid="stForm"] { background: #17211D; border: 0; border-top: 5px dashed #E0A06A; border-bottom: 5px dashed #E0A06A; border-radius: 6px; }
[data-testid="InputInstructions"] { display: none; }    /* "Press Enter to submit form": in inglese e inutile qui */

/* La carta della misura: un chip, con il valore atteso sul display del multimetro */
.misura { background: #17211D; padding: 1rem 1.25rem 1.1rem; margin: .5rem 0 1rem; border-radius: 6px;
          border-top: 6px dashed #8FD9B0; border-bottom: 6px dashed #8FD9B0; }
.misura .cosa { font-family: 'Share Tech Mono', monospace; color: #E0A06A; font-size: .95rem; margin: 0 0 .15rem; }
.misura .dove { font-family: 'Barlow Semi Condensed', sans-serif; font-weight: 700; font-size: 1.5rem;
                line-height: 1.15; color: #EEF2E6; margin: 0 0 .5rem; }
.misura .modo { display: inline-block; border: 1px solid #E0A06A; color: #E0A06A; border-radius: 4px;
                padding: 0 .45rem; font-size: .85rem; font-weight: 600; vertical-align: middle; margin-left: .4rem; }
.misura .condizioni { margin: 0 0 .7rem; max-width: 68ch; color: #CFE0D6; }
.misura .etichetta { color: #9DB5A8; font-size: .9rem; margin: 0 0 .2rem; }
.misura .atteso { font-family: 'Share Tech Mono', monospace; font-size: 1.05rem; color: #1D2A1A; background: #B9C8A0;
                  border: 4px solid #2A3A2E; border-radius: 6px; padding: .45rem .7rem; margin: 0; line-height: 1.35; max-width: 64ch; }
.misura .se { color: #CFE0D6; margin: .55rem 0 0; max-width: 68ch; }

.riepilogo { color: #CFE0D6; margin: 0 0 .8rem; max-width: 70ch; }
ol.ipotesi { padding-left: 1.3rem; margin: 0 0 1rem; }
ol.ipotesi li { margin: 0 0 .55rem; max-width: 70ch; }
ol.ipotesi .comp { font-weight: 600; color: #EEF2E6; }
.prob { display: inline-flex; gap: 2px; vertical-align: middle; margin-left: .45rem; }
.prob i { width: 14px; height: 6px; background: #2E6B54; border-radius: 1px; }
.prob i.on { background: #8FD9B0; }

.avviso { border-left: 4px solid #D9B25F; background: #33301A; padding: .45rem .8rem; margin: 0 0 .45rem;
          color: #F3E3B8; max-width: 72ch; border-radius: 0 6px 6px 0; }
.avviso.controllo { border-left-color: #F07B66; background: #3D1E19; color: #F8CFC6; }
.avviso .fonte-avviso { font-weight: 600; margin-right: .35rem; }
.avviso.bloccante { border-left-color: #F07B66; background: #4A1D17; color: #FBD7CF; font-weight: 600; }
.domande { margin: .2rem 0 .8rem; padding-left: 1.1rem; }
.fonti { color: #9DB5A8; font-size: .9rem; margin: .4rem 0 0; }
.fonti code { background: #0B2A1F; color: #CFE0D6; }
.dati { font-family: 'Share Tech Mono', monospace; color: #9DB5A8; font-size: .85rem; }
.scheda h3 { margin: .3rem 0 0; }
.scheda .codici { color: #9DB5A8; margin: .1rem 0 .6rem; }
.guide h4 { font-family: 'Barlow Semi Condensed', sans-serif; font-size: 1.05rem; margin: .9rem 0 .3rem; color: #8FD9B0; }
.guide ul { margin: 0 0 .4rem 1.1rem; padding: 0; }
.guide li { margin: .15rem 0; }
.guide ul.pagine { list-style: none; margin-left: 0; }
.guide ul.pagine li { display: grid; grid-template-columns: 7rem 1fr; gap: .5rem; margin: .35rem 0; }
.guide .tipo { font-size: .8rem; color: #9DB5A8; padding-top: .2rem; }
.guide .percorso { font-size: .8rem; color: #9DB5A8; }
.guide .vuoto { color: #9DB5A8; }
.procedura .obiettivo { font-family: 'Barlow Semi Condensed', sans-serif; font-size: 1.35rem; font-weight: 600; margin: .2rem 0 .6rem; color: #EEF2E6; }
.procedura ol.passi { list-style: none; counter-reset: passo; margin: 0; padding: 0; }
.procedura ol.passi > li { counter-increment: passo; position: relative; padding: 0 0 .9rem 2.6rem; }
.procedura ol.passi > li::before { content: counter(passo); position: absolute; left: 0; top: 0; width: 1.8rem; height: 1.8rem;
  border-radius: 50%; background: #12402F; border: 3px solid #D9B25F; box-sizing: border-box; color: #EEF2E6; font-weight: 600;
  text-align: center; line-height: 1.45rem; font-family: 'Share Tech Mono', monospace; }
.procedura ol.passi > li:not(:last-child)::after { content: ""; position: absolute; left: .82rem; top: 1.8rem; bottom: .2rem;
  border-left: 4px solid #B8743F; }
.procedura .titolo-passo { font-weight: 600; margin: .15rem 0 .2rem; color: #EEF2E6; }
.procedura .attrezzo { color: #E0A06A; font-weight: 600; margin: .25rem 0 0; }
.procedura .controllo { color: #9DB5A8; margin: .2rem 0 0; }
.procedura .controllo b, .procedura .attrezzo b { font-weight: 600; color: inherit; }
/* Lo scorrimento automatico si ferma un po' sotto la barra in alto di Streamlit */
[data-testid="stChatMessage"] { scroll-margin-top: 4.5rem; scroll-margin-bottom: 7rem; }
/* Loader "al banco": una scheda sotto i ferri. Cacciavite che avvita, pinza che posa un condensatore,
   corrente che scorre nelle piste, fumo di flussante dal chip. Un'unica scena, in loop. */
.banco { display: flex; align-items: center; gap: 18px; padding: .4rem 0; }
.banco svg { flex: none; overflow: visible; }
.banco .testo-loader { color: #9DB5A8; font-size: 1rem; line-height: 1.4; }
.banco .testo-loader b { color: #EEF2E6; }
.banco .cacciavite { animation: scendi 1.6s ease-in-out infinite; }
.banco .impugnatura { animation: gira-manico .4s linear infinite; }
.banco .taglio { transform-origin: 34px 63px; animation: avvita 1.6s ease-in-out infinite; }
.banco .pinza { animation: posa 2.4s ease-in-out infinite; }
.banco .ganascia-a { transform-origin: 158px 30px; animation: apri-a 2.4s ease-in-out infinite; }
.banco .ganascia-b { transform-origin: 158px 30px; animation: apri-b 2.4s ease-in-out infinite; }
.banco .condensatore { animation: lascia 2.4s ease-in-out infinite; }
.banco .posato { animation: posato 2.4s ease-in-out infinite; }
.banco .pista { stroke-dasharray: 5 7; animation: corrente 1.1s linear infinite; }
.banco .pista.lenta { animation-duration: 1.7s; }
.banco .fumo { animation: fumo 2.2s ease-out infinite; }
.banco .fumo.due { animation-delay: .7s; }
.banco .fumo.tre { animation-delay: 1.4s; }
.banco .led { animation: led 1.6s ease-in-out infinite; }
@keyframes scendi { 0%, 20%, 100% { transform: translateY(-16px); } 40%, 75% { transform: translateY(0); } }
@keyframes gira-manico { from { transform: translateX(0); } to { transform: translateX(-4px); } }
@keyframes avvita { 0%, 40% { transform: rotate(0deg); } 75%, 100% { transform: rotate(270deg); } }
@keyframes posa { 0%, 100% { transform: translateY(-12px); } 40%, 62% { transform: translateY(6px); } }
@keyframes apri-a { 0%, 45% { transform: rotate(0deg); } 55%, 80% { transform: rotate(7deg); } 100% { transform: rotate(0deg); } }
@keyframes apri-b { 0%, 45% { transform: rotate(0deg); } 55%, 80% { transform: rotate(-7deg); } 100% { transform: rotate(0deg); } }
@keyframes lascia { 0%, 50% { opacity: 1; } 51%, 100% { opacity: 0; } }
@keyframes posato { 0%, 50% { opacity: 0; } 51%, 96% { opacity: 1; } 100% { opacity: 0; } }
@keyframes corrente { to { stroke-dashoffset: -24; } }
@keyframes fumo { 0% { opacity: 0; transform: translate(0, 0) scale(.6); } 25% { opacity: .55; }
  100% { opacity: 0; transform: translate(6px, -26px) scale(1.6); } }
@keyframes led { 0%, 100% { opacity: .35; } 50% { opacity: 1; } }
@media (prefers-reduced-motion: reduce) { .banco * { animation: none !important; } }
</style>
"""

_LIVELLI = {"alta": 3, "media": 2, "bassa": 1}


def _barra(probabilita: str) -> str:
    n = _LIVELLI.get(probabilita, 0)
    return f'<span class="prob" title="probabilità {escape(probabilita)}">' + "".join(
        f'<i class="{"on" if k < n else ""}"></i>' for k in range(3)) + "</span>"


def risposta_html(passo, esito, con_domande: bool = True) -> str:
    if esito.bloccato:
        return "".join(f'<div class="avviso bloccante">{escape(a)}</div>' for a in esito.avvisi) + \
               '<p class="riepilogo">La risposta è stata fermata dai controlli di sicurezza. Riformula la richiesta o ' \
               'aggiungi le condizioni di misura.</p>'
    m = passo.prossima_misura
    parti = []
    # Gli avvisi aggiunti dai guardrail (codice) si distinguono da quelli scritti dal modello.
    for a in passo.avvertenze_sicurezza:
        if a in esito.avvisi:
            parti.append(f'<div class="avviso controllo"><span class="fonte-avviso">Controllo automatico:</span>{escape(a)}</div>')
        else:
            parti.append(f'<div class="avviso">{escape(a)}</div>')
    # Ordine del ragionamento: cosa sappiamo -> ipotesi -> quindi cosa misuro (richiesta del tecnico, 18 nov).
    if hasattr(passo, "ipotesi"):
        parti.append(f'<p class="riepilogo">{escape(passo.riepilogo)}</p>')
        voci = "".join(f'<li><span class="comp">{escape(i.componente)}</span>{_barra(i.probabilita)}<br>{escape(i.motivo)}</li>'
                       for i in passo.ipotesi)
        parti.append(f'<ol class="ipotesi">{voci}</ol>')
    # Domanda di teoria ("che differenza c'è tra…"): nessuna misura da fare, niente riquadro vuoto con i trattini.
    vuoto = lambda t: re.sub(r"[\s—–.-]", "", t or "") == ""
    if not (vuoto(m.dove) or (m.modalita == "altro" and vuoto(m.valore_atteso))):
        parti.append(
            '<div class="misura">'
            '<p class="cosa">Prossima misura</p>'
            f'<p class="dove">{escape(m.dove)}<span class="modo">{escape(m.modalita)}</span></p>'
            f'<p class="condizioni">{escape(m.condizioni)}</p>'
            '<p class="etichetta">Su una scheda sana</p>'
            f'<p class="atteso">{escape(m.valore_atteso)}</p>'
            '<p class="etichetta" style="margin-top:.55rem">Se il valore è diverso</p>'
            f'<p class="se" style="margin-top:0">{escape(m.se_diverso)}</p>'
            '</div>')
    if con_domande and passo.domande_al_tecnico:      # nell'app le domande diventano campi da compilare
        parti.append("<p><b>Mi serve sapere</b></p><ul class=\"domande\">"
                     + "".join(f"<li>{escape(q)}</li>" for q in passo.domande_al_tecnico) + "</ul>")
    fonti = ", ".join(f"<code>{escape(f)}</code>" for f in passo.fonti) or "nessuna pagina della wiki: da verificare"
    parti.append(f'<p class="fonti">Fonti: {fonti}</p>')
    return "".join(parti)


def _n(x: int) -> str:
    return f"{x:,}".replace(",", ".")                 # 27.661 all'italiana


def dati_html(info: dict) -> str:
    cache = info.get("token_cache", 0)
    in_cache = f" (di cui {_n(cache)} in cache)" if cache else ""
    return (f'<span class="dati">{info["durata_s"]:.1f} s — {_n(info["token_in"])} token in ingresso{in_cache}, '
            f'{_n(info["token_out"])} in uscita, {len(info["tool"])} letture della wiki, {escape(str(info["modello"]))}, '
            f'risposta {escape(str(info.get("dettaglio", "completa")))}, lettura {escape(str(info.get("lettura", "approfondita")))}</span>')


TIPI = {"caso": "Caso reale", "sintomo": "Sintomo", "tecnica": "Tecnica", "componente": "Componente",
        "strumento": "Strumento"}


def guide_html(d: dict, guide: dict) -> str:
    """Elenco delle guide di un dispositivo (nessuna chiamata all'LLM)."""
    titolo = escape(d.get("titolo", "?"))
    parti = [f"<div class='guide'><p>Ecco cosa c'è per <b>{titolo}</b>. "
             "Scrivi il sintomo e le misure già fatte per iniziare la diagnosi.</p>"]
    if guide["wiki"]:
        voci = "".join(f'<li><span class="tipo">{escape(TIPI.get(p["tipo"], p["tipo"]))}</span>'
                       f'<span>{escape(p["titolo"])}<br><span class="percorso">{escape(p["percorso"])}</span></span></li>' for p in guide["wiki"])
        parti.append(f"<h4>Nella nostra wiki ({len(guide['wiki'])})</h4><ul class='pagine'>{voci}</ul>")
    if guide["repairwiki"]:
        voci = "".join(f'<li><a href="{escape(g["url"], quote=True)}" target="_blank">{escape(g["titolo"])}</a></li>'
                       for g in guide["repairwiki"])
        parti.append(f"<h4>Guide originali su repair.wiki ({len(guide['repairwiki'])})</h4><ul>{voci}</ul>"
                     '<p class="dati">Testi di repair.wiki, licenza CC BY-SA 3.0.</p>')
    if not guide["wiki"] and not guide["repairwiki"]:
        parti.append('<p class="vuoto">Nessuna guida specifica per questo modello. Puoi comunque descrivere il guasto: '
                     "l'agente userà le pagine generali (sintomi, componenti, tecniche).</p>")
    return "".join(parti) + "</div>"


def procedura_html(proc, esito, con_domande: bool = True) -> str:
    """La risposta "come si fa": passi numerati in sequenza (qui i numeri hanno senso, è un ordine reale)."""
    if esito.bloccato:
        return risposta_html(proc, esito)
    parti = []
    for a in proc.avvertenze_sicurezza:
        classe = "avviso controllo" if a in esito.avvisi else "avviso"
        etichetta = '<span class="fonte-avviso">Controllo automatico:</span>' if a in esito.avvisi else ""
        parti.append(f'<div class="{classe}">{etichetta}{escape(a)}</div>')
    parti.append(f'<div class="procedura"><p class="obiettivo">{escape(proc.obiettivo)}</p>')
    voci = []
    for p in proc.passi:
        v = f'<li><p class="titolo-passo">{escape(p.titolo)}</p><div>{escape(p.azione)}</div>'
        if p.attrezzo:
            v += f'<p class="attrezzo">{escape(p.attrezzo)}</p>'
        if p.controllo:
            v += f'<p class="controllo"><b>Controllo:</b> {escape(p.controllo)}</p>'
        voci.append(v + "</li>")
    parti.append(f'<ol class="passi">{"".join(voci)}</ol>')
    if proc.verifica_finale:
        parti.append("<p><b>Verifica finale</b></p><ul>" + "".join(f"<li>{escape(x)}</li>" for x in proc.verifica_finale) + "</ul>")
    parti.append("</div>")
    if con_domande and proc.domande_al_tecnico:
        parti.append("<p><b>Mi serve sapere</b></p><ul class=\"domande\">"
                     + "".join(f"<li>{escape(q)}</li>" for q in proc.domande_al_tecnico) + "</ul>")
    fonti = ", ".join(f"<code>{escape(f)}</code>" for f in proc.fonti) or "nessuna pagina della wiki: da verificare"
    parti.append(f'<p class="fonti">Fonti: {fonti}</p>')
    return "".join(parti)


_SCENA = """<svg width="220" height="96" viewBox="0 0 220 96" aria-hidden="true">
  <rect x="6" y="56" width="208" height="34" rx="5" fill="#1F6B50"/>
  <rect x="6" y="56" width="208" height="34" rx="5" fill="none" stroke="#3E8A6C" stroke-width="2"/>
  <path class="pista" d="M46 76 H86 V68 H100" stroke="#D08A4E" stroke-width="2.2" fill="none"/>
  <path class="pista lenta" d="M128 68 H142 V80 H196" stroke="#D08A4E" stroke-width="2.2" fill="none"/>
  <path class="pista lenta" d="M18 84 H70 V82" stroke="#D08A4E" stroke-width="2" fill="none"/>
  <rect x="100" y="62" width="28" height="18" rx="2" fill="#1A2420"/>
  <g fill="#C9D2CD"><rect x="103" y="59" width="2" height="3"/><rect x="109" y="59" width="2" height="3"/>
    <rect x="115" y="59" width="2" height="3"/><rect x="121" y="59" width="2" height="3"/>
    <rect x="103" y="80" width="2" height="3"/><rect x="109" y="80" width="2" height="3"/>
    <rect x="115" y="80" width="2" height="3"/><rect x="121" y="80" width="2" height="3"/></g>
  <circle class="led" cx="196" cy="66" r="3" fill="#F2B84B"/>
  <rect x="151" y="62" width="14" height="6" rx="1" fill="#2E6B54"/>
  <rect class="posato" x="152" y="62" width="12" height="6" rx="1.5" fill="#D9A066"/>
  <circle class="fumo" cx="114" cy="58" r="3.5" fill="#C9D2CD"/>
  <circle class="fumo due" cx="118" cy="58" r="3" fill="#C9D2CD"/>
  <circle class="fumo tre" cx="110" cy="58" r="2.6" fill="#C9D2CD"/>
  <circle cx="34" cy="63" r="6.5" fill="#B9C4BE" stroke="#7C8C85" stroke-width="1.5"/>
  <g class="taglio"><rect x="29.5" y="62" width="9" height="2" rx="1" fill="#5B6A63"/></g>
  <g class="cacciavite">
    <rect x="32.5" y="30" width="3" height="27" fill="#8A9A92"/>
    <path d="M32.5 57 L35.5 57 L34 61 Z" fill="#8A9A92"/>
    <svg x="27" y="4" width="14" height="27" viewBox="0 0 14 27"><rect width="14" height="27" rx="4" fill="#B5652B"/>
      <g class="impugnatura" fill="#8E4E20"><rect x="2" y="3" width="2" height="21" rx="1"/><rect x="6" y="3" width="2" height="21" rx="1"/>
      <rect x="10" y="3" width="2" height="21" rx="1"/><rect x="14" y="3" width="2" height="21" rx="1"/></g></svg>
    <rect x="27" y="27" width="14" height="4" rx="1" fill="#8E4E20"/>
  </g>
  <g class="pinza">
    <g class="ganascia-a"><path d="M158 30 L154 56" stroke="#8A9A92" stroke-width="3.5" stroke-linecap="round"/>
      <path d="M158 30 L148 4" stroke="#1E5B45" stroke-width="6" stroke-linecap="round"/></g>
    <g class="ganascia-b"><path d="M158 30 L162 56" stroke="#8A9A92" stroke-width="3.5" stroke-linecap="round"/>
      <path d="M158 30 L168 4" stroke="#1E5B45" stroke-width="6" stroke-linecap="round"/></g>
    <circle cx="158" cy="30" r="3" fill="#1A2420"/>
    <rect class="condensatore" x="152" y="56" width="12" height="6" rx="1.5" fill="#D9A066"/>
  </g>
</svg>"""


def loader_html(testo: str) -> str:
    """Attesa "al banco": una scena animata (cacciavite, pinza, piste, fumo) + testo, es. il timer."""
    return f'<div class="banco" role="status">{_SCENA}<span class="testo-loader">{testo}</span></div>'
