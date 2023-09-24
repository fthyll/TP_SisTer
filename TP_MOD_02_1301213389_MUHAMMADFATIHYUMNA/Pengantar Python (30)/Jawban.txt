1. Python dibuat oleh seorang programmer bernama Guido van Rossum. Pengembangan bahasa pemrograman Python dimulai pada akhir 1980-an, dan versi pertamanya, Python 0.9.0, dirilis pada bulan Februari 1991. Python terus berkembang dan menjadi salah satu bahasa pemrograman yang paling populer dan digunakan secara luas di seluruh dunia.

2. Ada banyak perbedaan antara Python 2 dan Python 3, yang membuat Python 3 menjadi versi yang lebih disarankan dan umum digunakan saat ini. Berikut beberapa perbedaan utama:

   a. Print Statement:
      - Python 2: Menggunakan pernyataan `print` sebagai statement, contohnya: `print "Hello, World!"`.
      - Python 3: Menggunakan fungsi `print()` sebagai fungsi, contohnya: `print("Hello, World!")`.

   b. Pembagian:
      - Python 2: Operasi pembagian antara dua bilangan bulat akan menghasilkan bilangan bulat (floor division) jika keduanya juga bilangan bulat. Misalnya, `5 / 2` menghasilkan `2`.
      - Python 3: Operasi pembagian antara dua bilangan bulat akan menghasilkan bilangan float. Misalnya, `5 / 2` menghasilkan `2.5`.

   c. Fungsi `xrange()`:
      - Python 2: Terdapat fungsi `xrange()` yang efisien untuk melakukan perulangan pada range angka, terutama dalam penggunaan loop.
      - Python 3: Fungsi `xrange()` telah dihapus, dan fungsi `range()` di Python 3 memiliki perilaku yang sama seperti `xrange()` di Python 2.

   d. Unicode:
      - Python 2: String dianggap sebagai urutan byte, dan ada dua jenis string: string byte (`str`) dan string Unicode (`unicode`).
      - Python 3: Semua string dianggap sebagai string Unicode. Untuk mendefinisikan string byte, Anda harus menggunakan `bytes` atau `bytearray`.

   e. Pernyataan `input()`:
      - Python 2: Pernyataan `input()` mengambil masukan dari pengguna dan menganggapnya sebagai ekspresi Python.
      - Python 3: Pernyataan `input()` mengambil masukan dari pengguna dan mengembalikannya sebagai string.

   f. Fungsi `next()`:
      - Python 2: Fungsi `next()` digunakan dengan dua argumen, yaitu iterator dan nilai default.
      - Python 3: Fungsi `next()` digunakan dengan satu argumen, yaitu iterator.

Ini hanya beberapa perbedaan utama antara Python 2 dan Python 3. Python 3 dirilis dengan tujuan untuk memperbaiki beberapa masalah desain dan menyederhanakan bahasa, sehingga menjadi lebih modern dan aman. Python 2 sudah tidak lagi mendapatkan dukungan resmi dan disarankan untuk beralih ke Python 3 jika memungkinkan.