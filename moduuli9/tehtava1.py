
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus, matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka


def main():
    auto1 = Auto("ABC-123","142 km/h", 0, 0)

    print("Auton ominaisuudet:")
    print(f'{auto1.rekisteritunnus}, {auto1.huippunopeus}, {auto1.nopeus}, {auto1.matka}')
    return

main()

