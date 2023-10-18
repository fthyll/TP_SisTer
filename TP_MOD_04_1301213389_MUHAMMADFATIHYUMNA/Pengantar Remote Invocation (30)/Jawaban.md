**1. Pengantar Remote Invocation (30)**

**Remote Procedure Call (RPC)** adalah mekanisme komunikasi yang memungkinkan pemanggilan fungsi atau metode di komputer satu (pemanggil) untuk menjalankan kode di komputer lain (pelayan/server) melalui jaringan. Ini memungkinkan aplikasi terdistribusi untuk berkomunikasi dengan objek atau layanan yang berjalan di mesin yang berbeda, seolah-olah mereka beroperasi di mesin lokal.

Cara kerja RPC secara umum adalah sebagai berikut:

- **Pemanggil (Client)**: Pemanggil ingin menjalankan suatu fungsi atau metode yang berada di server. Pemanggil membuat pemanggilan ke fungsi tersebut seolah-olah itu ada di mesin lokalnya. Namun, pemanggil mengemas pemanggilan dengan parameter yang diperlukan dan mengirimnya ke server melalui jaringan.

- **Jaringan (Network)**: Pemanggilan RPC dikirimkan melalui jaringan (biasanya menggunakan protokol seperti HTTP, TCP/IP, atau protokol khusus) ke mesin yang menjalankan server RPC.

- **Pelayan (Server)**: Penerimaan pemanggilan RPC oleh server. Server membuka pesan yang diterima, mengekstrak parameter pemanggilan, dan menjalankan fungsi atau metode yang diminta dengan parameter tersebut. Hasilnya kemudian dikemas sebagai respons dan dikirim kembali ke pemanggil melalui jaringan.

- **Pemanggil Kembali (Client Callback)**: Dalam beberapa kasus, server juga dapat melakukan pemanggilan balik ke pemanggil, mengirimkan respons atau informasi tambahan jika diperlukan.

Keuntungan utama RPC adalah abstraksi yang mudah digunakan dan pemanggilan fungsi atau metode yang terasa lokal, meskipun melibatkan komunikasi antarproses. Ini memungkinkan aplikasi terdistribusi untuk beroperasi dengan cara yang lebih terstruktur dan terorganisir.

**2. Perbedaan RPC dan RMI (Remote Method Invocation)**

RPC (Remote Procedure Call) dan RMI (Remote Method Invocation) adalah dua pendekatan yang berbeda untuk mencapai tujuan yang serupa, yaitu memanggil kode yang berjalan di mesin yang berbeda melalui jaringan. Berikut adalah perbedaan utama antara keduanya:

**A. Bahasa dan Teknologi yang Digunakan:**
   - **RPC**: RPC bersifat lebih umum dan dapat diimplementasikan dalam berbagai bahasa pemrograman seperti Python, C++, Java, dan lainnya. Ini tidak terikat dengan bahasa tertentu.
   - **RMI**: RMI adalah mekanisme khusus yang digunakan dalam konteks Java. Ini memungkinkan objek Java untuk dipanggil dari mesin yang berbeda.

**B. Serialisasi Objek:**
   - **RPC**: Pada RPC, data yang dikirimkan antar mesin biasanya perlu di-serialisasi dan di-deserialisasi. Ini berarti objek dan data harus dikonversi menjadi format yang dapat dikirimkan melalui jaringan.
   - **RMI**: Dalam RMI, karena keduanya berjalan di lingkungan Java, objek Java dapat dikirimkan langsung tanpa perlu serialisasi/deserialisasi yang ekspansif.

**C. Kesalahan dan Manajemen Koneksi:**
   - **RPC**: Biasanya, RPC membutuhkan manajemen kesalahan, seperti mengatasi kehilangan paket atau konektivitas yang buruk, secara eksplisit dalam kode.
   - **RMI**: RMI memanfaatkan fitur Java seperti manajemen pengecualian untuk mengatasi masalah ini secara lebih terintegrasi.

**D. Platform Khusus:**
   - **RPC**: Dapat diimplementasikan di berbagai platform dan bahasa, sehingga lebih fleksibel.
   - **RMI**: Terbatas pada platform Java, yang membatasi interoperabilitas dengan aplikasi yang tidak berbasis Java.

**E. Middleware**: 
   - **RPC**: Biasanya membutuhkan penggunaan middleware (seperti gRPC, Apache Thrift) untuk mengatur panggilan RPC.
   - **RMI**: Adalah bagian dari Java API dan dapat diimplementasikan tanpa perlu middleware tambahan.

Pilihan antara RPC dan RMI tergantung pada kebutuhan aplikasi Anda dan lingkungan yang Anda gunakan. Jika Anda berurusan dengan aplikasi Java yang berbasis Java, RMI mungkin merupakan pilihan yang nyaman. Namun, jika Anda berurusan dengan aplikasi lintas bahasa atau lintas platform, maka RPC yang lebih generik mungkin lebih cocok.