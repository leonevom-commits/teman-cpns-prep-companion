"""Materi & flashcard Siap CPNS 2027 -> src/data/learning-modules.json, flashcards.json"""
import json, os
OUT = os.path.join(os.path.dirname(__file__), "..", "src", "data")

def m(id, cat, sub, title, summary, sections, points, example):
    return {"id": id, "category": cat, "sub": sub, "title": title, "summary": summary,
            "sections": [{"heading": h, "body": b} for h, b in sections], "keyPoints": points, "example": example}

M = [
 m("twk-nasionalisme","TWK","Nasionalisme","Nasionalisme & Sejarah Pergerakan","Nasionalisme adalah paham yang menempatkan kesetiaan tertinggi pada bangsa dan negara, tumbuh dari pengalaman sejarah perjuangan melawan penjajahan.",
  [("Tonggak pergerakan nasional","Budi Utomo (20 Mei 1908) menandai era organisasi modern. Sarekat Islam (1911/1912) menjadi organisasi massa pertama, Indische Partij (1912) berani menuntut kemerdekaan, dan Sumpah Pemuda (28 Oktober 1928) menyatukan identitas: satu tanah air, satu bangsa, dan menjunjung bahasa persatuan."),
   ("Menjelang proklamasi","BPUPKI dibentuk 29 April 1945 dan bersidang 29 Mei–1 Juni serta 10–17 Juli 1945. PPKI dibentuk 7 Agustus 1945. Setelah peristiwa Rengasdengklok (16 Agustus), naskah proklamasi dirumuskan di rumah Laksamana Maeda, diketik Sayuti Melik, dan dibacakan 17 Agustus 1945 di Pegangsaan Timur 56."),
   ("Nasionalisme dalam tugas ASN","ASN menunjukkan nasionalisme dengan mengutamakan kepentingan publik di atas golongan, menjaga persatuan dalam pelayanan, dan bangga menggunakan produk serta bahasa Indonesia tanpa merendahkan bangsa lain.")],
  ["Nasionalisme Indonesia bersifat terbuka (bukan chauvinisme)","20 Mei = Hari Kebangkitan Nasional; 28 Oktober = Sumpah Pemuda; 10 November = Hari Pahlawan","PPKI mengesahkan UUD 1945 dan memilih Presiden–Wapres pada 18 Agustus 1945"],
  "Seorang pegawai diminta memprioritaskan izin usaha milik kerabat pejabat. Sikap nasionalis-profesional: tetap memproses sesuai antrean karena kepentingan umum lebih utama."),
 m("twk-integritas","TWK","Integritas","Integritas & Antikorupsi","Integritas adalah konsistensi antara nilai, ucapan, dan tindakan, termasuk saat tidak diawasi.",
  [("Nilai antikorupsi","KPK merumuskan sembilan nilai antikorupsi: jujur, peduli, mandiri, disiplin, tanggung jawab, kerja keras, sederhana, berani, dan adil."),
   ("Bentuk korupsi","UU 31/1999 jo. UU 20/2001 mengelompokkan korupsi menjadi kerugian keuangan negara, suap-menyuap, penggelapan dalam jabatan, pemerasan, perbuatan curang, benturan kepentingan dalam pengadaan, dan gratifikasi."),
   ("Gratifikasi","Gratifikasi yang berhubungan dengan jabatan wajib dilaporkan ke KPK paling lambat 30 hari kerja sejak diterima. Penolakan adalah sikap terbaik bila pemberian terkait kewenangan."),
   ("Akuntabilitas dan transparansi","Akuntabilitas berarti setiap keputusan dapat dipertanggungjawabkan; transparansi berarti informasi publik dibuka sesuai UU 14/2008 tentang Keterbukaan Informasi Publik.")],
  ["Core values ASN: BerAKHLAK (Berorientasi pelayanan, Akuntabel, Kompeten, Harmonis, Loyal, Adaptif, Kolaboratif)","Lapor gratifikasi maksimal 30 hari kerja","Konflik kepentingan harus dideklarasikan, bukan disembunyikan"],
  "Rekanan memberi voucher belanja setelah tender selesai. Sikap berintegritas: menolak dengan sopan; jika terlanjur diterima, laporkan ke UPG/KPK."),
 m("twk-bela-negara","TWK","Bela Negara","Bela Negara & Wawasan Nusantara","Bela negara adalah tekad, sikap, dan perilaku warga negara yang dijiwai kecintaan pada NKRI berdasarkan Pancasila dan UUD 1945.",
  [("Dasar hukum","Pasal 27 ayat (3) UUD 1945: setiap warga negara berhak dan wajib ikut serta dalam upaya pembelaan negara. Pasal 30 ayat (1): hak dan kewajiban ikut serta dalam usaha pertahanan dan keamanan negara. UU 3/2002 tentang Pertahanan Negara."),
   ("Lima nilai dasar bela negara","Cinta tanah air; sadar berbangsa dan bernegara; setia pada Pancasila; rela berkorban; serta kemampuan awal bela negara."),
   ("Ancaman","Ancaman militer (agresi, pelanggaran wilayah) dan nonmiliter (ideologi, ekonomi, siber, narkoba, bencana). Hakikat ketahanan nasional adalah keuletan dan ketangguhan bangsa."),
   ("Wawasan Nusantara","Cara pandang bangsa tentang diri dan lingkungannya yang mengutamakan persatuan wilayah. Tonggaknya Deklarasi Djuanda 13 Desember 1957 yang diakui UNCLOS 1982.")],
  ["Bela negara tidak hanya militer: belajar, bekerja jujur, membayar pajak juga bela negara","Sishankamrata = sistem pertahanan semesta","Deklarasi Djuanda → konsep negara kepulauan"],
  "Hoaks provokatif beredar di grup kantor. Sikap bela negara: tidak meneruskan, mengklarifikasi dengan sumber resmi, dan mengingatkan rekan."),
 m("twk-pilar-negara","TWK","Pilar Negara","Pancasila, UUD 1945, NKRI, Bhinneka Tunggal Ika","Empat konsensus dasar berbangsa: Pancasila sebagai dasar negara, UUD NRI 1945 sebagai konstitusi, NKRI sebagai bentuk negara, dan Bhinneka Tunggal Ika sebagai semboyan.",
  [("Perumusan Pancasila","Usulan dasar negara disampaikan Moh. Yamin (29 Mei), Soepomo (31 Mei), dan Soekarno (1 Juni 1945). Panitia Sembilan menghasilkan Piagam Jakarta (22 Juni 1945). Tujuh kata sila pertama diubah dan Pancasila disahkan bersama UUD 1945 pada 18 Agustus 1945."),
   ("UUD 1945 dan amandemen","UUD 1945 diamandemen empat kali (1999–2002). Pembukaan tidak diubah karena memuat dasar negara dan tujuan nasional (alinea IV). Kedaulatan berada di tangan rakyat dan dilaksanakan menurut UUD (Pasal 1 ayat 2)."),
   ("Lembaga negara","Pasca-amandemen: MPR, DPR, DPD, Presiden, MA, MK, BPK, dan KY. MK menguji UU terhadap UUD; MA menguji peraturan di bawah UU terhadap UU; BPK memeriksa keuangan negara."),
   ("HAM dan sistem pemerintahan","HAM diatur Pasal 28A–28J. Indonesia menganut sistem presidensial: presiden adalah kepala negara sekaligus kepala pemerintahan dan dipilih langsung.")],
  ["Bhinneka Tunggal Ika berasal dari Kakawin Sutasoma karya Mpu Tantular","Pasal 37: bentuk NKRI tidak dapat diubah","Tujuan negara ada di alinea IV Pembukaan"],
  "Dua kelompok warga berselisih soal penggunaan balai desa. ASN menengahi dengan musyawarah — pengamalan sila ke-4."),
 m("twk-bahasa","TWK","Bahasa Negara","Bahasa Negara & Kalimat Efektif","Bahasa Indonesia berkedudukan sebagai bahasa nasional (Sumpah Pemuda 1928) dan bahasa negara (Pasal 36 UUD 1945).",
  [("Dasar hukum","UU 24/2009 tentang Bendera, Bahasa, dan Lambang Negara, serta Lagu Kebangsaan mewajibkan bahasa Indonesia dalam dokumen resmi negara, pidato resmi pejabat, dan nama bangunan."),
   ("EYD Edisi V","Pedoman ejaan yang berlaku sejak 2022. Contoh: kata baku 'apotek', 'kualitas', 'nasihat', 'risiko', 'praktik'; penulisan 'di' sebagai kata depan dipisah (di rumah), sebagai awalan digabung (dibaca)."),
   ("Kalimat efektif","Ciri: kesepadanan struktur (ada subjek-predikat), keparalelan, kehematan (tidak mubazir, mis. 'para hadirin' → 'hadirin'), kecermatan, kelogisan, dan kepaduan.")],
  ["Bahasa negara: Pasal 36 UUD 1945","Hindari pleonasme: 'naik ke atas', 'mundur ke belakang'","Surat dinas memakai bahasa baku dan lugas"],
  "Kalimat 'Bagi para peserta diharapkan hadir' tidak efektif. Perbaikan: 'Peserta diharapkan hadir.'"),
 m("tiu-verbal","TIU","Verbal","Kemampuan Verbal","Mengukur kemampuan memahami hubungan kata, makna, bacaan, dan penalaran logis.",
  [("Analogi","Temukan hubungan pasangan pertama (fungsi, bagian-keseluruhan, sebab-akibat, tempat) lalu terapkan pada pilihan. Buat kalimat penghubung: 'Pena digunakan untuk menulis'."),
   ("Sinonim & antonim","Perhatikan kelas kata; sinonim harus sejenis. Contoh: 'nisbi' = relatif, 'absolut' >< relatif."),
   ("Silogisme","Modus ponens: jika p maka q; p; jadi q. Modus tollens: jika p maka q; bukan q; jadi bukan p. Silogisme: semua A adalah B, semua B adalah C, maka semua A adalah C. Hati-hati dengan 'sebagian'."),
   ("Penalaran analitis","Buat tabel atau diagram posisi untuk soal urutan/penempatan. Coret kemungkinan yang melanggar syarat.")],
  ["Ingkaran 'semua' adalah 'ada/sebagian … tidak'","Jika p maka q setara dengan jika bukan q maka bukan p","Baca pertanyaan sebelum teks pada soal bacaan"],
  "Semua ASN wajib apel. Budi tidak apel. Kesimpulan: Budi bukan ASN (modus tollens)."),
 m("tiu-numerik","TIU","Numerik","Kemampuan Numerik","Mengukur kecepatan berhitung, mengenali pola bilangan, dan menyelesaikan soal cerita.",
  [("Deret","Cek selisih (tingkat 1 dan 2), rasio, deret bertingkat, atau dua deret berselang-seling."),
   ("Persentase & aritmetika sosial","Untung = jual − beli; persentase untung = untung/beli × 100%. Diskon bertingkat 20% lalu 10% = 1 − 0,8×0,9 = 28%, bukan 30%."),
   ("Kecepatan, jarak, waktu","J = K × W. Berpapasan: waktu = jarak / (K1 + K2). Menyusul: waktu = selisih jarak / (K1 − K2). Kecepatan rata-rata = total jarak / total waktu."),
   ("Perbandingan & rata-rata","Perbandingan senilai: a/b = c/d. Berbalik nilai (pekerja–waktu): p1×w1 = p2×w2. Rata-rata gabungan = (n1x1 + n2x2)/(n1+n2).")],
  ["Hafalkan pecahan umum: 1/8 = 12,5%; 1/6 ≈ 16,67%","Gunakan pembulatan untuk mengeliminasi pilihan","Kerjakan soal cepat dulu, tandai yang panjang"],
  "Harga Rp200.000 didiskon 25% lalu 10%: 200.000 × 0,75 × 0,9 = Rp135.000."),
 m("tiu-figural","TIU","Figural","Kemampuan Figural","Mengukur penalaran visual: pola, rotasi, pencerminan, dan analogi gambar.",
  [("Langkah analisis","Perhatikan satu atribut dalam satu waktu: jumlah sisi, arah, arsiran, posisi, dan ukuran."),
   ("Rotasi","Rotasi searah jarum jam mengubah arah objek dengan sudut tetap. Jika tiap langkah +45°, langkah berikutnya juga +45°."),
   ("Pencerminan","Cermin vertikal menukar kiri-kanan; cermin horizontal menukar atas-bawah. Sudut θ terhadap sumbu horizontal menjadi −θ pada cermin horizontal dan 180°−θ pada cermin vertikal."),
   ("Ketidaksamaan","Satu gambar berbeda atribut dasarnya (misalnya jumlah sisi) meskipun posisinya diputar.")],
  ["Rotasi tidak mengubah bentuk, hanya arah","Bayangan cermin tidak bisa diperoleh dengan rotasi saja (untuk bentuk asimetris)","Hitung jumlah elemen bila pola tidak terlihat"],
  "Panah menghadap 0°, 45°, 90°, … gambar berikutnya menghadap 135°."),
]
TKP = [
 ("Pelayanan Publik","Prinsip pelayanan publik berdasarkan UU 25/2009: kepastian, keterbukaan, kecepatan, non-diskriminasi, dan kemudahan akses. Respons terbaik selalu tetap melayani dengan ramah, solutif, dan sesuai prosedur.","Warga datang tanpa berkas lengkap. Skor 5: menjelaskan kekurangan dengan ramah dan membantu solusi tercepat."),
 ("Jejaring Kerja","Kemampuan membangun, membina, dan memanfaatkan hubungan kerja untuk tujuan organisasi. Pilih respons yang terbuka, kolaboratif, dan proaktif menjalin komunikasi.","Ditempatkan di tim baru. Skor 5: berinisiatif berkenalan dan menawarkan kontribusi."),
 ("Sosial Budaya","Kemampuan beradaptasi dan bekerja dalam masyarakat majemuk tanpa diskriminasi suku, agama, ras, maupun golongan.","Rekan berbeda agama merayakan hari besar. Skor 5: menghormati dan mengucapkan selamat sesuai kenyamanan masing-masing."),
 ("Teknologi Informasi dan Komunikasi","Kemauan mempelajari dan memanfaatkan TIK untuk meningkatkan kinerja, serta menjaga keamanan data.","Kantor beralih ke aplikasi baru. Skor 5: segera mempelajari dan membantu rekan yang kesulitan."),
 ("Profesionalisme","Bekerja sesuai standar, tuntas, tepat waktu, dan bertanggung jawab atas hasil kerja, termasuk mengakui kesalahan.","Atasan memberi tugas di luar keahlian. Skor 5: menerima, belajar cepat, dan berkonsultasi bila perlu."),
 ("Anti-Radikalisme","Sikap menolak paham yang ingin mengganti Pancasila dengan kekerasan, serta mengedepankan moderasi dan toleransi.","Ada ajakan grup yang menyebarkan paham anti-Pancasila. Skor 5: menolak, tidak menyebarkan, dan melaporkan ke pihak berwenang."),
]
for i, (sub, body, ex) in enumerate(TKP):
    M.append(m(f"tkp-{i+1}", "TKP", sub, sub, body,
      [("Karakteristik perilaku", body),
       ("Strategi menjawab", "Setiap opsi bernilai 1–5. Urutkan opsi dari yang paling proaktif-solutif (5) hingga yang menghindar atau melanggar aturan (1). Hindari opsi yang menyalahkan orang lain, menunda, atau hanya mementingkan diri sendiri."),
       ("Situasi kerja ASN", ex)],
      ["Tidak ada jawaban salah, yang ada skor rendah", "Pilih respons yang menyelesaikan masalah, bukan memindahkannya", "Konsisten dengan nilai BerAKHLAK"], ex))
