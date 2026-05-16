IMPLEMENTASI KAPASITAS AIR EMBER DENGAN STACK ARRAY


Mengapa Memilih Implementasi Kapasitas Air Ember? Karena Pemilihan studi kasus pengisian air ke dalam ember didasarkan pada kemudahan analogi fisik dalam kehidupan sehari-hari untuk memahami cara kerja struktur data Stack. LIFO (Last In, First Out): Pengguna bisa langsung membayangkan bahwa air yang pertama kali dituang akan mengendap di dasar ember paling bawah. Sebaliknya, air yang dituang terakhir kali akan berada di permukaan paling atas, dan otomatis menjadi air yang pertama kali keluar saat diciduk kembali (Pop).Kasus ini mempermudah pemahaman tentang batas maksimal kapasitas sperti memori namun versi air. Di dunia nyata, jika kita terus memaksa memasukkan air ke dalam ember yang sudah penuh, air tersebut akan meluap dan tumpah. Logika alamiah ini sangat sempurna untuk menjelaskan konsep error Stack Overflow (kondisi ketika tumpukan memori penuh) kepada siapa saja tanpa perlu penjelasan teknis yang sangat rumit.

Source Code

Input


![image alt](https://github.com/muhammaddarma2006-coder/PSD-TAP4-2515061003/blob/e164506f21300f56d8534f3415425a48e287569f/Screenshot%20(2471).png)


Fungsi main() diawali dengan mencetak judul simulasi ke layar dan langsung memasuki perulangan while True yang bertugas menjalankan menu interaktif secara terus-menerus hingga pengguna memilih untuk keluar. Di dalam perulangan ini, program menghitung jumlah gayung air saat ini menggunakan perintah n = len(ember_air) untuk kemudian menampilkan status keterisian ember secara real-time kepada pengguna sebelum menyajikan tiga pilihan tindakan.

Ketika pengguna memilih menu nomor satu, program akan meminta input volume air dalam satuan mililiter yang divalidasi menggunakan struktur try-except agar sistem tidak mengalami error jika pengguna salah memasukkan karakter selain angka. Jika input tersebut adalah angka yang lebih besar dari nol, variabel volume akan dikirim ke fungsi push_air(volume) untuk dimasukkan ke dalam tumpukan, namun jika input tidak valid, program akan langsung menampilkan pesan peringatan.

Selanjutnya, jika pengguna memilih menu nomor dua, program akan langsung mengeksekusi fungsi pop_air() untuk mengambil sekaligus menghapus lapisan air paling atas dari dalam ember. Terakhir, jika menu nomor tiga yang dipilih, program akan mencetak pesan bahwa simulasi telah selesai dan menggunakan perintah break untuk menghentikan perulangan while, sedangkan jika pengguna memasukkan angka di luar menu yang tersedia, blok else akan aktif untuk memperingatkan bahwa pilihan tersebut tidak valid.



![image alt](https://github.com/muhammaddarma2006-coder/PSD-TAP4-2515061003/blob/e164506f21300f56d8534f3415425a48e287569f/Screenshot%20(2468).png)


Fungsi pop_air() ini diawali dengan perintah n = len(ember_air) yang bertugas untuk menghitung berapa jumlah total gayung air yang saat ini sedang tertampung di dalam ember. Masuk ke baris berikutnya, terdapat struktur pengkondisian if n == 0: yang berfungsi sebagai sistem validasi untuk memastikan bahwa ember tidak dalam keadaan kosong sebelum proses pengambilan air dilakukan. Jika kondisi tersebut terpenuhi atau bernilai benar, program akan membatalkan tindakan dan mencetak pesan peringatan ke layar bahwa air gagal diambil karena ember sudah benar-benar kosong, yang dalam istilah struktur data dikenal dengan sebutan Stack Underflow.

Namun, jika kondisi tersebut tidak terpenuhi atau ember terbukti masih berisi air, program akan langsung meloncat ke blok else: untuk mengeksekusi perintah air_keluar = ember_air.pop(). Perintah pop() inilah yang menjadi mesin utama dari operasi ini, di mana sistem secara otomatis akan mengambil sekaligus menghapus data volume air yang berada di lapisan paling atas atau yang paling terakhir dimasukkan ke dalam array. Setelah data tersebut berhasil dikeluarkan dan disimpan sementara di dalam variabel air_keluar, fungsi ini diakhiri dengan mencetak pesan konfirmasi ke layar yang menginformasikan kepada pengguna mengenai jumlah mililiter air yang baru saja berhasil diciduk dari ember.


![image alt](https://github.com/muhammaddarma2006-coder/PSD-TAP4-2515061003/blob/e164506f21300f56d8534f3415425a48e287569f/Screenshot%20(2469).png)


Potongan kode pada gambar terakhir ini merupakan bagian paling awal dari program yang berfungsi untuk menyiapkan basis data serta melakukan konfigurasi awal sebelum simulasi dijalankan. Bagian ini diawali dengan pembuatan konstanta MAX_KAPASITAS = 5 yang bertugas menetapkan batas tertinggi kapasitas tampungan ember, di mana angka lima ini mengunci jumlah maksimal gayung air yang diperbolehkan masuk ke dalam sistem memori program. Tepat di bawahnya, terdapat deklarasi variabel ember_air = [] yang membuat sebuah List atau Array kosong sebagai wadah utama untuk menampung seluruh data volume air yang akan dimasukkan nantinya. Bagian ini sangat penting karena berfungsi sebagai fondasi tempat penyimpanan terpusat, sehingga fungsi-fungsi lain seperti penambahan air (Push) maupun pengambilan air (Pop) dapat mengelola data yang sama secara sinkron sepanjang simulasi berjalan.


![image alt](https://github.com/muhammaddarma2006-coder/PSD-TAP4-2515061003/blob/e164506f21300f56d8534f3415425a48e287569f/Screenshot%20(2470).png)


Fungsi push_air(volume_ml) ini diawali dengan perintah n = len(ember_air) yang bertugas untuk menghitung jumlah gayung air yang saat ini sudah berada di dalam ember. Masuk ke baris berikutnya, terdapat struktur percabangan if n >= MAX_KAPASITAS: yang berfungsi sebagai sistem validasi untuk memeriksa apakah jumlah air saat ini sudah menyentuh atau melewati batas maksimal tampungan yang diperbolehkan. Jika kondisi tersebut terpenuhi atau bernilai benar, program akan langsung membatalkan pengisian dan mencetak pesan peringatan ke layar bahwa air akan tumpah karena ember sudah penuh, yang dalam istilah struktur data dikenal dengan sebutan Stack Overflow. Namun, jika kondisi tersebut tidak terpenuhi atau ember masih memiliki ruang, program akan meloncat ke blok else: dan mengeksekusi perintah ember_air.append(volume_ml). Perintah append inilah yang menjadi mesin utama dari operasi Push, di mana data volume air yang baru dimasukkan akan ditumpuk di posisi paling atas atau di akhir baris array, kemudian diakhiri dengan mencetak pesan konfirmasi bahwa air berhasil ditambahkan ke dalam ember.




Output



![image alt](https://github.com/muhammaddarma2006-coder/PSD-TAP4-2515061003/blob/e164506f21300f56d8534f3415425a48e287569f/Screenshot%20(2464).png)


menunjukkan kondisi awal saat simulasi baru saja dijalankan oleh sistem. Pada baris pertama, program mencetak teks judul sebagai penanda bahwa pengguna telah masuk ke dalam menu simulasi kapasitas air ember berbasis metode Stack Array. Tepat di bawah judul tersebut, sistem langsung menampilkan status kondisi ember secara real-time, di mana terlihat tulisan total isi masih berukuran nol dari batas maksimal lima gayung, yang disertai dengan tampilan visual array berupa kurung siku kosong karena memang belum ada data air yang dimasukkan.


![image alt](https://github.com/muhammaddarma2006-coder/PSD-TAP4-2515061003/blob/e164506f21300f56d8534f3415425a48e287569f/Screenshot%20(2466).png)


ini kelanjutan proses ketika ember sudah terisi penuh dan pengguna mencoba memasukkan air lagi. program segera mengalirkan input tersebut ke dalam sistem validasi logika fungsi penambahan. Karena jumlah data sudah menyentuh batas tertinggi, program langsung memicu kondisi pengaman dengan menolak pengisian tersebut serta mencetak pesan peringatan bahwa tindakan gagal dilakukan karena air akan meluap, yang secara visual membuktikan terjadinya fenomena Stack Overflow pada tumpukan.


![image alt](https://github.com/muhammaddarma2006-coder/PSD-TAP4-2515061003/blob/e164506f21300f56d8534f3415425a48e287569f/Screenshot%20(2465).png)

Setelah pengguna menjatuhkan pilihan pada menu nomor, sistem langsung memunculkan perintah untuk  mengambil jumlah volume air di ember, di mana pengguna kemudian mengetikkan angka opsi 2 pada sistem menu. Program segera memproses input tersebut melalui fungsi penambahan, memasukkannya ke dalam urutan list terakhir, dan langsung mencetak pesan konfirmasi sukses yang menyatakan bahwa air sebanyak 600 mililiter telah berhasil mengambil air lapisan teratas dari ember.

ini adalah bagian video demonstrasi 4 yang saya buat
https://youtu.be/zViG_PpSPt0

