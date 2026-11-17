"""Aspetto dell'interfaccia: colori della scheda (solder mask verde, rame), carattere Barlow, e le funzioni che
trasformano un PassoDiagnosi in HTML.

Ogni testo che viene dal modello passa da html.escape: l'output dell'LLM è un dato NON fidato per chi lo
mostra (S15, output handling). Senza escape, un "<script>" o un link in una risposta finirebbe nella pagina.
"""
from html import escape

COLORI = {"fondo": "#F2F5F2", "inchiostro": "#1A2420", "maschera": "#1E5B45", "rame": "#B5652B",
          "muto": "#5E6E66", "linea": "#C9D4CD", "rosso": "#B42318", "ambra": "#8A5A00"}

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600&family=Barlow+Semi+Condensed:wght@500;600;700&display=swap');
/* Solo testo: NON le icone di Streamlit (sono un font a sé: cambiarlo mostra il nome dell'icona, es. "keyboard_double_…") */
html, body, .stApp, .stMarkdown, .stMarkdown p, .stMarkdown li, label, input, textarea, button p, .stCaption {
  font-family: 'Barlow', system-ui, sans-serif; }
h1, h2, h3 { font-family: 'Barlow Semi Condensed', 'Barlow', sans-serif; font-weight: 700; letter-spacing: .005em; }
h1 { font-size: 2.1rem; color: #1E5B45; margin-bottom: .2rem; }
.block-container { max-width: 920px; }

/* La carta della misura: l'unico elemento "forte" della pagina */
.misura { border-left: 6px solid #1E5B45; background: #FFFFFF; padding: 1rem 1.25rem 1.1rem; margin: .3rem 0 1rem;
          border-radius: 0 10px 10px 0; box-shadow: 0 1px 0 #C9D4CD; }
.misura .cosa { color: #5E6E66; font-size: .95rem; margin: 0 0 .15rem; }
.misura .dove { font-family: 'Barlow Semi Condensed', sans-serif; font-weight: 700; font-size: 1.5rem;
                line-height: 1.15; color: #1A2420; margin: 0 0 .5rem; }
.misura .modo { display: inline-block; border: 1px solid #1E5B45; color: #1E5B45; border-radius: 4px;
                padding: 0 .45rem; font-size: .85rem; font-weight: 600; vertical-align: middle; margin-left: .4rem; }
.misura .condizioni { margin: 0 0 .7rem; max-width: 68ch; }
.misura .etichetta { color: #5E6E66; font-size: .9rem; margin: 0; }
.misura .atteso { font-family: 'Barlow Semi Condensed', sans-serif; font-weight: 600; font-size: 1.2rem;
                  color: #B5652B; margin: 0; line-height: 1.3; max-width: 64ch; }
.misura .se { color: #33423B; margin: .55rem 0 0; max-width: 68ch; }

.riepilogo { color: #33423B; margin: 0 0 .8rem; max-width: 70ch; }
ol.ipotesi { padding-left: 1.3rem; margin: 0 0 1rem; }
ol.ipotesi li { margin: 0 0 .55rem; max-width: 70ch; }
ol.ipotesi .comp { font-weight: 600; }
.prob { display: inline-flex; gap: 2px; vertical-align: middle; margin-left: .45rem; }
.prob i { width: 14px; height: 6px; background: #C9D4CD; border-radius: 1px; }
.prob i.on { background: #1E5B45; }

.avviso { border-left: 4px solid #8A5A00; background: #FBF6EA; padding: .45rem .8rem; margin: 0 0 .45rem;
          color: #4A3600; max-width: 72ch; }
.avviso.controllo { border-left-color: #B42318; background: #FDF1EF; color: #6E1209; }
.avviso .fonte-avviso { font-weight: 600; margin-right: .35rem; }
.avviso.bloccante { border-left-color: #B42318; background: #FDEEEC; color: #6E1209; font-weight: 600; }
.domande { margin: .2rem 0 .8rem; padding-left: 1.1rem; }
.fonti { color: #5E6E66; font-size: .9rem; margin: .4rem 0 0; }
.fonti code { background: #E3EAE5; color: #1A2420; }
.dati { color: #5E6E66; font-size: .85rem; }
.scheda h3 { margin: .3rem 0 0; }
.scheda .codici { color: #5E6E66; margin: .1rem 0 .6rem; }
.guide h4 { font-family: 'Barlow Semi Condensed', sans-serif; font-size: 1.05rem; margin: .9rem 0 .3rem; color: #1E5B45; }
.guide ul { margin: 0 0 .4rem 1.1rem; padding: 0; }
.guide li { margin: .15rem 0; }
.guide ul.pagine { list-style: none; margin-left: 0; }
.guide ul.pagine li { display: grid; grid-template-columns: 7rem 1fr; gap: .5rem; margin: .35rem 0; }
.guide .tipo { font-size: .8rem; color: #5B6A63; padding-top: .2rem; }
.guide .percorso { font-size: .8rem; color: #5B6A63; }
.guide .vuoto { color: #5B6A63; }
.procedura .obiettivo { font-family: 'Barlow Semi Condensed', sans-serif; font-size: 1.35rem; font-weight: 600; margin: .2rem 0 .6rem; }
.procedura ol.passi { list-style: none; counter-reset: passo; margin: 0; padding: 0; }
.procedura ol.passi > li { counter-increment: passo; position: relative; padding: 0 0 .9rem 2.6rem; }
.procedura ol.passi > li::before { content: counter(passo); position: absolute; left: 0; top: 0; width: 1.8rem; height: 1.8rem;
  border-radius: 50%; background: #1E5B45; color: #FFFFFF; font-weight: 600; text-align: center; line-height: 1.8rem; }
.procedura ol.passi > li:not(:last-child)::after { content: ""; position: absolute; left: .87rem; top: 2rem; bottom: .2rem;
  border-left: 2px solid #C9D6CE; }
.procedura .titolo-passo { font-weight: 600; margin: .15rem 0 .2rem; }
.procedura .attrezzo { color: #B5652B; font-weight: 600; margin: .25rem 0 0; }
.procedura .controllo { color: #5B6A63; margin: .2rem 0 0; }
.procedura .controllo b, .procedura .attrezzo b { font-weight: 600; color: inherit; }
</style>
"""

_LIVELLI = {"alta": 3, "media": 2, "bassa": 1}


def _barra(probabilita: str) -> str:
    n = _LIVELLI.get(probabilita, 0)
    return f'<span class="prob" title="probabilità {escape(probabilita)}">' + "".join(
        f'<i class="{"on" if k < n else ""}"></i>' for k in range(3)) + "</span>"


def risposta_html(passo, esito) -> str:
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
    if hasattr(passo, "ipotesi"):
        parti.append(f'<p class="riepilogo">{escape(passo.riepilogo)}</p>')
        voci = "".join(f'<li><span class="comp">{escape(i.componente)}</span>{_barra(i.probabilita)}<br>{escape(i.motivo)}</li>'
                       for i in passo.ipotesi)
        parti.append(f'<ol class="ipotesi">{voci}</ol>')
    if passo.domande_al_tecnico:
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


def procedura_html(proc, esito) -> str:
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
    if proc.domande_al_tecnico:
        parti.append("<p><b>Mi serve sapere</b></p><ul class=\"domande\">"
                     + "".join(f"<li>{escape(q)}</li>" for q in proc.domande_al_tecnico) + "</ul>")
    fonti = ", ".join(f"<code>{escape(f)}</code>" for f in proc.fonti) or "nessuna pagina della wiki: da verificare"
    parti.append(f'<p class="fonti">Fonti: {fonti}</p>')
    return "".join(parti)
