import socket
import threading

# Inisialisasi server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))  # Ganti localhost dan port sesuai kebutuhan
server_socket.listen(5)

# Daftar klien yang terhubung
clients = []

# Mengirim pesan ke semua klien
def broadcast(message, sender):
    for client in clients:
        # Menambahkan namaclient sebelum pesan
        client.send(f"{sender} : {message}".encode('utf-8'))

# Menangani koneksi dari klien
def handle(client):
    nickname = client.recv(1024).decode('utf-8')
    clients.append(client)
    
    # Memberi tahu semua klien tentang klien yang terhubung
    broadcast(f"{nickname} bergabung dengan chat!", "Server")
    
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if not message:
                continue
            # Mengirim pesan ke semua klien dengan menyertakan namaclient
            broadcast(message, nickname)
        except:
            # Menghapus klien yang terputus
            clients.remove(client)
            broadcast(f"{nickname} keluar dari chat.", "Server")
            client.close()
            break

# Menerima koneksi dan menangani klien
def receive():
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Terhubung dengan {str(client_address)}")
        client_thread = threading.Thread(target=handle, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    print("Menunggu koneksi...")
    receive()
