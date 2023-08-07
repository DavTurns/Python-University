import random


def userwählt():
    """
    Der Spieler wählt zwischen Schere, Stein, Papier
    output: string "schere" oder "stein" oder "papier"
    """

    möglichkeiten = ["schere", "stein", "papier"]

    eingabe = int(
        input(
            """Wählen Sie zwischen:
    1.Schere
    2.Stein
    3.Papier
    """
        )
    )

    wahl = möglichkeiten[eingabe - 1]

    with open(
        wahl + ".txt",
        "r",
    ) as f:
        print(f.read())
    return wahl


def computerwählt():
    """
    Das Programm wählt zwischen Schere, Stein, Papier
    output: string "schere" oder "stein" oder "papier"
    """

    möglichkeiten = ["schere", "stein", "papier"]

    wahl = random.choice(möglichkeiten)
    with open(wahl + ".txt") as f:
        print(f.read())
    return wahl


def comparewahl(wahluser, wahlcomputer):
    """
    Diese Funktion vergleicht die beiden inputs von Spieler1 und Computer
    output: wenn Erste wahl gewinnt -> 1
            wenn zweite Wahl gewinnt -> 2
    """

    paarwahl = [wahluser, wahlcomputer]
    if (
        paarwahl == ["schere", "papier"]
        or paarwahl == ["papier", "stein"]
        or paarwahl == ["stein", "schere"]
    ):
        return 1

    paarwahl = [wahlcomputer, wahluser]

    if (
        paarwahl == ["schere", "papier"]
        or paarwahl == ["papier", "stein"]
        or paarwahl == ["stein", "schere"]
    ):
        return 2

    else:
        return 0
