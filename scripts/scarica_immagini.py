"""Scarica le foto dei dispositivi da Wikipedia/Wikimedia Commons, SOLO con licenza libera, con i crediti.

Come funziona (API gratuite, senza chiave):
  1. Costruisce il titolo ESATTO della voce secondo le convenzioni di Wikipedia ("iPad Air 4" -> "iPad Air (4th generation)")
     e verifica che esista. Niente "primo risultato della ricerca": prendeva il modello sbagliato (iPad 2 -> iPad Air 2).
  2. Wikipedia "pageimages" con pilicense=free restituisce l'immagine principale SOLO se ha licenza libera
     (le immagini "fair use", come molte foto Apple, vengono escluse).
  3. Commons "imageinfo" con extmetadata dà autore e licenza -> riga in app/immagini/CREDITI.md.
Wikimedia chiede un User-Agent che identifichi lo script: lo impostiamo sotto.

Registrazione (consigliata, gratuita): senza account Wikimedia concede ~500 richieste l'ora e risponde 429;
con un TOKEN personale (OAuth 2.0) ~10.000 l'ora. Come averlo: crea un account Wikimedia, poi su
https://meta.wikimedia.org/wiki/Special:OAuthConsumerRegistration/propose/oauth2 proponi un consumer
"owner-only" (solo per te, approvato subito) e copia l'Access token nel .env:
    WIKIMEDIA_TOKEN=...            # chiamate REST con "Authorization: Bearer <token>"
    WIKIMEDIA_CONTATTO=...         # email o pagina utente: va nello User-Agent (lo chiede la policy Wikimedia)

Avvio:  python scripts/scarica_immagini.py --solo ipad-air-4     # un dispositivo
        python scripts/scarica_immagini.py                       # tutti quelli senza foto
        python scripts/scarica_immagini.py --prova               # mostra cosa farebbe, senza scaricare
"""
from __future__ import annotations

import argparse
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

import os

from diagnosi.config import ROOT
from diagnosi.dispositivi import schede

CARTELLA = ROOT / "app" / "immagini"
CREDITI = CARTELLA / "CREDITI.md"
UA = "diagnosi-schede/0.1 (progetto didattico AITHO; " + (os.getenv("WIKIMEDIA_CONTATTO") or "uso con attribuzione") + ")"


def intestazioni() -> dict:
    """User-Agent sempre; il token solo se c'è (mai nel codice: sta nel .env, come la chiave OpenAI)."""
    h = {"User-Agent": UA}
    if os.getenv("WIKIMEDIA_TOKEN"):
        h["Authorization"] = "Bearer " + os.environ["WIKIMEDIA_TOKEN"]
    return h
LICENZE_OK = re.compile(r"^(cc[- ]?by|cc[- ]?by[- ]?sa|cc0|public domain|pd)", re.I)


def _get(url: str, params: dict, tentativi: int = 4) -> dict:
    """GET con pausa e nuovi tentativi se Wikimedia risponde 429 (troppe richieste)."""
    req = urllib.request.Request(url + "?" + urllib.parse.urlencode(params), headers=intestazioni())
    for n in range(tentativi):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code != 429 or n == tentativi - 1:
                raise
            attesa = int(e.headers.get("Retry-After") or 0) or 5 * (n + 1)
            print(f"    429: Wikimedia chiede di rallentare, attendo {attesa} s…")
            time.sleep(attesa)
    raise RuntimeError("irraggiungibile")


def _ordinale(n: int) -> str:
    return f"{n}{'th' if 10 <= n % 100 <= 20 else {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')}"


# Nomi che Wikipedia dà diversamente (verificati con --prova il 18 nov).
_SPECIALI = {"iPad Air 6": ["iPad Air (6th generation)", "iPad Air (M2)"],
             "iPad Mini 7": ["iPad Mini (7th generation)", "iPad Mini (A17 Pro)"],
             "iPhone 17 Air": ["iPhone Air"],
             "iPad Pro 9.7": ["iPad Pro (1st generation)"], "iPad Pro 10.5": ["iPad Pro (2nd generation)"]}
# Scelte a mano: la foto giusta esiste ma Wikipedia la mette in un'altra voce (l'Air 4 ha solo il logo).
SCELTE = {"ipad-air-4": "IPad_Air_4.png"}


