import json
import pandas as pd
from collections import Counter
from saveAndRemove import removeDataTerakhir

with open('data_pasien.json', 'r') as f:
        data = json.load(f)

df = pd.DataFrame(data)
df.to_csv('data_pasien.csv', index=False)

df = pd.read_csv("data_pasien.csv", header=None)
df_rapi = df.T

df_rapi.columns = ["No", "Nama", "Umur", "Jenis Kelamin", "Antrian", "Diagnosa Penyakit"]
df_rapi = df_rapi.iloc[:, 1:]

def aksesAdmin():
    print("\nSelamat datang admin")
    print("dengan akses sebagai admin, anda bisa:")
    print("1. Menghapus data pasien terakhir")
    print("2. Menghitung total pasien")
    print("3. Mencari data pasien")
    print("4. Analisis Datanya")
    pilihan = int(input("\nMau pilih yang mana? "))

    match pilihan:
        case 1:
            remove = removeDataTerakhir()
            print(remove)
            exit()
        case 2:
            arr_jumlah = df_rapi["Nama"].to_numpy()
            df_rapi_count = arr_jumlah.size
            
            print("\nBerikut datanya:")

            print(f"{df_rapih}")

            print(f"\nTotal data pasien adalah: {df_rapi_count}")
            exit()
        case 3:
            def linear_search(df, nama_dicari):
                nama_dicari = nama_dicari.lower()

                for i in range(len(df)):
                    if df.loc[i, "Nama"].lower() == nama_dicari:
                        return df.loc[i]
                return

            namaDicari = input("Masukan nama lengkap pasien yang ingin dicari:  ")

            hasil = linear_search(df_rapi, namaDicari)

            if hasil is not None:
                print("Data ditemukan:")
                print(hasil)
            else:
                print("Data tidak ditemukan")
                exit()
        case 4:
            print("\nBerikut hasil analisis dari data pasien: ")

            arr_diagnosis = df_rapi["Diagnosa Penyakit"].to_numpy()

            #Data Penyakit
            jumlahDiagnosis = arr_diagnosis.size

            counts_diagnosis = Counter(arr_diagnosis)

            most_frequent, count = counts_diagnosis.most_common(1)[0]

            print(f"Data paling banyak dari diagnosis penyakit adalah {most_frequent}")

            #Data Jenis Kelamin
            arr_jenis_kelamin = df_rapi["Jenis Kelamin"].to_numpy()

            jumlahJenisKelamin = arr_jenis_kelamin.size

            counts_jenis_kelamin = Counter(arr_jenis_kelamin)

            most_frequent, count = counts_jenis_kelamin.most_common(1)[0]

            print(f"Data paling banyak dari jenis kelamin adalah {most_frequent}")

            #Data umur
            arr_umur = df_rapi["Umur"].to_numpy()

            jumlahUmur = arr_umur.size
            totalUmur = 0
            for i in arr_umur:
                totalUmur += int(i)
            average_umur = int(totalUmur) / jumlahUmur

            print(f"Rata-rata umur dari data pasien adalah {int(average_umur)}")

            print(f"Total jumlah data pasien keseluruhan adalah {jumlahDiagnosis} pasien")
            exit()








