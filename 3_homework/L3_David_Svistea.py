import turtle
from threading import Thread


def menu():
    """
    Erstellt ein eingabemenu
    Input: /
    Output: Nummer der Aufgabe in int (1-3)
    """

    print("1: Zwei Rechtecke")
    print("2: Herz")
    print("3: Zwei Häuser")
    wahl = int(input("Gib die Nummer des Programms ein, das du ausführen willst: "))

    return wahl


def aufgabe1():
    """
    zeichnet ein rechteck mit 100X200px
    und ein kleines mit 25X50px
    """
    t = turtle.Pen()

    def rechteck(höhe, breite):
        """
        zeichnet ein rechteck
        wichtig!: Turtle muss nach rechts zeigen bevor rechteck() aufgerufen wird
        und endet nach unten zeigend
        input: int, int
        """

        t.down()
        t.forward(breite)
        t.left(90)
        t.forward(höhe)
        t.left(90)
        t.forward(breite)
        t.left(90)
        t.forward(höhe)
        t.up()

    rechteck(100, 200)

    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(25)
    t.right(90)
    rechteck(25, 50)


# aufgabe1()


def aufgabe2():
    """
    Zeichnet ein Herz
    """
    t = turtle.Pen()

    # funktion 90 grad Kurve
    def kreissegment(grad):
        for i in range(grad):
            t.left(1)
            t.forward(1)

    # Herz zeichnen mit Funktionen
    t.left(45)
    t.forward(120)
    kreissegment(180)
    t.right(90)
    kreissegment(180)
    t.forward(120)


# aufgabe2()


def aufgabe3():
    """
    Man soll zwei Häuser relativ gleichzeitig zeichnen
    """

    t1 = turtle.Pen()
    t2 = turtle.Pen()

    # t2 wird zur seite verschoben3
    t2.up()
    t2.backward(250)
    t2.down()

    def rechteck(höhe, breite):
        """
        zeichnet ein rechteck
        wichtig!: Turtle muss nach rechts zeigen bevor rechteck() aufgerufen wird
        und endet nach unten zeigend
        input: int, int
        """

        t1.down()
        t2.down()
        t1.forward(breite)
        t2.forward(breite)
        t1.left(90)
        t2.left(90)
        t1.forward(höhe)
        t2.forward(höhe)
        t1.left(90)
        t2.left(90)
        t1.forward(breite)
        t2.forward(breite)
        t1.left(90)
        t2.left(90)
        t1.forward(höhe)
        t2.forward(höhe)
        t1.up()
        t2.up()

    def b_right(grad):
        """
        führt .right() für beide turtles aus
        """
        t1.right(grad)
        t2.right(grad)

    def b_left(grad):
        """
        führt .left() für beide turtles aus
        """
        t1.left(grad)
        t2.left(grad)

    def b_forward(pixel):
        """
        führt .forward() für beide turtles aus
        """
        t1.forward(pixel)
        t2.forward(pixel)

    def b_up():
        """
        führt .up() für beide turtles aus
        """
        t1.up()
        t2.up()

    def b_down():
        """
        führt .down() für beide turtles aus
        """
        t1.down()
        t2.down()

    """
    Jetzt werden durch aufrufen der Funktionen und einzelnen Bewegungen das Haus gebaut
    """
    # Grundriss
    rechteck(100, 200)

    b_left(90)
    b_forward(40)

    # Tür
    rechteck(40, 20)

    b_left(90)
    b_forward(80)
    b_left(90)
    b_forward(40)
    b_right(90)

    # Fenster
    rechteck(30, 60)

    b_left(90)
    b_forward(80)
    b_left(90)
    b_forward(60)

    # Dach
    b_left(45)
    b_down()
    b_forward(141)
    b_left(90)
    b_forward(141)


def main():
    aufgabennummer = menu()

    if aufgabennummer == 1:
        aufgabe1()
    if aufgabennummer == 2:
        aufgabe2()
    if aufgabennummer == 3:
        aufgabe3()


main()
