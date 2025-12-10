# Kelas Induk (Parent Class)
class Hewan:
    def buat_suara(self):
        raise NotImplementedError("Subclass harus mengimplementasikan metode abstrak ini")

# Kelas Anak (Child Class)
class Anjing(Hewan):
    def buat_suara(self):
        return "Guk! Guk!"

# Kelas Anak (Child Class)
class Kucing(Hewan):
    def buat_suara(self):
        return "Meong! Meong!"

# Kelas Anak (Child Class)
class Bebek(Hewan):
    def buat_suara(self):
        return "Kwek! Kwek!"

# Fungsi untuk mendemonstrasikan polimorfisme
def cetak_suara(hewan):
    # Metode yang sama (buat_suara) dipanggil pada objek yang berbeda,
    # dan menghasilkan hasil yang berbeda.
    print(f"Hewan ini bersuara: {hewan.buat_suara()}")

# Membuat objek dari kelas-kelas yang berbeda
obyek_anjing = Anjing()
obyek_kucing = Kucing()
obyek_bebek = Bebek()

print("--- Demonstrasi Polimorfisme ---")
cetak_suara(obyek_anjing)
cetak_suara(obyek_kucing)
cetak_suara(obyek_bebek)