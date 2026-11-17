"""Interfaccia di diagnosi — Streamlit (stile di Lezione4_15-5/EsempiStreamlit/app_chat.py).

A sinistra: la scheda del dispositivo riconosciuto (dalla wiki: icona, codici modello, componenti, casi)
e le pagine della wiki consultate. Al centro: la chat con l'agente diagnostico.

Avvio:  streamlit run app/streamlit_app.py
"""
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import streamlit as st

from diagnosi.agent import SessioneDiagnosi
from diagnosi.config import MODEL_DEMO, MODEL_DEV
from diagnosi.dispositivi import casi_del_dispositivo, schede, trova_dispositivo

st.set_page_config(page_title="Diagnosi schede", page_icon="🔧", layout="wide")

# Icone generiche disegnate in SVG (niente immagini Apple o di repair.wiki: licenze diverse dal testo).
ICONE = {
    "phone": '<svg width="56" height="96" viewBox="0 0 56 96"><rect x="3" y="3" width="50" height="90" rx="10" '
             'fill="none" stroke="currentColor" stroke-width="4"/><rect x="20" y="9" width="16" height="4" rx="2" fill="currentColor"/></svg>',
    "tablet": '<svg width="96" height="128" viewBox="0 0 96 128"><rect x="3" y="3" width="90" height="122" rx="10" '
              'fill="none" stroke="currentColor" stroke-width="4"/><circle cx="48" cy="12" r="3" fill="currentColor"/></svg>',
}

CARTELLA_IMMAGINI = Path(__file__).parent / "immagini"


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
                credito = f"Foto: {celle[1]} · {celle[2]} · {celle[3]}"
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
    st.session_state.messaggi = []          # (ruolo, contenuto, extra)
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
    st.header("🔧 Diagnosi schede")
    modello = st.selectbox("Modello", [MODEL_DEV, MODEL_DEMO])
    scelta = st.selectbox("Dispositivo", [AUTO, *elenco_dispositivi()],
                          help="Scegli il dispositivo al banco, oppure lascia che venga riconosciuto dal testo (es. A2316).")
    dettaglio = st.radio("Risposta", ["completa", "breve"], horizontal=True,
                         format_func={"completa": "Completa (ipotesi + misura)", "breve": "Solo prossima misura"}.get)
    lettura = st.radio("Consultazione wiki", ["approfondita", "rapida"], horizontal=True,
                       format_func={"approfondita": "Approfondita", "rapida": "Rapida (≤3 pagine, meno token)"}.get)
    # Cambiare modello, dispositivo o modalità = nuova diagnosi (le misure di un dispositivo non valgono per un altro).
    s_ = st.session_state.sessione
    if (st.button("Nuova diagnosi") or s_ is None or s_.model != modello or scelta != st.session_state.scelta
            or s_.dettaglio != dettaglio or s_.lettura != lettura):
        st.session_state.scelta = scelta
        nuova_sessione(modello, dettaglio, lettura)
    st.divider()

    d = st.session_state.dispositivo
    if d:
        foto, credito = immagine_e_credito(d["percorso"])
        if foto:
            st.image(str(foto), width="stretch")
            st.caption(credito or "Foto: credito mancante in app/immagini/CREDITI.md")
        else:
            st.markdown(ICONE.get(d.get("categoria"), ICONE["phone"]), unsafe_allow_html=True)
        st.subheader(d.get("titolo", "?"))
        if d.get("codici_modello"):
            st.caption("Codici: " + " · ".join(d["codici_modello"]))
        if d.get("componenti_chiave"):
            st.write("**Componenti chiave:** " + ", ".join(d["componenti_chiave"]))
        casi = casi_del_dispositivo(d.get("titolo", ""))
        st.write(f"**Casi in wiki:** {len(casi)}")
        for c in casi:
            st.caption(c)
        st.caption(f"wiki/{d['percorso']}")
    else:
        st.info("Scrivi modello o codice (es. A2316): qui comparirà la scheda del dispositivo.")

    lette = list(st.session_state.sessione.pagine_lette)
    if lette:
        st.divider()
        st.write(f"**Pagine della wiki consultate ({len(lette)})**")
        for p in lette:
            st.caption(p)

