"""Generator bank soal Teman CPNS -> src/data/*.json
Jalankan: python3 scripts/gen_questions.py
Soal TWK/TKP/SKB/TIU verbal ditulis manual; TIU numerik & figural dibangkitkan
secara deterministik (seed tetap) agar bervariasi dan jawabannya terverifikasi.
"""
import json, random, os
from fractions import Fraction

OUT = os.path.join(os.path.dirname(__file__), "..", "src", "data")
rng = random.Random(2026)
D = {"m": "Mudah", "s": "Sedang", "h": "Sulit"}


def place(correct, wrongs):
    """Acak posisi jawaban benar; return (options, answerIndex)."""
    opts = [correct] + wrongs[:4]
    rng.shuffle(opts)
    return opts, opts.index(correct)


# ---------------------------------------------------------------- TWK
TWK = [
 ("Nasionalisme","Organisasi Budi Utomo didirikan pada 20 Mei 1908. Tanggal tersebut kini diperingati sebagai…","Hari Kebangkitan Nasional",["Hari Sumpah Pemuda","Hari Pahlawan","Hari Pendidikan Nasional","Hari Lahir Pancasila"],"Budi Utomo (dr. Sutomo dkk., STOVIA) dianggap tonggak kebangkitan nasional; 20 Mei ditetapkan sebagai Hari Kebangkitan Nasional.","m","Sejarah Pergerakan Nasional"),
 ("Nasionalisme","Ikrar Sumpah Pemuda dibacakan pada Kongres Pemuda II tanggal…","28 Oktober 1928",["20 Mei 1908","17 Agustus 1945","10 November 1945","1 Juni 1945"],"Kongres Pemuda II di Batavia, 27–28 Oktober 1928, menghasilkan ikrar satu tanah air, satu bangsa, dan menjunjung bahasa persatuan.","m","Sumpah Pemuda"),
 ("Nasionalisme","Peristiwa pengamanan Soekarno–Hatta oleh golongan muda agar tidak terpengaruh Jepang menjelang proklamasi dikenal sebagai peristiwa…","Rengasdengklok",["Linggarjati","Renville","Bandung Lautan Api","Ambarawa"],"Pada 16 Agustus 1945 golongan muda membawa Soekarno–Hatta ke Rengasdengklok untuk mendesak proklamasi segera.","m","Proklamasi"),
 ("Nasionalisme","Naskah proklamasi diketik oleh…","Sayuti Melik",["Sukarni","B.M. Diah","Ahmad Soebardjo","Fatmawati"],"Naskah tulisan tangan Soekarno diketik oleh Sayuti Melik dengan beberapa perubahan, lalu ditandatangani Soekarno–Hatta.","s","Proklamasi"),
 ("Nasionalisme","Perumusan naskah proklamasi dilakukan di rumah…","Laksamana Tadashi Maeda",["Ahmad Soebardjo","Djiauw Kie Siong","Soekarno di Pegangsaan Timur 56","Mohammad Hatta"],"Naskah dirumuskan di rumah Laksamana Maeda, Jl. Imam Bonjol No. 1 Jakarta, pada dini hari 17 Agustus 1945.","s","Proklamasi"),
 ("Nasionalisme","Pertempuran 10 November 1945 di Surabaya yang kemudian diperingati sebagai Hari Pahlawan dipicu antara lain oleh tewasnya…","Brigjen A.W.S. Mallaby",["Jenderal Spoor","Letjen Imamura","Van Mook","Jenderal Christison"],"Tewasnya Brigjen Mallaby (30 Oktober 1945) memicu ultimatum Inggris yang ditolak arek-arek Surabaya hingga pecah pertempuran 10 November.","s","Revolusi Fisik"),
 ("Nasionalisme","Sikap yang paling mencerminkan nasionalisme dalam kehidupan sehari-hari adalah…","Mengutamakan produk dalam negeri tanpa merendahkan bangsa lain",["Menolak semua budaya asing","Hanya bergaul dengan suku sendiri","Mengutamakan kepentingan daerah di atas nasional","Menganggap bangsa sendiri paling unggul"],"Nasionalisme Indonesia bersifat terbuka: cinta tanah air tanpa chauvinisme. Mencintai produk dalam negeri adalah wujud konkret.","m","Konsep Nasionalisme"),
 ("Nasionalisme","Tokoh yang dikenal sebagai Bapak Pendidikan Nasional dengan semboyan 'Tut Wuri Handayani' adalah…","Ki Hajar Dewantara",["Dewi Sartika","R.A. Kartini","K.H. Ahmad Dahlan","Douwes Dekker"],"Ki Hajar Dewantara mendirikan Taman Siswa (1922); hari lahirnya, 2 Mei, diperingati sebagai Hari Pendidikan Nasional.","m","Tokoh Nasional"),
 ("Nasionalisme","Organisasi Indische Partij (1912) didirikan oleh tiga serangkai, yaitu…","Douwes Dekker, Tjipto Mangoenkoesoemo, Soewardi Soerjaningrat",["Soekarno, Hatta, Sjahrir","H.O.S. Tjokroaminoto, Agus Salim, Abdul Muis","dr. Sutomo, Wahidin, Gunawan","Semaun, Darsono, Tan Malaka"],"Indische Partij adalah organisasi politik pertama yang terang-terangan menuntut kemerdekaan Hindia.","s","Sejarah Pergerakan Nasional"),
 ("Integritas","Seorang pegawai menerima hadiah dari rekanan proyek yang sedang ia tangani. Menurut UU Tipikor, hadiah tersebut termasuk…","Gratifikasi yang wajib dilaporkan ke KPK",["Rezeki pribadi","Bonus kinerja yang sah","Tanda terima kasih wajar","Hak pegawai"],"Gratifikasi terkait jabatan wajib dilaporkan ke KPK paling lambat 30 hari kerja (UU 20/2001 Pasal 12C).","m","UU Tipikor"),
 ("Integritas","Batas waktu pelaporan gratifikasi kepada KPK sejak diterima adalah…","30 hari kerja",["7 hari kerja","14 hari kerja","60 hari kerja","90 hari kalender"],"Pasal 12C UU 20/2001: penerima wajib melapor paling lambat 30 hari kerja sejak gratifikasi diterima.","s","UU Tipikor"),
 ("Integritas","Nilai dasar ASN 'BerAKHLAK' merupakan akronim dari…","Berorientasi Pelayanan, Akuntabel, Kompeten, Harmonis, Loyal, Adaptif, Kolaboratif",["Beriman, Amanah, Kreatif, Hebat, Loyal, Aktif, Kompak","Bersih, Adil, Kompeten, Hormat, Loyal, Aman, Kreatif","Berani, Akurat, Kuat, Handal, Lugas, Andal, Komunikatif","Berbudaya, Arif, Kerja keras, Hemat, Lurus, Aspiratif, Kritis"],"Core values ASN BerAKHLAK diluncurkan Presiden pada 27 Juli 2021.","m","Core Values ASN"),
 ("Integritas","Prinsip akuntabilitas dalam pemerintahan berarti…","Setiap kegiatan dan hasilnya dapat dipertanggungjawabkan kepada publik",["Pegawai bebas menentukan anggaran","Keputusan hanya diketahui pimpinan","Laporan cukup dibuat saat diminta","Kinerja dinilai dari kedekatan dengan atasan"],"Akuntabilitas = kewajiban mempertanggungjawabkan kinerja dan penggunaan sumber daya kepada pemberi mandat/publik.","m","Good Governance"),
 ("Integritas","Konflik kepentingan terjadi ketika…","Kepentingan pribadi berpotensi memengaruhi keputusan dalam jabatan",["Dua pegawai berbeda pendapat","Atasan memberi tugas tambahan","Pegawai mengikuti organisasi profesi","Instansi bekerja sama dengan swasta"],"Konflik kepentingan (UU 30/2014 Administrasi Pemerintahan) membuat pejabat wajib menghindari keputusan yang menguntungkan dirinya.","s","Etika Pemerintahan"),
 ("Integritas","Lembaga independen yang berwenang memeriksa pengelolaan dan tanggung jawab keuangan negara adalah…","BPK",["KPK","BPKP","OJK","Ombudsman"],"Pasal 23E UUD 1945: BPK memeriksa pengelolaan dan tanggung jawab keuangan negara, bebas dan mandiri.","m","Lembaga Negara"),
 ("Integritas","Ombudsman Republik Indonesia berwenang mengawasi…","Penyelenggaraan pelayanan publik dan dugaan maladministrasi",["Tindak pidana korupsi","Pemilu","Peredaran uang","Perbankan"],"UU 37/2008: Ombudsman mengawasi pelayanan publik oleh penyelenggara negara dan pemerintahan.","s","Lembaga Negara"),
 ("Bela Negara","Dasar konstitusional hak dan kewajiban warga negara ikut serta dalam upaya pembelaan negara terdapat pada…","Pasal 27 ayat (3) UUD 1945",["Pasal 28 UUD 1945","Pasal 31 ayat (1) UUD 1945","Pasal 33 UUD 1945","Pasal 1 ayat (3) UUD 1945"],"Pasal 27 (3): 'Setiap warga negara berhak dan wajib ikut serta dalam upaya pembelaan negara.' Lihat juga Pasal 30 ayat (1).","m","UUD 1945"),
 ("Bela Negara","Sistem pertahanan dan keamanan Indonesia menurut Pasal 30 UUD 1945 disebut…","Sistem Pertahanan dan Keamanan Rakyat Semesta (Sishankamrata)",["Sistem Pertahanan Terpadu","Wajib Militer Nasional","Pertahanan Garis Depan","Sistem Keamanan Kolektif"],"Sishankamrata menempatkan TNI dan Polri sebagai kekuatan utama dan rakyat sebagai kekuatan pendukung.","s","Ketahanan Nasional"),
 ("Bela Negara","Wawasan Nusantara secara konseptual dideklarasikan pertama kali melalui…","Deklarasi Djuanda 13 Desember 1957",["Sumpah Pemuda 1928","Konferensi Meja Bundar 1949","UNCLOS 1982","Dekrit Presiden 1959"],"Deklarasi Djuanda menyatakan laut di antara pulau sebagai wilayah Indonesia; diakui internasional dalam UNCLOS 1982.","s","Wawasan Nusantara"),
 ("Bela Negara","Kondisi dinamis bangsa yang berisi keuletan dan ketangguhan menghadapi ancaman, gangguan, hambatan, dan tantangan disebut…","Ketahanan nasional",["Wawasan nusantara","Politik luar negeri","Integrasi nasional","Bela negara"],"Ketahanan nasional mencakup asta gatra: 3 gatra alamiah (geografi, demografi, SDA) dan 5 gatra sosial (ipoleksosbudhankam).","m","Ketahanan Nasional"),
 ("Bela Negara","Yang termasuk gatra alamiah (trigatra) dalam ketahanan nasional adalah…","Geografi, demografi, sumber kekayaan alam",["Ideologi, politik, ekonomi","Sosial, budaya, hankam","Politik, demografi, budaya","Ekonomi, geografi, hukum"],"Trigatra: letak geografis, keadaan penduduk, kekayaan alam. Pancagatra: ideologi, politik, ekonomi, sosial budaya, hankam.","s","Ketahanan Nasional"),
 ("Bela Negara","Contoh bela negara non-fisik bagi seorang ASN adalah…","Bekerja profesional dan menolak praktik korupsi",["Mengikuti latihan militer wajib","Bergabung dengan milisi","Mengangkat senjata saat damai","Menjaga perbatasan bersenjata"],"Bela negara non-fisik diwujudkan lewat profesi: disiplin, integritas, dan pengabdian sesuai bidang.","m","Konsep Bela Negara"),
 ("Bela Negara","Ancaman yang berbentuk penyebaran hoaks dan propaganda melalui media sosial dikategorikan sebagai ancaman…","Nonmiliter",["Militer","Hibrida bersenjata","Agresi","Konvensional"],"UU 3/2002 membagi ancaman militer dan nonmiliter; ancaman siber dan ideologis termasuk nonmiliter.","m","Ancaman Nasional"),
 ("Pilar Negara","Sidang BPUPKI pertama berlangsung pada tanggal…","29 Mei – 1 Juni 1945",["10–17 Juli 1945","18 Agustus 1945","22 Juni 1945","1–7 Juli 1945"],"Sidang I BPUPKI membahas dasar negara; Soekarno menyampaikan pidato 'Pancasila' pada 1 Juni 1945.","m","Sejarah Perumusan Pancasila"),
 ("Pilar Negara","Piagam Jakarta dirumuskan oleh Panitia Sembilan pada…","22 Juni 1945",["1 Juni 1945","18 Agustus 1945","17 Agustus 1945","29 Mei 1945"],"Piagam Jakarta 22 Juni 1945 kemudian menjadi rancangan Pembukaan UUD; tujuh kata sila pertama diubah pada 18 Agustus 1945.","m","Sejarah Perumusan Pancasila"),
 ("Pilar Negara","Tokoh yang berperan melobi perubahan tujuh kata dalam Piagam Jakarta pada 18 Agustus 1945 adalah…","Mohammad Hatta",["Soekarno","Muhammad Yamin","Soepomo","A.A. Maramis"],"Hatta menerima keberatan dari wakil Indonesia timur, lalu berkonsultasi dengan tokoh Islam (Ki Bagus Hadikusumo, Kasman, dll.).","s","Sejarah Perumusan Pancasila"),
 ("Pilar Negara","Alinea keempat Pembukaan UUD 1945 memuat…","Tujuan negara dan dasar negara Pancasila",["Pernyataan kemerdekaan semua bangsa","Perjuangan pergerakan kemerdekaan","Pengakuan rahmat Tuhan atas kemerdekaan","Bentuk negara federal"],"Alinea IV: melindungi segenap bangsa, memajukan kesejahteraan umum, mencerdaskan kehidupan bangsa, ikut ketertiban dunia, serta rumusan Pancasila.","m","Pembukaan UUD 1945"),
 ("Pilar Negara","Pasal 1 ayat (3) UUD NRI 1945 menyatakan bahwa…","Negara Indonesia adalah negara hukum",["Kedaulatan berada di tangan rakyat","Indonesia adalah negara kesatuan berbentuk republik","Presiden memegang kekuasaan pemerintahan","Bendera negara ialah Sang Merah Putih"],"Ayat (1) negara kesatuan berbentuk republik; ayat (2) kedaulatan rakyat; ayat (3) negara hukum (hasil amandemen ketiga).","m","UUD 1945"),
 ("Pilar Negara","Amandemen UUD 1945 dilakukan sebanyak empat kali pada kurun waktu…","1999–2002",["1998–2001","1945–1949","2000–2004","1959–1966"],"Perubahan I (1999), II (2000), III (2001), IV (2002) oleh MPR.","m","UUD 1945"),
 ("Pilar Negara","Semboyan Bhinneka Tunggal Ika berasal dari kitab…","Sutasoma karya Mpu Tantular",["Negarakertagama karya Mpu Prapanca","Arjunawiwaha karya Mpu Kanwa","Pararaton","Bharatayuddha karya Mpu Sedah"],"Kutipan 'Bhinneka tunggal ika tan hana dharma mangrwa' terdapat dalam Kakawin Sutasoma (abad ke-14, Majapahit).","m","Bhinneka Tunggal Ika"),
 ("Pilar Negara","Lembaga negara yang berwenang menguji undang-undang terhadap UUD adalah…","Mahkamah Konstitusi",["Mahkamah Agung","Komisi Yudisial","DPR","MPR"],"Pasal 24C UUD 1945; MA menguji peraturan di bawah undang-undang terhadap undang-undang.","m","Lembaga Negara"),
 ("Pilar Negara","Masa jabatan anggota Komisi Yudisial sesuai undang-undang adalah…","5 tahun",["4 tahun","6 tahun","7 tahun","10 tahun"],"UU 18/2011: anggota KY memegang jabatan 5 tahun dan dapat dipilih kembali untuk satu periode.","h","Lembaga Negara"),
 ("Pilar Negara","Pasal UUD 1945 yang mengatur bahwa bumi, air, dan kekayaan alam dikuasai negara untuk kemakmuran rakyat adalah…","Pasal 33 ayat (3)",["Pasal 27 ayat (2)","Pasal 31 ayat (4)","Pasal 34 ayat (1)","Pasal 28H ayat (1)"],"Pasal 33 ayat (3) merupakan dasar demokrasi ekonomi dan pengelolaan SDA.","s","UUD 1945"),
 ("Pilar Negara","Ketentuan tentang Hak Asasi Manusia dalam UUD 1945 hasil amandemen terdapat pada…","Bab XA Pasal 28A–28J",["Bab X Pasal 26–28","Bab XI Pasal 29","Bab XIII Pasal 31–32","Bab XIV Pasal 33–34"],"Bab XA ditambahkan pada Perubahan Kedua (2000).","s","HAM"),
 ("Pilar Negara","Sistem pemerintahan Indonesia berdasarkan UUD NRI 1945 adalah…","Presidensial",["Parlementer","Semi-presidensial","Monarki konstitusional","Kolegial"],"Presiden adalah kepala negara sekaligus kepala pemerintahan, dipilih langsung dan tidak bertanggung jawab kepada DPR.","m","Sistem Pemerintahan"),
 ("Bahasa Negara","Bahasa Indonesia ditetapkan sebagai bahasa negara dalam…","Pasal 36 UUD 1945",["Pasal 35 UUD 1945","Pasal 32 ayat (2) UUD 1945","Sumpah Pemuda butir pertama","Pasal 36A UUD 1945"],"Pasal 36: 'Bahasa Negara ialah Bahasa Indonesia.' Sumpah Pemuda menjadikannya bahasa persatuan.","m","Kedudukan Bahasa"),
 ("Bahasa Negara","Penulisan kata berikut yang baku adalah…","Apotek",["Apotik","Aktifitas","Analisa","Nasehat"],"Bentuk baku: apotek, aktivitas, analisis, nasihat (KBBI).","m","Bahasa Baku"),
 ("Bahasa Negara","Kalimat efektif di antara pilihan berikut adalah…","Para peserta diharap hadir tepat waktu.",["Para peserta-peserta diharap hadir tepat waktu.","Bagi para peserta diharap hadir tepat waktu.","Para hadirin sekalian diharap hadir tepat waktu.","Kepada para peserta-peserta diharapkan hadir."],"'Para' sudah bermakna jamak sehingga tidak perlu kata ulang; kata depan 'bagi/kepada' di awal membuat kalimat tidak bersubjek.","s","Kalimat Efektif"),
 ("Bahasa Negara","Penulisan huruf kapital yang benar menurut EYD adalah…","Kami berangkat ke Jawa Barat bulan Juli.",["Kami berangkat ke jawa barat bulan juli.","Kami Berangkat ke Jawa Barat Bulan Juli.","kami berangkat ke Jawa barat bulan Juli.","Kami berangkat ke Jawa Barat Bulan juli."],"Nama geografis dan nama bulan diawali huruf kapital; kata umum tidak.","m","EYD"),
 ("Bahasa Negara","Penggunaan tanda baca yang tepat terdapat pada kalimat…","Ia membeli buku, pena, dan penggaris.",["Ia membeli: buku, pena, dan penggaris.","Ia membeli buku pena, dan penggaris.","Ia, membeli buku, pena dan, penggaris.","Ia membeli buku; pena; penggaris."],"Koma memisahkan unsur perincian; titik dua tidak dipakai bila perincian merupakan pelengkap yang mengakhiri pernyataan.","s","EYD"),
 ("Bahasa Negara","Unsur yang wajib ada dalam surat dinas resmi instansi pemerintah adalah…","Kop surat, nomor, perihal, isi, dan tanda tangan pejabat",["Gambar dan stiker instansi","Salam pembuka bahasa daerah","Tanda tangan seluruh pegawai","Catatan kaki referensi"],"Tata naskah dinas mensyaratkan kepala (kop), nomor, sifat/lampiran/hal, batang tubuh, dan kaki (tanda tangan, nama jabatan).","s","Dokumen Resmi"),
]

