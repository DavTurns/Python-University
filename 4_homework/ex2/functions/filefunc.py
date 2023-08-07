"""
Hier sind alle Funktionen, die was mit Files zu tun haben"""


def readfiles(path):
    """
    Die Funktion gibt den Inhalt einer Datei aus
    Input: Dateipfad (string)
    Output: Inhaltdatei (string)
    """
    with open(path) as f:
        return f.read()


def writefiles(path, string):
    """
    Diese Funktion schreibt einen String in eine Datei
    Input: Dateipfad (string), Inhalt zum schreiben (string)
    """
    with open(path, "w") as f:
        return f.write(string)
