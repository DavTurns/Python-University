"""
Hier sind alle Funktionen, die was mit UI zu tun haben
"""


def eingangmenu():
    print(
        """
    Geben Sie die Nummer vom Programm ein, welches Sie ausführen wollen:
        
        Bestellung:
            1.Neue Bestellung erstellen

        Speisekarte bearbeiten:
            2.Gericht hinzufügen
            3.Informationen Gericht lesen
            4.Gericht aktualisieren
            5.Gericht löschen

        Kundenliste bearbeiten:
            6.Neuen Kunden hinzufügen
            7.Kundendaten lesen
            8.Kundendaten aktualisieren
            9.Kunde löschen
    
    """
    )
    return eingabe()


# ---------------UImethoden von bestellung-----------------------
def auswahlkunde():
    print(
        """
    1.Bestellung auf neuen Kunden machen
    2.Bestellung auf bestehenden Kunden machen
    """
    )
    return eingabe()


def gericht_hinzufügen_bestellung():
    print(
        """Geben Sie die ID des gewünschten Gerichts ein.
            Drücken Sie NUR ENTER wenn Sie keine weiteren Gerichte hinzufügen wollen! 
            """
    )


def gericht_hinzufügen_bestellung_wie_oft():
    print(
        """Wie oft wollen Sie dieses Gericht bestellen?
    """
    )


def kundendaten_eingeben():
    print(
        """\nGeben Sie die Kundendaten unter folgendem Format wieder:
    Beispiel: Max Mustermann,Frankfurterstr. 5

    """
    )
    return eingabe()


def suchdaten_eingeben(gesuchtes):
    """
    input: str Was für ein typ ist gesucht. z.B Kunde
    output: str eingegebene Daten
    """
    print(
        f"""{gesuchtes} suchen (wenn möglich, Angaben so präzise wie möglich machen) 
    
    """
    )
    return eingabe()


def gerichtsorte_wählen():
    print(
        """
    Wählen Sie die Gerichtsorte:
    1.Essen
    2.Getränk
    
    """
    )
    return eingabe()


def gerichtdaten_eingeben():
    print(
        """\nGeben Sie die Gerichtsinformationen unter folgendem Format wieder:
    Gerichtname,Preis(in €),Portionsgröße(in g),Zubereitungszeit(in min) (Als Mengenangaben bitte nur Zahlen nennen)
    Beispiel: Pizza Salami,25.50,350,30
    
    """
    )
    return eingabe()


def getränkedaten_eingeben():
    print(
        """\nGeben Sie die Getränkeinformationen unter folgendem Format wieder:
    GetränkeName,Preis(in €),Portionsgröße(in ml),Alkoholgehalt(in %) (Als Mengenangaben bitte nur Zahlen nennen)
    Beispiel: Bier,2.50,500,4.9
    
    """
    )
    return eingabe()


def id_aus_karte_wählen(karte_als_string):
    print(
        f"""
    Wähle durch Eingabe von ID aus folgendem Menu:
    {karte_als_string}
    
    """
    )
    return eingabe()


def eingabe():
    return str(input("Eingabe:"))


# ------------Informierende Funktionen----------------------
# folgende Funktionen geben nur informationen und haben keinen Returnwert


def weiter():
    input(
        """
    
    weiter (drücke ENTER)"""
    )


def normalprint(inhalt):
    print(inhalt)


def karten_anzeigen(speisekarte, getränkekarte):
    print(
        f"""
    Speisen:

    {speisekarte}
    
    Getränke:

    {getränkekarte}

    """
    )


def nichtgefunden(wo, eingabe):
    print(f"wir haben in der Datenbank {wo}, keinen Eintrag zu: {eingabe}")


def gefunden(wo, eingabe, was):
    print(
        f"""
        Erfolg!

    Ihre Eingabe hat in der Datenbank '{wo}' einen Eintrag zu '{eingabe}' gefunden"""
    )
    kundeninformationen(was)


def mehrere_ergebnisse(wo, eingabe, liste):
    print(
        """
    Es wurden mehrere Ergebnisse gefunden.
    """
    )

    for Kunde in liste:
        kundeninformationen(Kunde)
    print("Geben Sie den vollständigen Namen ein!")


def kundeninformationen(Kunde):
    print(f"{Kunde.id} {Kunde.name} {Kunde.adresse}")


def info_gelöscht(Eintrag):
    print(f"{Eintrag} wurde gelöscht")


def info_erfolgreichgeändert(Eintrag):
    print(f"{Eintrag} wurde erfolgreich geändert")
