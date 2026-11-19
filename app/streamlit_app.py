"""Interfaccia di diagnosi — Streamlit (stile di Lezione4_15-5/EsempiStreamlit/app_chat.py).

A sinistra: la scheda del dispositivo riconosciuto (dalla wiki: icona, codici modello, componenti, casi)
e le pagine della wiki consultate. Al centro: la chat con l'agente diagnostico.

Avvio:  streamlit run app/streamlit_app.py
"""
import re
from html import escape
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

from aspetto import CSS, dati_html, loader_html, procedura_html, risposta_html
from diagnosi.agent import SessioneDiagnosi
from diagnosi.config import MODEL_DEMO, MODEL_DEV
from diagnosi.traduzioni import traduci, tradotta
from diagnosi.dispositivi import (casi_del_dispositivo, guide_del_dispositivo, leggi_guida, schede, solo_dispositivo,
                                  trova_dispositivo)

st.set_page_config(page_title="Diagnosi al banco", page_icon="🔧", layout="wide")
st.markdown(CSS, unsafe_allow_html=True)

# Icone generiche disegnate in SVG (niente immagini Apple o di repair.wiki: licenze diverse dal testo).
ICONE = {
    "phone": '<svg width="56" height="96" viewBox="0 0 56 96"><rect x="3" y="3" width="50" height="90" rx="10" '
             'fill="none" stroke="currentColor" stroke-width="4"/><rect x="20" y="9" width="16" height="4" rx="2" fill="currentColor"/></svg>',
    "tablet": '<svg width="96" height="128" viewBox="0 0 96 128"><rect x="3" y="3" width="90" height="122" rx="10" '
              'fill="none" stroke="currentColor" stroke-width="4"/><circle cx="48" cy="12" r="3" fill="currentColor"/></svg>',
}

CARTELLA_IMMAGINI = Path(__file__).parent / "immagini"
# Avatar della chat, disegnati per il progetto: l'agente è un tecnico in camice con gli occhiali-lente,
# il riparatore al banco è il suo multimetro (porta le misure).
AVATAR = {"assistant": str(CARTELLA_IMMAGINI / "avatar_tecnico.png"),
          "user": str(CARTELLA_IMMAGINI / "avatar_multimetro.png")}


def immagine_e_credito(percorso_wiki: str) -> tuple[Path | None, str]:
    """Foto del dispositivo (se presente in app/immagini/) e la sua riga di credito da CREDITI.md."""
    nome = Path(percorso_wiki).stem
    foto = next((f for ext in (".jpg", ".jpeg", ".png", ".webp") if (f := CARTELLA_IMMAGINI / f"{nome}{ext}").exists()), None)
    credito = ""
    crediti = CARTELLA_IMMAGINI / "CREDITI.md"
    if foto and crediti.exists():
        for riga in crediti.read_text(encoding="utf-8").splitlines():
            celle = [c.strip() for c in riga.strip("|").split("|")]
            if celle and celle[0] == foto.name and len(celle) >= 4:
                fonte = celle[1]
                if fonte.startswith("http"):  # link corto: mostra solo il sito
                    sito = "Wikimedia Commons" if "wikimedia" in fonte else fonte.split("/")[2]
                    fonte = f"[{sito}]({fonte})"
                credito = f"Immagine: {fonte}, {celle[2]}, licenza {celle[3]}"
    return foto, credito


AUTO = "Riconosci dal testo"


@st.cache_data
def elenco_dispositivi() -> dict[str, dict]:
    """Titolo -> scheda, iPad prima e iPhone dopo, in ordine alfabetico. In cache: la wiki non cambia durante l'uso."""
    tutte = {s["titolo"]: s for s in schede() if s.get("titolo")}
    return dict(sorted(tutte.items(), key=lambda kv: (not kv[0].lower().startswith("ipad"), kv[0].lower())))


# ── stato della sessione (S04: senza session_state Streamlit dimentica tutto a ogni interazione)
if "sessione" not in st.session_state:
    st.session_state.sessione = None
    st.session_state.messaggi = []          # (ruolo, contenuto, extra[, guide])
    st.session_state.dispositivo = None
    st.session_state.scelta = AUTO
    st.session_state.dispositivo_comunicato = False


