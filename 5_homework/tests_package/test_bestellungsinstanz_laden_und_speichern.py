from model_package.modelle import Bestellung
from repository_package.repository import OrderFormatter
import os


def test67():
    """
    testet, ob Konvertierung und Speicherung einer Bestellungsinstanz funktioniert
    """
    print("-----------TEST 6----------------\n\n")
    print(
        """TEST: Konvertierung und Speicherung von Bestellungsinstanz
    UND Lesen und Konvertierung von Bestellungsinstanz wird ausgeführt"""
    )

    Orepo = OrderFormatter("Test_Bestellungen.csv")

    order = Bestellung("2", "3", ["1", "2", "3"], ["4", "5", "6"])
    Orepo.save([order])
    realer_inhalt = Orepo.readfile().split("\n")[-1]

    vorrausgesetzter_inhalt = "2;3;1,2,3;4,5,6;0"

    try:
        assert realer_inhalt == vorrausgesetzter_inhalt
        print("Test 'KONVERTIERUNG UND SPEICHERUNG' erfolgreich")
    except:
        print("Test 'KONVERTIERUNG UND SPEICHERUNG' fehlgeschlagen")

    saved_order = Orepo.load()[0]
    print("-----------TEST 7----------------\n\n")

    try:
        assert order == saved_order
        print("Test 'LESEN UND KONVERTIERUNG' erfolgreich")
    except:
        print("Test 'LESEN UND KONVERTIERUNG' fehlgeschlagen")

    os.remove("Test_Bestellungen.csv")


test67()
