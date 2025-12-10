from abc import ABC, abstractmethod

class Menu:
    def __init__(self, nama, harga):
        self.nama = nama
        self.__harga = harga # encapsulation
        self.__stok = 10 # private

    def get_harga(self):
        return self.__harga # Getter
    
    def set_harga(self, harga_baru):
        try: # Exception Handling
            harga_baru = int(harga_baru)
            if harga_baru > 0:
                self.__harga = harga_baru
            else:
                print("Harga harus lebih dari 0!")
        except ValueError:
            print("Harga harus angka!")

    def cek_stok(self):
        return self.__stok
    
    def kurangi_stok(self, jumlah):
        if jumlah <= self.__stok:
            self.__stok -= jumlah
        else:
            print("Stok tidak cukup!")

class Makanan(Menu): # Inheritance
    def hitung_total(self, qty):
        return self.get_harga() * qty

class Minuman(Menu):
      def hitung_total(self, qty):
        total = self.get_harga() * qty
        return total - (total * 0.1) # Diskon minuman 10%
      
class Pembayaran(ABC):
    @abstractmethod
    def proses(self, total, uang):
        pass

class Gopay(Pembayaran):
    def proses(self, total, uang):
        if uang < total:
            print("Saldo GoPay tidak cukup!")
        else:
            print(f"Pembayaran Rp {total} dengan GoPay berhasil!") 
            print(f"Kembalian : Rp {uang - total}")

class Shopee(Pembayaran):
    def proses(self, total, uang):
        if uang < total:
            print("Saldo Shopee tidak cukup!")
        else:
            print(f"Pembayaran Rp {total} dengan Shopee berhasil!") 
            print(f"Kembalian : Rp {uang - total}")

class QRIS(Pembayaran):
    def proses(self, total, uang):
        if uang < total:
            print("Saldo tidak cukup!")
        else:
            print(f"Pembayaran Rp {total} dengan QRIS berhasil!") 
            print(f"Kembalian : Rp {uang - total}")

try:
    ayam = Makanan("Ayam geprek", 15000)
    es_teh = Minuman("Es Teh", 3000)

    qty_ayam = int(input("Beli ayam geprek berapa? "))
    qty_teh = int(input("Beli es teh berapa? "))

    total_ayam = ayam.hitung_total(qty_ayam)
    total_teh = es_teh.hitung_total(qty_teh)
    total_semua = total_ayam + total_teh

    print("\n=== Rincian Pesanan ===")
    print(f"Ayam geprek x {qty_ayam} = Rp {total_ayam}")
    print(f"Es teh x {qty_teh} = Rp {total_teh}")
    print(f"Total bayar = Rp {total_semua}")

    # Metode bayar
    print("\nPilih Metode Pembayaran: ")
    print("1. GoPay")
    print("2. Shopee")
    print("3. QRIS")

    pilihan = input("Masukkan pilihan pembayaran (1-3): ")

    if pilihan == "1":
        pay = Gopay()
    elif pilihan == "2":
        pay = Shopee()
    elif pilihan == "3":
        pay = QRIS()
    else:
        print("Metode pembayaran tidak valid!")
        exit()

    uang = int(input("Masukkan jumlah uang membayar : "))
    pay.proses(total_semua, uang)

except ValueError:
    print("Input harus berupa angka!")