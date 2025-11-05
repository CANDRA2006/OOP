class Mobil:
    def __init__(self, merk, warna):
        self.merk = merk
        self.warna = warna
        self.kecepatan = 0 # Default mobil diam 

    def maju(self, tambah=10):
        self.kecepatan += tambah
        print(f"{self.merk} {self.warna} maju dengan kecepatan {self.kecepatan} km/jam")

    def mundur(self, kurang=5):
        if  self.kecepatan - kurang < 0:
             self.kecepatan = 0
        else:
            self.kecepatan -= kurang
        print(f"{self.merk} {self.warna} mundur {self.kecepatan} km/jam")
    
    def berhenti(self):
        self.kecepatan = 0
        print(f"{self.merk} {self.warna} berhenti")

    def info(self):
        print(f"{self.merk} {self.warna} | kecepatan: {self.kecepatan} km/jam.")

# Menu input user
merk = input("Masukkan merk mobil: ")
warna = input("Masukkan warna mobil: ")
mobil = Mobil(merk, warna)

# Menu Interaktif 
while True:
    print("\n=== PILIH MENU ===")
    print("1. Maju")
    print("2. Mundur")
    print("3. Berhenti")
    print("4. Info Mobil")
    print("5. Keluar")

    pilihan = input("Pilih menu 1 - 5 = ")
    if pilihan == "1":
        tambah = int(input("Maju berapa km/jam? "))
        mobil.maju(tambah)
    if pilihan == "2":
        kurang = int(input("Mundur berapa km/jam?"))
        mobil.mundur(kurang)
    elif pilihan == "3":
        mobil.berhenti()
    elif pilihan == "4":
        mobil.info()
    elif pilihan == "5":
        print("Program Selesai")
        break
    else:
        print("Pilihan tidak valid")