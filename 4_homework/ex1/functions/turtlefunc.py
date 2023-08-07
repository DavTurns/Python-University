import turtle


#Hier sind alle Funktionen, die etwas mit Turtle zu tun haben

def anweisungausführen(turtle, char):
    """
    Diese Funktion führt den eingegebenen Befehl in Turtle aus
    Input: Turtleobjekt, befehl (string)
    """
    
    if char == "w":
        turtle.forward(10)

    if char == "s":
        turtle.backward(10)

    if char == "a":
        turtle.left(45)

    if char == "d":
        turtle.right(45)

    if char == "f":
        turtle.up()
        
    if char == "g":
        turtle.down()



"""
Folgende Funktionen sind Teil von Programm neueszeichen,
sie werden aufgerufen, wenn der Benutzer die Jeweilige Taste drückt 
und die anweisung wird zur anweisungsliste hinzugefügt"""

