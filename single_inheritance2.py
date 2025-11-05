# Single inheritance dangan atribut tambahan
class Manusia: # Parent
    def __init__(self, nama):
        self.nama = nama

    def bicara(self):
        print(f"Halo nama saya {self.nama}")

class Mahasiswa(Manusia): # Child
    def __init__(self, nama, nim, prodi) :
        super().__init__(nama) # Override
        self.nim = nim
        self.prodi = prodi

    def belajar(self):
        print(f"Mahasiswa dengan nama {self.nama} dan NIM {self.nim} dari prodi {self.prodi} sedang belajar")

mhs = Mahasiswa("Candra","60324042", "Informatika")

mhs.bicara()
mhs.belajar()