# Latihan Object-Oriented Programming (OOP) Python

Repository ini berisi kumpulan latihan implementasi konsep OOP dalam Python, mencakup constructor, encapsulation, dan berbagai jenis inheritance.

## 📋 Daftar Isi

- [Constructor](#constructor)
- [Encapsulation](#encapsulation)
- [Inheritance](#inheritance)
  - [Single Inheritance](#single-inheritance)
  - [Multilevel Inheritance](#multilevel-inheritance)
  - [Multiple Inheritance](#multiple-inheritance)

---

## 🚗 Constructor

### 1. `mobil_constructor.py`
Program simulasi mobil dengan constructor untuk menginisialisasi atribut merk, warna, dan kecepatan.

**Fitur:**
- Inisialisasi mobil dengan merk dan warna
- Method `maju()` - menambah kecepatan
- Method `mundur()` - mengurangi kecepatan
- Method `berhenti()` - menghentikan mobil
- Method `info()` - menampilkan informasi mobil

**Contoh Penggunaan:**
```python
mobil1 = Mobil("Bugatti", "Merah")
mobil1.maju(30)
mobil1.info()
```

### 2. `constructor-car.py`
Versi interaktif dari program mobil dengan menu input user.

**Fitur:**
- Input merk dan warna dari user
- Menu interaktif untuk kontrol mobil
- Opsi: Maju, Mundur, Berhenti, Info, Keluar

### 3. `class_kucing.py`
Program simulasi virtual pet kucing dengan sistem energi.

**Fitur:**
- Sistem energi (0-100)
- Method `makan()` - menambah energi
- Method `main()` - bermain (mengurangi energi)
- Method `tidur()` - memulihkan energi
- Method `info()` - menampilkan status kucing
- Menu interaktif untuk berinteraksi dengan kucing

---

## 🔒 Encapsulation

### `encapsulation.py`
Demonstrasi konsep encapsulation menggunakan atribut private (double underscore `__`).

**Contoh yang Diimplementasikan:**

1. **Class Mahasiswa** (commented)
   - Atribut private: `__nilai`
   - Getter: `tampilkan_nilai()`
   - Setter dengan validasi: `ubah_nilai()`

2. **Class Mahasiswa dengan Getter/Setter** (commented)
   - Setter: `set_nama()`, `set_nilai()`
   - Getter: `get_nama()`, `get_nilai()`
   - Validasi nilai 0-100

3. **Class Pegawai** (active)
   - Atribut private: `__nama`, `__gaji`
   - Validasi gaji minimum 2.000.000
   - Getter dan Setter methods

**Konsep yang Dipelajari:**
- Private attributes (`__variable`)
- Data validation
- Getter dan Setter methods
- Data protection

---

## 🔗 Inheritance

### Single Inheritance

#### `inheritance.py`
Implementasi dasar single inheritance dengan class `Manusia` sebagai parent dan `Mahasiswa` sebagai child.

**Fitur:**
- Parent class: `Manusia` dengan method `bicara()`
- Child class: `Mahasiswa` dengan method tambahan `belajar()`
- Inheritance method dari parent ke child

#### `single_inheritance2.py`
Single inheritance dengan atribut tambahan menggunakan `super()`.

**Fitur:**
- Penggunaan `super().__init__()` untuk override constructor
- Atribut tambahan di child class: `nim`, `prodi`
- Demonstrasi method overriding

---

### Multilevel Inheritance

#### `multilevel_inheritance.py`
Inheritance bertingkat: Manusia → Mahasiswa → Asdos

**Hierarki:**
```
Manusia (bicara)
    ↓
Mahasiswa (belajar)
    ↓
Asdos (mengajar)
```

**Fitur:**
- 3 level inheritance
- Penggunaan `super()` untuk memanggil constructor parent
- Setiap level menambahkan atribut dan method baru

---

### Multiple Inheritance

#### `multiple_inheritance.py`
Inheritance dari multiple parent classes.

**Struktur:**
```
Manusia (nama, bicara)    Mahasiswa (nim, belajar)
              ↓                    ↓
                    Asdos
              (mengajar mata kuliah)
```

**Fitur:**
- Inheritance dari 2 parent class
- Manual constructor call untuk setiap parent
- Kombinasi method dari multiple parents

---

## 🚀 Cara Menjalankan

Pastikan Python 3.x sudah terinstall, kemudian jalankan file sesuai kebutuhan:

```bash
# Constructor
python mobil_constructor.py
python constructor-car.py
python class_kucing.py

# Encapsulation
python encapsulation.py

# Inheritance
python inheritance.py
python single_inheritance2.py
python multilevel_inheritance.py
python multiple_inheritance.py
```

---


## 📝 Catatan

- Beberapa code dalam `encapsulation.py` di-comment untuk menunjukkan berbagai pendekatan
- Program interaktif memerlukan input dari user
- Validasi input sudah diimplementasikan untuk mencegah error

---

## 🤝 Kontribusi

Silakan fork repository ini dan eksperimen dengan code untuk pembelajaran lebih lanjut!

---

**Happy Coding! 🐍✨**
