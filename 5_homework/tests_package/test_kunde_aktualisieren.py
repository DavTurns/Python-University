from controller_package import controller
from model_package import modelle


def test4():
    print("-----------TEST 4----------------\n\n")
    con1 = controller.Controller(
        "kundenliste_path",
        "speisekarte_path",
        "getränkekarte_path",
        "bestellungen_path",
    )
    k1 = modelle.Kunde("1", "David", "Brasov")
    k2 = modelle.Kunde("2", "Daniel", "Bucuresti")
    k3 = modelle.Kunde("3", "Dob", "Grovestreet")
    Kundenliste = [k1, k2, k3]
    neuer_name = "Carl Johnson"
    neue_adresse = "Grovestreet"

    con1.kunde_aktualisieren(Kundenliste, k3, neuer_name, neue_adresse)

    try:
        assert k3.name == neuer_name and k3.adresse == neue_adresse
        print("Test 'Kundenname aktualisieren' erfolgreich")
    except:
        print("Test 'Kundenname aktualisieren' fehlgeschlagen")


test4()
