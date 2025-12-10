class User:
    def __init__(self, nama):
        self.nama = nama
        self.umur = None

    def set_umur(self):
        while True:
            try:
                umur = int(input("Masukkan umur: "))
                if umur < 0 or umur > 120:
                    raise ValueError("Umur harus antara 0 dan 120.")
                self.umur = umur
                break
            except ValueError as e:
                print(f"Error: {str(e)}")

    def info(self):
        if self.umur is not None:
            print(f"Nama: {self.nama}")
            print(f"Umur: {self.umur}")
        else:
            print(f"Nama: {self.nama}")
            print("Umur belum diisi.")