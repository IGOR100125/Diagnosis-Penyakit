# 🩺 Program Diagnosis Penyakit Melalui Relasi Gejala

Program Diagnosis Penyakit Melalui Relasi Gejala merupakan aplikasi berbasis **Python** yang dirancang untuk membantu proses identifikasi penyakit berdasarkan gejala yang dipilih oleh pengguna. Sistem ini menerapkan konsep relasi antara **gejala** dan **penyakit**, sehingga dapat memberikan hasil diagnosis secara otomatis berdasarkan data yang tersedia.

Aplikasi memiliki dua jenis pengguna, yaitu **Admin** dan **Pasien**, yang masing-masing memiliki hak akses berbeda. Selain melakukan diagnosis, sistem juga mengelola data pasien serta mengubah data hasil diagnosis ke dalam format **JSON** dan **CSV** agar dapat dianalisis lebih lanjut menggunakan **Pandas DataFrame**.

---

# 📌 Fitur Utama

## 👨‍💼 Admin

Admin memiliki akses penuh terhadap sistem, di antaranya:

* Menambahkan data pasien
* Mengubah data pasien
* Menghapus data pasien
* Melihat seluruh data pasien
* Melakukan analisis hasil diagnosis
* Mengelola data penyakit dan gejala
* Mengekspor data ke format JSON dan CSV

## 🧑‍⚕️ Pasien

Pasien dapat menggunakan sistem untuk melakukan diagnosis penyakit dengan cara:

* Mengisi identitas pasien
* Memilih gejala yang dialami
* Mendapatkan hasil diagnosis penyakit
* Data pasien otomatis disimpan ke dalam sistem

---

# 🔄 Alur Sistem

1. Pengguna memilih jenis akun (**Admin** atau **Pasien**).

2. Jika masuk sebagai **Pasien**:

   * Mengisi identitas diri.
   * Memilih gejala yang dirasakan.
   * Sistem mencocokkan gejala dengan basis pengetahuan.
   * Sistem menampilkan hasil diagnosis.
   * Data pasien disimpan.

3. Jika masuk sebagai **Admin**:

   * Login ke sistem.
   * Mengelola data pasien (Create, Read, Update, Delete).
   * Melakukan analisis data diagnosis.
   * Mengekspor data menjadi JSON dan CSV.

4. Data yang tersimpan kemudian diproses menjadi:

   * **JSON** sebagai format pertukaran data.
   * **CSV** sebagai dataset.

5. Dataset CSV kemudian dapat dibaca menggunakan **Pandas DataFrame** untuk proses analisis data, visualisasi, maupun pengolahan lanjutan.

---

# 🏗️ Arsitektur Sistem

```text
Pasien
   │
   ▼
Input Identitas + Gejala
   │
   ▼
Relasi Gejala ↔ Penyakit
   │
   ▼
Hasil Diagnosis
   │
   ▼
Database/Data Penyimpanan
   │
   ├────────► JSON
   │
   └────────► CSV
                    │
                    ▼
            Pandas DataFrame
                    │
                    ▼
             Analisis Data
```

---

# 📂 Struktur Proyek

```text
Diagnosis-Penyakit/
│
├── data/
│   ├── data_pasien.json
│   ├── data_pasien.csv
│   ├── dataPasienDummy.py
│   └── diagnosisPenyakit.py
│
├── admin/
│   ├── admin
│
├── pasien/
│   └── main.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

# 💻 Teknologi yang Digunakan

* Python
* JSON
* CSV
* Pandas
* DataFrame
* NumPy *(opsional)*
* Tkinter *(jika menggunakan GUI)*
* CustomTkinter *(jika menggunakan GUI modern)*

---

# 📊 Pengolahan Data

Setelah proses diagnosis selesai, seluruh data pasien akan disimpan ke dalam sistem.

Selanjutnya sistem melakukan proses:

```
Data Pasien
      │
      ▼
JSON
      │
      ▼
CSV
      │
      ▼
Pandas DataFrame
      │
      ▼
Manipulasi Data
```

Dengan menggunakan **Pandas DataFrame**, data dapat diproses untuk berbagai kebutuhan, seperti:

* Filtering data
* Sorting data
* Statistik sederhana
* Menghitung jumlah pasien
* Menghitung frekuensi penyakit
* Visualisasi data
* Persiapan dataset machine learning

---

# 🚀 Cara Menjalankan Program

1. Clone repository

```bash
git clone https://github.com/IGOR100125/Diagnosis-Penyakit
```

2. Masuk ke folder proyek

```bash
cd Diagnosis-Penyakit
```

3. Install dependency

```bash
pip install -r requirements.txt
```

4. Jalankan program

```bash
python main.py
```

---

# 📈 Contoh Alur Diagnosis

```text
Input Data Pasien
        │
        ▼
Pilih Gejala
        │
        ▼
Relasi Gejala dengan Penyakit
        │
        ▼
Menentukan Penyakit
        │
        ▼
Simpan Data Pasien
        │
        ▼
Konversi JSON
        │
        ▼
Konversi CSV
        │
        ▼
Analisis Menggunakan Pandas
```

---

# 🎯 Tujuan Proyek

Proyek ini dikembangkan untuk:

* Mempelajari implementasi sistem diagnosis sederhana.
* Mengimplementasikan konsep relasi antara gejala dan penyakit.
* Menerapkan operasi CRUD pada data pasien.
* Mengelola data menggunakan format JSON dan CSV.
* Memanfaatkan Pandas DataFrame dalam proses analisis data.
* Menjadi media pembelajaran mengenai pengolahan data kesehatan menggunakan Python.

---

# 🤝 Kontribusi

Kontribusi sangat terbuka. Silakan lakukan:

1. Fork repository.
2. Buat branch baru.
3. Lakukan perubahan.
4. Commit perubahan.
5. Push ke repository.
6. Ajukan Pull Request.

---

# 📄 Lisensi

Proyek ini dibuat untuk tujuan pembelajaran dan pengembangan sistem diagnosis penyakit berbasis Python. Silakan digunakan, dimodifikasi, dan dikembangkan sesuai kebutuhan dengan tetap mencantumkan atribusi kepada pengembang.
