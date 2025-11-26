from abc import ABC, abstractmethod

class PetugasRS(ABC):
    """Class abstract untuk petugas rumah sakit"""
    
    @abstractmethod
    def kerja(self):
        """Method abstract untuk pekerjaan"""
        pass

class Perawat(PetugasRS):
    """Class untuk perawat"""
    
    def kerja(self):
        return "Merawat pasien di ruang perawatan"

class Dokter(PetugasRS):
    """Class untuk dokter"""
    
    def kerja(self):
        return "Melakukan pemeriksaan terhadap pasien"

class PetugasLab(PetugasRS):
    """Class untuk petugas laboratorium"""
    
    def kerja(self):
        return "Melakukan tes laboratorium"

# Program Utama
if __name__ == "__main__":
    # Membuat list berisi objek ketiga class
    petugas_list = [
        Perawat(),
        Dokter(),
        PetugasLab()
    ]
    
    # Menggunakan perulangan untuk memanggil method kerja()
    for petugas in petugas_list:
        print(petugas.kerja())