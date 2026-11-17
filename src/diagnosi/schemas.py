"""Lo schema della risposta: cosa DEVE contenere ogni passo di diagnosi.

È lo stesso meccanismo del Lab 02 (Ticket + structured_response): invece di testo libero,
il modello compila un oggetto Pydantic validato. Così il resto del programma (UI, guardrail,
valutazione) legge campi precisi invece di interpretare prosa.
"""
from typing import Literal

from pydantic import BaseModel, Field


class Ipotesi(BaseModel):
    componente: str = Field(description="Sigla o nome del componente sospettato, es. 'CD3217 (U3100)'")
    motivo: str = Field(description="Perché è sospettato, in base a sintomi e misure già fatte")
    probabilita: Literal["alta", "media", "bassa"]


class Misura(BaseModel):
    dove: str = Field(description="Punto di misura: net, pin, condensatore, connettore")
    modalita: Literal["diode mode", "tensione", "corrente", "resistenza", "termocamera", "visiva", "altro"]
    condizioni: str = Field(description="Es. 'con batteria collegata, cavo USB inserito, iPad spento'")
    valore_atteso: str = Field(description="Valore su scheda sana, con unità di misura")
    se_diverso: str = Field(description="Cosa significa se il valore misurato è diverso")


class PassoDiagnosi(BaseModel):
    dispositivo: str = Field(description="nome commerciale più codice modello, per esempio 'iPad Air 4 (A2316)', oppure “sconosciuto” se l’utente non l’ha detto.")
    riepilogo: str = Field(description="Cosa sappiamo finora, in una o due frasi")
    ipotesi: list[Ipotesi] = Field(description="Ipotesi ordinate dalla più probabile")
    prossima_misura: Misura
    avvertenze_sicurezza: list[str] = Field(
        default_factory=list,
        description="Rischi per il tecnico o la scheda (batteria Li-ion, limite di corrente, ESD...)",
    )
    fonti: list[str] = Field(
        default_factory=list,
        description="Pagine della wiki usate. Vuoto se la risposta non si basa su fonti.",
    )
    domande_al_tecnico: list[str] = Field(
        default_factory=list,
        description="Informazioni mancanti da chiedere prima di procedere",
    )


class PassoBreve(BaseModel):
    """Risposta ridotta ("solo la prossima misura"): scelta dal riparatore per risparmiare token in uscita."""
    dispositivo: str = Field(description="nome commerciale più codice modello, oppure 'sconosciuto'")
    prossima_misura: Misura
    avvertenze_sicurezza: list[str] = Field(default_factory=list, description="Rischi per il tecnico o la scheda")
    fonti: list[str] = Field(default_factory=list, description="Pagine della wiki usate")
    domande_al_tecnico: list[str] = Field(default_factory=list, description="Informazioni mancanti, al massimo 2")


# ── Modalità PROCEDURA: il tecnico chiede "come si fa" (sostituire un chip, programmare una ROM...), non una diagnosi.
# Uno schema diverso perché la forma dell'output decide cosa il modello può dire: con PassoDiagnosi una procedura
# finiva schiacciata in "ipotesi + una misura" (risposta reale del 17 nov, inutile per il tecnico).
class PassoProcedura(BaseModel):
    titolo: str = Field(description="Cosa si fa in questo passo, poche parole (es. 'Rimuovi il CD3217')")
    azione: str = Field(description="Istruzioni concrete, nell'ordine, come le spiegheresti a un collega al banco")
    attrezzo: str = Field(default="", description="Attrezzo e impostazioni (es. 'aria calda, temperatura secondo la "
                                                  "tua stazione'); solo valori presenti nelle fonti, altrimenti dillo")
    controllo: str = Field(default="", description="Come capisci che il passo è riuscito prima di andare avanti")


class Procedura(BaseModel):
    dispositivo: str = Field(description="nome commerciale più codice modello, oppure 'sconosciuto'")
    obiettivo: str = Field(description="Cosa ottiene la procedura, in una frase")
    passi: list[PassoProcedura] = Field(description="Passi in ordine, da 4 a 12")
    verifica_finale: list[str] = Field(default_factory=list, description="Misure e prove per confermare il lavoro")
    avvertenze_sicurezza: list[str] = Field(default_factory=list, description="Rischi per il tecnico o la scheda")
    fonti: list[str] = Field(default_factory=list, description="Pagine della wiki usate")
    domande_al_tecnico: list[str] = Field(default_factory=list, description="Informazioni mancanti, al massimo 2")
