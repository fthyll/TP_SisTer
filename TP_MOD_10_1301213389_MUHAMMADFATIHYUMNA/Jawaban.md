**a. Bagaimana Thread Bekerja:**

Thread adalah unit kecil dari eksekusi dalam sebuah proses. Proses adalah program yang sedang berjalan, dan setiap proses dapat memiliki satu atau lebih thread. Thread berbagi sumber daya seperti memori dan file yang sama dalam suatu proses, namun setiap thread memiliki register dan stack sendiri.

Contoh konkret permasalahan yang dapat dieksekusi secara parallel:

Misalkan Anda memiliki program yang perlu menghitung jumlah elemen dalam sebuah array. Dengan menggunakan thread, Anda dapat membagi array menjadi bagian-bagian kecil dan membiarkan setiap thread menghitung jumlah bagian tersebut secara bersamaan. Akibatnya, proses tersebut menjadi lebih cepat karena beberapa thread dapat bekerja secara parallel.

**b. Siklus Hidup Thread:**

Siklus hidup thread umumnya terdiri dari beberapa tahap:

1. **New (Baru):** Thread baru diciptakan tetapi belum memulai eksekusi.
2. **Runnable (Dapat Dijalankan):** Thread siap untuk dieksekusi, tetapi sistem operasi belum memilihnya untuk dieksekusi.
3. **Blocked (Diblokir):** Thread berhenti sementara karena menunggu sumber daya atau kondisi tertentu.
4. **Waiting (Menunggu):** Thread menunggu sampai thread lain melakukan operasi tertentu.
5. **Timed Waiting (Menunggu Waktu):** Thread menunggu untuk jangka waktu tertentu.
6. **Terminated (Dihentikan):** Thread selesai dieksekusi atau dihentikan secara paksa.
