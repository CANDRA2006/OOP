from abc import ABC, abstractmethod
class Pembayaran(ABC): #class abstract
    @abstractmethod 
    def proses_pembayaran(self):
        pass

class KartuDebit(Pembayaran): # Hierarchical inheritance
    def proses_pembayaran(self, jumlah):
        print(f"Pembayaran sebesar Rp {jumlah} dengan kartu debit berhasil")

class GoPay(Pembayaran):
    def proses_pembayaran(self, jumlah):
        print(f"Pembayaran sebesar Rp {jumlah} dengan GoPay berhasil")

class ShopeePay(Pembayaran):
    def proses_pembayaran(self, jumlah):
        print(f"Pembayaran sebesar Rp {jumlah} dengan ShopeePay berhasil")

# Penggunaan 
p1 = KartuDebit()
p2 = GoPay()
p3 = ShopeePay()

print("=== Status Pembayaran ===")
for p in [p1, p2, p3]:
    p.proses_pembayaran(90000)