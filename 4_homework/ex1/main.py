from functions.dictfunc import *
from functions.turtlefunc import *
import turtle

"""
Programm
zwei Unterprogramme

menu
1.text
2.neues Zeichen
-----
2. Neues Zeichen
    Programm fragt welches Zeichen eingefügt werden soll
    Programm vergewissert dass input nur ein Zeichen ist, das im dict nicht vorkommt
    Programm startet turtle und nimmt zeichenkombination auf(Beendet mit ENTER)
    Eingabe wie im spiel
    Wenn kein kommand eingegeben wurde
"""


def zeichenlöschen_main(dictpath):
    """
    Diese Datei löscht einen Eintrag aus dem Dictionary
    Input: Dateipfad
    """

    wörterbuch = eval(readfile(dictpath))
    zulöschendezeichen = str(input("Geben Sie das zulöschende Zeichen ein"))

    if zulöschendezeichen in wörterbuch:
        wörterbuch.pop(zulöschendezeichen)
        print("Zeichen: " + zulöschendezeichen + " erfolgreich gelöscht")
    else:
        print("Zeichen nicht vorhanden")

    overwritedict(dictpath, wörterbuch)


def neueszeichen_main(dictpath):
    """
    Das ist die Hauptfunktion des 2.Programms
    Es lässt den Benutzer nach Belieben eine neue Zeichnung hinzufügen,
    welche einer Taste assoziiert wird.
    Input: Dateipfad (string)
    """
    # Das eigentliche Programm fängt erst weiter unten an
    # Das sind die Funktionen, die ausgeführt werden wenn man ein eine Taste drückt.
    # Jede Funktion fügt außerdem auch noch den eingegebenen Buchstaben in die Anweisungsliste ein.

    def w_rec():
        turtle.forward(10)
        anweisungsliste.append("w")

    def d_rec():
        turtle.right(45)
        anweisungsliste.append("d")

    def a_rec():
        turtle.left(45)
        anweisungsliste.append("a")

    def s_rec():
        turtle.backward(10)
        anweisungsliste.append("s")

    def f_rec():
        turtle.up()
        anweisungsliste.append("f")

    def g_rec():
        turtle.down()
        anweisungsliste.append("g")

    def exit():
        turtle.bye()

    # --------Hier fängt das eigentliche Progamm an--------------------------------

    zeichenbuch = eval(readfile(dictpath))
    neueszeichen = ""

    while True:
        neueszeichen = str(
            input(
                "Geben Sie ein Zeichen ein, \nan welches Sie die Zeichnung koppeln wollen:"
            )
        )
        if len(neueszeichen) != 1:
            print("Error, das Zeichen soll eine Stelle lang sein")
        if neueszeichen in zeichenbuch:
            print("Error, das Zeichen ist schon im Wörterbuch registriert")
        else:
            break

    anweisungsliste = []
    sc = turtle.Screen()
    sc.setup(0.5, 0.5)

    turtle.listen()
    turtle.onkey(w_rec, "w")
    turtle.onkey(d_rec, "d")
    turtle.onkey(a_rec, "a")
    turtle.onkey(s_rec, "s")
    turtle.onkey(f_rec, "f")
    turtle.onkey(g_rec, "g")
    turtle.onkey(exit, "")

    # sc.onkey(exit(),'') #wenn Enter gedrückt wird bricht das programm ab
    turtle.mainloop()

    zeichenbuch[
        neueszeichen
    ] = anweisungsliste  # Zeichen mit Anweisungsliste wird in Dict hinzugefügt

    overwritedict(dictpath, zeichenbuch)


def textnachricht_main(dictpath):
    """
    Diese Funktion schreibt einen eingegebenen Text in Turtle auf
    input: Dateifad (string)
    """

    dictionary = eval(readfile(dictpath))

    wort = str(input("Geben Sie ein Wort ein: "))

    for char in wort:
        if char not in dictionary:
            print(f"Error - {char} nicht definiert in Dictionary")
            return

    t = turtle.Pen()
    t.up()
    t.goto(-300, 0)

    for zeichen in wort:
        anweisungsliste = dictionary[zeichen]
        t.down()
        for anweisung in anweisungsliste:
            anweisungausführen(t, anweisung)

        t.up()
        t.forward(30)

    input()


def menu(dictpath):
    """
    DAS IST DAS HAUPTPROGRAMM!!!
    input: (type str) Pfad der Datei, wo der dictionary liegt
    Der Benutzer wählt mit Eingabe (1-3) ein Unterprogramm aus:
    1.Textnachricht zeichnen 2.Neues Zeichen erstellen 3.Vorhandenes Zeichen löschen
    """
    auswahl = str(
        input(
            "Wählen Sie das gewünschte Programm aus\n1.Textnachricht zeichnen\n2.Neues Zeichen erstellen\n3.Vorhandenes Zeichen löschen\nIhre Wahl: "
        )
    )
    match auswahl:
        case "1":
            textnachricht_main(dictpath)

        case "2":
            neueszeichen_main(dictpath)

        case "3":
            zeichenlöschen_main(dictpath)


if __name__ == "__main__":
    pfaddictionary = ""  # define your path where your dictionary should be found
    menu(pfaddictionary)
