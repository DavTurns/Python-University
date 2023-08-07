from controller_package import controller
from ui_package import ui
from tests_package.test_bestellungsinstanz_laden_und_speichern import *
from tests_package.test_gericht_hinzufügen import *
from tests_package.test_kunde_aktualisieren import *
from tests_package.test_rechnungsstring_erstellen import *
from tests_package.test_suche_kunde_name_adresse import *
import os


def main():
    test1()
    test2()
    test3()
    test4()
    test5()
    test67()
    dir_path = os.path.dirname(__file__)
    path_Kundenliste = os.path.join(dir_path, "repository_package/Kundenliste.csv")
    path_Speisekarte = os.path.join(dir_path, "repository_package/Speisekarte.csv")
    path_Getränkeliste = os.path.join(dir_path, "repository_package/Getränke.csv")
    path_Bestellungen = os.path.join(dir_path, "repository_package/Bestellungen.csv")
    while True:
        ui.weiter()

        c = controller.Controller(
            path_Kundenliste, path_Speisekarte, path_Getränkeliste, path_Bestellungen
        )
        c.run()