# ---------------------------------------------------------------- TKP (skor 1-5 per opsi)
TKP = [
 ("Pelayanan Publik","Seorang warga datang 5 menit sebelum loket tutup dengan berkas yang lengkap. Sikap Anda…",[("Melayani hingga selesai dengan ramah",5),("Melayani tetapi meminta ia bergegas",4),("Menerima berkas dan memintanya kembali besok",3),("Menyarankan datang lebih pagi besok",2),("Menolak karena loket akan tutup",1)]),
 ("Pelayanan Publik","Pemohon layanan marah karena prosedur dianggap berbelit. Anda…",[("Mendengarkan, menjelaskan alur dengan tenang, dan membantu melengkapinya",5),("Menjelaskan prosedur sesuai SOP",4),("Memberikan brosur prosedur",3),("Meminta ia bertanya ke petugas informasi",2),("Mengabaikan karena prosedur sudah ditetapkan",1)]),
 ("Pelayanan Publik","Anda menemukan bahwa formulir layanan sulit dipahami masyarakat lanjut usia. Anda…",[("Mengusulkan formulir sederhana dan sementara membantu mereka mengisi",5),("Membantu mengisi formulir saat diminta",4),("Melaporkan keluhan kepada atasan",3),("Meminta keluarga mereka mendampingi",2),("Membiarkan karena formulir sudah standar",1)]),
 ("Pelayanan Publik","Kerabat Anda meminta didahulukan dalam antrean layanan. Anda…",[("Menolak dengan sopan dan memintanya mengikuti antrean",5),("Menjelaskan aturan antrean kepadanya",4),("Meminta rekan lain yang melayani",3),("Melayani diam-diam saat sepi",2),("Langsung mendahulukannya",1)]),
 ("Pelayanan Publik","Sistem layanan daring kantor sedang gangguan sementara antrean panjang. Anda…",[("Beralih ke prosedur manual darurat dan menginformasikan warga",5),("Mengumumkan gangguan dan perkiraan waktu pulih",4),("Meminta warga menunggu",3),("Meminta warga datang di hari lain",2),("Menutup layanan",1)]),
 ("Pelayanan Publik","Masyarakat memberi masukan bahwa jam layanan kurang sesuai kebutuhan pekerja. Anda…",[("Menganalisis data kunjungan dan mengusulkan jam layanan alternatif",5),("Meneruskan masukan kepada pimpinan",4),("Mencatat masukan",3),("Menjelaskan bahwa jam layanan sudah ketentuan",2),("Tidak menanggapi",1)]),
 ("Pelayanan Publik","Seorang penyandang disabilitas kesulitan mengakses lantai dua kantor layanan. Anda…",[("Melayaninya di lantai satu dan mengusulkan fasilitas aksesibel",5),("Membantunya naik ke lantai dua",4),("Memanggil petugas lantai dua",3),("Memintanya mewakilkan kepada orang lain",2),("Memintanya kembali bersama pendamping",1)]),
 ("Pelayanan Publik","Anda keliru memberikan informasi kepada pemohon sehingga ia harus datang lagi. Anda…",[("Meminta maaf, menghubunginya, dan memastikan prosesnya dipercepat",5),("Meminta maaf saat ia datang lagi",4),("Memperbaiki informasi untuk pemohon berikutnya",3),("Menyalahkan informasi dari atasan",2),("Diam saja",1)]),
 ("Jejaring Kerja","Anda ditugaskan membangun kerja sama dengan instansi lain yang belum Anda kenal. Anda…",[("Mempelajari tugas instansi tersebut lalu menghubungi dan menjadwalkan pertemuan",5),("Mengirim surat resmi permohonan kerja sama",4),("Meminta kontak dari rekan kerja",3),("Menunggu instansi lain menghubungi",2),("Menyerahkan tugas kepada rekan",1)]),
 ("Jejaring Kerja","Rekan dari divisi lain meminta data yang Anda miliki untuk keperluan dinas. Anda…",[("Memberikan data sesuai prosedur dan siap membantu bila perlu",5),("Memberikan data setelah izin atasan",4),("Memberikan sebagian data",3),("Memintanya mencari sendiri",2),("Menolak karena itu data Anda",1)]),
 ("Jejaring Kerja","Dalam forum lintas instansi, pendapat Anda ditolak mayoritas peserta. Anda…",[("Menerima keputusan dan mendukung pelaksanaannya",5),("Menerima sambil mencatat risiko untuk dievaluasi",4),("Diam dan mengikuti saja",3),("Mengulang argumen hingga forum berakhir",2),("Meninggalkan forum",1)]),
 ("Jejaring Kerja","Tim proyek Anda terdiri dari anggota berbagai latar belakang yang sulit berkoordinasi. Anda…",[("Mengusulkan pembagian peran dan jadwal koordinasi rutin",5),("Mengajak anggota berdiskusi informal",4),("Mengerjakan bagian Anda dengan baik",3),("Melaporkan kesulitan kepada atasan",2),("Bekerja sendiri tanpa koordinasi",1)]),
 ("Jejaring Kerja","Mitra kerja sama terlambat mengirim bahan sehingga program terancam mundur. Anda…",[("Menghubungi mitra, mencari solusi bersama, dan menyusun rencana cadangan",5),("Mengingatkan mitra secara resmi",4),("Menunggu sambil menyiapkan bagian lain",3),("Melaporkan keterlambatan saja",2),("Menyalahkan mitra di rapat",1)]),
 ("Jejaring Kerja","Anda mendapat informasi pelatihan bermanfaat dari jejaring profesi. Anda…",[("Membagikannya kepada rekan yang relevan",5),("Membagikan di grup kantor",4),("Mengikutinya sendiri",3),("Menyimpan untuk nanti",2),("Mengabaikannya",1)]),
 ("Jejaring Kerja","Atasan meminta Anda mewakili kantor di rapat koordinasi daerah. Anda…",[("Mempersiapkan bahan, hadir, dan melaporkan hasilnya",5),("Hadir dan mencatat hasil rapat",4),("Hadir sesuai undangan",3),("Meminta rekan lain menggantikan",2),("Menolak karena bukan tugas Anda",1)]),
 ("Jejaring Kerja","Anda baru dipindahtugaskan ke unit baru. Langkah pertama Anda…",[("Memperkenalkan diri dan mempelajari proses kerja dari rekan",5),("Membaca SOP unit",4),("Menunggu arahan atasan",3),("Bekerja seperti di unit lama",2),("Menjaga jarak dari rekan baru",1)]),
 ("Sosial Budaya","Anda ditempatkan di daerah dengan adat yang sangat berbeda. Anda…",[("Mempelajari dan menghormati adat setempat sambil bekerja sesuai aturan",5),("Menghormati adat setempat",4),("Beradaptasi seperlunya",3),("Bergaul dengan sesama pendatang saja",2),("Meminta pindah tugas",1)]),
 ("Sosial Budaya","Rekan kerja berbeda agama sedang merayakan hari raya. Anda…",[("Mengucapkan selamat dan menggantikan tugasnya bila diperlukan",5),("Mengucapkan selamat",4),("Menghormati tanpa berkomentar",3),("Tidak peduli",2),("Menyindir perbedaan tersebut",1)]),
 ("Sosial Budaya","Ada candaan bernada SARA di grup percakapan kantor. Anda…",[("Mengingatkan dengan sopan bahwa candaan itu tidak pantas",5),("Mengingatkan pengirim secara pribadi",4),("Tidak menanggapi",3),("Keluar dari grup",2),("Ikut tertawa",1)]),
 ("Sosial Budaya","Warga sekitar kantor mengadakan kerja bakti hari Minggu. Anda…",[("Ikut serta dan mengajak rekan kerja",5),("Ikut serta",4),("Menyumbang konsumsi tanpa hadir",3),("Hadir sebentar",2),("Tidak ikut karena hari libur",1)]),
 ("Sosial Budaya","Dalam tim terdapat anggota yang sulit berbahasa Indonesia baku karena latar daerah. Anda…",[("Berkomunikasi dengan sabar dan membantunya beradaptasi",5),("Memaklumi dan berbicara perlahan",4),("Berkomunikasi seperlunya",3),("Meminta orang lain menerjemahkan",2),("Menertawakan logatnya",1)]),
 ("Sosial Budaya","Program kantor ditolak sebagian masyarakat karena dianggap bertentangan dengan kebiasaan lokal. Anda…",[("Berdialog dengan tokoh masyarakat untuk menyesuaikan pendekatan program",5),("Melakukan sosialisasi ulang",4),("Menunda program",3),("Tetap melaksanakan sesuai rencana",2),("Membatalkan program",1)]),
 ("Sosial Budaya","Rekan baru berasal dari suku yang berbeda dan tampak canggung. Anda…",[("Menyapa, mengajaknya bergabung, dan membantu orientasi",5),("Menyapanya dengan ramah",4),("Bersikap biasa saja",3),("Menunggu ia menyapa lebih dulu",2),("Menghindarinya",1)]),
 ("Sosial Budaya","Pembagian bantuan sosial diminta didahulukan untuk kelompok etnis tertentu. Anda…",[("Membagikan berdasarkan kriteria kelayakan yang adil",5),("Menjelaskan bahwa pembagian sesuai data",4),("Meminta keputusan atasan",3),("Mengikuti permintaan agar tidak ribut",2),("Menolak membagikan bantuan",1)]),
 ("Teknologi Informasi dan Komunikasi","Kantor menerapkan aplikasi kerja baru yang belum Anda kuasai. Anda…",[("Mempelajarinya dengan aktif dan membantu rekan yang kesulitan",5),("Mengikuti pelatihan yang disediakan",4),("Mempelajari saat dibutuhkan",3),("Meminta rekan mengerjakan bagian aplikasi",2),("Tetap memakai cara lama",1)]),
 ("Teknologi Informasi dan Komunikasi","Anda menerima email berisi tautan meminta kata sandi akun kantor. Anda…",[("Tidak mengklik, melaporkan ke tim TI sebagai phishing",5),("Menghapus email tersebut",4),("Menanyakan ke rekan apakah aman",3),("Membuka tautan untuk memeriksa",2),("Mengisi kata sandi",1)]),
 ("Teknologi Informasi dan Komunikasi","Rekan meminjam akun aplikasi kepegawaian Anda karena akunnya terkunci. Anda…",[("Menolak dan membantunya menghubungi admin",5),("Menolak dengan sopan",4),("Mengoperasikan sendiri untuknya",3),("Meminjamkan sebentar sambil diawasi",2),("Memberikan kata sandi",1)]),
 ("Teknologi Informasi dan Komunikasi","Atasan meminta laporan data bulanan yang selama ini dikerjakan manual berjam-jam. Anda…",[("Membuat templat otomatis berbasis spreadsheet agar lebih cepat",5),("Mengerjakan manual dengan teliti",4),("Meminta bantuan rekan",3),("Mengerjakan mendekati tenggat",2),("Meminta tenggat diperpanjang",1)]),
 ("Teknologi Informasi dan Komunikasi","Anda melihat berita viral tentang kebijakan instansi yang belum jelas sumbernya. Anda…",[("Memverifikasi ke sumber resmi sebelum menanggapi",5),("Tidak menyebarkannya",4),("Menanyakan kepada rekan",3),("Membagikan dengan catatan 'belum pasti'",2),("Langsung membagikan",1)]),
 ("Teknologi Informasi dan Komunikasi","Data pribadi masyarakat tersimpan di laptop kantor yang akan Anda bawa dinas. Anda…",[("Memastikan file terenkripsi dan laptop terkunci kata sandi",5),("Memindahkan data ke server kantor",4),("Menjaga laptop agar tidak hilang",3),("Menyimpan salinan di flashdisk pribadi",2),("Membiarkan apa adanya",1)]),
 ("Teknologi Informasi dan Komunikasi","Instansi meluncurkan layanan digital, tetapi banyak warga belum paham. Anda…",[("Membuat panduan sederhana dan membuka pendampingan",5),("Menjelaskan saat warga bertanya",4),("Membagikan tautan panduan",3),("Meminta warga belajar sendiri",2),("Kembali ke layanan manual",1)]),
 ("Teknologi Informasi dan Komunikasi","Anda diminta mengelola media sosial instansi. Anda…",[("Menyusun konten informatif terjadwal dan merespons warga dengan cepat",5),("Mengunggah informasi resmi secara rutin",4),("Mengunggah bila ada kegiatan",3),("Menyalin konten instansi lain",2),("Jarang membuka akun",1)]),
 ("Profesionalisme","Anda diberi tugas mendesak saat pekerjaan lain menumpuk. Anda…",[("Menyusun prioritas, mengomunikasikan tenggat, dan menyelesaikan bertahap",5),("Mengerjakan tugas mendesak lebih dulu",4),("Lembur menyelesaikan semua",3),("Meminta tugas dialihkan",2),("Menolak tugas",1)]),
 ("Profesionalisme","Atasan memberikan kritik keras atas laporan Anda. Anda…",[("Menerima, meminta masukan rinci, dan memperbaiki",5),("Memperbaiki laporan",4),("Menerima dengan diam",3),("Membela diri",2),("Tersinggung dan menunda",1)]),
 ("Profesionalisme","Anda menemukan kesalahan dalam pekerjaan yang sudah Anda serahkan. Anda…",[("Segera melapor, memperbaiki, dan mencegah terulang",5),("Memperbaiki diam-diam",4),("Menunggu ada yang menyadari",3),("Berharap kesalahan tidak berdampak",2),("Menyalahkan rekan",1)]),
 ("Profesionalisme","Rekan sering datang terlambat dan pekerjaannya dibebankan kepada Anda. Anda…",[("Membicarakan baik-baik dengannya dan bila berlanjut melapor ke atasan",5),("Menegurnya secara pribadi",4),("Mengerjakan saja tugasnya",3),("Membicarakannya dengan rekan lain",2),("Ikut datang terlambat",1)]),
 ("Profesionalisme","Ada pelatihan pengembangan kompetensi di luar jam kerja. Anda…",[("Mengikuti dan menerapkan hasilnya dalam pekerjaan",5),("Mengikuti pelatihan",4),("Mengikuti bila diwajibkan",3),("Mencari alasan tidak ikut",2),("Menolak",1)]),
 ("Profesionalisme","Target kerja tim tidak tercapai. Sebagai anggota, Anda…",[("Mengevaluasi kontribusi diri dan mengusulkan perbaikan",5),("Ikut evaluasi tim",4),("Menunggu arahan berikutnya",3),("Menganggap itu tanggung jawab ketua",2),("Menyalahkan anggota lain",1)]),
 ("Profesionalisme","Atasan meminta Anda memalsukan tanggal pada dokumen. Anda…",[("Menolak dengan sopan dan menjelaskan risikonya",5),("Menolak",4),("Meminta perintah tertulis",3),("Melakukan karena takut",2),("Melakukannya tanpa pikir panjang",1)]),
 ("Profesionalisme","Pekerjaan Anda selesai lebih cepat dari jadwal. Anda…",[("Memeriksa ulang hasil lalu menawarkan bantuan kepada tim",5),("Memeriksa ulang hasil kerja",4),("Melaporkan ke atasan",3),("Bersantai sampai jam pulang",2),("Pulang lebih awal",1)]),
 ("Anti-Radikalisme","Anda menerima pesan berantai yang mengajak menolak Pancasila sebagai dasar negara. Anda…",[("Tidak menyebarkan, memberi klarifikasi, dan melaporkan ke kanal resmi",5),("Menghapus dan tidak menyebarkannya",4),("Mengabaikan pesan",3),("Membaca untuk tahu isinya",2),("Meneruskannya",1)]),
 ("Anti-Radikalisme","Rekan kerja mulai menunjukkan pandangan bahwa kelompok lain harus dimusuhi. Anda…",[("Mengajaknya berdialog dan melaporkan bila mengarah ke tindakan",5),("Mengajaknya berdiskusi tentang toleransi",4),("Menjaga jarak",3),("Membiarkan karena urusan pribadi",2),("Mendukung pandangannya",1)]),
 ("Anti-Radikalisme","Anda diundang kajian yang ternyata mengajarkan kekerasan atas nama agama. Anda…",[("Meninggalkan kegiatan dan melaporkannya ke pihak berwenang",5),("Meninggalkan kegiatan",4),("Tidak datang lagi",3),("Mengikuti sampai selesai",2),("Mengajak teman bergabung",1)]),
 ("Anti-Radikalisme","Di media sosial muncul ajakan aksi anarkis terhadap fasilitas umum. Anda…",[("Melaporkan konten dan mengingatkan untuk menyampaikan aspirasi secara damai",5),("Melaporkan konten",4),("Tidak ikut dan mengabaikan",3),("Menonton perkembangannya",2),("Ikut menyebarkan",1)]),
 ("Anti-Radikalisme","Siswa/warga binaan Anda bertanya mengapa Indonesia tidak berdasarkan satu agama. Anda…",[("Menjelaskan sejarah konsensus Pancasila sebagai pemersatu kemajemukan",5),("Menjelaskan bahwa itu ketentuan UUD",4),("Menyarankan ia bertanya kepada guru agama",3),("Menghindari topik",2),("Menyetujui bahwa seharusnya satu agama",1)]),
 ("Anti-Radikalisme","Anda menemukan buku bacaan di perpustakaan kantor yang memuat ujaran kebencian. Anda…",[("Melaporkan ke pengelola agar ditinjau sesuai ketentuan",5),("Menyampaikan ke rekan pengelola",4),("Tidak membacanya",3),("Membiarkan",2),("Merekomendasikan ke orang lain",1)]),
 ("Anti-Radikalisme","Terjadi perdebatan politik panas di kantor menjelang pemilu. Sebagai ASN, Anda…",[("Menjaga netralitas dan mengajak rekan kembali fokus bekerja",5),("Menjaga netralitas",4),("Tidak ikut berdebat",3),("Ikut berdebat sedikit",2),("Mengampanyekan calon tertentu",1)]),
 ("Anti-Radikalisme","Tetangga mengajak bergabung dengan kelompok yang menolak hormat bendera. Anda…",[("Menolak dan menjelaskan makna simbol negara",5),("Menolak dengan sopan",4),("Mengatakan akan pikir-pikir",3),("Datang untuk melihat",2),("Bergabung",1)]),
]

