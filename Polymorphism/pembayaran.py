# 1. Kelas Induk (Antarmuka Dasar)
class MetodePembayaran:
    def proses_pembayaran(self, jumlah):
        # Ini adalah metode "abstrak" yang harus diimplementasikan oleh kelas anak
        raise NotImplementedError("Setiap metode pembayaran harus mengimplementasikan proses_pembayaran.")

# 2. Kelas Anak: Kartu Kredit
class KartuKredit(MetodePembayaran):
    def __init__(self, nomor, cvv):
        self.nomor = nomor
        self.cvv = cvv

    def proses_pembayaran(self, jumlah):
        # Logika spesifik untuk memproses kartu kredit
        print(f"💳 Memproses pembayaran Kartu Kredit sebesar Rp{jumlah:,.2f}...")
        # (Tambahkan logika otorisasi kartu, dll. di sini)
        return True

# 3. Kelas Anak: PayPal
class PayPal(MetodePembayaran):
    def __init__(self, email):
        self.email = email

    def proses_pembayaran(self, jumlah):
        # Logika spesifik untuk memproses PayPal
        print(f"🅿️ Memproses pembayaran PayPal sebesar Rp{jumlah:,.2f} untuk akun {self.email}...")
        return True

# 4. Kelas Anak: Transfer Bank
class TransferBank(MetodePembayaran):
    def __init__(self, nama_bank):
        self.nama_bank = nama_bank

    def proses_pembayaran(self, jumlah):
        # Logika spesifik untuk memproses Transfer Bank
        print(f"🏦 Memproses pembayaran Transfer Bank ({self.nama_bank}) sebesar Rp{jumlah:,.2f}...")
        # (Tambahkan logika pembuatan kode transfer, dll. di sini)
        return True

# 5. Fungsi Utama untuk Menggunakan Sistem
def lakukan_transaksi(metode, jumlah_transaksi):
    print("\n--- Transaksi Baru Dimulai ---")
    if metode.proses_pembayaran(jumlah_transaksi):
        print("✅ Transaksi Berhasil.")
    else:
        print("❌ Transaksi Gagal.")
    print("------------------------------")

# Membuat objek-objek pembayaran
kartu = KartuKredit("1234-5678-9012-3456", "456")
paypal = PayPal("user@email.com")
bank = TransferBank("BCA")

# Melakukan transaksi menggunakan objek yang berbeda
lakukan_transaksi(kartu, 500000.00)
lakukan_transaksi(paypal, 125000.50)
lakukan_transaksi(bank, 75000.00)