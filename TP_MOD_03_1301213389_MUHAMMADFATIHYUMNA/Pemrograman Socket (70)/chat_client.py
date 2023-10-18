import socket
import threading

# Inisialisasi klien socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.18.38', 12345))  # Ganti localhost dan port sesuai kebutuhan

# Menginputkan nama panggilan
nickname = input("Masukkan nama panggilan Anda: ")
client_socket.send(nickname.encode('utf-8'))

# Mengirim pesan
def send():
    while True:
        message = input(f"{nickname} : ")
        client_socket.send(message.encode('utf-8'))

# Menerima pesan
def receive():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            # Koneksi terputus
            print("Terputus dari server.")
            client_socket.close()
            break

# Menjalankan thread untuk mengirim dan menerima pesan
send_thread = threading.Thread(target=send)
receive_thread = threading.Thread(target=receive)

send_thread.start()
receive_thread.start()
