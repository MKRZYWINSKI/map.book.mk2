class User:
    def __init__(self,imie,nazwisko,posty,miejscowosc):
        self.imie=imie
        self.nazwisko=nazwisko
        self.posty=posty
        self.miejscowosc=miejscowosc





zmienna_w_pamięci_na_użytkownika_1=User(imie='kacper',nazwisko='Macioch',posty='996969',miejscowosc='Ząbki')
zmienna_w_pamięci_na_użytkownika_2=User(imie='dominik',nazwisko='Macioch',posty='996969',miejscowosc='Ząbki')
print(zmienna_w_pamięci_na_użytkownika_2.imie)
print(zmienna_w_pamięci_na_użytkownika_1.imie)