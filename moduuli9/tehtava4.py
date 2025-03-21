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

    autot = []
    for i in range(10):
        kilpa_auto = Auto(f'ABC-{i+1}', random.randint(100,200),0,0)
        autot.append(kilpa_auto)

    flag = True
    while flag:

        for kilpa_auto in autot:
            kilpa_auto.kulje(1)
            kilpa_auto.accelerate(muutos =(int(random.randint(-10,15))))
            if kilpa_auto.matka >= 10000:
                print(f'Auto {kilpa_auto.rekisteritunnus} pääsi maaliin!')
                flag = False
    autot.sort(key=lambda a: a.matka, reverse=True)
    taulukko = f"""x-------------------------------------------------------------x
| Rekkari | Huippunopeus | Lopullinen nopeus | Kuljettu matka |"""
    taulukko2 = f"x-------------------------------------------------------------x"
    print(taulukko)

    for kilpa_auto in autot:
            print(f'| {kilpa_auto.rekisteritunnus}   | {kilpa_auto.huippunopeus} km/h     | {kilpa_auto.nopeus} km/h            | {kilpa_auto.matka} km      |')

    print(taulukko2)

    # taulukko voisi olla hienompi




main()







