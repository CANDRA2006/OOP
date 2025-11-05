# Single Inheritance
class Manusia: # Parent
    def __init__(self, nama):
        self.nama = nama

    def bicara(self):
        print(f"Halo, nama saya {self.nama}")

class Mahasiswa(Manusia): # Child 
    def belajar(self):
        print(f"{self.nama} sedang belajar")

mhs = Mahasiswa("Candra")

mhs.bicara()
mhs.belajar() 

class Manusia:
    def __init__(self, nama):
        self.nama = nama

    def bicara(self):
        print(f"Halo nama saya {self.nama}")

class Mahasiswa:
    def __init__(self, nama):
        self.nama = nama

    def bicara(self):
        print(f"Halo nama saya {self.nama}")

    def belajar(self):
        print(f"{self.nama} sedang belajar")

mhs = Mahasiswa("Candra")

mhs.bicara()
mhs.belajar()




