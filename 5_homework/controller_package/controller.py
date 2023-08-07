from ui_package import ui
from model_package import modelle
from repository_package import repository
import random


class Controller:
    def __init__(
        self, kundenliste_path, speisekarte_path, getränkekarte_path, bestellungen_path
    ):
        self.programmnummer = None
        self.kundenliste_path = kundenliste_path
        self.speisekarte_path = speisekarte_path
        self.getränkekarte_path = getränkekarte_path
        self.bestellungen_path = bestellungen_path

    def run(self):
        """
        Dieses ist das hauptprogramm, welches je nach Option ein Unterprogramm (Methode) aufruft
        """

        self.programmnummer = ui.eingangmenu()
        match self.programmnummer:
            case "1":
                self.neuebestellung()
            case "2":
                self.gericht_hinzufügen()
            case "3":
                self.gericht_lesen()
            case "4":
                self.gericht_bearbeiten()
            case "5":
                self.gericht_löschen()
            case "6":
                self.kunde_hinzufügen()
            case "7":
                self.kunde_lesen()
            case "8":
                self.kunde_bearbeiten()
            case "9":
                self.kunde_löschen()

    def neuebestellung(self):
        """
        Diese methode erschafft eine neue Bestellung
        """

        getränk_formatter = repository.DrinkFormatter(self.getränkekarte_path)
        dish_formatter = repository.CookedDishFormatter(self.speisekarte_path)
        kunden_formatter = repository.CustomerFormatter(self.kundenliste_path)
        bestellung_formatter = repository.OrderFormatter(self.bestellungen_path)

        # Kundeid eingeben, neuen Kunden erstellen oder bestehenden Kunden eingeben
        auswahl_neuekunde_oder_bestehenderkunde = ui.auswahlkunde()
        # assert auswahl_neuekunde_oder_bestehenderkunde in {"1","2"}
        Kunde = 0
        if auswahl_neuekunde_oder_bestehenderkunde == "1":
            Kunde = self.kunde_hinzufügen()
        if auswahl_neuekunde_oder_bestehenderkunde == "2":
            Kunde = self.kunde_lesen()

        # Kunde -> ausgewälter Kunde

        # BEMERKUNG Gericht => Nur essbar, Essen => Gericht + Getränk
        getränke_liste = getränk_formatter.load()
        gerichte_liste = dish_formatter.load()
        essen_liste = getränke_liste + gerichte_liste

        gerichte_liste_ids = [essen.id for essen in gerichte_liste]
        getränke_liste_ids = [essen.id for essen in getränke_liste]
        essen_liste_ids = gerichte_liste_ids + getränke_liste_ids

        gerichte_liste_ids_bestellung = []
        getränke_liste_ids_bestellung = []

        while True:
            self.gericht_lesen()
            ui.gericht_hinzufügen_bestellung()
            essen_id = ui.eingabe()

            if essen_id == "":
                break

            if essen_id not in essen_liste_ids:
                print("\n\nError ID nicht in der Liste\n\n")
                continue

            ui.gericht_hinzufügen_bestellung_wie_oft()
            häufigkeit = int(ui.eingabe())

            if essen_id in gerichte_liste_ids:
                for i in range(häufigkeit):
                    gerichte_liste_ids_bestellung.append(essen_id)

            if essen_id in getränke_liste_ids:
                for i in range(häufigkeit):
                    getränke_liste_ids_bestellung.append(essen_id)

        # gerichte_liste_ids_bestellung <- Ids aller bestellten Gerichte
        # getränke_liste_ids_bestellung <- Ids aller bestellten Getränke

        # überprüfen ob überhaupt eine Speise/Getränk bestellt wurde
        try:
            assert (
                len(gerichte_liste_ids_bestellung + getränke_liste_ids_bestellung) > 0
            )
        except:
            raise ValueError("Sie müssen mindestens eine Speise/Getränk bestellen")

        bestellungen_liste = bestellung_formatter.load()
        bestellung_id = self.neue_id_finden(bestellungen_liste)

        # neue Bestellung wird instanziert
        neue_bestellung = modelle.Bestellung(
            bestellung_id,
            Kunde.id,
            gerichte_liste_ids_bestellung,
            getränke_liste_ids_bestellung,
        )
        neue_bestellung.kostenberechnung(essen_liste)
        bestellungen_liste.append(neue_bestellung)
        bestellung_formatter.save(bestellungen_liste)

        neue_bestellung.anzeigen_rechnung(essen_liste, Kunde)

    """
    CRUD-Methoden zu Gericht
    """

    def gericht_hinzufügen(self):
        """
        CREATE-Methode
        """

        gerichtart = ui.gerichtsorte_wählen()

        formatter = repository.CookedDishFormatter(self.speisekarte_path)
        formatter_drink = repository.DrinkFormatter(self.getränkekarte_path)

        liste_dish = formatter.load()
        liste_drink = formatter_drink.load()

        liste = liste_dish + liste_drink

        if gerichtart == "1":
            eingabe_daten_string = ui.gerichtdaten_eingeben()
            eingabe_daten_liste = eingabe_daten_string.split(",")
            id_neue_gericht = self.neue_id_finden(liste)

            k1 = modelle.GekochtesGericht(
                id_neue_gericht,
                eingabe_daten_liste[0],
                eingabe_daten_liste[1],
                eingabe_daten_liste[2],
                eingabe_daten_liste[3],
            )
            liste_dish.append(k1)
            formatter.save(liste_dish)

        elif gerichtart == "2":
            eingabe_daten_string = ui.getränkedaten_eingeben()
            eingabe_daten_liste = eingabe_daten_string.split(",")
            id_neue_getränk = self.neue_id_finden(liste)

            k1 = modelle.Getränk(
                id_neue_getränk,
                eingabe_daten_liste[0],
                eingabe_daten_liste[1],
                eingabe_daten_liste[2],
                eingabe_daten_liste[3],
            )
            liste_drink.append(k1)
            formatter_drink.save(liste_drink)
        else:
            raise ValueError("Falscher Wert, wähle entweder 1 oder 2")

    def gericht_lesen(self):
        """
        READ-Methode
        """

        formatter = repository.DrinkFormatter(self.getränkekarte_path)
        getränkekarte = formatter.readfile()

        formatter = repository.CookedDishFormatter(self.speisekarte_path)
        speisekarte = formatter.readfile()

        ui.karten_anzeigen(speisekarte, getränkekarte)

    def gericht_bearbeiten(self):
        """
        UPDATE-Methode
        """

        self.gericht_lesen()

        ui.normalprint("Geben Sie eine ID ein\n")
        gewählte_id = ui.eingabe()

        gerichtart = ui.gerichtsorte_wählen()

        if gerichtart == "1":
            formatter = repository.CookedDishFormatter(self.speisekarte_path)
            liste = formatter.load()

            eingabe_daten_string = ui.gerichtdaten_eingeben()
            eingabe_daten_liste = eingabe_daten_string.split(",")

            for gericht in liste:
                if gericht.id == gewählte_id:
                    gericht.name = eingabe_daten_liste[0]
                    gericht.preis = eingabe_daten_liste[1]
                    gericht.portionsgröße = eingabe_daten_liste[2]
                    gericht.zubereitungszeit = eingabe_daten_liste[3]

            formatter.save(liste)

        elif gerichtart == "2":
            formatter = repository.DrinkFormatter(self.getränkekarte_path)
            liste_drink = formatter.load()

            eingabe_daten_string = ui.getränkedaten_eingeben()
            eingabe_daten_liste = eingabe_daten_string.split(",")

            for getränk in liste_drink:
                if getränk.id == gewählte_id:
                    getränk.name = eingabe_daten_liste[0]
                    getränk.preis = eingabe_daten_liste[1]
                    getränk.portionsgröße = eingabe_daten_liste[2]
                    getränk.alkoholgehalt = eingabe_daten_liste[3]

            formatter.save(liste_drink)
        else:
            raise ValueError("Falsche Eingabe")

    def gericht_löschen(self):
        """
        DELETE-Methode
        """
        # Formatter instanziieren
        formatter = repository.CookedDishFormatter(self.speisekarte_path)
        formatter_g = repository.DrinkFormatter(self.getränkekarte_path)

        speisekarte_als_string = formatter.readfile()
        speisekarte_als_liste = formatter.load()

        getränkekarte_als_string = formatter_g.readfile()
        getränkekarte_als_liste = formatter_g.load()

        ui.karten_anzeigen(speisekarte_als_string, getränkekarte_als_string)
        zulöschende_id = ui.eingabe()

        speisekarte_als_liste = list(
            filter(
                lambda gericht: True if gericht.id != zulöschende_id else False,
                speisekarte_als_liste,
            )
        )
        getränkekarte_als_liste = list(
            filter(
                lambda getränk: True if getränk.id != zulöschende_id else False,
                getränkekarte_als_liste,
            )
        )

        formatter.save(speisekarte_als_liste)
        formatter_g.save(getränkekarte_als_liste)
        # wie kann ich das besser machen?

    """
    CRUD-Methoden zu Kundenliste
    """

    def kunde_hinzufügen(self):
        """
        Create-Methode
        """
        # wir lesen kundenliste aus
        formatter = repository.CustomerFormatter(self.kundenliste_path)

        liste = formatter.load()
        eingabe_daten_string = ui.kundendaten_eingeben()

        eingabe_daten_liste = eingabe_daten_string.split(",")

        id_neue_kunde = self.neue_id_finden(liste)

        k1 = modelle.Kunde(
            id_neue_kunde, eingabe_daten_liste[0], eingabe_daten_liste[1]
        )
        liste.append(k1)
        formatter.save(liste)
        return k1

    def kunde_lesen(self):
        """
        READ-Methode

        Dient gleichzeitig als Kunde auswählen
        output: gefundener Kunde (objekt Kunde)"

        """
        formatter = repository.CustomerFormatter(self.kundenliste_path)
        kundenliste = formatter.load()

        while len(kundenliste) > 1:
            eingabe = ui.suchdaten_eingeben("Kunde")

            kundenliste = self.kunde_suchen(eingabe, kundenliste)
            for Kunde in kundenliste:
                ui.normalprint(Kunde)

        if len(kundenliste) == 0:
            raise ValueError("Keinen Kunden gefunden")
        return kundenliste[0]

    def kunde_suchen(self, eingabe, kundenliste):
        return list(
            filter(
                lambda Kunde: True
                if eingabe.casefold() in Kunde.name.casefold()
                or eingabe.casefold() in Kunde.adresse.casefold()
                else False,
                kundenliste,
            )
        )

    def kunde_bearbeiten(self):
        """
        UPDATE-Methode
        arbeitete mit kunde_lesen()
        """
        # Kundenliste aus Repository laden
        formatter = repository.CustomerFormatter(self.kundenliste_path)
        liste = formatter.load()

        # Zu bearbeitenden Kunden auswählen
        ausgewählterkunde = self.kunde_lesen()

        # Neue Kundendaten eingeben und in Liste umwandeln
        eingabe_daten_liste = ui.kundendaten_eingeben().split(",")

        # Kunde in liste wird bearbeitet
        liste = self.kunde_aktualisieren(
            liste, ausgewählterkunde, eingabe_daten_liste[0], eingabe_daten_liste[1]
        )

        # bearbeitete liste wird in Repository gespeichert
        formatter.save(liste)

        # info an Benutzer
        ui.info_erfolgreichgeändert(ausgewählterkunde.name)

    def kunde_aktualisieren(
        self, Kundenliste, ausgewählterkunde, neuer_name, neue_adresse
    ):
        for Kunde in Kundenliste:
            if Kunde.id == ausgewählterkunde.id:
                Kunde.name = neuer_name
                Kunde.adresse = neue_adresse
        return Kundenliste

    def kunde_löschen(self):
        """
        DELETE-Methode
        arbeitet mit kunde_lesen()
        """
        formatter = repository.CustomerFormatter(self.kundenliste_path)
        liste = formatter.load()

        ausgewählterkunde = self.kunde_lesen()

        for Kunde in liste:
            if ausgewählterkunde.id == Kunde.id:
                liste.remove(Kunde)
                break

        formatter.save(liste)

        ui.info_gelöscht(ausgewählterkunde.name)

    # -----------Hier enden die Crud methoden------------------
    def neue_id_finden(self, liste):
        """
        Diese Methode findet zufällig eine ID, die nicht in der jeweiligen liste verfügbar ist
        """

        liste_aller_ids = [obj.id for obj in liste]
        while True:
            id_neu = random.randint(1, 1000)
            if id_neu not in liste_aller_ids:
                return id_neu