def titoli_candidati(titolo: str) -> list[str]:
    """Titoli possibili della voce di Wikipedia, dal più probabile. Es. 'iPad Air 4' -> 'iPad Air (4th generation)'."""
    t = titolo.strip()
    if t in _SPECIALI:
        return _SPECIALI[t]
    m = re.fullmatch(r"iPad( Air| Mini| mini)? (\d+)", t, flags=re.I)
    if m:
        famiglia = "iPad" + (m.group(1) or "").title()
        return [f"{famiglia} ({_ordinale(int(m.group(2)))} generation)", t]
    m = re.fullmatch(r"iPad Pro 12\.9 (\d)\w* Gen", t, flags=re.I)          # 12.9" n-esima = iPad Pro n-esima gen.
    if m:
        return [f"iPad Pro ({_ordinale(int(m.group(1)))} generation)"]
    m = re.fullmatch(r"iPad Pro 11in (\d)\w* Gen", t, flags=re.I)            # 11" n-esima = iPad Pro (n+2)-esima gen.
    if m:
        return [f"iPad Pro ({_ordinale(int(m.group(1)) + 2)} generation)"]
    m = re.fullmatch(r"iPhone SE (2016|2020|2022)", t, flags=re.I)
    if m:
        return [f"iPhone SE ({ {'2016': '1st', '2020': '2nd', '2022': '3rd'}[m.group(1)]} generation)"]
    # Plus / Pro Max / mini / XS Max: Wikipedia li tratta nella voce del modello base (stesso design).
    base = re.sub(r"\s+(Plus|Max|Mini)$", "", t, flags=re.I)
    return [t] if base == t else [t, base]


def coerente(titolo: str, voce: str) -> bool:
    """La voce trovata è dello STESSO modello? Stessi numeri e stessa famiglia (Air/Mini/Pro/Max/Plus), niente liste."""
    if voce.lower().startswith("list of"):
        return False
    num_t = re.findall(r"\d+", titolo.split(".")[0])
    for famiglia in ("air", "mini", "pro", "max", "plus"):
        if (famiglia in titolo.lower()) != (famiglia in voce.lower()):
            return False
    return all(n in re.findall(r"\d+", voce) for n in num_t[:1])


def voce_wikipedia(titolo: str) -> str | None:
    for candidato in titoli_candidati(titolo):
        d = _get("https://en.wikipedia.org/w/api.php",
                 {"action": "query", "titles": candidato, "redirects": 1, "format": "json"})
        for pagina in d.get("query", {}).get("pages", {}).values():
            if "missing" not in pagina and coerente(candidato, pagina["title"]):   # i candidati sono costruiti apposta
                return pagina["title"]
    return None


def foto_adatta(titolo: str, voce: str, file_: str) -> tuple[bool, str]:
    """(si può usare, nota). Scarta i loghi e le foto di altri modelli; segnala le foto di un modello simile."""
    f = file_.lower()
    if "logo" in f:
        return False, "solo il logo, non una foto"
    num_titolo = re.findall(r"\d+", titolo.split(".")[0])
    num_file = re.findall(r"(?:ipad|air|mini|iphone|pro)[ _-]*(\d{1,2})(?!\d)(?![.,]\d)", f)   # "10.2-inch" = pollici
    if re.search(r"ipad pro", titolo, re.I):            # "11in", "12.9": sono pollici, non generazioni
        num_titolo = []
    if not num_titolo and not re.search(r"ipad pro", titolo, re.I) and re.search(r"\d", f):   # "iPad Air" (2013) e foto "IPad_Air_2020"
        return False, "foto di un modello più recente"
    if num_titolo and num_file and num_file[0] != num_titolo[0]:
        return True, "foto di un modello simile"
    if voce.lower() != titoli_candidati(titolo)[0].lower() and voce.lower() != titolo.lower():
        return True, "foto del modello base (stesso design)"
    return True, ""


def immagine_libera(voce: str) -> str | None:
    """Nome del file (su Commons) dell'immagine principale della voce, solo se con licenza libera."""
    d = _get("https://en.wikipedia.org/w/api.php",
             {"action": "query", "prop": "pageimages", "piprop": "name", "pilicense": "free",
              "titles": voce, "redirects": 1, "format": "json"})
    pagine = d.get("query", {}).get("pages", {})
    return next((p.get("pageimage") for p in pagine.values() if p.get("pageimage")), None)