# ---------------------------------------------------------------- SKB
SKB = [
 ("Guru dan Tenaga Pendidikan","Kurikulum yang menekankan pembelajaran berdiferensiasi dan Profil Pelajar Pancasila adalah…","Kurikulum Merdeka",["KTSP","Kurikulum 2013 revisi 2016","Kurikulum Berbasis Kompetensi 2004","Kurikulum 1994"],"Kurikulum Merdeka menekankan materi esensial, projek penguatan profil pelajar Pancasila, dan diferensiasi.","m"),
 ("Guru dan Tenaga Pendidikan","Penilaian yang dilakukan selama proses pembelajaran untuk memperbaiki pembelajaran disebut…","Asesmen formatif",["Asesmen sumatif","Asesmen diagnostik","Ujian akhir","Penilaian portofolio akhir"],"Asesmen formatif memberi umpan balik berkelanjutan; sumatif menilai capaian di akhir.","m"),
 ("Guru dan Tenaga Pendidikan","Menurut taksonomi Bloom revisi, tingkat kognitif tertinggi adalah…","Mencipta (create)",["Mengevaluasi","Menganalisis","Menerapkan","Memahami"],"Urutan revisi Anderson & Krathwohl: mengingat, memahami, menerapkan, menganalisis, mengevaluasi, mencipta.","s"),
 ("Dokter","Tatalaksana awal syok anafilaktik pada dewasa adalah…","Epinefrin 0,3–0,5 mg intramuskular di paha anterolateral",["Antihistamin oral","Kortikosteroid oral","Parasetamol IV","Observasi saja"],"Epinefrin IM 0,01 mg/kgBB (maks 0,5 mg dewasa) adalah lini pertama anafilaksis.","s"),
 ("Dokter","Program JKN dikelola oleh…","BPJS Kesehatan",["Kementerian Kesehatan","BPJS Ketenagakerjaan","Dinas Kesehatan","Asuransi swasta"],"UU 24/2011: BPJS Kesehatan menyelenggarakan Jaminan Kesehatan Nasional.","m"),
 ("Dokter","Diagnosis hipertensi pada dewasa ditegakkan bila tekanan darah klinik berulang ≥…","140/90 mmHg",["120/80 mmHg","130/85 mmHg","160/100 mmHg","150/95 mmHg"],"Pedoman nasional (PERHI) menggunakan batas ≥140/90 mmHg pada pengukuran klinik.","m"),
 ("Perawat","Prinsip enam benar pemberian obat meliputi benar pasien, obat, dosis, waktu, rute, dan…","Dokumentasi",["Harga","Merek","Ruangan","Dokter"],"Enam benar: pasien, obat, dosis, waktu, rute, dokumentasi.","m"),
 ("Perawat","Urutan proses keperawatan yang benar adalah…","Pengkajian, diagnosis, perencanaan, implementasi, evaluasi",["Diagnosis, pengkajian, implementasi, perencanaan, evaluasi","Perencanaan, pengkajian, diagnosis, evaluasi, implementasi","Pengkajian, perencanaan, diagnosis, evaluasi, implementasi","Implementasi, evaluasi, pengkajian, diagnosis, perencanaan"],"Proses keperawatan terdiri atas lima tahap berurutan.","m"),
 ("Bidan","Kunjungan antenatal minimal sesuai standar terbaru Kemenkes adalah…","6 kali",["4 kali","2 kali","8 kali","10 kali"],"Standar ANC minimal 6 kali: 2 kali trimester I, 1 kali trimester II, 3 kali trimester III (Permenkes 21/2021).","s"),
 ("Bidan","Inisiasi Menyusu Dini (IMD) dilakukan dengan meletakkan bayi di dada ibu selama minimal…","1 jam",["10 menit","30 menit","3 jam","6 jam"],"IMD dilakukan kontak kulit ke kulit sedikitnya 1 jam segera setelah lahir.","m"),
 ("Pranata Komputer dan IT","Model jaringan OSI memiliki berapa lapisan?","7",["4","5","6","8"],"Physical, Data Link, Network, Transport, Session, Presentation, Application.","m"),
 ("Pranata Komputer dan IT","Perintah SQL untuk menghapus seluruh baris tabel tanpa menghapus strukturnya adalah…","TRUNCATE",["DROP","ALTER","REVOKE","CREATE"],"TRUNCATE mengosongkan tabel; DROP menghapus tabel beserta strukturnya.","s"),
 ("Pranata Komputer dan IT","Sistem Pemerintahan Berbasis Elektronik (SPBE) diatur dalam…","Perpres 95 Tahun 2018",["UU 11 Tahun 2008","PP 71 Tahun 2019","Perpres 39 Tahun 2019","UU 27 Tahun 2022"],"Perpres 95/2018 tentang SPBE. Satu Data Indonesia diatur Perpres 39/2019; PDP oleh UU 27/2022.","h"),
 ("Auditor","Bukti audit yang paling andal umumnya adalah…","Bukti yang diperoleh langsung oleh auditor dari pihak independen",["Keterangan lisan dari pihak yang diaudit","Fotokopi dokumen internal","Catatan pribadi pegawai","Laporan tidak bertanggal"],"Keandalan bukti meningkat bila diperoleh langsung auditor dan dari sumber independen.","s"),
 ("Auditor","Lembaga pengawas intern pemerintah yang bertanggung jawab langsung kepada Presiden adalah…","BPKP",["BPK","Inspektorat Daerah","KPK","Itjen Kementerian"],"BPKP (Perpres 192/2014) adalah APIP yang bertanggung jawab kepada Presiden.","m"),
 ("Analis Kebijakan","Tahapan siklus kebijakan publik yang tepat dimulai dari…","Penyusunan agenda",["Evaluasi kebijakan","Implementasi","Adopsi kebijakan","Formulasi"],"Siklus Dunn: penyusunan agenda, formulasi, adopsi, implementasi, evaluasi.","m"),
 ("Analis Kebijakan","Dokumen ringkas berisi rekomendasi kebijakan untuk pengambil keputusan disebut…","Policy brief",["Naskah akademik","Rencana strategis","LAKIP","Kerangka acuan kerja"],"Policy brief menyajikan masalah, opsi, dan rekomendasi secara ringkas bagi pimpinan.","m"),
 ("Analis Keuangan","Rasio lancar (current ratio) dihitung dengan rumus…","Aset lancar ÷ liabilitas jangka pendek",["Total utang ÷ ekuitas","Laba bersih ÷ penjualan","Kas ÷ total aset","Ekuitas ÷ total aset"],"Current ratio mengukur kemampuan membayar kewajiban jangka pendek.","m"),
 ("Analis Keuangan","Standar Akuntansi Pemerintahan yang berlaku saat ini menggunakan basis…","Akrual",["Kas","Kas menuju akrual","Komitmen","Modifikasi kas"],"PP 71/2010 menetapkan SAP berbasis akrual.","s"),
 ("Arsiparis","Arsip yang memiliki nilai guna kesejarahan dan dinyatakan permanen disebut…","Arsip statis",["Arsip dinamis aktif","Arsip inaktif","Arsip vital","Arsip terjaga"],"UU 43/2009: arsip statis dikelola lembaga kearsipan karena nilai guna kesejarahan.","m"),
 ("Arsiparis","Daftar yang berisi jangka waktu penyimpanan arsip dan keterangan nasib akhirnya disebut…","Jadwal Retensi Arsip (JRA)",["Klasifikasi arsip","Daftar isi berkas","Buku agenda","Indeks arsip"],"JRA menentukan masa simpan aktif/inaktif serta keterangan musnah, permanen, atau dinilai kembali.","s"),
 ("Pustakawan","Sistem klasifikasi yang membagi ilmu pengetahuan menjadi 10 kelas utama (000–900) adalah…","Dewey Decimal Classification",["Library of Congress","Colon Classification","UDC Bliss","Sistem Cutter"],"DDC: 000 karya umum, 100 filsafat, 200 agama, … 900 sejarah dan geografi.","m"),
 ("Pustakawan","Nomor standar internasional untuk buku adalah…","ISBN",["ISSN","DOI","ISMN","EAN"],"ISBN untuk buku; ISSN untuk terbitan berseri.","m"),
 ("Penyuluh","Metode penyuluhan dengan memperlihatkan hasil nyata penerapan teknologi di lapangan disebut…","Demonstrasi hasil (demplot)",["Ceramah","Anjangsana","Siaran radio","Brosur"],"Demonstrasi plot/hasil efektif mengubah perilaku karena sasaran melihat bukti langsung.","s"),
 ("Penyuluh","Dalam teori adopsi inovasi Rogers, kelompok yang paling awal menerima inovasi disebut…","Inovator",["Pengadopsi awal","Mayoritas awal","Mayoritas akhir","Laggard"],"Urutan: innovators, early adopters, early majority, late majority, laggards.","m"),
 ("Administrasi Pemerintahan","Asas umum pemerintahan yang baik (AUPB) diatur dalam…","UU 30 Tahun 2014",["UU 5 Tahun 2014","UU 23 Tahun 2014","UU 25 Tahun 2009","UU 20 Tahun 2023"],"UU 30/2014 tentang Administrasi Pemerintahan memuat AUPB seperti kepastian hukum, kemanfaatan, ketidakberpihakan.","s"),
 ("Administrasi Pemerintahan","Undang-undang tentang ASN yang berlaku saat ini adalah…","UU 20 Tahun 2023",["UU 5 Tahun 2014","UU 43 Tahun 1999","UU 8 Tahun 1974","UU 25 Tahun 2009"],"UU 20/2023 menggantikan UU 5/2014 tentang ASN.","m"),
 ("Jabatan Teknis Lainnya","Dalam K3, urutan hierarki pengendalian risiko yang paling efektif dimulai dari…","Eliminasi",["Alat pelindung diri","Pengendalian administratif","Rekayasa teknik","Substitusi"],"Hierarki: eliminasi, substitusi, rekayasa teknik, administratif, APD.","s"),
 ("Jabatan Teknis Lainnya","Pengadaan barang/jasa pemerintah saat ini diatur oleh…","Perpres 16/2018 jo. Perpres 12/2021",["Keppres 80/2003","Perpres 54/2010","UU 1/2004","PP 12/2019"],"Perpres 16/2018 sebagaimana diubah Perpres 12/2021 tentang Pengadaan Barang/Jasa Pemerintah.","h"),
]

