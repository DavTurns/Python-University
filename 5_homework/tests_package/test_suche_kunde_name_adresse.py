from repository_package import repository
from model_package import modelle
from controller_package import controller
import os


def test2():
    print("-----------TEST 2----------------\n\n")
    controller1 = controller.Controller(
        "kundenliste_test.csv",
        "speisekarte_test.csv",
        "getränkekarte_test.csv",
        "bestellungen_test.csv",
    )
    # kundenrepo = repository.CustomerFormatter("kundenliste_test.csv")
    Kunde1 = modelle.Kunde("1", "David", "Brasov")
    Kunde2 = modelle.Kunde("2", "Daniel", "Brasov")
    Kunde3 = modelle.Kunde("2", "David", "Cluj")
    liste = [Kunde1, Kunde2, Kunde3]

    print("Fall 1: Eindeutiges Ergebnis, Groß/Kleinschreibung berücksichtigt...")
    try:
        assert controller1.kunde_suchen("Dan", liste) == [Kunde2]
        print("Erfolgreich")
    except:
        print("Fehlgeschlagen")

    print("Fall 2: Eindeutiges Ergebnis, Groß/Kleinschreibung nicht berücksichtigt...")
    try:
        assert controller1.kunde_suchen("dan", liste) == [Kunde2]
        print("Erfolgreich")
    except:
        print("Fehlgeschlagen")

    print("Fall 3: Nicht eindeutiges Ergebnis, Groß/Kleinschreibung berücksichtigt...")
    try:
        assert controller1.kunde_suchen("Dav", liste) == [Kunde1, Kunde3]
        print("Erfolgreich")
    except:
        print("Fehlgeschlagen")

    print(
        "Fall 4: Nicht eindeutiges Ergebnis, Groß/Kleinschreibung nicht berücksichtigt..."
    )
    try:
        assert controller1.kunde_suchen("dav", liste) == [Kunde1, Kunde3]
        print("Erfolgreich")
    except:
        print("Fehlgeschlagen")

    print("Fall 5: Nicht eindeutiges Ergebnis, keine Eingabe...")
    try:
        assert controller1.kunde_suchen("", liste) == liste
        print("Erfolgreich")
    except:
        print("Fehlgeschlagen")
    print("\n\n")


def test3():
    print("-----------TEST 3----------------\n\n")
    controller1 = controller.Controller(
        "kundenliste_test.csv",
        "speisekarte_test.csv",
        "getränkekarte_test.csv",
        "bestellungen_test.csv",
    )
    # kundenrepo = repository.CustomerFormatter("kundenliste_test.csv")
    Kunde1 = modelle.Kunde("1", "David", "Brasov")
    Kunde2 = modelle.Kunde("2", "Daniel", "Brasov")
    Kunde3 = modelle.Kunde("2", "David", "Cluj")
    liste = [Kunde1, Kunde2, Kunde3]

    print("Fall 1: Eindeutiges Ergebnis, Groß/Kleinschreibung berücksichtigt...")
    try:
        assert controller1.kunde_suchen("Clu", liste) == [Kunde3]
        print("Erfolgreich")
    except:
        print("Fehlgeschlagen")

    print("Fall 2: Eindeutiges Ergebnis, Groß/Kleinschreibung nicht berücksichtigt...")
    try:
        assert controller1.kunde_suchen("lUj", liste) == [Kunde3]
        print("Erfolgreich")
    except:
        print("Fehlgeschlagen")

    print("Fall 3: Nicht eindeutiges Ergebnis, Groß/Kleinschreibung berücksichtigt...")
    try:
        assert controller1.kunde_suchen("Bra", liste) == [Kunde1, Kunde2]
        print("Erfolgreich")
    except:
        print("Fehlgeschlagen")

    print(
        "Fall 4: Nicht eindeutiges Ergebnis, Groß/Kleinschreibung nicht berücksichtigt..."
    )
    try:
        assert controller1.kunde_suchen("RAS", liste) == [Kunde1, Kunde2]
        print("Erfolgreich")
    except:
        print("Fehlgeschlagen")

    print("Fall 5: Nicht eindeutiges Ergebnis, keine Eingabe...")
    try:
        assert controller1.kunde_suchen("", liste) == liste
        print("Erfolgreich")
    except:
        print("Fehlgeschlagen")
    print("\n\n")


test2()
test3()
