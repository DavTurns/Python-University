from functions.filefunc import *


def main(path, gesuchtstr, ersatzstr):
    """
    Diese Funktion Ersetzt in einer Datei ein gesuchtes Wort mit einem Anderen
    und gibt zurück wie oft der String ersetzt wurde
    Input: Dateipfad, gesuchter String, ersätzender String
    Output: Wie oft ersetzt wurde in int
    """

    string = readfiles(path)
    count = string.count(gesuchtstr)
    string = string.replace(gesuchtstr, ersatzstr)

    writefiles(path, string)

    print(f"{gesuchtstr} wurde {count} mal ersetzt.")
    if count == 0:
        print("Es wurde kein Wort zum Ersetzen gefunden")


if __name__ == "__main__":
    file = "meine_datei.txt"  # change to custom filepath
    main(file, "katze", "hund")
