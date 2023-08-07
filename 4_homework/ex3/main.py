"""
info: the user should be located in same path when running main.py
      the game is rock scissor paper
"""

from functions.wahlfunc import userwählt, comparewahl, computerwählt
from functions.printfunc import zwischenstand


def main():
    userscore = 0
    computerscore = 0

    while userscore < 2 and computerscore < 2:
        wahluser = userwählt()
        print(f"Ihre wahl ist {wahluser}")

        wahlcomputer = computerwählt()
        print(f"Das Programm wählt {wahlcomputer}")

        gewinner = comparewahl(wahluser, wahlcomputer)

        match gewinner:
            case 1:
                userscore += 1
                print("Du gewinnst einen Punkt")
                zwischenstand(userscore, computerscore)

            case 2:
                computerscore += 1
                print("Das Programm gewinnt ein Punkt")
                zwischenstand(userscore, computerscore)

            case 0:
                print("Keiner gewinnt")
                zwischenstand(userscore, computerscore)

        print("")

    if userscore == 2:
        print("DU HAST GEWONNEN")

    else:
        print("DU HAST VERLOREN")


if __name__ == "__main__":
    main()
