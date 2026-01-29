def diagnosis_penyakit():
    penyakit = penyakit = {

    # ================== Pernapasan ==================
    "Flu": {
        "gejala": {
            "demam": 3,
            "batuk": 2,
            "pilek": 2
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

    "Bronkitis Ringan": {
        "gejala": {
            "batuk berdahak": 4,
            "sesak napas": 3,
            "demam": 2
        },
        "saran": "Perbanyak istirahat dan hindari asap",
        "obat": ["Obat batuk", "Paracetamol"]
    },

    "Sinusitis Ringan": {
        "gejala": {
            "hidung tersumbat": 3,
            "nyeri wajah": 4,
            "sakit kepala": 2
        },
        "saran": "Uap air hangat dan istirahat",
        "obat": ["Dekongestan"]
    },

    # ================== Pencernaan ==================
    "Maag": {
        "gejala": {
            "nyeri ulu hati": 4,
            "mual": 2,
            "perut kembung": 1
        },
        "saran": "Makan teratur",
        "obat": ["Antasida"]
    },

    "GERD Ringan": {
        "gejala": {
            "nyeri ulu hati": 4,
            "asam naik": 3,
            "mual": 2
        },
        "saran": "Hindari makanan pedas dan asam",
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
            "sakit perut": 2,
            "pusing": 1
        },
        "saran": "Hentikan makanan pemicu",
        "obat": ["Oralit"]
    },

    "Sembelit": {
        "gejala": {
            "sulit bab": 4,
            "perut kembung": 2,
            "nyeri perut": 2
        },
        "saran": "Perbanyak serat dan air",
        "obat": ["Laksatif ringan"]
    },

    # ================== Demam & Darah ==================
    "Demam Berdarah Ringan": {
        "gejala": {
            "demam tinggi": 4,
            "nyeri sendi": 3,
            "bintik merah": 4
        },
        "saran": "Istirahat total dan banyak minum",
        "obat": ["Paracetamol"]
    },

    "Tifus Ringan": {
        "gejala": {
            "demam": 4,
            "lemas": 3,
            "nafsu makan turun": 2
        },
        "saran": "Istirahat total dan makan lunak",
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

    "Hipertensi": {
        "gejala": {
            "lemas": 3,
            "pusing": 3,
            "pandangan berkunang": 2
        },
        "saran": "Bangun perlahan dan cukup cairan",
        "obat": ["Suplemen"]
    },

    "Infeksi Saluran Kemih Ringan": {
        "gejala": {
            "nyeri saat buang air kecil": 4,
            "sering buang air kecil": 3,
            "nyeri perut bawah": 2
        },
        "saran": "Perbanyak minum air putih",
        "obat": ["Antibiotik sesuai anjuran"]
    },

    # ================== Saraf, Otot & Psikologis ==================
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

    "Tegang Otot": {
        "gejala": {
            "nyeri otot": 4,
            "kaku": 3,
            "lelah": 2
        },
        "saran": "Peregangan dan istirahat",
        "obat": ["Obat pereda nyeri"]
    },

    "Insomnia": {
        "gejala": {
            "sulit tidur": 4,
            "lelah": 3,
            "sulit konsentrasi": 2
        },
        "saran": "Atur jam tidur dan hindari kafein",
        "obat": ["Suplemen tidur"]
    },

    "Stres Ringan": {
        "gejala": {
            "cemas": 3,
            "mudah lelah": 2,
            "sulit konsentrasi": 3
        },
        "saran": "Kelola stres dan istirahat",
        "obat": ["Relaksasi"]
    },

    "Kecemasan Ringan": {
        "gejala": {
            "gelisah": 3,
            "jantung berdebar": 3,
            "sulit tidur": 2
        },
        "saran": "Latihan pernapasan",
        "obat": ["Suplemen penenang ringan"]
    },

    # ================== Mata & THT ==================
    "Konjungtivitis Ringan": {
        "gejala": {
            "mata merah": 4,
            "mata gatal": 3,
            "mata berair": 2
        },
        "saran": "Hindari menyentuh mata",
        "obat": ["Obat tetes mata"]
    },

    "Radang Tenggorokan": {
        "gejala": {
            "sakit saat menelan": 4,
            "tenggorokan kering": 3,
            "batuk": 2
        },
        "saran": "Minum air hangat",
        "obat": ["Obat hisap tenggorokan"]
    },

    "Otitis Eksterna Ringan": {
        "gejala": {
            "nyeri telinga": 4,
            "telinga gatal": 3,
            "telinga terasa penuh": 2
        },
        "saran": "Jaga telinga tetap kering",
        "obat": ["Obat tetes telinga"]
    },

    # ================== Kulit ==================
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
    },

    "Infeksi Jamur Kulit": {
        "gejala": {
            "gatal": 3,
            "kulit bersisik": 4,
            "kemerahan": 2
        },
        "saran": "Jaga kulit tetap kering",
        "obat": ["Salep antijamur"]
    },

    "Biang Keringat": {
        "gejala": {
            "ruam merah": 3,
            "gatal": 3,
            "kulit perih": 2
        },
        "saran": "Hindari panas berlebih",
        "obat": ["Bedak atau salep ringan"]
    },

    # ================== Umum ==================
    "Dehidrasi Ringan": {
        "gejala": {
            "haus berlebihan": 4,
            "mulut kering": 3,
            "lemas": 2
        },
        "saran": "Perbanyak minum air",
        "obat": ["Oralit"]
    },

    "Kelelahan": {
        "gejala": {
            "lelah": 4,
            "mengantuk": 3,
            "sulit konsentrasi": 2
        },
        "saran": "Istirahat dan tidur cukup",
        "obat": ["Vitamin"]
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
