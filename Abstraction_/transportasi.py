from abc import ABC, abstractmethod

class Transportasi(ABC):
    """Class abstract untuk transportasi"""
    
    @abstractmethod
    def perjalanan(self, jarak):
        """Method abstract untuk perjalanan"""
        pass

class MotorOnline(Transportasi):
    """Class untuk motor online"""
    
    def perjalanan(self, jarak):
        return f"Perjalanan {jarak} km menggunakan motor online"

class MobilOnline(Transportasi):
    """Class untuk mobil online"""
    
    def perjalanan(self, jarak):
        return f"Perjalanan {jarak} km menggunakan mobil online"

# Contoh penggunaan
if __name__ == "__main__":
    # Membuat list berisi kedua objek transportasi
    transportasi_list = [
        MotorOnline(),
        MobilOnline()
    ]
    
    # Menjalankan dengan jarak 12 km
    jarak = 12
    for transportasi in transportasi_list:
        print(transportasi.perjalanan(jarak))