def nuova_sessione(modello: str, dettaglio: str, lettura: str):
    st.session_state.sessione = SessioneDiagnosi(model=modello, dettaglio=dettaglio, lettura=lettura)
    st.session_state.messaggi = []
    st.session_state.dispositivo_comunicato = False
    scelta = st.session_state.scelta
    st.session_state.dispositivo = None if scelta == AUTO else elenco_dispositivi()[scelta]

# ── riquadro laterale
with st.sidebar:
    st.header("Diagnosi al banco")
    modello = st.selectbox("Modello", [MODEL_DEV, MODEL_DEMO])
    scelta = st.selectbox("Dispositivo", [AUTO, *elenco_dispositivi()],
                          help="Scegli il dispositivo al banco, oppure lascia che venga riconosciuto dal testo (es. A2316).")
    dettaglio = st.radio("Risposta", ["completa", "breve"], horizontal=True,
                         format_func={"completa": "Completa (ipotesi + misura)", "breve": "Solo prossima misura"}.get)
    lettura = st.radio("Consultazione wiki", ["approfondita", "rapida"], horizontal=True,
                       format_func={"approfondita": "Approfondita", "rapida": "Rapida"}.get)
    # Cambiare modello, dispositivo o modalità = nuova diagnosi (le misure di un dispositivo non valgono per un altro).
    s_ = st.session_state.sessione
    if (st.button("Nuova diagnosi") or s_ is None or s_.model != modello or scelta != st.session_state.scelta
            or s_.dettaglio != dettaglio or s_.lettura != lettura):
        st.session_state.scelta = scelta
        try:
            nuova_sessione(modello, dettaglio, lettura)
        except RuntimeError as e:              # chiave mancante o PROVIDER sbagliato: messaggio chiaro, non un traceback
            st.error(f"{e}\n\nPoi ferma Streamlit (Ctrl+C) e rilancialo: il .env si legge solo all'avvio.")
            st.stop()
    st.divider()

    d = st.session_state.dispositivo
    if d:
        foto, credito = immagine_e_credito(d["percorso"])
        if foto:
            st.image(str(foto), width=150)          # larghezza fissa: gli iPhone sono alti e stretti
            st.caption(credito or "Foto: credito mancante in app/immagini/CREDITI.md")
        else:
            st.markdown(ICONE.get(d.get("categoria"), ICONE["phone"]), unsafe_allow_html=True)
        st.subheader(d.get("titolo", "?"))
        if d.get("codici_modello"):
            st.caption("Codici modello: " + ", ".join(d["codici_modello"]))
        if d.get("componenti_chiave"):
            st.write("**Componenti chiave:** " + ", ".join(d["componenti_chiave"]))
        casi = casi_del_dispositivo(d.get("titolo", ""))
        st.write(f"**Casi in wiki:** {len(casi)}")
        for c in casi:
            st.caption(c)
        st.caption(f"wiki/{d['percorso']}")
    else:
        st.info("Scegli il dispositivo qui sopra, oppure scrivi modello o codice nel messaggio (es. A2316).")

    lette = list(st.session_state.sessione.pagine_lette)
    if lette:
        st.divider()
        st.write(f"**Pagine lette in questa diagnosi: {len(lette)}**")
        for p in lette:
            st.caption(p)

# ── chat
st.markdown('<p class="serigrafia">DIAGNOSI-AL-BANCO REV 1.0</p>', unsafe_allow_html=True)
st.title("Diagnosi al banco")
st.markdown("Scrivi sintomi e misure già fatte: ricevi una misura alla volta, con il valore atteso e le pagine della wiki "
            "da cui viene. Chiedi \"come sostituisco…\" o \"come programmo…\" per avere la procedura passo per passo.")

@st.cache_data(show_spinner=False)
def guide_per(percorso: str) -> dict:
    """Guide di un dispositivo, in cache: la prima volta legge ~450 file, poi è immediato (la wiki non cambia in sessione)."""
    return guide_del_dispositivo(next(s for s in schede() if s["percorso"] == percorso))


