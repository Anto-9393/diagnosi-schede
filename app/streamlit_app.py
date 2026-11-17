"""Interfaccia di diagnosi — Streamlit (stile di Lezione4_15-5/EsempiStreamlit/app_chat.py).

A sinistra: la scheda del dispositivo riconosciuto (dalla wiki: icona, codici modello, componenti, casi)
e le pagine della wiki consultate. Al centro: la chat con l'agente diagnostico.

Avvio:  streamlit run app/streamlit_app.py
"""
import streamlit as st

from diagnosi.agent import SessioneDiagnosi
from diagnosi.config import MODEL_DEMO, MODEL_DEV
from diagnosi.dispositivi import trova_dispositivo

st.set_page_config(page_title="Diagnosi schede", page_icon="🔧", layout="wide")

# Icone generiche disegnate in SVG (niente immagini Apple o di repair.wiki: licenze diverse dal testo).
ICONE = {
    "phone": '<svg width="56" height="96" viewBox="0 0 56 96"><rect x="3" y="3" width="50" height="90" rx="10" '
             'fill="none" stroke="currentColor" stroke-width="4"/><rect x="20" y="9" width="16" height="4" rx="2" fill="currentColor"/></svg>',
    "tablet": '<svg width="96" height="128" viewBox="0 0 96 128"><rect x="3" y="3" width="90" height="122" rx="10" '
              'fill="none" stroke="currentColor" stroke-width="4"/><circle cx="48" cy="12" r="3" fill="currentColor"/></svg>',
}

# ── stato della sessione (S04: senza session_state Streamlit dimentica tutto a ogni interazione)
if "sessione" not in st.session_state:
    st.session_state.sessione = None
    st.session_state.messaggi = []          # (ruolo, contenuto, extra)
    st.session_state.dispositivo = None

# ── riquadro laterale
with st.sidebar:
    st.header("🔧 Diagnosi schede")
    modello = st.selectbox("Modello", [MODEL_DEV, MODEL_DEMO])
    if st.button("Nuova diagnosi") or st.session_state.sessione is None or st.session_state.sessione.model != modello:
        st.session_state.sessione = SessioneDiagnosi(model=modello)
        st.session_state.messaggi, st.session_state.dispositivo = [], None
    st.divider()

    d = st.session_state.dispositivo
    if d:
        st.markdown(ICONE.get(d.get("categoria"), ICONE["phone"]), unsafe_allow_html=True)
        st.subheader(d.get("titolo", "?"))
        if d.get("codici_modello"):
            st.caption("Codici: " + " · ".join(d["codici_modello"]))
        if d.get("componenti_chiave"):
            st.write("**Componenti chiave:** " + ", ".join(d["componenti_chiave"]))
        st.write(f"**Casi in wiki:** {len(d.get('casi') or [])}")
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
        with st.spinner("Consulto la wiki…"):
            passo, esito, info = st.session_state.sessione.chiedi(msg)
        if esito.bloccato:
            testo = "**Risposta bloccata dai guardrail di sicurezza.**\n\n" + "\n".join(f"- {a}" for a in esito.avvisi)
            st.error(testo)
        else:
            if not st.session_state.dispositivo:
                st.session_state.dispositivo = trova_dispositivo(passo.dispositivo)
            m = passo.prossima_misura
            righe = [f"**{passo.riepilogo}**", "", "**Ipotesi**"]
            righe += [f"{i}. `{ip.probabilita}` **{ip.componente}** — {ip.motivo}" for i, ip in enumerate(passo.ipotesi, 1)]
            righe += ["", f"**Prossima misura:** {m.dove} — *{m.modalita}*",
                      f"- condizioni: {m.condizioni}", f"- valore atteso: **{m.valore_atteso}**", f"- se diverso: {m.se_diverso}"]
            if passo.domande_al_tecnico:
                righe += ["", "**Domande**"] + [f"- {q}" for q in passo.domande_al_tecnico]
            righe += ["", "**Fonti:** " + (", ".join(f"`{f}`" for f in passo.fonti) or "nessuna — da verificare")]
            avvertenze = [f"> ⚠️ {a}" for a in passo.avvertenze_sicurezza]
            testo = "\n".join(avvertenze + ([""] if avvertenze else []) + righe)
            st.markdown(testo)
        extra = f"{info['durata_s']} s · token {info['token_in']}/{info['token_out']} · {len(info['tool'])} tool · {info['modello']}"
        st.caption(extra)
    st.session_state.messaggi.append(("assistant", testo, extra))
    st.rerun()
