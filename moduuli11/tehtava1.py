class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi
    def tulosta_tiedot(self):
        print(f'Nimi: {self.nimi}')
class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivu):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivu = sivu
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f'Kirjoittaja: {self.kirjoittaja}')
        print(f'Sivumäärä: {self.sivu}')


class Lehti(Julkaisu):
    def __init__(self, nimi, toimittaja):
        super().__init__(nimi)
        self.toimittaja = toimittaja
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f'Toimittaja: {self.toimittaja}')

akuankka = Lehti("Aku Ankka", "Aki Hyyppä")
hytti = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

akuankka.tulosta_tiedot()
print('')
hytti.tulosta_tiedot()