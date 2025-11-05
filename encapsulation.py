# class Mahasiswa:
#     def __init__(self, nama , nilai):
#         self.nama = nama      # Public
#         self.__nilai = nilai  # Privat/Encapsulation

#     def tampilkan_nilai(self):
#         print(f"Nilai {self.nama} adalah {self.__nilai}")

#     def ubah_nilai(self, nilai_baru):
#         if 0 <= nilai_baru <= 100:
#             self.__nilai = nilai_baru
#             print(f"Nilai berhasil diubah")
#         else:
#             print(f"Nilai tidak valid! ")

# # Penggunaan
# mhs1 = Mahasiswa("Yamal", 90)

# mhs1.tampilkan_nilai()
# mhs1.__nilai = 50 # Tidak akan merubah nilai
# mhs1.tampilkan_nilai() # Nilai tetap 90

# mhs1.ubah_nilai(100) #  Ubah nilai lewat Method
# mhs1.tampilkan_nilai()

# class Mahasiswa:
#     def __init__(self):
#         self.__nama = "" # Encapsulation/Private
#         self.__nilai = 0  # Encapsulation/Private

#     def set_nama(self, nama):
#         self.__nama = nama
    
#     def set_nilai(self, nilai):
#         if 0 <= nilai <= 100: # Private 
#             self.__nilai = nilai
#         else:
#             print("Nilai tidak valid!")
    
#     def get_nama(self):
#         return self.__nama
    
#     def get_nilai(self):
#         return self.__nilai
    
# # Penggunaan
# mhs1 = Mahasiswa()
# mhs1.set_nama("Pedri")
# mhs1.set_nilai(100)

# print("Nama: ", mhs1.get_nama())
# print("Nilai: ", mhs1.get_nilai())

class Pegawai:
    def __init__(self):
        self.__nama = ""
        self.__gaji = 0

    def set_nama(self, nama):
        self.__nama = nama

    def set_gaji(self, gaji):
        if gaji >= 2000000:
            self.__gaji = gaji
        else:
            print("Gaji kecil")

    def get_nama(self):
        return self.__nama

    def get_gaji(self):
        return self.__gaji

# Buat objek 
pgw1 = Pegawai()

# Tetapkan nama dan gaji awal
pgw1.set_nama("Verdonk")
pgw1.set_gaji(3500000)

# Cetak nama dan gaji
print("Nama:", pgw1.get_nama())
print("Gaji:", pgw1.get_gaji())

# Ubah gaji menjadi 1.000.000
pgw1.set_gaji(1000000)

# Cetak gaji yang diperbarui
print("Gaji Diperbarui:", pgw1.get_gaji())