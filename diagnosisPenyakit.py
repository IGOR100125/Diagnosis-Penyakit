def diagnosis_penyakit():
    penyakit = {

        #Pernapasan
        "Flu": {
            "gejala": {
                "demam": 3,
                "batuk": 2,
                "pilek": 2,
                "nyeri otot": 1
            },
            "saran": "Istirahat cukup dan perbanyak cairan",
            "obat": ["Paracetamol", "Obat flu"]
        },

        "Covid-19 Ringan": {
            "gejala": {
                "demam": 3,
                "batuk kering": 3,
                "kehilangan penciuman": 4,
                "lemas": 2
            },
            "saran": "Isolasi mandiri dan istirahat",
            "obat": ["Paracetamol", "Vitamin C"]
        },

        "ISPA": {
            "gejala": {
                "batuk": 2,
                "sesak napas": 3,
                "demam": 2
            },
            "saran": "Hindari asap rokok",
            "obat": ["Obat batuk"]
        },

        "Asma Ringan": {
            "gejala": {
                "sesak napas": 4,
                "batuk": 2,
                "dada terasa berat": 3
            },
            "saran": "Hindari pemicu asma",
            "obat": ["Inhaler"]
        },

        #Pencernaan
        "Maag": {
            "gejala": {
                "nyeri ulu hati": 4,
                "mual": 2,
                "perut kembung": 1
            },
            "saran": "Makan teratur",
            "obat": ["Antasida"]
        },

        "Diare": {
            "gejala": {
                "bab cair": 4,
                "mual": 2,
                "lemas": 2
            },
            "saran": "Minum oralit",
            "obat": ["Oralit"]
        },

        "Keracunan Makanan": {
            "gejala": {
                "muntah": 4,
                "diare": 3,
                "sakit perut": 2
            },
            "saran": "Hentikan makanan pemicu",
            "obat": ["Oralit"]
        },

        #Demam & darah
        "Demam Berdarah Ringan": {
            "gejala": {
                "demam tinggi": 4,
                "nyeri sendi": 3,
                "bintik merah": 4
            },
            "saran": "Istirahat total dan banyak minum",
            "obat": ["Paracetamol"]
        },

        "Hipertensi Ringan": {
            "gejala": {
                "pusing": 3,
                "sakit kepala": 3,
                "leher terasa kaku": 2
            },
            "saran": "Kurangi garam dan stres",
            "obat": ["Obat sesuai anjuran"]
        },

        "Hipotensi": {
            "gejala": {
                "lemas": 3,
                "pusing": 3,
                "pandangan berkunang": 2
            },
            "saran": "Bangun perlahan dan cukup cairan",
            "obat": ["Suplemen"]
        },

        #Saraf
        "Migrain": {
            "gejala": {
                "sakit kepala sebelah": 4,
                "sensitif cahaya": 3,
                "mual": 2
            },
            "saran": "Istirahat di tempat gelap",
            "obat": ["Paracetamol"]
        },

        "Vertigo": {
            "gejala": {
                "pusing berputar": 4,
                "mual": 3,
                "sulit berdiri": 2
            },
            "saran": "Duduk atau berbaring",
            "obat": ["Obat vertigo"]
        },

        #Kulit
        "Alergi": {
            "gejala": {
                "gatal": 3,
                "bersin": 2,
                "ruam": 2
            },
            "saran": "Hindari pemicu",
            "obat": ["Antihistamin"]
        },

        "Eksim Ringan": {
            "gejala": {
                "kulit kering": 3,
                "gatal": 3,
                "kemerahan": 2
            },
            "saran": "Gunakan pelembap",
            "obat": ["Salep kulit"]
        }
    }

    input_pasien = input("Masukkan gejala (pisahkan dengan koma): ").lower()
    gejala_pasien = [g.strip() for g in input_pasien.split(",")]

    hasil = []

    for nama, data in penyakit.items():
        skor = 0
        for g in gejala_pasien:
            if g in data["gejala"]:
                skor += data["gejala"][g]

        if skor > 0:
            hasil.append((nama, skor))

    hasil.sort(key=lambda x: x[1], reverse=True)

    if hasil:
        nama_penyakit, skor = hasil[0]
        data = penyakit[nama_penyakit]

        print("\nKemungkinan penyakit:", nama_penyakit)
        print("Skor kecocokan:", skor)
        print("Saran:", data["saran"])
        print("Obat:", ", ".join(data["obat"]))
        return nama_penyakit
    else:
        print("Penyakit tidak ditemukan")
        return "Tidak diketahui"