@st.cache_data(show_spinner=False)
def testo_guida(percorso: str) -> str:
    return leggi_guida(percorso)


TIPI_GUIDA = {"caso": "Caso reale", "sintomo": "Sintomo", "tecnica": "Tecnica", "componente": "Componente",
              "strumento": "Strumento"}


def mostra_guide(guide: dict, n: int):
    """Elenco delle guide del modello: ogni titolo si apre QUI, dalla wiki interna (nessun link a repair.wiki)."""
    if guide["wiki"]:
        st.markdown(f"**Nella nostra wiki ({len(guide['wiki'])})**")
        for p in guide["wiki"]:
            with st.expander(f"{TIPI_GUIDA.get(p['tipo'], p['tipo'])}: {p['titolo']}"):
                st.markdown(testo_guida(p["percorso"]))
                st.caption(f"wiki/{p['percorso']}")
    if guide["repairwiki"]:
        st.markdown(f"**Guide di repair.wiki, copia locale ({len(guide['repairwiki'])})**")
        for g in guide["repairwiki"]:
            it = tradotta(g["percorso"])                     # già tradotta una volta? allora dal file, 0 token
            with st.expander(g["titolo"] + ("" if it else " (in inglese)")):
                if it:
                    st.markdown(it)
                    st.caption(f"Traduzione salvata in raw/repairwiki/tradotte/, originale {g['percorso']}")
                    continue
                if st.button("Traduci in italiano", key=f"traduci-{n}-{g['percorso']}"):
                    attesa = st.empty()
                    attesa.markdown(loader_html("Traduco la guida, solo questa volta…"), unsafe_allow_html=True)
                    try:
                        _, tin, tout = traduci(g["percorso"])
                        attesa.empty()
                        st.rerun()
                    except Exception as e:                   # noqa: BLE001 — rete o chiave: lo dico, non crasho
                        attesa.empty()
                        st.error(f"Traduzione non riuscita: {e}")
                st.markdown(testo_guida(g["percorso"]))
                st.caption(f"{g['percorso']} (testo CC BY-SA 3.0)")
    if not guide["wiki"] and not guide["repairwiki"]:
        st.info("Nessuna guida specifica per questo modello: descrivi il guasto e l'agente userà le pagine generali.")


def scorri(dove: str = "start"):
    """Porta la pagina sull'ultimo messaggio: "end" mentre si aspetta (si vede il loader), "start" quando arriva la
    risposta (si legge dall'alto). Streamlit non lo fa da solo: un piccolo script nella pagina madre."""
    st.session_state.n_scorri = st.session_state.get("n_scorri", 0) + 1
    components.html(f"""<script>
      const vai = () => {{
        const m = window.parent.document.querySelectorAll('[data-testid="stChatMessage"]');
        if (m.length) m[m.length - 1].scrollIntoView({{behavior: "smooth", block: "{dove}"}});
      }};
      setTimeout(vai, 150);
      setTimeout(vai, 700);     // di nuovo dopo che Streamlit ha finito di disegnare (e di scorrere da solo)
    </script><!-- {st.session_state.n_scorri} -->""", height=0)


for n, (ruolo, contenuto, extra, *altro) in enumerate(st.session_state.messaggi):
    with st.chat_message(ruolo, avatar=AVATAR[ruolo]):
        if ruolo == "assistant":
            st.markdown(contenuto, unsafe_allow_html=True)     # HTML costruito da aspetto.py, testo già escapato
        else:
            st.markdown(contenuto)
        if altro:
            mostra_guide(altro[0], n)
        if extra:
            st.markdown(extra, unsafe_allow_html=True)

if st.session_state.get("scorri"):            # è appena arrivata una risposta: mostrala dall'inizio
    st.session_state.scorri = False
    scorri("start")

