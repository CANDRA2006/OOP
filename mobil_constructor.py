class Mobil:
    def __init__(self, merk, warna):
        self.merk = merk
        self.warna = warna
        self.kecepatan = 0 # Defaut mobil diam

    def maju(self, tambah=10):
        self.kecepatan += tambah
        print(f"{self.merk} {self.warna} maju dengan kecepatan {self.kecepatan} km/jam.")

    def mundur(self, kurang=5):
        if self.kecepatan - kurang < 0:
            self.kecepatan = 0
        else:
            self.kecepatan -= kurang
        print(f"{self.merk} {self.warna} mundur/berkurang kecepatan jadi {self.kecepatan} km/jam.")

    def berhenti(self):
        self.kecepatan = 0                                     
        print(f"{self.merk} {self.warna} berhenti.")

    def info(self):
        print(f"{self.merk} {self.warna} | kecepatan: {self.kecepatan} km/jam.")

# Contoh Penggunaan
Mobil1 = Mobil("Bugatti", "Merah")
Mobil2 = Mobil("Ford", "Hitam")

Mobil1.info()
Mobil2.info()

print("\n--- SIMULASI MOBIL 1 ---")
Mobil1.maju()
Mobil1.maju(20)
Mobil1.mundur(15)
Mobil1.berhenti()

print("\n--- SIMULASI MOBIL 2 ---")
Mobil2.maju(30)
Mobil2.mundur(10)
Mobil2.info()
