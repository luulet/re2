def main():
    class Hissi:
        def __init__(self, kerros, high, low):
            self.kerros = kerros
            self.high = high
            self.low = low

        def siirry_kerrokseen(self, uusi_kerros):

            for i in self.high:


                if uusi_kerros > self.kerros and self.kerros < self.high:
                    h.up()
                elif uusi_kerros < self.kerros and self.kerros > self.low:
                    h.down()
                else:
                    return


        def up(self):
            self.kerros = self.kerros + 1
            print(f'Hissin uusi kerros: {self.kerros}')

        def down(self):
            self.kerros = self.kerros - 1
            print(f'Hissin uusi kerros: {self.kerros}')

    h = Hissi(1, 10, 1)
    print(f'Hissin kerros: {h.kerros}')
    h.siirry_kerrokseen(5)
    h.siirry_kerrokseen(1)

main()
