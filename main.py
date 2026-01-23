import json
import os
from diagnosisPenyakit import diagnosis_penyakit
from dataPasienDummy import pasien
from admin import aksesAdmin
from save import saveDataPasien

namaAdmin = "rama"
passwordAdmin = "ramaganteng"
adminAkses = [namaAdmin, passwordAdmin]

def pilihanAdmin():
    if pilihan == "admin":
        print("Login sebagai admin")
        inputNamaAdmin = input("Masukan nama:   ").lower()
        inputPasswordAdmin = input("Masukan password:   ")
        inputAdmin = [inputNamaAdmin, inputPasswordAdmin]
        while inputAdmin == adminAkses:
            return aksesAdmin()
        print("Nama atau password salah!")
        return pilihanAdmin()
    elif pilihan == "pasien":
        print("Daftar sebagai pasien")
    else:
        pilihanAdm = pilihanAdmin()
        print(pilihanAdm)


pilihan = input("Mau daftar sebagai pasien atau masuk sebagai admin?    ").lower()
pilihanAdmins = pilihanAdmin()
print(pilihanAdmins)

def load_data():
    if not os.path.exists("data_pasien.json"):
        return {}

    with open("data_pasien.json", "r") as file:
        return json.load(file)

def save_data(data):
    with open("data_pasien.json", "w") as file:
        json.dump(data, file, indent=4)

data_pasien = load_data()

print("Selamat Datang di Program Diagnosis Penyakit kecil-kecilan kami :)")
print("Perlu diingat kami hanya mendiagnosa penyakit berdasarkan gejala")
print("Mohon maaf apabila penyakit anda tidak dapat ditemukan, anda bisa periksa lebih lanjut ke Rumah sakit saja :)")

nama = input("Masukkan nama pasien: ")
usia = int(input("Masukkan usia pasien: "))

while True:
    jk = input("Masukkan jenis kelamin (L/P): ").strip().lower()
    if jk == "l":
        jenis_kelamin = "Laki-laki"
        break
    elif jk == "p":
        jenis_kelamin = "Perempuan"
        break
    else:
        print("Input salah! Masukkan L atau P.")

hasil_diagnosis = diagnosis_penyakit()

if data_pasien:
    nomor_antrian_baru = max(map(int, data_pasien.keys())) + 1
else:
    nomor_antrian_baru = 1

data_pasien[str(nomor_antrian_baru)] = {
    "nama": nama,
    "usia": usia,
    "jenis_kelamin": jenis_kelamin,
    "nomor_antrian": nomor_antrian_baru,
    "diagnosis": hasil_diagnosis
}

save_data(data_pasien)

print("\nData pasien berhasil disimpan")
print("Nomor Antrian:", nomor_antrian_baru)
print("Diagnosis:", hasil_diagnosis)

save_data_pasien = saveDataPasien()
print(save_data_pasien)
