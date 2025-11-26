class AlatMusik: 
    def mainkan(self):
        pass


class Gitar(AlatMusik):
    def mainkan(self):
        print("Gitar dipetik... jreng!")


class Piano(AlatMusik):
    def mainkan(self):
        print("Piano dimainkan... ting ting!")


class Drum(AlatMusik):
    def mainkan(self):
        print("Drum dipukul... dum dum!")


gitar = Gitar()
piano = Piano()
drum = Drum()

alat_musik = [gitar, piano, drum]

print("=== Memainkan Alat Musik ===\n")
for alat in alat_musik:
    alat.mainkan()