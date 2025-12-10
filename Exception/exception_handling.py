# class Mahasiswa:
#     def __init__(self, nama):
#         self.nama = nama
#         self.__nilai = None

#     def set_nilai(self):
#         try:
#             nilai = int(input(f"Masukkan nilai untuk {self.nama}: "))
#             if 0 <= nilai <= 100:
#                 self.__nilai = nilai
#                 print("Nilai berhasil disimpan!")
#             else:
#                 print("Nilai harus antara 0-100")
#         except ValueError:
#             print("Input harus berupa angka!")

#     def get_nilai(self):
#         return self.__nilai

# # Penggunaan
# m1 = Mahasiswa("Candra")
# m1.set_nilai()
# print("Nilai akhir: ", m1.get_nilai())

# class Produk:
#     def __init__(self, nama, harga):
#         self.nama = nama
#         self.harga = harga

#     def update_harga(self):
#         try:
#             harga_baru = int(input(f"Update harga untuk {self.nama}: "))
#             if harga_baru <= 0:
#                 print("Harga harus lebih dari 0!")
#             else:
#                 self.harga = harga_baru
#                 print("Harga baru berhaasil diupdate")
#         except ValueError:
#             print("Harga harus berupa angka!")

# # Penggunaan
# p = Produk("Dompet", 200000)
# p.update_harga()
# print("Harga sekarang", p.harga)

from abc import ABC, abstractmethod

class Bank(ABC):
    @abstractmethod
    def tarik(self, jumlah):
        pass

class BRI(Bank):
    def __init__(self, saldo):
        self.saldo = saldo

    def tarik(self, jumlah):
        try:
            jumlah = int(jumlah)
            if jumlah <= 0:
                print("Jumlah harus positif!")
            elif jumlah > self.saldo:
                print("Saldo tidak cukup")
            else:
                self.saldo -= jumlah
                print("Penarikan berhasil!")
        except ValueError:
            print("Jumlah harus berupa angka")

class BCA(Bank):
    def __init__(self, saldo):
        self.saldo = saldo

    def tarik(self, jumlah):
        try:
            jumlah = int(jumlah)
            if jumlah <= 0:
                print("Jumlah harus positif!")
            elif jumlah > self.saldo:
                print("Saldo tidak cukup")
            else:
                self.saldo -= jumlah
                print("Penarikan berhasil!")
        except ValueError:
            print("Jumlah harus berupa angka")

# Polymorphism
banks = [BRI (1000000), BCA(5000000)]

for bank in banks:
    bank.tarik(input("Masukkan jumlah penarikan: "))
    print("Saldo tersisa: ", bank.saldo)