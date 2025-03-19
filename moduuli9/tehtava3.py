



def main():
    class Auto:
        def __init__(self, rekisteritunnus, huippunopeus, nopeus, matka):
            self.rekisteritunnus = rekisteritunnus
            self.huippunopeus = huippunopeus
            self.nopeus = nopeus
            self.matka = matka

        def accelerate(self, muutos):
            for i in muutos:

                self.nopeus += i

                if self.nopeus > self.huippunopeus:
                    self.nopeus = self.huippunopeus

                elif self.nopeus <= 0:
                    self.nopeus = 0


                if auto1.nopeus >= 142:
                    print(f'Auton tämänhetkinen nopeus: {auto1.nopeus} km/h')

        def kulje(self, time):
            self.matka += time * self.nopeus
    muutos =(30,70,50,-200)
    auto1 = Auto("ABC-123",142, 60, 2000)

    print("Auton ominaisuudet:")
    print(f'{auto1.rekisteritunnus}, {auto1.huippunopeus}, {auto1.nopeus} km/h, {auto1.matka} km')

    # auto1.accelerate(muutos)
    print(f'Auton tämänhetkinen nopeus: {auto1.nopeus} km/h')
    print(f'Auton kuljettu matka ennen: {auto1.matka} km')
    auto1.kulje(1.5)
    print(f'Auton kuljettu matka jälkeen: {auto1.matka:.0f} km')

    return

main()







