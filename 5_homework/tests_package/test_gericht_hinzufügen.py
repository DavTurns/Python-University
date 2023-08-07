from model_package import modelle
from repository_package import repository
import os


def test1():
    """
    Testet das Hinzufügen eines Gerichtes
    """
    print("-----------TEST 1----------------\n\n")
    krepo = repository.CookedDishFormatter(("Test_Gerichtkarte.csv"))
    liste = krepo.load()

    Gericht = modelle.GekochtesGericht("3", "Food", 22.0, "350", 40)
    liste.append(Gericht)
    krepo.save(liste)
    erneute_liste = krepo.load()

    try:
        assert erneute_liste[0] == Gericht
        print("Test: 'GERICHT HINZUFÜGEN' erfolgreich")
    except:
        print("Test: 'GERICHT HINZUFÜGEN' fehlgeschlagen!")

    os.remove("Test_Gerichtkarte.csv")


test1()