SKB = {
 "Guru dan Tenaga Pendidikan":("Kurikulum Merdeka, pedagogi, asesmen, dan profil pelajar Pancasila.",["Kurikulum Merdeka berfokus pada materi esensial dan pembelajaran berdiferensiasi","Asesmen formatif untuk memperbaiki proses, sumatif untuk mengukur capaian","Enam dimensi Profil Pelajar Pancasila"]),
 "Dokter":("Pelayanan kesehatan primer, etika kedokteran, dan sistem JKN.",["Puskesmas sebagai FKTP menangani 144 diagnosis kompetensi dokter umum","Informed consent wajib sebelum tindakan","Rujukan berjenjang dalam JKN"]),
 "Perawat":("Proses keperawatan, keselamatan pasien, dan etika keperawatan.",["Proses keperawatan: pengkajian, diagnosis, perencanaan, implementasi, evaluasi","Enam sasaran keselamatan pasien (identifikasi, komunikasi, obat, operasi, infeksi, jatuh)","Hand hygiene lima momen WHO"]),
 "Bidan":("Asuhan kehamilan, persalinan, nifas, dan kesehatan ibu-anak.",["Kunjungan ANC minimal 6 kali (standar terbaru)","Inisiasi Menyusu Dini minimal 1 jam","Tanda bahaya kehamilan harus segera dirujuk"]),
 "Pranata Komputer dan IT":("Jaringan, basis data, keamanan informasi, dan SPBE.",["SPBE diatur Perpres 95/2018","Model OSI tujuh lapisan","Normalisasi basis data mengurangi redundansi"]),
 "Auditor":("Standar audit intern pemerintah, SPIP, dan pengawasan.",["SPIP diatur PP 60/2008 dengan lima unsur","APIP: BPKP, Inspektorat","Bukti audit harus cukup, kompeten, relevan"]),
 "Analis Kebijakan":("Siklus kebijakan publik dan analisis alternatif.",["Siklus: agenda, formulasi, adopsi, implementasi, evaluasi","Analisis biaya-manfaat dan RIA","Policy brief ringkas berbasis bukti"]),
 "Analis Keuangan":("Keuangan negara, APBN/APBD, dan akuntansi pemerintahan.",["UU 17/2003 tentang Keuangan Negara","SAP berbasis akrual (PP 71/2010)","Laporan keuangan pemerintah diperiksa BPK"]),
 "Arsiparis":("Pengelolaan arsip dinamis dan statis.",["UU 43/2009 tentang Kearsipan","Arsip dinamis: aktif, inaktif, vital","JRA menentukan jangka simpan dan nasib akhir arsip"]),
 "Pustakawan":("Pengelolaan perpustakaan dan layanan informasi.",["UU 43/2007 tentang Perpustakaan","Klasifikasi DDC membagi ilmu menjadi 10 kelas","Katalogisasi deskriptif dan subjek"]),
 "Penyuluh":("Metode penyuluhan, pemberdayaan, dan komunikasi.",["Penyuluhan partisipatif melibatkan sasaran sejak perencanaan","Tahapan adopsi: sadar, minat, menilai, mencoba, menerapkan","Demplot sebagai metode percontohan"]),
 "Administrasi Pemerintahan":("Administrasi pemerintahan, tata naskah dinas, dan pelayanan.",["UU 30/2014 tentang Administrasi Pemerintahan","AUPB: kepastian hukum, kemanfaatan, ketidakberpihakan, kecermatan, dll.","Naskah dinas mengikuti pedoman tata naskah instansi"]),
 "Jabatan Teknis Lainnya":("Manajemen ASN, kinerja, dan etika jabatan.",["UU 20/2023 tentang ASN","ASN terdiri atas PNS dan PPPK","Sistem merit: kualifikasi, kompetensi, kinerja"]),
}
for i, (sub, (summary, pts)) in enumerate(SKB.items()):
    M.append(m(f"skb-{i+1}", "SKB", sub, f"SKB {sub}", summary,
      [("Ruang lingkup kisi-kisi", summary + " Kisi-kisi resmi ditetapkan per jabatan oleh instansi pembina; selalu cocokkan dengan pengumuman instansi tujuan."),
       ("Konsep inti", " ".join(p + "." for p in pts)),
       ("Strategi belajar", "Pelajari regulasi pokok jabatan, pahami alur kerja harian, lalu latih soal studi kasus yang menuntut keputusan sesuai prosedur.")],
      pts, f"Soal SKB {sub} sering berbentuk studi kasus: pilih tindakan yang sesuai regulasi dan standar profesi."))

