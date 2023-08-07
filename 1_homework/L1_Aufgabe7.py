def ex_a():
    """
    Task: Lese Sequenzen von positiven ganzen Zahlen (das Lesen jeder Sequenz endet mit 0, das
    Lesen aller Sequenzen endet mit -1) und bestimme das maximale Element jeder Sequenz
    und das maximale Element der globalen Sequenz.
    """
    zeichenkette = "7801123hh40AES29-1303330233h819fh9f310f13f0"
    sequenzliste = []  # Liste aller Sequenzen in der Zeichenkette
    sequenz = ""
    maximale_elemente = ""

    if (
        "-1" in zeichenkette and zeichenkette[0] != "-" and zeichenkette[1] != "1"
    ):  # wenn -1 vorhanden ist, aber nicht am Anfang steht
        index_ende = zeichenkette.find("-1")  # alles hinter -1 wird gelöscht
        # print(index_ende)

        if index_ende != 0:  # alles ab -1 nach hinten wird gelöscht
            zeichenkette = zeichenkette[0:index_ende]
            print(zeichenkette)

            for zeichen in zeichenkette:
                if (
                    zeichen.isnumeric() == True and zeichen != "0"
                ):  # ist das zeichen eine Zahl und nicht 0
                    sequenz += zeichen

                if (
                    zeichen == "0" and sequenz != ""
                ):  # ist das Zeichen 0 und ist die sequenz befüllt
                    sequenzliste.append(sequenz)
                    sequenz = ""

        print("sequenzenliste ist ", sequenzliste)

        for element in range(0, len(sequenzliste)):
            maximales_element_sequenz = max(sequenzliste[element])
            print(
                "Das maximale Element der Sequenz ",
                sequenzliste[element],
                " ist " + maximales_element_sequenz,
            )
            maximale_elemente += str(maximales_element_sequenz)
        if maximale_elemente != "":
            print(
                "Das maximale Element der Globalen Sequenz ist: ",
                max(maximale_elemente),
            )


def ex_b():
    """
    Task:  Geben Sie die längste zusammenhängende Teilsequenz mit einem Vektor aus Zahlen so
    an, dass alle Elemente in einem bestimmten Intervall liegen
    """
    liste = [5, 1, 2, 3, 4, 1, 5, 6, 1, 7, 8, 9, 22, 3, 6, 6, 6, 6]
    intervall = [4, 10]  # unser beliebiges Intervall
    aktuelle_sequenz = []
    größte_sequenz = []
    for element in range(len(liste)):
        if (
            liste[element] >= intervall[0] and liste[element] <= intervall[1]
        ):  # wenn Zahl im Intervall ist
            aktuelle_sequenz.append(
                liste[element]
            )  # wird diese zur aktuellen Sequenz hinzugefügt

        elif aktuelle_sequenz and len(größte_sequenz) < len(aktuelle_sequenz):
            print("Die aktuell größte Sequenz ist: ", aktuelle_sequenz)
            größte_sequenz = aktuelle_sequenz  # Es wird die größte sequenz aktualisiert
            aktuelle_sequenz = []
        else:
            aktuelle_sequenz = []
    print("Die größte Sequenz der Liste ist: ", größte_sequenz)


if __name__ == "__main__":
    ex_a()
    ex_b()
