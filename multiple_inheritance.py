#Multiple Inheritance
class Manusia:
    def __init__(self, nama):
        self.nama = nama

    def bicara(self):
        print(f"Halo nama saya {self.nama}")

class Mahasiswa:
    def __init__(self, nim):
        self.nim = nim

    def belajar(self):
        print(f"Mahasiswa dengan NIM {self.nim} sedang belajar")

class Asdos(Manusia, Mahasiswa): # Child
    def __init__(self, nama, nim, mata_kuliah):
        Manusia.__init__(self, nama) # Panggil Constructor Manusia
        Mahasiswa.__init__(self, nim) # Panggil Constructor Mahasiswa
        self.mata_kuliah = mata_kuliah

    def mengajar(self):
        print(f"{self.nama} dengan NIM {self.nim} mengajar Mata Kuliah {self.mata_kuliah} ")

asdos = Asdos("Candra", "60324042", "Kalkulus")

asdos.bicara()
asdos.belajar()
asdos.mengajar()