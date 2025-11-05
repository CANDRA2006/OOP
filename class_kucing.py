class Kucing:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
        self.energi = 50  # Default energi 50 dari 100

    def makan(self, porsi=10):
        self.energi += porsi
        if self.energi > 100:
            self.energi = 100
        print(f"{self.nama} makan. Energi sekarang {self.energi}/100")

    def main(self, lama=15):
        if self.energi - lama < 0:
            print(f"{self.nama} terlalu lelah untuk bermain")
        else:
            self.energi -= lama
            print(f"{self.nama} bermain. Energi sekarang {self.energi}/100")

    def tidur(self, jam=1):
        pulih = jam * 20
        self.energi += pulih
        if self.energi > 100:
            self.energi = 100
        print(f"{self.nama} tidur {jam} jam. Energi sekarang {self.energi}/100")

    def info(self):
        print(f"Kucing {self.nama}, Umur: {self.umur} tahun. Energi: {self.energi}/100")

# MENU INTERAKTIF
nama_kucing = input("Masukkan nama kucing: ")
umur_kucing = int(input("Masukkan umur kucing (tahun): "))
kucing = Kucing(nama_kucing, umur_kucing)

while True:
    print("\n=== MENU ===")
    print("1. Info Kucing")
    print("2. Makan")
    print("3. Main")
    print("4. Tidur")
    print("5. Keluar")

    pilihan = input("Pilih aksi (1-5): ")

    if pilihan == "1":
        kucing.info()
    elif pilihan == "2":
        porsi = int(input("Masukkan porsi makan: "))
        kucing.makan(porsi)
    elif pilihan == "3":
        lama = int(input("Masukkan lama bermain (menit): "))
        kucing.main(lama)
    elif pilihan == "4":
        jam = int(input("Masukkan lama tidur (jam): "))
        kucing.tidur(jam)
    elif pilihan == "5":
        print("Program Selesai")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")

            