def info_commons(nome_file: str) -> dict | None:
    d = _get("https://commons.wikimedia.org/w/api.php",
             {"action": "query", "titles": f"File:{nome_file}", "prop": "imageinfo",
              "iiprop": "url|extmetadata", "iiurlwidth": 600, "format": "json"})
    for p in d.get("query", {}).get("pages", {}).values():
        if p.get("imageinfo"):
            return p["imageinfo"][0]
    return None


def credito(info: dict, nome_file: str) -> tuple[str, str, str] | None:
    """(fonte, autore, licenza) se la licenza è libera, altrimenti None."""
    meta = info.get("extmetadata", {})
    licenza = re.sub(r"<[^>]+>", "", meta.get("LicenseShortName", {}).get("value", "")).strip()
    if not LICENZE_OK.match(licenza):
        return None
    autore = re.sub(r"<[^>]+>", "", meta.get("Artist", {}).get("value", "sconosciuto")).strip()[:80]
    fonte = info.get("descriptionurl") or f"https://commons.wikimedia.org/wiki/File:{urllib.parse.quote(nome_file)}"
    return fonte, autore, licenza


def main():
    import sys
    sys.stdout.reconfigure(encoding="utf-8")       # Windows: con "> file.txt" userebbe cp1252 e si ferma su "‑", "é"...
    ap = argparse.ArgumentParser()
    ap.add_argument("--solo", help="nome della pagina dispositivo, es. ipad-air-4")
    ap.add_argument("--prova", action="store_true", help="non scarica, mostra solo cosa troverebbe")
    ap.add_argument("--anche-simili", action="store_true",
                    help="scarica anche le foto di un modello simile o del modello base (segnate con ~)")
    args = ap.parse_args()
    CARTELLA.mkdir(parents=True, exist_ok=True)
    print("Token Wikimedia:", "sì (fino a ~5.000 richieste/ora)" if os.getenv("WIKIMEDIA_TOKEN")
          else "NO, accesso anonimo (~500 richieste/ora): aggiungi WIKIMEDIA_TOKEN nel .env")

    for s in schede():
        nome = Path(s["percorso"]).stem
        if args.solo and nome != args.solo:
            continue
        if any((CARTELLA / f"{nome}{e}").exists() for e in (".jpg", ".jpeg", ".png", ".webp")):
            print(f"= {nome}: foto già presente, salto")
            continue
        time.sleep(1.5)                                          # gentilezza verso Wikimedia (evita il 429)
        try:
            voce = voce_wikipedia(s["titolo"])
            file_ = SCELTE.get(nome) or (immagine_libera(voce) if voce else None)
            info = info_commons(file_) if file_ else None
            cred = credito(info, file_) if info else None
        except Exception as e:                                   # noqa: BLE001
            print(f"! {nome}: errore di rete ({type(e).__name__}: {e})")
            continue
        if not cred:
            motivo = "voce non trovata" if not voce else f"voce '{voce}' senza immagine libera"
            print(f"- {nome}: {motivo}")
            continue
        fonte, autore, licenza = cred
        ok, nota = foto_adatta(s["titolo"], voce or "", file_)
        if not ok:
            print(f"x {nome}: {file_} scartata ({nota})")
            continue
        url = info.get("thumburl") or info["url"]          # per gli SVG Commons dà un PNG già pronto
        ext = Path(urllib.parse.urlparse(url).path).suffix.lower() or ".jpg"
        segno = "~" if nota else "+"
        print(f"{segno} {nome}: {voce} -> {file_} [{licenza}, {autore}]" + (f"  ({nota})" if nota else ""))
        if args.prova or (nota and not args.anche_simili):
            continue
        req = urllib.request.Request(url, headers=intestazioni())
        with urllib.request.urlopen(req, timeout=60) as r:
            (CARTELLA / f"{nome}{ext}").write_bytes(r.read())
        with CREDITI.open("a", encoding="utf-8") as f:
            f.write(f"| {nome}{ext} | {fonte} | {autore.replace('|', '/')} | {licenza} |\n")


if __name__ == "__main__":
    main()
