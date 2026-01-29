import json
import pandas as pd
from collections import Counter
from saveAndRemove import removeDataTerakhir

def load_data():
    with open('data_pasien.json', 'r') as f:
        data = json.load(f)

    df = pd.DataFrame(data)
    df.to_csv('data_pasien.csv', index=False)

    df = pd.read_csv("data_pasien.csv", header=None)

    df_rapi = df.T
    df_rapi.columns = ["No", "Nama", "Umur", "Jenis Kelamin", "Antrian", "Diagnosa Penyakit"]
    
    df_rapi = df_rapi.iloc[:, 1:]

    return df_rapi

def aksesAdmin():
    while True:
        df_rapi = load_data()

        print("\nSELAMAT DATANG ADMIN")
        print("1. Menghapus data pasien terakhir")
        print("2. Menghitung total pasien")
        print("3. Mencari data pasien")
        print("4. Analisis data pasien")
        print("0. Keluar")

        pilihan = int(input("\nMau pilih yang mana? "))

        match pilihan:
            case 1:
                remove = removeDataTerakhir()
                print(remove)
                input("\nTekan ENTER untuk kembali ke menu...")

            case 2:
                total_pasien = df_rapi["Nama"].size
                print("\nData pasien:")
                print(df_rapi)
                print(f"\nTotal data pasien: {total_pasien}")
                input("\nTekan ENTER untuk kembali ke menu...")

            case 3:
                def linear_search(df, nama_dicari):
                    nama_dicari = nama_dicari.lower()
                    for i in range(len(df)):
                        if df.loc[i, "Nama"].lower() == nama_dicari:
                            return df.loc[i]
                    return None

                namaDicari = input("Masukkan nama lengkap pasien: ")
                hasil = linear_search(df_rapi, namaDicari)

                if hasil is not None:
                    print("\nData ditemukan:")
                    print(hasil)
                else:
                    print("\nData tidak ditemukan")

                input("\nTekan ENTER untuk kembali ke menu...")
            case 4:
                print("\nHASIL ANALISIS DATA")

                arr_diagnosis = df_rapi["Diagnosa Penyakit"].to_numpy()
                counts_diagnosis = Counter(arr_diagnosis)
                penyakit_terbanyak = counts_diagnosis.most_common(1)[0][0]

                print(f"Penyakit terbanyak: {penyakit_terbanyak}")

                arr_jk = df_rapi["Jenis Kelamin"].to_numpy()
                counts_jk = Counter(arr_jk)
                jk_terbanyak = counts_jk.most_common(1)[0][0]

                print(f"Jenis kelamin terbanyak: {jk_terbanyak}")

                arr_umur = df_rapi["Umur"].astype(int).to_numpy()
                rata_umur = arr_umur.mean()

                print(f"Rata-rata umur pasien: {int(rata_umur)}")
                print(f"Total pasien: {len(arr_umur)}")

                input("\nTekan ENTER untuk kembali ke menu...")
            case 0:
                print("\nKeluar dari program")
                exit()
            case _:
                print("Pilihan tidak valid!")
