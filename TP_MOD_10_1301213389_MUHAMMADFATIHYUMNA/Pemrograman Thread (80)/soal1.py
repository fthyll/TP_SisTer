import threading

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_primes(start, end):
    count = 0
    for num in range(start, end + 1):
        if is_prime(num):
            count += 1
    print(f"Banyaknya bilangan prima dari {start} hingga {end}: {count}")

# Menentukan rentang n dan m
n = 1
m = 1000000

# Membagi pekerjaan menjadi dua thread
mid = (n + m) // 2

thread1 = threading.Thread(target=count_primes, args=(n, mid))
thread2 = threading.Thread(target=count_primes, args=(mid + 1, m))

# Menjalankan thread
thread1.start()
thread2.start()

# Menunggu hingga kedua thread selesai
thread1.join()
thread2.join()
