from model_package import modelle
from repository_package import repository
import datetime


def test5():
    print("-----------TEST 5----------------\n\n")
    dishrepo = repository.CookedDishFormatter("Speisekarte_test.csv")

    GekochtGerichtListe = [modelle.GekochtesGericht("1", "Gericht1", 1, "100", 10)]
    GetränkeListe = [modelle.Getränk("2", "Getränk1", 2, "200", 0.5)]
    GerichtListe = GekochtGerichtListe + GetränkeListe

    Kunde1 = modelle.Kunde("7", "Gigi", "Pipera")

    Liste_ID_Gerichte = ["1", "1"]
    Liste_ID_Getränke = ["2", "2"]

    bestellung1 = modelle.Bestellung(
        "1", Kunde1.id, Liste_ID_Gerichte, Liste_ID_Getränke
    )
    bestellung1.kostenberechnung(GerichtListe)

    berechnete_rechnung = bestellung1._Bestellung__erzeugen_rechnung(
        GerichtListe, Kunde1
    )

    def convert_to_preis_name(gericht_id):
        for speise in GerichtListe:  # wie kann ich das effizienter machen?
            if speise.id == gericht_id:
                return f"\n{speise.preis}   {speise.name}"

    getränke_mit_preis = "".join(list(map(convert_to_preis_name, Liste_ID_Getränke)))
    gerichte_mit_preis = "".join(list(map(convert_to_preis_name, Liste_ID_Gerichte)))

    liste_aller_speisen_ids = [speise.id for speise in GerichtListe]
    vorbereitungszeit = sum(
        list(
            map(
                lambda id: GerichtListe[
                    liste_aller_speisen_ids.index(id)
                ].zubereitungszeit,
                Liste_ID_Gerichte,
            )
        )
    )
    now = datetime.datetime.now()

    vorraussichtliche_lieferung = (
        now + datetime.timedelta(minutes=vorbereitungszeit)
    ).strftime("%d.%m.%Y %H:%M")
    now_print = now.strftime("%d.%m.%Y %H:%M")

    vorgesehene_rechnung = f"""
        
-------------------------Rechnung------------------------------
Zeit:{now_print}
RechnungsID: {"1"}
von Kunde: {Kunde1}
Vorraussichtliche Lieferzeit:{vorraussichtliche_lieferung}

Gerichte:
{gerichte_mit_preis}

Getränke:
{getränke_mit_preis}
---------------------------------------------------------------
{6}€ Gesamtkosten
        
Vielen Dank :)
        """

    try:
        assert berechnete_rechnung == vorgesehene_rechnung
        print("Test 'Rechnungsstring berechnen' erfolgreich")
    except:
        print("Test 'Rechnungsstring berechnen' fehlgeschlagen")


test5()
