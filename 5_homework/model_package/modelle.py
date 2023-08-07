import functools
import datetime


class Identifizierbar:
    def __init__(self, id):
        self.id = id


class Gericht(Identifizierbar):
    def __init__(self, id, preis, portionsgröße="350g"):
        Identifizierbar.__init__(self, id)
        self.preis = preis
        self.portionsgröße = portionsgröße


class GekochtesGericht(Gericht):
    def __init__(self, id, name, preis, portionsgröße, zubereitungszeit):
        Gericht.__init__(self, id, preis, portionsgröße)
        self.zubereitungszeit = zubereitungszeit
        self.name = name

    def __eq__(self, other):
        return (
            self.id == other.id
            and self.preis == other.preis
            and self.portionsgröße == other.portionsgröße
            and self.zubereitungszeit == other.zubereitungszeit
        )

    def __add__(self, other):
        return self.preis + other.preis

    def __str__(self):
        return f"{self.id}, {self.name}, {self.preis}, {self.portionsgröße}, {self.zubereitungszeit}"


class Getränk(Gericht):
    def __init__(self, id, name, preis, portionsgröße, alkoholgehalt):
        super().__init__(id, preis, portionsgröße)
        self.alkoholgehalt = alkoholgehalt
        self.name = name

    def __add__(self, other):
        return self.preis + other.preis


class Kunde(Identifizierbar):
    def __init__(self, id, name, adresse):
        Identifizierbar.__init__(self, id)
        self.name = name
        self.adresse = adresse

    def __str__(self):
        return f"{self.id} {self.name} {self. adresse}"


class Bestellung(Identifizierbar):
    def __init__(
        self, id, kunden_id, liste_id_gerichte, liste_id_getränke, gesamtkosten=0
    ):
        super().__init__(id)
        self.kunden_id = kunden_id
        self.liste_id_gerichte = liste_id_gerichte
        self.liste_id_getränke = liste_id_getränke
        self.gesamtkosten = gesamtkosten

    def __eq__(self, other):
        return (
            self.id == other.id
            and self.kunden_id == other.kunden_id
            and self.liste_id_gerichte == other.liste_id_gerichte
            and self.liste_id_getränke == other.liste_id_getränke
            and self.gesamtkosten == other.gesamtkosten
        )

    def kostenberechnung(self, liste_gerichte):
        liste_gerichte_ids = [obj.id for obj in liste_gerichte]
        liste_gerichte_preise = list(
            map(
                lambda id: liste_gerichte[liste_gerichte_ids.index(id)].preis,
                self.liste_id_gerichte + self.liste_id_getränke,
            )
        )

        self.gesamtkosten = functools.reduce(lambda a, b: a + b, liste_gerichte_preise)

    def __erzeugen_rechnung(self, liste_aller_speisen, kunde):
        """
        privat!
        Erzeugt eine Rechnung anhand der Attribute von Bestellung
        Output: Rechnung (str)
        """

        def convert_to_preis_name(gericht_id):
            for speise in liste_aller_speisen:  # wie kann ich das effizienter machen?
                if speise.id == gericht_id:
                    return f"\n{speise.preis}   {speise.name}"

        getränke_mit_preis = "".join(
            list(map(convert_to_preis_name, self.liste_id_getränke))
        )
        gerichte_mit_preis = "".join(
            list(map(convert_to_preis_name, self.liste_id_gerichte))
        )

        liste_aller_speisen_ids = [speise.id for speise in liste_aller_speisen]
        vorbereitungszeit = sum(
            list(
                map(
                    lambda id: liste_aller_speisen[
                        liste_aller_speisen_ids.index(id)
                    ].zubereitungszeit,
                    self.liste_id_gerichte,
                )
            )
        )
        print(vorbereitungszeit)
        now = datetime.datetime.now()

        vorraussichtliche_lieferung = (
            now + datetime.timedelta(minutes=vorbereitungszeit)
        ).strftime("%d.%m.%Y %H:%M")
        now_print = now.strftime("%d.%m.%Y %H:%M")
        rechnung = f"""
        
-------------------------Rechnung------------------------------
Zeit:{now_print}
RechnungsID: {self.id}
von Kunde: {kunde}
Vorraussichtliche Lieferzeit:{vorraussichtliche_lieferung}

Gerichte:
{gerichte_mit_preis}

Getränke:
{getränke_mit_preis}
---------------------------------------------------------------
{self.gesamtkosten}€ Gesamtkosten
        
Vielen Dank :)
        """

        return rechnung

    def anzeigen_rechnung(self, liste_aller_speisen, kunde):
        print(self._erzeugen_rechnung(liste_aller_speisen, kunde))