if msg := st.chat_input("Es.: non carica, 0,002 A con batteria e cavo, oppure: come sostituisco il CD3217?"):
    # Solo il modello (es. "iPad Air 4", "A2316"): elenco delle guide, senza chiamare l'LLM (zero token).
    # Ma solo all'INIZIO della diagnosi o se si chiedono le guide: a metà conversazione "A2316" è la risposta
    # a una domanda dell'agente ("che modello è?") e deve arrivare all'agente.
    inizio = not st.session_state.messaggi
    chiede_guide = bool(re.search(r"\b(guid[ae]|guides|elenc[oa]|lista)\b", msg, re.I))
    st.session_state.messaggi.append(("user", msg, ""))
    nominato = trova_dispositivo(msg) or st.session_state.dispositivo
    if nominato and solo_dispositivo(msg, nominato) and (inizio or chiede_guide):
        if st.session_state.scelta == AUTO:
            st.session_state.dispositivo = nominato
        with st.chat_message("user", avatar=AVATAR["user"]):
            st.markdown(msg)
        with st.chat_message("assistant", avatar=AVATAR["assistant"]):
            attesa = st.empty()
            attesa.markdown(loader_html(f"Cerco le guide di <b>{escape(nominato.get('titolo', ''))}</b>…"),
                            unsafe_allow_html=True)
            scorri("end")
            guide = guide_per(nominato["percorso"])
            attesa.empty()
        titolo = escape(nominato.get("titolo", "?"))
        testo = (f"<p>Ecco cosa c'è per <b>{titolo}</b>: apri una guida per leggerla qui. "
                 "Oppure scrivi il sintomo e le misure già fatte per iniziare la diagnosi.</p>")
        extra = '<span class="dati">Risposta immediata dalla wiki: 0 token, nessuna chiamata al modello.</span>'
        st.session_state.messaggi.append(("assistant", testo, extra, guide))
        st.session_state.scorri = True
        st.rerun()
    if not st.session_state.dispositivo:
        st.session_state.dispositivo = trova_dispositivo(msg)
    with st.chat_message("user", avatar=AVATAR["user"]):
        st.markdown(msg)
    with st.chat_message("assistant", avatar=AVATAR["assistant"]):
        # Il dispositivo scelto dal menu si comunica all'agente nel primo messaggio, con i codici modello.
        d = st.session_state.dispositivo
        da_inviare = msg
        # (Vale anche per il dispositivo riconosciuto dal testo, es. dopo l'elenco delle guide che l'agente non ha visto.)
        if d and not st.session_state.dispositivo_comunicato:
            codici = f" (codici {', '.join(d['codici_modello'])})" if d.get("codici_modello") else ""
            da_inviare = f"Dispositivo al banco: {d['titolo']}{codici}. Pagina wiki: {d['percorso']}.\n\n{msg}"
            st.session_state.dispositivo_comunicato = True
        # Timer dal vivo: l'agente lavora in un thread, l'interfaccia aggiorna il contatore ogni 0,2 s.
        # La scena si disegna UNA volta (ridisegnarla 5 volte al secondo faceva ripartire l'animazione);
        # si aggiorna solo il numero dei secondi.
        scena, timer = st.empty(), st.empty()
        scena.markdown(loader_html("Consulto la wiki…"), unsafe_allow_html=True)
        scorri("end")
        t0 = time.perf_counter()
        with ThreadPoolExecutor(max_workers=1) as pool:
            lavoro = pool.submit(st.session_state.sessione.chiedi, da_inviare)
            while not lavoro.done():
                timer.caption(f"{time.perf_counter() - t0:.1f} s")
                time.sleep(0.2)
            passo, esito, info = lavoro.result()
        scena.empty()
        timer.empty()
        if not esito.bloccato and not st.session_state.dispositivo:
            st.session_state.dispositivo = trova_dispositivo(passo.dispositivo)
        testo = (procedura_html if hasattr(passo, "passi") else risposta_html)(passo, esito)
        st.markdown(testo, unsafe_allow_html=True)
        extra = dati_html(info)
        st.markdown(extra, unsafe_allow_html=True)
    st.session_state.messaggi.append(("assistant", testo, extra))
    st.session_state.scorri = True
    st.rerun()
