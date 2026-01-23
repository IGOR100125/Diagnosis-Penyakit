import json
import pandas as pd

def saveDataPasien():
    with open('data_pasien.json', 'r') as f:
        data = json.load(f)

    df = pd.DataFrame(data)
    df.to_csv('data_pasien.csv', index=False)

def removeDataTerakhir():
    with open('data_pasien.json', 'r') as file1:
        data = json.load(file1)

    if len(data) == 0:
        return "Data kosong, tidak ada yang dihapus."

    last_key = list(data.keys())[-1]
    data.pop(last_key)


    with open('data_pasien.json', 'w') as file2:
        json.dump(data, file2, indent=4)

    df = pd.DataFrame(data)
    df.to_csv('data_pasien.csv', index=False)

    return "Data terakhir berhasil dihapus."

