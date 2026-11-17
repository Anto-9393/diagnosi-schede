"""Exporter Prometheus delle diagnosi — la parte "metriche" della ricetta S11 §7 (passi 8–10).

Invece di contare solo mentre un processo è vivo, l'exporter LEGGE docs/log/sessioni.jsonl a ogni lettura di
Prometheus: Grafana mostra tutte le diagnosi (anche quelle fatte da terminale, Streamlit o Claude Desktop via MCP)
e le nuove compaiono entro uno scrape. Il log resta l'unica fonte di verità.

Regole S11 rispettate: Histogram per la latenza con bucket scelti sui NOSTRI tempi (10–17 s misurati),
Counter per ciò che si accumula, label a bassa cardinalità (mai il testo della domanda o l'id sessione).

Avvio:  python -m diagnosi.metriche          -> http://localhost:8001/metrics (8000 è del server MCP in HTTP)
"""
from __future__ import annotations

import json
import os
import time
from collections import Counter as Conta
from pathlib import Path

from prometheus_client import REGISTRY, start_http_server
from prometheus_client.core import CounterMetricFamily, GaugeMetricFamily, HistogramMetricFamily

from diagnosi.config import ROOT

LOG_FILE = ROOT / "docs" / "log" / "sessioni.jsonl"
BUCKET_LATENZA = (2, 5, 8, 10, 12, 15, 20, 30, 45, 60)     # secondi: le diagnosi reali stanno tra 10 e 17 s
BUCKET_TOKEN = (5_000, 10_000, 20_000, 30_000, 40_000, 50_000, 75_000, 100_000)
# Prezzi in USD per 1M di token, per la STIMA del costo. Default: listino gpt-4o-mini usato nel corso (S11).
# Per il tuo modello metti i prezzi veri nel .env: PREZZO_INPUT_USD_1M, PREZZO_CACHE_USD_1M, PREZZO_OUTPUT_USD_1M.
PREZZO_IN = float(os.getenv("PREZZO_INPUT_USD_1M", "0.15"))
PREZZO_CACHE = float(os.getenv("PREZZO_CACHE_USD_1M", str(PREZZO_IN)))
PREZZO_OUT = float(os.getenv("PREZZO_OUTPUT_USD_1M", "0.60"))

_TIPI_AVVISO = [("BLOCCATO", "bloccante"), ("LIMITE DI CORRENTE", "limite_corrente"), ("SCOLLEGA", "iniezione_con_batteria"),
                ("cella Li-ion", "tensione_batteria"), ("fuori dal plausibile", "valore_impossibile"),
                ("Sigle non presenti", "sigle_non_verificate"), ("Nessuna fonte", "senza_fonti"),
                ("Fonti dichiarate", "fonti_non_lette")]


def leggi_log(file: Path = LOG_FILE) -> list[dict]:
    if not file.exists():
        return []
    righe = []
    for r in file.read_text(encoding="utf-8").splitlines():
        try:
            righe.append(json.loads(r))
        except json.JSONDecodeError:
            continue                                   # una riga rotta non deve fermare le metriche
    return righe


def _istogramma(nome, aiuto, valori, bucket):
    h = HistogramMetricFamily(nome, aiuto)
    cumulati = [(str(b), sum(v <= b for v in valori)) for b in bucket] + [("+Inf", len(valori))]
    h.add_metric([], cumulati, sum_value=float(sum(valori)))
    return h


class CollectorDiagnosi:
    def __init__(self, file: Path = LOG_FILE):
        self.file = file

    def collect(self):
        righe = leggi_log(self.file)
        richieste = CounterMetricFamily("diagnosi_richieste", "Risposte dell'agente", labels=["esito", "lettura", "dettaglio"])
        for (esito, lettura, dettaglio), n in Conta(("bloccata" if r.get("bloccato") else "ok",
                                                     r.get("lettura", "approfondita"), r.get("dettaglio", "completa"))
                                                    for r in righe).items():
            richieste.add_metric([esito, lettura, dettaglio], n)
        yield richieste

        token = CounterMetricFamily("diagnosi_token", "Token consumati", labels=["tipo"])
        tin = sum(r.get("token_in", 0) for r in righe)
        tcache = sum(r.get("token_cache", 0) for r in righe)
        tout = sum(r.get("token_out", 0) for r in righe)
        for tipo, v in (("input", tin), ("input_in_cache", tcache), ("output", tout)):
            token.add_metric([tipo], v)
        yield token

        costo = CounterMetricFamily("diagnosi_costo_stimato_usd", "Costo stimato (prezzi da .env o listino del corso)")
        costo.add_metric([], ((tin - tcache) * PREZZO_IN + tcache * PREZZO_CACHE + tout * PREZZO_OUT) / 1_000_000)
        yield costo

        tool = CounterMetricFamily("diagnosi_tool_chiamate", "Chiamate per tool", labels=["tool"])
        for nome, n in Conta(t.split("(", 1)[0] for r in righe for t in r.get("tool", [])).items():
            tool.add_metric([nome], n)
        yield tool

        avvisi = CounterMetricFamily("diagnosi_guardrail_avvisi", "Avvisi dei guardrail", labels=["tipo"])
        conta = Conta(tipo for r in righe for a in r.get("avvisi", []) for chiave, tipo in _TIPI_AVVISO if chiave in a)
        for _, tipo in _TIPI_AVVISO:
            avvisi.add_metric([tipo], conta.get(tipo, 0))
        yield avvisi

        yield _istogramma("diagnosi_latenza_secondi", "Tempo per risposta", [r.get("durata_s", 0) for r in righe], BUCKET_LATENZA)
        yield _istogramma("diagnosi_token_input_per_risposta", "Token in ingresso per risposta",
                          [r.get("token_in", 0) for r in righe], BUCKET_TOKEN)

        ultima = GaugeMetricFamily("diagnosi_ultima_risposta_timestamp", "Ora dell'ultima risposta (unix)")
        ultima.add_metric([], self.file.stat().st_mtime if self.file.exists() else 0)
        yield ultima


def avvia(porta: int = 8001):
    REGISTRY.register(CollectorDiagnosi())
    start_http_server(porta)
    print(f"Metriche su http://localhost:{porta}/metrics (legge {LOG_FILE.relative_to(ROOT)}). Ctrl+C per fermare.")
    while True:
        time.sleep(3600)


if __name__ == "__main__":
    avvia(int(os.getenv("PORTA_METRICHE", "8001")))
