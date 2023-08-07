from functools import reduce

# Benotung:
# 1.a 3 Punkte
# 1.b 1 Punkt
# 2.a 2 Punkte
# 2.b 2 Punkte
# 3. 1 Punkt
# Insgesamt: 9 Punkte

# 1.
# a. Geben sei eine Textdatei mit dem Namen "zahlen.txt" an, auf eine mehreren Zeilen, Zahlen die durch
# die Zeichenkette "UBB" getrennt sind.
# schreiben Sie eine Funktion namens "ub1", die:
#   - einen Parameter namens "even_row" erhält
#   - aus der angegebenen CSV-Datei "zahlen.txt" liest
#   - wenn "even_row" der Wert "True" (bool) hat, behalten nur die Zeilen, wo alle Zahlen gerade Zahlen sind (0.25p)
#   - wenn "even_row" der Wert "False" (bool) hat, behalten nur die Zeilen, wo alle Zahlen ungerade Zahlen sind (0.25p)
#   - Das Ergebnis der Funktion ist die Summe der Zahlen der behaltenen Zeilen (0.5p)
# Es sind keine for- oder while-Schleifen erlaubt. Es wird erwartet, dass die Lösung map, filter oder reduce und
# andere mathematische Operationen, falls erforderlich, benutzt sind. (2p)
#
# b. Schreiben Sie für die Funktion "ub1" zwei Testfälle. (1p)
# Einer, der das erwartete Ergebnis der Funktion bestätigt und ein anderer, der absichtlich fehlschlägt.
#


def ub1(even_row):
    with open("zahlen.txt", "r") as f:
        inhalt = f.read().split("\n")

        def is_even(char):
            if char.isalpha() == True:
                return False

            char = int(char)

            if char % 2 == 0:
                return True

            return False

        def is_uneven(char):
            if char.isalpha() == True:
                return False

            char = int(char)

            if char % 2:
                return True

            return False

        temp = []

        if even_row == True:  # wenn eine ungerade in
            temp = list(
                filter(
                    lambda zeile: False
                    if len(list(filter(is_uneven, zeile))) > 0
                    else True,
                    inhalt,
                )
            )

        if even_row == False:
            temp = list(
                filter(
                    lambda zeile: False
                    if len(list(filter(is_even, zeile))) > 0
                    else True,
                    inhalt,
                )
            )

        def is_num(char):
            try:
                int(char)

                return True

            except:
                return False

        return temp


# 2.
# a. Schreiben Sie die Definition für eine Klasse namens "Shop".
# Die Klasse sollte in der Lage sein, das Folgende zu tun:
#    - bei der Initialisierung wird die Instanzvariable "products" auf einen gegebenen Parameter gesetzt.
#      Der Typ des Parameters ist eine Liste von strings. (0.5p)
#    - eine Methode namens "buy" haben, die:
#       - einen einzelnen ganzzahligen Parameter namens "price" bekommt
#       - für alle Element aus der Liste "products" prüft, dass die doppelte Länge des Elements nicht größer als "price" ist (0.5pp)
#       - gibt eine neue Liste mit strings zurück, die dem folgenden Format behalten: "<element> - <price>" (0.5p)
#       - eine benutzerdefinierte Ausnahme namens "BadName" wirft, wenn die Prüfung der Lange nicht fördert(0.5p)
#


class BadName(Exception):
    def __init__(self, message):
        self.message = message


class Shop:
    def __init__(self, products):
        if type(products) != list:
            raise TypeError("Keine Liste")

        for prod in products:
            if type(prod) != str:
                raise TypeError("Kein String")

        self.products = products

    def buy(self, price):
        if type(price) != int:
            raise TypeError("kein int")

        temp = []

        for prod in self.products:
            if 2 * len(prod) > price:
                raise BadName("doppeltelänge eines elem > price")

            temp.append(f"{prod} - {price}")

        return temp


class BetterShop(Shop):
    def __init__(self, products):
        super().__init__(products)

        self.total = 0

    def buy(self, price):
        try:
            super().buy(price)

            self.total += price

        except:
            self.total = -1

    def __sub__(self, other):
        temp = []

        for elem in self.products:
            if elem in other.products:
                temp.append(elem)

        return temp


b1 = BetterShop(["Pizza", "Döner", "Sprite", "Hemd"])

b2 = BetterShop(["Cola", "Sprite", "Döner"])

print(b1 - b2)


# b. Schreiben Sie die Definition für eine Klasse namens "BetterShop", die von "Shop" erbt.
#  Die Klasse sollte folgendes können:
#   - bei der Initialisierung setzt sie neben den Variablen von "Shop" auch eine Instanzvariable namens
#     "total" auf 0 (0.25p)
#   - Überschreiben der Methode "buy", um Folgendes zu tun:
#       - Wiederverwendung der Methode "buy" aus der Basisklasse (0.25)
#       - Im Falle eines erfolgreichen Aufrufs wird das Ergebnis zurückgegeben und die Instanzvariable "total" mit dem
#         Wert von "price" erhöht (0.25p)
#       - im Falle einen fehlgeschlagenen Aufruf wird die Instanzvariable "total" auf -1 gesetzt (0.25p)
#   - Das Ergebnis der Subtraktion zwischen zwei Instanzen des Typs "BetterShop" (shop1 - shop2) ist eine Liste
#     von strings die sich in der "products" der beiden Instanzen befinden.
#     (1p)
#
# 3. Schreibe die folgende Funktion so um, dass sie rekursiv ist: (1p)


def my_func(some_list, other_function):
    my_list = []

    for num in some_list:
        if other_function(num):
            my_list.append(num)

    return my_list


def my_func_rec(other_function, some_list, filtered_list):
    if len(some_list) == 0:
        return filtered_list

    if other_function(some_list[0]):
        filtered_list.append(some_list[0])

    return my_func_rec(other_function, some_list[1:], filtered_list)


if __name__ == "__main__":
    print(
        my_func_rec(lambda x: True if x < 13 else False, [1, 66, 33, 2, 3, 64, -2], [])
    )
    print(ub1(0))
