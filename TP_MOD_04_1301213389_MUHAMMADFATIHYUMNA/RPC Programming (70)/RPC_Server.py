import socket

# Inisialisasi server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 8888)
server_socket.bind(server_address)
server_socket.listen(5)

print("Voting server is ready.")

candidates = {
    "1": "Prabowo Subianto",
    "2": "Anies Baswedan",
    "3": "Ganjar Pranowo"
}

votes = {candidate_id: 0 for candidate_id in candidates.keys()}

while True:
    print("Menungu Koneksi...")
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    # Menerima pesan dari client
    message = client_socket.recv(1024).decode()

    if message.startswith("VOTE"):
        candidate_id = message.split()[1]
        if candidate_id in candidates:
            votes[candidate_id] += 1
            print(f"{candidates[candidate_id]} menerima 1 suara.")
        else:
            print("Nomer kandidat tidak valid")

    elif message == "RESULTS":
        print("Mengirim hasil pemilihan ke client...")
        result_str = "\n".join([f"{candidates[candidate_id]}: {votes[candidate_id]} votes" for candidate_id in votes.keys()])
        client_socket.send(result_str.encode())

    elif message == "CANDIDATES":
        print("Mengirim daftar kandidat ke client...")
        candidate_list = "\n".join([f"{candidate_id}. {candidates[candidate_id]}" for candidate_id in candidates.keys()])
        client_socket.send(candidate_list.encode())

    elif message == "EXIT":
        print("Keluar dari program voting...")
        break

    client_socket.close()

server_socket.close()
