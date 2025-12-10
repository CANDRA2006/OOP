class Gitar:
    def mainkan(self):
        print("Gitar dipetik... jreng!")


class Piano:
    def mainkan(self):
        print("Piano dimainkan... ting ting!")


class Drum:
    def mainkan(self):
        print("Drum dipukul... dum dum!")

gitar = Gitar()
piano = Piano()
drum = Drum()

alat_musik = [gitar, piano, drum]

print("=== Memainkan Alat Musik ===\n")
for alat in alat_musik:
    alat.mainkan()