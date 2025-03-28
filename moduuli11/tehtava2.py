import random

def main():
    class Auto:
        def __init__(self, rekisteritunnus, huippunopeus, nopeus, matka):
            self.rekisteritunnus = rekisteritunnus
            self.huippunopeus = huippunopeus
            self.nopeus = nopeus
            self.matka = matka

        def accelerate(self, muutos):
            self.nopeus += muutos

            if self.nopeus > self.huippunopeus:
                    self.nopeus = self.huippunopeus

            elif self.nopeus <= 0:
                    self.nopeus = 0

        def kulje(self, time):
            self.matka += time * self.nopeus

    class Sahkoauto(Auto):
        def __init__(self, rekisteritunnus, huippunopeus, nopeus, matka, akkukapasiteetti):
            self.akkukapasiteetti = akkukapasiteetti
            super().__init__(rekisteritunnus, huippunopeus, nopeus, matka)
    class  Polttomoottoriauto(Auto):
        def __init__(self, rekisteritunnus, huippunopeus, nopeus, matka, bensatankki):
            self.bensatankki = bensatankki
            super().__init__(rekisteritunnus, huippunopeus, nopeus, matka)



    sahko = Sahkoauto("ABC-15", 180, 115, 0, 52.5)
    poltto = Polttomoottoriauto("ACD-123", 165, 150, 0, 32.3)

    sahko.kulje(3)
    poltto.kulje(3)

    print(f'Sähköauton mittarilukema: {sahko.matka} km')
    print(f'Polttomoottoriauton mittarilukema: {poltto.matka} km')

main()







