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
    muutos =(int(random.randint(-10,15)))
    auto1 = Auto("ABC-123",142, 60, 0)
    autot = []
    for i in range(10):
        kilpa_auto = Auto(f'ABC-{i+1}', random.randint(100,200),0,0)
        autot.append(kilpa_auto)

    for kilpa_auto in autot:
        print(kilpa_auto.rekisteritunnus)
        print(kilpa_auto.huippunopeus)

    while True:
        kilpa_auto.kulje(1)
        kilpa_auto.accelerate(muutos)

        for kilpa_auto in autot:
            print(kilpa_auto.matka)
   # print("Auton ominaisuudet:")
   # print(f'{auto1.rekisteritunnus}, {auto1.huippunopeus}, {auto1.nopeus} km/h, {auto1.matka} km')
    # auto1.accelerate(muutos)



main()







