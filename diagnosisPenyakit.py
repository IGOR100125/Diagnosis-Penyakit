def diagnosis_penyakit():
    penyakit = {

        #Pernapasan & Infeksi
        "Flu": {
            "gejala": ["demam", "batuk", "pilek"],
            "saran": "Istirahat cukup dan minum air hangat",
            "obat": ["Paracetamol", "Obat flu"]
        },
        "Batuk Pilek": {
            "gejala": ["batuk", "pilek"],
            "saran": "Hindari udara dingin dan istirahat",
            "obat": ["Obat batuk"]
        },
        "Radang Tenggorokan": {
            "gejala": ["sakit tenggorokan", "batuk"],
            "saran": "Kumur air garam dan istirahat suara",
            "obat": ["Obat pelega tenggorokan"]
        },
        "ISPA": {
            "gejala": ["batuk", "sesak napas"],
            "saran": "Istirahat dan hindari asap rokok",
            "obat": ["Obat batuk"]
        },
        "Asma Ringan": {
            "gejala": ["sesak napas", "batuk"],
            "saran": "Hindari pemicu asma",
            "obat": ["Inhaler (jika ada)"]
        },
        "Sinusitis": {
            "gejala": ["hidung tersumbat", "sakit kepala"],
            "saran": "Uap hangat dan istirahat",
            "obat": ["Obat flu"]
        },
        "Bronkitis Ringan": {
            "gejala": ["batuk berdahak", "sesak"],
            "saran": "Perbanyak cairan dan istirahat",
            "obat": ["Obat batuk"]
        },

        #Demam & Infeksi umum
        "Demam": {
            "gejala": ["demam", "sakit kepala"],
            "saran": "Kompres dan perbanyak cairan",
            "obat": ["Paracetamol"]
        },
        "Demam Tinggi": {
            "gejala": ["demam tinggi", "lemas"],
            "saran": "Istirahat dan minum banyak cairan",
            "obat": ["Paracetamol"]
        },
        "Tipes": {
            "gejala": ["demam tinggi", "lemas", "mual"],
            "saran": "Istirahat total dan cukup cairan",
            "obat": ["Obat sesuai anjuran"]
        },
        "Demam Berdarah Ringan": {
            "gejala": ["demam tinggi", "nyeri sendi"],
            "saran": "Istirahat dan banyak minum",
            "obat": ["Paracetamol"]
        },

        #Pencernaan
        "Maag": {
            "gejala": ["nyeri ulu hati", "mual"],
            "saran": "Makan teratur dan hindari pedas",
            "obat": ["Antasida"]
        },
        "Gastritis": {
            "gejala": ["nyeri lambung", "mual"],
            "saran": "Hindari makanan asam dan pedas",
            "obat": ["Antasida"]
        },
        "GERD": {
            "gejala": ["dada panas", "mual"],
            "saran": "Hindari makan sebelum tidur",
            "obat": ["Antasida"]
        },
        "Diare": {
            "gejala": ["bab cair", "mual"],
            "saran": "Minum oralit dan cukup cairan",
            "obat": ["Oralit"]
        },
        "Keracunan Makanan": {
            "gejala": ["muntah", "diare", "bab cair"],
            "saran": "Hentikan makanan pemicu dan hidrasi",
            "obat": ["Oralit"]
        },
        "Sembelit": {
            "gejala": ["sulit bab", "perut kembung"],
            "saran": "Perbanyak serat dan minum air",
            "obat": ["Laksatif ringan"]
        },

        #Kepala dan Saraf
        "Sakit Kepala": {
            "gejala": ["pusing", "mual"],
            "saran": "Istirahat dan kurangi aktivitas",
            "obat": ["Paracetamol"]
        },
        "Migrain": {
            "gejala": ["sakit kepala sebelah", "sensitif cahaya"],
            "saran": "Istirahat di tempat gelap",
            "obat": ["Paracetamol"]
        },
        "Vertigo": {
            "gejala": ["pusing berputar", "mual"],
            "saran": "Duduk atau berbaring",
            "obat": ["Obat vertigo ringan"]
        },
        "Insomnia": {
            "gejala": ["sulit tidur"],
            "saran": "Atur jam tidur dan kurangi penggunaan gadget",
            "obat": ["Suplemen"]
        },

        #Darah dan Tekanan Darah
        "Hipertensi Ringan": {
            "gejala": ["pusing", "sakit kepala"],
            "saran": "Kurangi garam dan stres",
            "obat": ["Obat sesuai anjuran"]
        },
        "Hipotensi": {
            "gejala": ["lemas", "pusing"],
            "saran": "Bangun perlahan dan cukup cairan",
            "obat": ["Suplemen"]
        },
        "Anemia": {
            "gejala": ["lemas", "pucat"],
            "saran": "Konsumsi makanan bergizi",
            "obat": ["Suplemen zat besi"]
        },

        #Kulit dan Alergi
        "Alergi": {
            "gejala": ["gatal", "bersin"],
            "saran": "Hindari pemicu alergi",
            "obat": ["Antihistamin"]
        },
        "Biduran": {
            "gejala": ["bentol", "gatal"],
            "saran": "Hindari pemicu dan jaga kebersihan",
            "obat": ["Antihistamin"]
        },
        "Gatal Kulit": {
            "gejala": ["gatal"],
            "saran": "Jaga kebersihan kulit",
            "obat": ["Salep anti gatal"]
        },
        "Eksim Ringan": {
            "gejala": ["kulit kering", "gatal"],
            "saran": "Gunakan pelembap",
            "obat": ["Salep kulit"]
        },

        #Otot dan Sendi
        "Nyeri Sendi": {
            "gejala": ["nyeri sendi", "kaku"],
            "saran": "Istirahat dan kompres hangat",
            "obat": ["Obat nyeri"]
        },
        "Rematik Ringan": {
            "gejala": ["nyeri sendi", "bengkak"],
            "saran": "Hindari aktivitas berat",
            "obat": ["Obat nyeri"]
        },
        "Pegal Otot": {
            "gejala": ["nyeri otot"],
            "saran": "Peregangan ringan",
            "obat": ["Obat nyeri"]
        },
        "Keseleo Ringan": {
            "gejala": ["nyeri", "bengkak"],
            "saran": "Istirahat dan kompres",
            "obat": ["Obat nyeri"]
        },

        #Lainnya
        "Dehidrasi": {
            "gejala": ["haus", "lemas"],
            "saran": "Minum air secara bertahap",
            "obat": ["Oralit"]
        },
        "Kelelahan": {
            "gejala": ["lemas", "mengantuk"],
            "saran": "Istirahat cukup",
            "obat": ["Suplemen"]
        },
        "Stres Ringan": {
            "gejala": ["gelisah", "sulit tidur"],
            "saran": "Relaksasi dan atur waktu istirahat",
            "obat": ["Suplemen"]
        }
    }

    input_pasien = input("Masukkan gejala yang dirasakan: ").lower()

    gejala_pasien = []
    for data in penyakit.values():
        for g in data["gejala"]:
            if g in input_pasien and g not in gejala_pasien:
                gejala_pasien.append(g)

    hasil = []
    for nama, data in penyakit.items():
        cocok = set(gejala_pasien) & set(data["gejala"])
        if cocok:
            hasil.append((nama, len(cocok)))

    hasil.sort(key=lambda x: x[1], reverse=True)

    if hasil:
        nama_penyakit = hasil[0][0]
        data = penyakit[nama_penyakit]

        print("\nKemungkinan penyakit:", nama_penyakit)
        print("Saran:", data["saran"])
        print("Obat:", ", ".join(data["obat"]))
        return nama_penyakit
    else:
        print("Penyakit tidak ditemukan")
        return "Tidak diketahui"