# ---------------------------------------------------------------- TIU verbal
VERBAL = [
 ("Analogi Kata","DOKTER : STETOSKOP = PETANI : …","CANGKUL",["SAWAH","PADI","PUPUK","KERBAU"],"Stetoskop adalah alat kerja dokter; cangkul alat kerja petani.","m"),
 ("Analogi Kata","AIR : HAUS = MAKANAN : …","LAPAR",["KENYANG","NASI","PIRING","DAPUR"],"Air menghilangkan haus; makanan menghilangkan lapar.","m"),
 ("Analogi Kata","PENA : PENULIS = KUAS : …","PELUKIS",["CAT","KANVAS","WARNA","GAMBAR"],"Alat dan penggunanya.","m"),
 ("Analogi Kata","BENIH : POHON = TELUR : …","AYAM",["CANGKANG","SARANG","KUNING","GORENG"],"Bentuk awal menjadi bentuk dewasa.","m"),
 ("Analogi Kata","GELAP : TERANG = RAJIN : …","MALAS",["PANDAI","GIAT","TEKUN","CERDAS"],"Pasangan antonim.","m"),
 ("Analogi Kata","KAKI : SEPATU = KEPALA : …","TOPI",["RAMBUT","SISIR","OTAK","WAJAH"],"Bagian tubuh dan penutupnya.","m"),
 ("Analogi Kata","TERMOMETER : SUHU = BAROMETER : …","TEKANAN UDARA",["KECEPATAN ANGIN","KELEMBAPAN","CURAH HUJAN","GEMPA"],"Alat ukur dan besaran yang diukur.","s"),
 ("Sinonim","Sinonim kata NIRMALA adalah…","Bersih tanpa noda",["Indah","Gelap","Tanpa nama","Sederhana"],"Nirmala (KBBI): bersih, tanpa cacat/noda.","s"),
 ("Sinonim","Sinonim kata ABSAH adalah…","Sah",["Batal","Lengkap","Asli palsu","Mutlak"],"Absah berarti sah, valid.","m"),
 ("Sinonim","Sinonim kata FRIKSI adalah…","Perpecahan",["Persatuan","Gesekan halus","Fiksi","Kesepakatan"],"Friksi: pergeseran yang menimbulkan perbedaan pendapat; perpecahan.","s"),
 ("Sinonim","Sinonim kata ELABORASI adalah…","Penggarapan secara tekun dan cermat",["Peringkasan","Penolakan","Penghapusan","Perayaan"],"Elaborasi: penjabaran/penggarapan secara rinci.","s"),
 ("Sinonim","Sinonim kata PROMINEN adalah…","Terkemuka",["Rendah hati","Pemula","Biasa","Tersembunyi"],"Prominen: terkemuka, menonjol.","s"),
 ("Antonim","Antonim kata DEFISIT adalah…","Surplus",["Kekurangan","Rugi","Utang","Inflasi"],"Defisit (kekurangan) berlawanan dengan surplus (kelebihan).","m"),
 ("Antonim","Antonim kata FANA adalah…","Baka",["Sementara","Mati","Lenyap","Rusak"],"Fana = tidak kekal; baka = kekal.","m"),
 ("Antonim","Antonim kata KONKRET adalah…","Abstrak",["Nyata","Padat","Jelas","Pasti"],"Konkret (nyata) lawan abstrak (tidak berwujud).","m"),
 ("Antonim","Antonim kata SKEPTIS adalah…","Yakin",["Ragu","Kritis","Curiga","Sinis"],"Skeptis = kurang percaya; lawannya yakin/percaya.","m"),
 ("Antonim","Antonim kata EKSPLISIT adalah…","Implisit",["Tersurat","Jelas","Terbuka","Gamblang"],"Eksplisit (tersurat) lawan implisit (tersirat).","m"),
 ("Silogisme","Semua ASN wajib menjaga netralitas. Rina adalah ASN. Kesimpulan yang tepat…","Rina wajib menjaga netralitas",["Rina tidak wajib menjaga netralitas","Sebagian ASN tidak netral","Rina mungkin netral","Tidak dapat disimpulkan"],"Modus barbara: semua A adalah B; C adalah A; maka C adalah B.","m"),
 ("Silogisme","Jika hujan, jalan basah. Jalan tidak basah. Kesimpulan…","Tidak hujan",["Hujan","Jalan kering karena panas","Mungkin hujan","Tidak dapat disimpulkan"],"Modus tollens: p→q, ¬q, maka ¬p.","m"),
 ("Silogisme","Semua peserta yang lulus SKD mengikuti SKB. Sebagian peserta SKB berasal dari luar Jawa. Kesimpulan yang pasti benar…","Sebagian peserta yang lulus SKD mungkin berasal dari luar Jawa",["Semua peserta dari luar Jawa lulus SKD","Tidak ada peserta luar Jawa yang lulus","Semua peserta SKB berasal dari Jawa","Peserta luar Jawa tidak mengikuti SKD"],"Premis kedua bersifat 'sebagian', sehingga kesimpulan hanya dapat bersifat kemungkinan; pilihan lain menyalahi premis.","h"),
 ("Silogisme","Jika Andi rajin belajar, ia lulus. Jika ia lulus, ia diangkat. Andi rajin belajar. Kesimpulan…","Andi diangkat",["Andi tidak lulus","Andi lulus tetapi tidak diangkat","Andi tidak diangkat","Tidak dapat disimpulkan"],"Silogisme hipotetis: p→q, q→r, p, maka r.","m"),
 ("Silogisme","Tidak ada pegawai yang disiplin datang terlambat. Budi datang terlambat. Kesimpulan…","Budi bukan pegawai yang disiplin",["Budi pegawai disiplin","Budi bukan pegawai","Semua pegawai terlambat","Budi kadang disiplin"],"Jika semua pegawai disiplin tidak terlambat, maka yang terlambat bukan pegawai disiplin.","s"),
 ("Penalaran Analitis","Lima orang (A, B, C, D, E) duduk berjajar. A di ujung kiri. C tepat di tengah. B di sebelah kanan C. E tidak bersebelahan dengan A. Siapa yang duduk di sebelah kanan A?","D",["B","C","E","Tidak dapat ditentukan"],"Posisi: 1=A, 3=C, 4=B. Sisa posisi 2 dan 5 untuk D/E. E tidak di samping A sehingga E di 5, D di 2.","h"),
 ("Penalaran Analitis","P lebih tinggi dari Q. R lebih pendek dari Q. S lebih tinggi dari P. Siapa yang paling pendek?","R",["P","Q","S","Tidak dapat ditentukan"],"Urutan: S > P > Q > R.","m"),
 ("Pemahaman Bacaan","'Digitalisasi layanan publik mempercepat proses, namun kesenjangan akses internet membuat sebagian warga tertinggal.' Gagasan utama kalimat tersebut adalah…","Digitalisasi bermanfaat tetapi perlu memperhatikan pemerataan akses",["Digitalisasi harus dihentikan","Internet sudah merata","Layanan manual lebih cepat","Warga menolak digitalisasi"],"Kalimat memuat manfaat sekaligus tantangan (kesenjangan akses).","m"),
 ("Penarikan Kesimpulan","Semua kantor di kawasan X menerapkan kerja hibrida. Kantor Y tidak menerapkan kerja hibrida. Maka…","Kantor Y tidak berada di kawasan X",["Kantor Y berada di kawasan X","Kantor Y akan menerapkan kerja hibrida","Sebagian kantor X tidak hibrida","Tidak dapat disimpulkan"],"Kontraposisi: jika di X maka hibrida ⇒ jika tidak hibrida maka tidak di X.","s"),
]


