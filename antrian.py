from dataPasienAwal import pasien

def antrian_fifo():
    return pasien[min(pasien.keys())]

def antrian_lifo():
    return pasien[max(pasien.keys())]

antrififo = antrian_lifo()
print(antrififo)