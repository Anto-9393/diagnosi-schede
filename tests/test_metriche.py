"""L'exporter calcola le metriche dal log (nessuna rete, nessun Docker)."""
import json

from diagnosi.metriche import CollectorDiagnosi


def test_metriche_dal_log(tmp_path):
    log = tmp_path / "sessioni.jsonl"
    righe = [
        {"durata_s": 15.1, "token_in": 43706, "token_out": 1147, "token_cache": 0, "tool": ["leggi_indice()", "leggi_pagina(a.md)"],
         "avvisi": [], "bloccato": False, "lettura": "approfondita", "dettaglio": "completa"},
        {"durata_s": 13.0, "token_in": 27661, "token_out": 1176, "token_cache": 9216, "tool": ["leggi_pagina(b.md)"],
         "avvisi": ["Iniezione di tensione con la batteria collegata: SCOLLEGA la batteria"], "bloccato": False, "lettura": "rapida"},
    ]
    log.write_text("\n".join(json.dumps(r) for r in righe) + "\nriga rotta\n", encoding="utf-8")
    m = {f.name: f for f in CollectorDiagnosi(log).collect()}
    valori = lambda nome: {tuple(s.labels.values()): s.value for s in m[nome].samples}
    assert sum(valori("diagnosi_richieste").values()) == 2
    assert valori("diagnosi_token")[("input",)] == 71367 and valori("diagnosi_token")[("input_in_cache",)] == 9216
    assert valori("diagnosi_tool_chiamate")[("leggi_pagina",)] == 2
    assert valori("diagnosi_guardrail_avvisi")[("iniezione_con_batteria",)] == 1
    lat = {s.labels.get("le"): s.value for s in m["diagnosi_latenza_secondi"].samples if s.name.endswith("_bucket")}
    assert lat["12"] == 0 and lat["15"] == 1 and lat["+Inf"] == 2
    assert m["diagnosi_costo_stimato_eur"].samples[0].value > 0
    assert m["diagnosi_ultima_token_input"].samples[0].value == 27661 and m["diagnosi_ultima_durata_secondi"].samples[0].value == 13.0