def build_fact(prefix, rows, cat, has_sub=True, ref_default=None):
    out = []
    for i, r in enumerate(rows, 1):
        if cat == "SKB":
            sub, q, c, w, e, d = r; ref = f"Materi SKB {sub}"
        elif len(r) == 7:
            sub, q, c, w, e, d, ref = r
        else:
            sub, q, c, w, e, d = r; ref = ref_default or f"Materi {cat} {sub}"
        opts, a = place(c, w)
        out.append({"id": f"{prefix}-{i:03d}", "category": cat, "sub": sub, "question": q,
                    "options": opts, "answer": a, "explanation": e, "difficulty": D[d],
                    "reference": ref, "tags": [sub.lower()]})
    return out


def build_tkp():
    out = []
    for i, (sub, q, pairs) in enumerate(TKP, 1):
        p = list(pairs); rng.shuffle(p)
        best = max(p, key=lambda x: x[1])[0]
        out.append({"id": f"TKP-{i:03d}", "category": "TKP", "sub": sub, "question": q,
                    "options": [x[0] for x in p], "scores": [x[1] for x in p],
                    "answer": [x[1] for x in p].index(5),
                    "explanation": f"Respons terbaik (skor 5): \"{best}\" — paling proaktif, solutif, dan sesuai nilai BerAKHLAK. Skor menurun untuk respons yang pasif, menghindar, atau melanggar etika ASN.",
                    "difficulty": "Sedang", "reference": f"Materi TKP {sub}", "tags": [sub.lower()]})
    return out


