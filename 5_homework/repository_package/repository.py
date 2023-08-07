from model_package import modelle


class DataFormatter:
    def __init__(self, datei):
        self.datei = datei

    def save(self, liste_objekte):
        """
        speichert eine Liste von Objekten in einer Datei
        """
        string = self.convert_to_string(liste_objekte)
        self.writetofile(string)

    def load(self):
        """
        liest eine Liste von Objekten aus einer Datei
        """

        liste_objekte_string = self.readfile()
        return self.convert_from_string(liste_objekte_string)

    def readfile(self):
        """
        liest den Inhalt einer Datei und gibt ihn zurück
        """
        inhalt = ""
        try:
            with open(self.datei, "r") as f:
                inhalt = f.read()
        except:
            f = open(self.datei, "x")
            f.close()
        return inhalt

    def writetofile(self, string):
        """
        schreibt einen String in eine Datei und überschreibt die Datei
        """
        with open(self.datei, "w") as f:
            f.write(string)

    def convert_to_string(self, liste_objekte):
        """
        empfängt als Argument eine Liste von Objekten, die in
        einen String konvertiert und später in der Datei gespeichert werden
        müssen. Da von anderen Klassen individuell geerbt, wird sie hier nur definiert.
        """

    def convert_from_string(self, string):
        """
        empfängt einen String und konvertiert ihn in eine
        Liste von Objekten, die zuvor aus einer Datei gelesen wurden. Soll nicht
        implementiert werden, nur definiert. Da von anderen Klassen individuell geerbt, wird sie hier nur definiert.
        """


class CookedDishFormatter(DataFormatter):
    # self, id, name, preis, portionsgröße, zubereitungszeit

    def convert_to_string(self, liste_objekte):
        string = "ID,Name,Preis(in €),Portionsgröße(in g),Zubereitungszeit(in min)"
        string += "".join(
            list(
                map(
                    lambda obj: "\n"
                    + str(obj.id)
                    + ","
                    + str(obj.name)
                    + ","
                    + str(obj.preis)
                    + ","
                    + str(obj.portionsgröße)
                    + ","
                    + str(obj.zubereitungszeit),
                    liste_objekte,
                )
            )
        )
        return string

    def convert_from_string(self, string):
        if string != "":
            templist = string.split("\n")
            templist.pop(0)

            def lineinobj(line):
                temp = line.split(",")
                return modelle.GekochtesGericht(
                    temp[0], temp[1], float(temp[2]), temp[3], int(temp[4])
                )

            return list(map(lineinobj, templist))
        return list()


class DrinkFormatter(DataFormatter):
    def convert_to_string(self, liste_objekte):
        string = "ID,Name,Preis(in €),Portionsgröße(in ml),Alkoholgehalt(in %)"
        string += "".join(
            list(
                map(
                    lambda obj: "\n"
                    + str(obj.id)
                    + ","
                    + str(obj.name)
                    + ","
                    + str(obj.preis)
                    + ","
                    + str(obj.portionsgröße)
                    + ","
                    + str(obj.alkoholgehalt),
                    liste_objekte,
                )
            )
        )
        return string

    def convert_from_string(self, string):
        if string != "":
            templist = string.split("\n")
            templist.pop(0)

            def lineinobj(line):
                temp = line.split(",")
                return modelle.Getränk(
                    temp[0], temp[1], float(temp[2]), temp[3], temp[4]
                )

            return list(map(lineinobj, templist))
        return list()


class CustomerFormatter(DataFormatter):
    def convert_to_string(self, liste_objekte):
        string = "ID,Name,Adresse"
        string += "".join(
            list(
                map(
                    lambda obj: "\n"
                    + str(obj.id)
                    + ","
                    + str(obj.name)
                    + ","
                    + str(obj.adresse),
                    liste_objekte,
                )
            )
        )
        return string

    def convert_from_string(self, string):
        if string != "":
            templist = string.split("\n")
            templist.pop(0)

            def lineinobj(line):
                temp = line.split(",")
                return modelle.Kunde(temp[0], temp[1], temp[2])

            return list(map(lineinobj, templist))
        return list()


class OrderFormatter(DataFormatter):
    def convert_to_string(self, liste_objekte):
        string = (
            "Bestellungsid;Kundenid;Liste_ID_Gerichte;Liste_ID_Getränke;Gesamtpreis"
        )
        string += "".join(
            list(
                map(
                    lambda obj: f"\n{str(obj.id)};{str(obj.kunden_id)};{','.join(obj.liste_id_gerichte)};{','.join(obj.liste_id_getränke)};{str(obj.gesamtkosten)}",
                    liste_objekte,
                )
            )
        )
        return string

    def convert_from_string(self, string):
        if string != "":
            templist = string.split("\n")
            templist.pop(0)

            def lineinobj(line):
                temp = line.split(";")
                return modelle.Bestellung(
                    temp[0],
                    temp[1],
                    temp[2].split(","),
                    temp[3].split(","),
                    float(temp[4]),
                )

            return list(map(lineinobj, templist))
        return list()
