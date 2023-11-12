### 1. Perkalian Matriks:

Perkalian matriks adalah operasi dasar dalam aljabar linear. Untuk memahami cara kerjanya, kita dapat mengambil contoh dua matriks, A dan B, yang memiliki ukuran yang memungkinkan untuk dikalikan (jumlah kolom matriks A harus sama dengan jumlah baris matriks B).

Misalkan matriks A berukuran m x n, dan matriks B berukuran n x p. Hasil perkalian matriks C, disebut juga matriks produk, akan memiliki ukuran m x p. Setiap elemen C dihitung dengan menjumlahkan perkalian setiap elemen baris matriks A dengan elemen kolom matriks B yang sesuai.

Rumusnya adalah sebagai berikut:

\[C_{ij} = \sum_{k=1}^{n} A_{ik} \cdot B_{kj}\]

di mana:
- \(C_{ij}\) adalah elemen ke-(i, j) dari matriks hasil C.
- \(A_{ik}\) adalah elemen ke-(i, k) dari matriks A.
- \(B_{kj}\) adalah elemen ke-(k, j) dari matriks B.
- \(n\) adalah jumlah kolom matriks A (atau jumlah baris matriks B).

Contoh:
\[C_{11} = A_{11}B_{11} + A_{12}B_{21} + \ldots + A_{1n}B_{n1}\]

### 2. Trapezoidal Rule:

Trapezoidal Rule digunakan untuk mengestimasi nilai integral suatu fungsi dengan mengaproksimasi daerah di bawah kurva fungsi sebagai trapesium. Ini adalah metode numerik yang umum digunakan untuk menghitung integral tentu dari sebuah fungsi.

Cara kerjanya adalah dengan membagi interval integral menjadi beberapa subinterval dan kemudian menggunakan trapesium untuk mengaproksimasi area di bawah kurva di setiap subinterval.

Rumus Trapezoidal Rule untuk mengaproksimasi integral dari \(a\) ke \(b\) dari suatu fungsi \(f(x)\) adalah:

\[ \int_{a}^{b} f(x) \,dx \approx \frac{h}{2} [f(a) + 2f(x_1) + 2f(x_2) + \ldots + 2f(x_{n-1}) + f(b)] \]

di mana:
- \(h\) adalah panjang setiap subinterval, \(h = \frac{b - a}{n}\).
- \(x_i\) adalah titik pada subinterval ke-\(i\).

Semakin banyak subinterval yang digunakan (semakin besar \(n\)), semakin akurat aproksimasi integralnya.