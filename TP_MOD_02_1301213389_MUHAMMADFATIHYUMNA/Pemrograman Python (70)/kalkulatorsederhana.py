# Fungsi untuk menjumlahkan dua angka
def tambah(angka1, angka2):
    return angka1 + angka2

# Fungsi untuk mengurangkan dua angka
def kurang(angka1, angka2):
    return angka1 - angka2

# Fungsi untuk mengalikan dua angka
def kali(angka1, angka2):
    return angka1 * angka2

# Fungsi untuk membagi dua angka
def bagi(angka1, angka2):
    if angka2 == 0:
        return "Tidak bisa membagi dengan nol"
    return angka1 / angka2

# Menampilkan informasi pengguna
print("KALKULATOR SEDERHANA")
print("====================")
print("NAMA : MUHAMMAD FATIH YUMNA LAJUWIRDI LIRRAHMAN")
print("NIM : 1301213389")
print("KELAS : IF-45-05")
print("====================")
# Input dua angka dari pengguna
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))
print("====================")

# Menampilkan menu operasi kepada pengguna
print("Pilih operasi yang diinginkan:")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
print("====================")
# Input operasi yang diinginkan oleh pengguna
pilihan = input("Masukkan nomor operasi (1/2/3/4): ")

# Melakukan perhitungan sesuai dengan operasi yang dipilih
if pilihan == '1':
    print("Hasil penjumlahan:", tambah(angka1, angka2))
elif pilihan == '2':
    print("Hasil pengurangan:", kurang(angka1, angka2))
elif pilihan == '3':
    print("Hasil perkalian:", kali(angka1, angka2))
elif pilihan == '4':
    print("Hasil pembagian:", bagi(angka1, angka2))
else:
    print("Pilihan operasi tidak valid")
