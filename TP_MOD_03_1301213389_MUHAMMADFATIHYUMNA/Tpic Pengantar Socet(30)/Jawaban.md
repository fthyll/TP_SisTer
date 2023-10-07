**Lifecycle TCP Socket:**

TCP (Transmission Control Protocol) adalah protokol yang digunakan untuk koneksi berbasis aliran (stream) dalam jaringan komputer. Berikut adalah tahapan atau lifecycle dari sebuah TCP socket:

1. **Pengikatan (Binding):** Saat server TCP pertama kali dibuat, ia harus mengikat (bind) ke alamat dan port tertentu pada mesin fisik yang akan digunakan untuk mendengarkan koneksi dari klien. Pengikatan ini dilakukan menggunakan metode `bind()`.

2. **Pendengaran (Listening):** Setelah mengikat socket ke alamat dan port, server harus memulai proses pendengaran untuk menerima koneksi masuk. Server dapat memanggil metode `listen()` untuk memulai pendengaran.

3. **Penerimaan Koneksi (Accepting Connections):** Ketika klien mencoba terhubung, server akan menerima permintaan koneksi masuk dengan menggunakan metode `accept()`. Setelah permintaan diterima, server akan membuat socket baru yang disebut "socket anak" untuk berkomunikasi dengan klien.

4. **Koneksi Terbentuk (Connection Established):** Setelah koneksi diterima oleh server, koneksi TCP resmi antara server dan klien terbentuk. Komunikasi data dapat dimulai antara keduanya.

5. **Transmisi Data (Data Transmission):** Selama koneksi berlangsung, data dapat dikirimkan antara server dan klien menggunakan metode `send()` dan `receive()`. Data dikirim dalam bentuk aliran (stream) dan akan dibaca oleh penerima dalam urutan yang benar.

6. **Penutupan (Closing):** Setelah komunikasi selesai, baik server maupun klien dapat memutuskan koneksi dengan menggunakan metode `close()`. Setelah koneksi ditutup, socket tidak dapat digunakan lagi.

7. **Pemusnahan (Cleanup):** Setelah socket ditutup, server dan klien harus membersihkan sumber daya yang digunakan oleh socket, seperti menutup file descriptor dan melepaskan memori yang dialokasikan.

**Lifecycle UDP Socket:**

UDP (User Datagram Protocol) adalah protokol yang digunakan untuk koneksi tanpa koneksi (connectionless) dalam jaringan komputer. Lifecycle dari sebuah UDP socket lebih sederhana daripada TCP:

1. **Pengikatan (Binding):** Seperti dalam TCP, pengikatan adalah langkah pertama di mana socket diikat ke alamat dan port tertentu pada mesin fisik yang akan digunakan. Pengikatan ini dilakukan menggunakan metode `bind()`.

2. **Transmisi Data (Data Transmission):** Setelah socket diikat, Anda dapat mengirim dan menerima datagram UDP menggunakan metode `send()` dan `receive()`. Datagram UDP adalah unit data terpisah yang dikirimkan tanpa jaminan pengiriman atau urutan.

3. **Penutupan (Closing):** Setelah komunikasi selesai, socket dapat ditutup menggunakan metode `close()`. UDP tidak memiliki koneksi terbentuk seperti TCP, sehingga penutupan socket lebih sederhana.

4. **Pemusnahan (Cleanup):** Setelah socket ditutup, sumber daya yang digunakan oleh socket harus dibersihkan, seperti menutup file descriptor dan melepaskan memori yang dialokasikan.

Ketika menggunakan UDP, tidak ada koneksi aktif yang dipertahankan, sehingga tidak ada tahapan seperti pendengaran atau penerimaan koneksi seperti yang ada dalam TCP. Datagram UDP dikirimkan tanpa perlu menjalin koneksi terlebih dahulu.