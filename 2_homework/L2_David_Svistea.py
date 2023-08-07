def aufgabe1(liste):
    """
    Diese Funktion soll alle wiederholenden Zahlen in einer Liste löschen
    Input: Liste
    Output: Liste ohne wiederholende Zahlen
    """

    indexliste_doppelt_zahlen = []
    for zahl in liste:  # geht jede zahl in der Liste durch
        if (
            zahl in liste[liste.index(zahl) + 1 :]
        ):  # wenn die zahl, im nachfolgenden Teil der Liste existiert
            wdh = liste.count(zahl)  # wird gezählt wie oft diese in der Liste ist
            zähler = 0
            while zähler < wdh:
                liste.remove(zahl)  # und so oft wird diese gelöscht
                zähler += 1
    return liste


def aufgabe2(liste):
    """
    Zählt Anzahl symmetrische Paare in Liste
    Input: Liste aus Zahlen der Struktur xy
    Output: Anzahl symmetrische Paare in der Liste: int
    """

    count_symmetrische_paare = 0  # Anzahl symmetrische Paare startet bei 0

    for index in range(
        len(liste) - 1
    ):  # geht jede Zahl im Array durch bis zur vorletzten Zahl
        erste_zahl = str(liste[index])

        for zweiter_index in range(
            index + 1, len(liste)
        ):  # vergleicht diese mit jeder darauffolgende Zahl
            zweite_zahl = str(liste[zweiter_index])
            if (
                erste_zahl[0] == zweite_zahl[1] and erste_zahl[1] == zweite_zahl[0]
            ):  # überprüft, ob sie symmetrisch sind
                count_symmetrische_paare += 1  # wenn ja wird der counter +1

    return count_symmetrische_paare


def aufgabe3(liste):
    """
    Generiert die größtemögliche Zahl,
    die aus der Konkatenation der Elemente der Liste gebildet ist.
    Input: Liste
    Output: siehe Oben (in Str)
    """

    liste.sort(reverse=True)  # ist auch durch einen Algorithmus möglich
    größtemögliche_zahl = ""

    for zahl in liste:
        größtemögliche_zahl += str(zahl)

    return größtemögliche_zahl


def aufgabe4(liste, methode):
    """
    Verschlüsseln Sie die Elemente der Liste, indem Sie das erste Element als Schlüssel
    benützen und die Methode selbst wählen (+, *, XOR)

    Input: Liste, methode("+","*","XOR")
    Output: Verschlüsselte Liste
    """
    print(liste)

    def mitnullenfüllen(binärzahl, wunschlänge):
        """
        Füllt den Leerraum von String einer Binären Zahl
        mit beliebig vielen 0 aus bis wunschlänge erreichtwurde
        z.B "1010" -> "00001010" mit wunschlänge = 8
        Input: binärzahl in Str, wunsch in int
        Output: binärzahl in Str
        """

        # print(range(wunschlänge - len(binärzahl)))
        for i in range(wunschlänge - len(binärzahl)):
            binärzahl = "0" + binärzahl

        return binärzahl

    Schlüssel = liste[0]
    verschlüsselte_liste = [Schlüssel]
    if methode == "+":
        for zahl in liste[1:]:
            verschlüsselte_liste.append(zahl + Schlüssel)
    if methode == "*":
        for zahl in liste[1:]:
            verschlüsselte_liste.append(zahl * Schlüssel)
    if methode == "XOR":
        Binärschlüssel = mitnullenfüllen(bin(Schlüssel)[2:], 7)
        # ^ wandelt den Schlüssel in binär um, löscht die vorderen zwei chars
        # (weil 0b siehe dokumentation von bin()), und stellt die Zahl mit 7 Bits dar

        for zahl in liste[1:]:
            bin_verschlüsselte_zahl = ""
            binärzahl = mitnullenfüllen(bin(zahl)[2:], 7)
            for index in range(0, 7):
                bin_ergebnis = "0"

                if binärzahl[index] == Binärschlüssel[index]:
                    bin_ergebnis = "0"
                else:
                    bin_ergebnis = "1"

                bin_verschlüsselte_zahl += bin_ergebnis

            verschlüsselte_liste.append(int(bin_verschlüsselte_zahl, 2))

    return verschlüsselte_liste