# ---------------------------------------------------------------- TIU numerik (generated)
def num_wrongs(c, spread=None):
    s = set(); spread = spread or max(2, abs(c) // 8 or 2)
    while len(s) < 4:
        d = rng.choice([-1, 1]) * rng.randint(1, spread)
        if c + d != c: s.add(c + d)
    return [str(x) for x in s]


def fmt(x):
    if isinstance(x, float) and x.is_integer(): x = int(x)
    return f"{x}".replace(".", ",")


def gen_numeric():
    items = []
    def add(sub, q, c, w, e, d):
        items.append((sub, q, str(c), [str(x) for x in w], e, d))
    seen = set()
    # Deret aritmetika & geometri & bertingkat
    for _ in range(40):
        kind = rng.choice(["ar", "geo", "lvl", "alt"])
        if kind == "ar":
            a, b = rng.randint(2, 40), rng.randint(3, 15)
            s = [a + b * i for i in range(5)]; c = a + b * 5; e = f"Deret aritmetika dengan beda {b}."
        elif kind == "geo":
            a, r = rng.randint(1, 6), rng.choice([2, 3])
            s = [a * r ** i for i in range(5)]; c = a * r ** 5; e = f"Setiap suku dikali {r}."
        elif kind == "lvl":
            a, d0, dd = rng.randint(1, 10), rng.randint(1, 4), rng.randint(1, 3)
            s = [a]; d = d0
            for _ in range(4): s.append(s[-1] + d); d += dd
            c = s[-1] + d; e = f"Selisih antarsuku bertambah {dd} (bertingkat): {', '.join(str(s[i+1]-s[i]) for i in range(4))}, {d}."
        else:
            a, p, m = rng.randint(2, 10), rng.randint(3, 9), rng.randint(1, 4)
            s = [a]
            for i in range(4): s.append(s[-1] + p if i % 2 == 0 else s[-1] - m)
            c = s[-1] + p; e = f"Pola berselang: +{p}, −{m}, +{p}, −{m}, +{p}."
        key = tuple(s)
        if key in seen: continue
        seen.add(key)
        add("Deret Angka", f"Lanjutan deret {', '.join(map(str, s))}, … adalah", c, num_wrongs(c), e, "s" if kind in ("lvl", "alt") else "m")
    # Persentase
    for _ in range(25):
        p = rng.choice([10, 12, 15, 20, 25, 30, 35, 40, 45]); n = rng.randint(4, 60) * 20
        c = n * p // 100
        if (p, n) in seen: continue
        seen.add((p, n))
        add("Persentase", f"Harga barang Rp{n:,}".replace(",", ".") + f" didiskon {p}%. Besar potongan harga adalah… (dalam rupiah)", f"{c:,}".replace(",", "."), [f"{x:,}".replace(",", ".") for x in {c + n // 20, c - n // 20, n - c, c + n // 10}], f"{p}% × {n:,} = {c:,}.".replace(",", "."), "m")
    # Kecepatan jarak waktu
    for _ in range(20):
        v = rng.choice([40, 45, 50, 60, 72, 80, 90]); t = rng.choice([1.5, 2, 2.5, 3, 4])
        c = int(v * t)
        if (v, t) in seen: continue
        seen.add((v, t))
        add("Kecepatan, Jarak, dan Waktu", f"Sebuah mobil melaju dengan kecepatan rata-rata {v} km/jam selama {fmt(t)} jam. Jarak yang ditempuh adalah… km", c, num_wrongs(c, 30), f"Jarak = kecepatan × waktu = {v} × {fmt(t)} = {c} km.", "m")
    # Rata-rata
    for _ in range(20):
        n = rng.randint(4, 6); vals = [rng.randint(55, 95) for _ in range(n)]
        tot = sum(vals); target = rng.randint(70, 90)
        need = target * (n + 1) - tot
        if not (40 <= need <= 100): continue
        add("Rata-rata", f"Nilai {n} ujian Dina: {', '.join(map(str, vals))}. Agar rata-rata {n+1} ujian menjadi {target}, nilai ujian berikutnya harus…", need, num_wrongs(need, 8), f"Total yang diperlukan {target}×{n+1} = {target*(n+1)}; dikurangi total sekarang {tot} = {need}.", "s")
    # Pecahan
    for _ in range(20):
        a, b, c2, d2 = rng.randint(1, 5), rng.randint(2, 9), rng.randint(1, 5), rng.randint(2, 9)
        f = Fraction(a, b) + Fraction(c2, d2)
        if (a, b, c2, d2) in seen: continue
        seen.add((a, b, c2, d2))
        ans = f"{f.numerator}/{f.denominator}"
        w = set()
        for alt in [Fraction(a + c2, b + d2), f + Fraction(1, f.denominator), f - Fraction(1, f.denominator * 2), Fraction(a * c2, b * d2), f * 2]:
            s = f"{alt.numerator}/{alt.denominator}"
            if s != ans: w.add(s)
        w = list(w)[:4]
        while len(w) < 4: w.append(f"{f.numerator + len(w) + 1}/{f.denominator}")
        add("Pecahan dan Desimal", f"Hasil dari {a}/{b} + {c2}/{d2} adalah…", ans, w, f"Samakan penyebut: KPK({b},{d2}). Hasil disederhanakan menjadi {ans}.", "s")
    # Rasio
    for _ in range(20):
        x, y = rng.randint(2, 7), rng.randint(2, 7)
        if x == y: continue
        k = rng.randint(3, 15); tot = (x + y) * k
        if (x, y, k) in seen: continue
        seen.add((x, y, k))
        add("Rasio dan Perbandingan", f"Perbandingan uang Ani dan Budi adalah {x} : {y}. Jika jumlah uang mereka Rp{tot}.000, uang Ani adalah… ribu rupiah", x * k, num_wrongs(x * k, 6), f"Bagian Ani = {x}/{x+y} × {tot}.000 = {x*k}.000.", "m")
    # Aritmetika sosial (untung)
    for _ in range(20):
        beli = rng.randint(5, 40) * 10; p = rng.choice([10, 15, 20, 25, 30])
        jual = beli * (100 + p) // 100
        if beli * (100 + p) % 100 or (beli, p) in seen: continue
        seen.add((beli, p))
        add("Aritmetika Sosial", f"Pedagang membeli barang seharga Rp{beli}.000 dan ingin untung {p}%. Harga jual barang tersebut adalah… ribu rupiah", jual, num_wrongs(jual, 15), f"Harga jual = {beli}.000 × (100%+{p}%) = {jual}.000.", "m")
    # Operasi hitung
    for _ in range(20):
        a, b, c3 = rng.randint(12, 99), rng.randint(11, 49), rng.randint(2, 9)
        v = a * c3 - b
        add("Operasi Hitung", f"Hasil dari {a} × {c3} − {b} adalah…", v, num_wrongs(v, 12), f"Kerjakan perkalian dahulu: {a}×{c3} = {a*c3}, lalu dikurangi {b} = {v}.", "m")
    # Perbandingan kuantitatif
    for _ in range(12):
        a, b = rng.randint(2, 9), rng.randint(2, 9)
        P = a ** 2 + b ** 2; Q = (a + b) ** 2
        c = "P < Q"
        add("Perbandingan Kuantitatif", f"Jika P = {a}² + {b}² dan Q = ({a} + {b})², maka…", c, ["P > Q", "P = Q", "P = 2Q", "Hubungan tidak dapat ditentukan"], f"P = {P}, Q = {Q}. Karena (a+b)² = a²+b²+2ab dan 2ab > 0, P < Q.", "s")
    # Soal cerita pekerjaan
    for _ in range(12):
        a, b = rng.choice([(6, 12), (4, 12), (10, 15), (12, 24), (6, 3), (20, 30), (8, 24), (9, 18), (15, 10), (5, 20)])
        t = Fraction(a * b, a + b)
        if (a, b, "kerja") in seen: continue
        seen.add((a, b, "kerja"))
        ans = fmt(float(t))
        add("Soal Cerita", f"Pekerjaan dapat diselesaikan A dalam {a} hari dan B dalam {b} hari. Jika bekerja bersama, pekerjaan selesai dalam… hari", ans, [fmt(float(t) + 1), fmt(float(t) + 2), fmt((a + b) / 2), fmt(abs(a - b) or 1)], f"Kecepatan gabungan 1/{a} + 1/{b} = {a+b}/{a*b}; waktu = {a*b}/{a+b} = {ans} hari.", "s")
    return items


# ---------------------------------------------------------------- TIU figural (SVG)
def poly(n, cx=30, cy=30, r=20, rot=-90, fill="none"):
    import math
    pts = [f"{cx + r*math.cos(math.radians(rot + 360*i/n)):.1f},{cy + r*math.sin(math.radians(rot + 360*i/n)):.1f}" for i in range(n)]
    return f'<polygon points="{" ".join(pts)}" fill="{fill}" stroke="currentColor" stroke-width="2.5"/>'


def arrow(angle):
    return f'<g transform="rotate({angle} 30 30)"><line x1="30" y1="48" x2="30" y2="14" stroke="currentColor" stroke-width="3"/><polygon points="30,8 23,18 37,18" fill="currentColor"/></g>'


def dots(n):
    import math
    if n == 0: return ""
    return "".join(f'<circle cx="{30 + 14*math.cos(2*math.pi*i/n):.1f}" cy="{30 + 14*math.sin(2*math.pi*i/n):.1f}" r="4" fill="currentColor"/>' for i in range(n))


def svg(inner): return f'<svg viewBox="0 0 60 60" xmlns="http://www.w3.org/2000/svg">{inner}</svg>'


def gen_figural():
    items = []
    # Serial rotasi panah
    for step in [45, 90, 135, -45, -90, 30]:
        start = rng.choice([0, 45, 90])
        seq = [svg(arrow(start + step * i)) for i in range(4)]
        correct = svg(arrow(start + step * 4))
        wr = [svg(arrow(start + step * 4 + d)) for d in (45, 90, 180, -45)]
        items.append(("Rotasi Bentuk", f"Panah berputar {abs(step)}° {'searah' if step>0 else 'berlawanan arah'} jarum jam pada setiap langkah. Gambar berikutnya adalah…", seq, correct, wr, f"Setiap gambar diputar {abs(step)}°, sehingga gambar kelima berada pada sudut {start + step*4}°.", "s"))
    # Serial jumlah sisi
    for start in [3, 4, 5]:
        seq = [svg(poly(start + i)) for i in range(3)]
        correct = svg(poly(start + 3))
        wr = [svg(poly(start + k)) for k in (2, 5, 1)] + [svg(poly(start + 3, fill="currentColor"))]
        items.append(("Serial Gambar", "Perhatikan pola jumlah sisi. Gambar selanjutnya adalah…", seq, correct, wr, f"Jumlah sisi bertambah satu: {start}, {start+1}, {start+2}, maka berikutnya {start+3} sisi tanpa arsiran.", "m"))
    # Serial jumlah titik
    for start, st in [(1, 1), (2, 2), (1, 2)]:
        seq = [svg('<circle cx="30" cy="30" r="25" fill="none" stroke="currentColor" stroke-width="2"/>' + dots(start + st*i)) for i in range(3)]
        c = start + st*3
        correct = svg('<circle cx="30" cy="30" r="25" fill="none" stroke="currentColor" stroke-width="2"/>' + dots(c))
        wr = [svg('<circle cx="30" cy="30" r="25" fill="none" stroke="currentColor" stroke-width="2"/>' + dots(c + d)) for d in (-1, 1, 2, -2) if c + d > 0][:4]
        items.append(("Kelanjutan Pola Visual", "Jumlah titik di dalam lingkaran mengikuti pola tertentu. Gambar berikutnya adalah…", seq, correct, wr, f"Titik bertambah {st} pada setiap gambar sehingga berikutnya {c} titik.", "m"))
    # Ketidaksamaan: 4 segitiga + 1 segi empat
    for n_odd, n_base in [(4, 3), (6, 5), (3, 4), (5, 6)]:
        items.append(("Ketidaksamaan Gambar", "Manakah gambar yang berbeda dari yang lain?", [], svg(poly(n_odd)), [svg(poly(n_base, rot=r)) for r in (-90, -60, -30, 0)], f"Empat gambar memiliki {n_base} sisi (hanya diputar), satu gambar memiliki {n_odd} sisi.", "m"))
    # Pencerminan horizontal panah
    for a in [30, 60, 120, 150]:
        items.append(("Pencerminan", f"Cermin diletakkan vertikal di sebelah kanan gambar. Bayangan dari gambar adalah…", [svg(arrow(a))], svg(arrow(-a)), [svg(arrow(a)), svg(arrow(a + 180)), svg(arrow(180 - a)), svg(arrow(a + 90))], f"Pencerminan terhadap garis vertikal mengubah sudut {a}° menjadi −{a}°.", "s"))
    # Analogi gambar: isi/kosong
    for n in [3, 4, 5, 6]:
        m = n + 1 if n < 6 else 3
        items.append(("Analogi Gambar", "Bentuk kosong menjadi bentuk terarsir. Seperti itu pula, bentuk kedua menjadi…", [svg(poly(n)), svg(poly(n, fill="currentColor")), svg(poly(m))], svg(poly(m, fill="currentColor")), [svg(poly(m)), svg(poly(n, fill="currentColor")), svg(poly(m + 1, fill="currentColor")), svg(poly(n))], "Hubungan pasangan pertama: bentuk sama, berubah menjadi terarsir.", "m"))
    out = []
    for i, (sub, q, seq, c, w, e, d) in enumerate(items, 1):
        opts = [c] + w[:4]; rng.shuffle(opts)
        out.append({"id": f"TIU-F{i:03d}", "category": "TIU", "sub": sub, "group": "Figural", "question": q, "figures": seq,
                    "options": opts, "optionType": "svg", "answer": opts.index(c), "explanation": e,
                    "difficulty": D[d], "reference": f"Materi TIU Figural – {sub}", "tags": ["figural", sub.lower()]})
    return out


def main():
    os.makedirs(OUT, exist_ok=True)
    twk = build_fact("TWK", TWK, "TWK")
    tkp = build_tkp()
    skb = build_fact("SKB", SKB, "SKB")
    verbal = build_fact("TIU-V", VERBAL, "TIU")
    for q in verbal: q["group"] = "Verbal"
    numeric = build_fact("TIU-N", gen_numeric(), "TIU")
    for q in numeric: q["group"] = "Numerik"
    fig = gen_figural()
    # dedupe question text
    def dd(lst):
        seen, res = set(), []
        for q in lst:
            if q["question"] in seen: continue
            seen.add(q["question"]); res.append(q)
        return res
    tiu = dd(verbal + numeric) + fig
    for name, data in [("twk", twk), ("tiu", tiu), ("tkp", tkp), ("skb", skb)]:
        with open(os.path.join(OUT, f"{name}-questions.json"), "w") as f:
            json.dump(data, f, ensure_ascii=False, indent=1)
        print(name, len(data))


main()
