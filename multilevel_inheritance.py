# Multilevel Inheritance
class Manusia:
    def __init__(self, nama):
        self.nama = nama

    def bicara(self):
        print(f"Nama saya {self.nama}")

class Mahasiswa(Manusia):
    def __init__(self, nama, nim):
        super().__init__(nama)
        self.nim = nim

    def belajar(self):
        print(f"Mahasiswa dengan nama {self.nama} dan NIM {self.nim} sedang belajar")

class Asdos(Mahasiswa):
    def __init__(self, nama, nim, mata_kuliah):
        super().__init__(nama, nim)
        self.mata_kuliah = mata_kuliah

    def mengajar(self):
        print(f"Mahasiswa dengan nama {self.nama} dan NIM {self.nim} sedang mengajar {self.mata_kuliah}")


asdos = Asdos("Candra", "1234", "Pemrograman")
asdos.bicara()
asdos.belajar()
asdos.mengajar()