# ── chat
st.title("Diagnosi guidata a livello scheda")
st.caption("Descrivi dispositivo, sintomi e misure. L'agente consulta la wiki e propone una misura alla volta.")

for ruolo, contenuto, extra in st.session_state.messaggi:
    with st.chat_message(ruolo):
        st.markdown(contenuto)
        if extra:
            st.caption(extra)

if msg := st.chat_input("Es. iPad Air 4 A2316, non carica, PC non lo rileva, 0.002 A con batteria…"):
    st.session_state.messaggi.append(("user", msg, ""))
    if not st.session_state.dispositivo:
        st.session_state.dispositivo = trova_dispositivo(msg)
    with st.chat_message("user"):
        st.markdown(msg)
    with st.chat_message("assistant"):
        # Il dispositivo scelto dal menu si comunica all'agente nel primo messaggio, con i codici modello.
        d = st.session_state.dispositivo
        da_inviare = msg
        if st.session_state.scelta != AUTO and d and not st.session_state.dispositivo_comunicato:
            codici = f" (codici {', '.join(d['codici_modello'])})" if d.get("codici_modello") else ""
            da_inviare = f"Dispositivo al banco: {d['titolo']}{codici}. Pagina wiki: {d['percorso']}.\n\n{msg}"
            st.session_state.dispositivo_comunicato = True
        # Timer dal vivo: l'agente lavora in un thread, l'interfaccia aggiorna il contatore ogni 0,2 s.
        timer = st.empty()
        t0 = time.perf_counter()
        with ThreadPoolExecutor(max_workers=1) as pool:
            lavoro = pool.submit(st.session_state.sessione.chiedi, da_inviare)
            while not lavoro.done():
                timer.markdown(f"⏱️ **{time.perf_counter() - t0:.1f} s** — consulto la wiki…")
                time.sleep(0.2)
            passo, esito, info = lavoro.result()
        timer.markdown(f"⏱️ Risposta in **{time.perf_counter() - t0:.1f} s**")
        if esito.bloccato:
            testo = "**Risposta bloccata dai guardrail di sicurezza.**\n\n" + "\n".join(f"- {a}" for a in esito.avvisi)
            st.error(testo)
        else:
            if not st.session_state.dispositivo:
                st.session_state.dispositivo = trova_dispositivo(passo.dispositivo)
            m = passo.prossima_misura
            righe = []
            if hasattr(passo, "ipotesi"):                    # risposta completa
                righe += [f"**{passo.riepilogo}**", "", "**Ipotesi**"]
                righe += [f"{i}. `{ip.probabilita}` **{ip.componente}** — {ip.motivo}" for i, ip in enumerate(passo.ipotesi, 1)]
                righe += [""]
            righe += [f"**Prossima misura:** {m.dove} — *{m.modalita}*",
                      f"- condizioni: {m.condizioni}", f"- valore atteso: **{m.valore_atteso}**", f"- se diverso: {m.se_diverso}"]
            if passo.domande_al_tecnico:
                righe += ["", "**Domande**"] + [f"- {q}" for q in passo.domande_al_tecnico]
            righe += ["", "**Fonti:** " + (", ".join(f"`{f}`" for f in passo.fonti) or "nessuna — da verificare")]
            avvertenze = [f"> ⚠️ {a}" for a in passo.avvertenze_sicurezza]
            testo = "\n".join(avvertenze + ([""] if avvertenze else []) + righe)
            st.markdown(testo)
        extra = (f"⏱️ {info['durata_s']} s · token {info['token_in']}/{info['token_out']} "
                 f"(in cache {info.get('token_cache', 0)}) · {len(info['tool'])} tool · "
                 f"{info['modello']} · risposta {info['dettaglio']} · lettura {info['lettura']}")
        st.caption(extra)
    st.session_state.messaggi.append(("assistant", testo, extra))
    st.rerun()
