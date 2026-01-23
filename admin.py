import os
import json
import pandas as pd
import numpy as np
from collections import Counter
from diagnosisPenyakit import diagnosis_penyakit
from save import removeDataTerakhir

def aksesAdmin():
    print("Selamat datang admin :)")
    print("dengan akses sebagai admin, anda bisa:")
    print("1. Menghapus data pasien")
    print("2. Menghitung total pasien")
    print("3. Mencari data pasien")
    print("4. Analisis Datanya")
    pilihan = int(input("Mau pilih yang mana?   "))

    match pilihan:
        case 1:
            remove = removeDataTerakhir()
            print(remove)
        case 2:
            with open('data_pasien.json', 'r') as f:
                    data = json.load(f)

            df = pd.DataFrame(data)
            df.to_csv('data_pasien.csv', index=False)
            df_bersih = df
            
            nama_file = 'data_pasien.csv'
            df = pd.read_csv(nama_file)

            df = pd.read_csv("data_pasien.csv", header=None)
            df_rapi = df.T

            df_rapi.columns = ["No", "Nama", "Umur", "Jenis Kelamin", "Antrian", "Diagnosa Penyakit"]
            df_rapi = df_rapi.iloc[:, 1:]
            df_rapi_count = arr_diagnosis.size
            
            print(df_rapi)

            print(f"Total data pasien adalah: {df_rapi_count}")
        case 3:
            pass
        case 4:
            print("Berikut hasil analisis dari data pasien: ")

            with open('data_pasien.json', 'r') as f:
                    data = json.load(f)

            df = pd.DataFrame(data)
            df.to_csv('data_pasien.csv', index=False)
            df_bersih = df

            nama_file = 'data_pasien.csv'
            df = pd.read_csv(nama_file)

            df = pd.read_csv("data_pasien.csv", header=None)
            df_rapi = df.T

            df_rapi.columns = ["No", "Nama", "Umur", "Jenis Kelamin", "Antrian", "Diagnosa Penyakit"]
            df_rapi = df_rapi.iloc[:, 1:]

            arr_diagnosis = df_rapi["Diagnosa Penyakit"].to_numpy()

            #Data Penyakit
            jumlahDiagnosis = arr_diagnosis.size

            counts_diagnosis = Counter(arr_diagnosis)

            most_frequent, count = counts_diagnosis.most_common(1)[0]

            print(f"Rata-rata diagnosis penyakit dari data pasien adalah {most_frequent}")

            #Data Jenis Kelamin
            arr_jenis_kelamin = df_rapi["Jenis Kelamin"].to_numpy()

            jumlahJenisKelamin = arr_jenis_kelamin.size

            counts_jenis_kelamin = Counter(arr_jenis_kelamin)

            most_frequent, count = counts_jenis_kelamin.most_common(1)[0]

            print(f"Rata-rata jenis kelamin dari data pasien adalah {most_frequent}")

            #Data umur
            arr_umur = df_rapi["Umur"].to_numpy()

            jumlahUmur = arr_umur.size
            totalUmur = 0
            for i in arr_umur:
                totalUmur += int(i)
            average_umur = int(totalUmur) / jumlahUmur

            print(f"Rata-rata umur dari data pasien adalah {int(average_umur)}")

            print(f"Total jumlah data pasien keseluruhan adalah {jumlahUmur}")