F = {
 "Pancasila":[("Sila ke-1","Ketuhanan Yang Maha Esa — lambang bintang"),("Sila ke-2","Kemanusiaan yang adil dan beradab — rantai"),("Sila ke-3","Persatuan Indonesia — pohon beringin"),("Sila ke-4","Kerakyatan yang dipimpin oleh hikmat kebijaksanaan dalam permusyawaratan/perwakilan — kepala banteng"),("Sila ke-5","Keadilan sosial bagi seluruh rakyat Indonesia — padi dan kapas"),("Hari Lahir Pancasila","1 Juni (pidato Soekarno 1945)"),("Piagam Jakarta","22 Juni 1945, rumusan Panitia Sembilan")],
 "UUD 1945":[("Pasal 1 ayat (3)","Negara Indonesia adalah negara hukum"),("Pasal 27 ayat (3)","Hak dan kewajiban ikut serta dalam upaya pembelaan negara"),("Pasal 28A–28J","Hak asasi manusia"),("Pasal 33","Perekonomian disusun sebagai usaha bersama berdasar asas kekeluargaan"),("Pasal 36","Bahasa negara ialah bahasa Indonesia"),("Pasal 37 ayat (5)","Bentuk NKRI tidak dapat diubah"),("Jumlah amandemen","Empat kali, 1999–2002")],
 "Sejarah Nasional":[("20 Mei 1908","Berdirinya Budi Utomo"),("28 Oktober 1928","Sumpah Pemuda"),("16 Agustus 1945","Peristiwa Rengasdengklok"),("18 Agustus 1945","PPKI mengesahkan UUD 1945"),("10 November 1945","Pertempuran Surabaya"),("13 Desember 1957","Deklarasi Djuanda"),("27 Desember 1949","Pengakuan kedaulatan (KMB)")],
 "Lembaga Negara":[("MK","Menguji UU terhadap UUD, memutus sengketa kewenangan lembaga, pembubaran parpol, sengketa hasil pemilu"),("MA","Mengadili kasasi dan menguji peraturan di bawah UU terhadap UU"),("BPK","Memeriksa pengelolaan dan tanggung jawab keuangan negara"),("KY","Mengusulkan pengangkatan hakim agung dan menjaga kehormatan hakim"),("DPD","Mewakili daerah, mengajukan RUU terkait otonomi daerah"),("MPR","Mengubah dan menetapkan UUD, melantik presiden")],
 "Tokoh Nasional":[("dr. Wahidin Sudirohusodo","Penggagas Budi Utomo"),("Ki Hajar Dewantara","Bapak Pendidikan Nasional, Taman Siswa"),("Mohammad Yamin","Pengusul dasar negara 29 Mei 1945"),("Fatmawati","Penjahit bendera pusaka"),("Bung Tomo","Penggerak arek-arek Surabaya"),("Ir. Djuanda","Pencetus Deklarasi Djuanda")],
 "Istilah Pemerintahan":[("Desentralisasi","Penyerahan urusan pemerintahan dari pusat ke daerah otonom"),("Dekonsentrasi","Pelimpahan sebagian urusan pusat kepada gubernur sebagai wakil pemerintah pusat"),("Tugas pembantuan","Penugasan dari pusat ke daerah untuk melaksanakan sebagian urusan"),("BerAKHLAK","Core values ASN"),("Sistem merit","Manajemen ASN berdasarkan kualifikasi, kompetensi, dan kinerja"),("SPBE","Sistem Pemerintahan Berbasis Elektronik")],
 "Rumus Matematika":[("Jarak","J = K × W"),("Persentase untung","(Jual − Beli) / Beli × 100%"),("Bunga tunggal","B = M × p × t"),("Luas lingkaran","πr²"),("Rata-rata gabungan","(n₁x₁ + n₂x₂) / (n₁ + n₂)"),("Berbalik nilai","p₁ × w₁ = p₂ × w₂")],
 "Kosakata Verbal":[("Nisbi","Relatif, tidak mutlak"),("Absah","Sah, valid"),("Konklusi","Kesimpulan"),("Laten","Tersembunyi, terpendam"),("Prolog >< ?","Epilog"),("Fiktif >< ?","Faktual"),("Pandir","Bodoh"),("Insinuasi","Tuduhan tersembunyi, sindiran")],
 "Konsep Penting SKB":[("UU ASN terbaru","UU 20/2023"),("SPIP","PP 60/2008, lima unsur pengendalian intern"),("Kearsipan","UU 43/2009"),("Keuangan Negara","UU 17/2003"),("Administrasi Pemerintahan","UU 30/2014"),("Pelayanan Publik","UU 25/2009")],
}
cards = []
for deck, items in F.items():
    for j, (f, b) in enumerate(items, 1):
        cards.append({"id": f"FC-{deck[:3].upper()}-{j:02d}", "deck": deck, "front": f, "back": b})

os.makedirs(OUT, exist_ok=True)
json.dump(M, open(os.path.join(OUT, "learning-modules.json"), "w"), ensure_ascii=False, indent=1)
json.dump(cards, open(os.path.join(OUT, "flashcards.json"), "w"), ensure_ascii=False, indent=1)
print(len(M), len(cards))
