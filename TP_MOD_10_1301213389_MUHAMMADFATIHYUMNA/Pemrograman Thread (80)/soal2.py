import threading
import math

def calculate_factorial(num, result):
    result[0] = math.factorial(num)

if __name__ == "__main__":
    n = 15
    m = 20

    # Inisialisasi hasil faktorial
    result_n = [0]
    result_m = [0]

    # Membuat dua thread untuk menghitung faktorial secara parallel
    thread1 = threading.Thread(target=calculate_factorial, args=(n, result_n))
    thread2 = threading.Thread(target=calculate_factorial, args=(m, result_m))

    # Memulai eksekusi thread
    thread1.start()
    thread2.start()

    # Menunggu kedua thread selesai
    thread1.join()
    thread2.join()

    print(f"{n}! = {result_n[0]}")
    print(f"{m}! = {result_m[0]}")