def aufgabe5(liste, bedingung):  # todo filter
    """
    Filtern Sie die Zahlen, die eine bestimmte Beziehung zwischen Zahlen haben, die in einem
    String angegeben wird. (z.B: “x=y*3”, “x/y=2“, …)

    Input: Liste, bedingung in String
    Output: Liste mit gefilterten Zahlen
    """

    bedingung = bedingung.replace("=", "==")
    bedingung = bedingung.replace("/", "//")

    def filter_funktion(zahl):
        string_zahl = str(zahl)
        x = int(string_zahl[0])
        y = int(string_zahl[1])
        return eval(bedingung)

    return list(filter(filter_funktion, liste))


def aufgabe6(liste):
    """
    Finden Sie die längste zusammenhängende Domino Teilfolge. Eine Domino Teilfolge ist
    definiert als x1y1, x2y2, wo y1=x2. (z.B: 89, 95, 54)

    Input: Liste
    Output: Liste
    """

    dominoteilfolgen_liste = []
    # dominoteilfolge_aktuell
    dominoteilfolgen_liste.append(
        [liste[0]]
    )  # Das Erste Element ist automatisch schon eine Teilfolge
    indexaktuelleteilfolge = 0

    for index in range(1, len(liste)):
        y1 = str(liste[index - 1])[1]
        x2 = str(liste[index])[0]
        if y1 == x2:
            pass
            # wir bleiben bei der aktuellen Teilfolgenliste
        else:
            dominoteilfolgen_liste.append([])
            indexaktuelleteilfolge += 1
            # wir beginnen eine neue Teilfolgenliste

        dominoteilfolgen_liste[indexaktuelleteilfolge].append(liste[index])

    dominoteilfolgen_liste.sort(key=len)
    print(dominoteilfolgen_liste)
    return dominoteilfolgen_liste[-1]
    # for zahl in liste:


def aufgabe7(liste, index_von, index_zu):
    """
    Finden Sie den kleinsten gemeinsamen Vielfachen zwischen Index from und to, welche
    gegeben sind.
    input: array, int , int
    output: array,
    """

    def kgV(x, z):
        """
        berechnet kgV von zwei Zahlen
        Input: int, int
        out: int
        """
        if x > z:
            x, z = z, x
        x_zähler = x
        while x_zähler <= x * z:
            if x_zähler % z == 0:
                return x_zähler
            x_zähler += x

    # hier wird nur das gewünschte Intervall der Liste dargestellt
    if index_zu != -1:
        intervall = liste[index_von : index_zu + 1]
    else:
        intervall = liste[index_von:]
    print(intervall)
    if 0 not in intervall:
        kgv_liste_temp = []
        while len(intervall) != 1:
            kgv_liste_temp.clear()
            for index in range(
                1, len(intervall)
            ):  # weil wir die hintere Zahl indexieren
                kgv_liste_temp.append(kgV(intervall[index - 1], intervall[index]))
            intervall = kgv_liste_temp.copy()
            print(intervall)
        return intervall
    else:
        return 0


if __name__ == "__main__":
    zahlenreihe = [42, 81, 18, 54]

    print("a1: ", aufgabe1(zahlenreihe))
    print("a2: ", aufgabe2(zahlenreihe))
    print("a3: ", aufgabe3(zahlenreihe))
    print("a4: ", aufgabe4(zahlenreihe, "XOR"))
    print("a5: ", aufgabe5([13, 26, 34, 10, 39, 13, 30, 21], "y=3*x"))
    print("a6: ", aufgabe6([89, 95, 54, 30, 31, 15, 58, 18, 55, 59, 99, 99, 99]))
    print("a7: ", aufgabe7([2, 40, 33, 32, 10], 1, 4))
