def main():
    class Hissi:
        def __init__(self, kerros, high, low):
            self.kerros = kerros
            self.high = high
            self.low = low

        def siirry_kerrokseen(self, uusi_kerros):

            for i in self.high:


                if uusi_kerros > self.kerros and self.kerros < self.high:
                    self.up()
                elif uusi_kerros < self.kerros and self.kerros > self.low:
                    self.down()
                else:
                    return


        def up(self):
            self.kerros = self.kerros + 1
            print(f'Hissin uusi kerros: {self.kerros}')

        def down(self):
            self.kerros = self.kerros - 1
            print(f'Hissin uusi kerros: {self.kerros}')

    class Talo:
        def __init__(self, hissikpl, high, low):
            self.hissikpl = hissikpl
            self.high = high
            self.low = low
            self.hissit = []
        def luonti(self, hissikpl):
            for i in range(hissikpl):
                self.hissit.append(i+1)
        def aja(self):
            

    t = Talo(5,10,1)
    t.luonti(t.hissikpl)
    print(t.hissit)

    t = Talo


main()
