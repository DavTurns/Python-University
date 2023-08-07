"""
Hier sind alle Funktionen, die den dictionary beeinflussen
"""


def readfile(dictpath):
    """
    ließt string aus einer Datei
    BEM: Datei soll nur eine Zeile haben
    input: (type str) Pfad der Datei, wo der dictionary liegt
    output: (type str) Inhalt der Datei
    """
    with open(dictpath, "r") as f:
        return f.read()


def overwritedict(dictpath, dict):
    """
    Diese Funktion schreibt einen dict als string in eine Datei
    Input: Dateipfad (string), Wörterbuch (dict)
    Output:
    """
    string = str(dict)
    with open(dictpath, "w") as f:
        f.write(string)
