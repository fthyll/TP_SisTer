import socket

def vote(candidate_id):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 8888)
    client_socket.connect(server_address)

    message = f"VOTE {candidate_id}"
    client_socket.send(message.encode())

    response = client_socket.recv(1024).decode()
    print(response)

    client_socket.close()

def get_results():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 8888)
    client_socket.connect(server_address)

    message = "RESULTS"
    client_socket.send(message.encode())

    results = client_socket.recv(1024).decode()
    print("Voting Results:")
    print(results)

    client_socket.close()

def get_candidates():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 8888)
    client_socket.connect(server_address)

    message = "CANDIDATES"
    client_socket.send(message.encode())

    candidates = client_socket.recv(1024).decode()
    print("Daftar Calon Presiden 2024:")
    print(candidates)

    client_socket.close()

def main():
    while True:
        print("\nOptions:")
        print("1. Daftar Calon Presiden 2024")
        print("2. Vote")
        print("3. Hasil Pemilihan")
        print("4. Exit")
        choice = input("Masukan pilihanmu: ")

        if choice == "1":
            get_candidates()
        elif choice == "2":
            print("1.Prabowo Subianto")
            print("2.Anies Baswedan")
            print("3.Ganjar Pranowo")
            candidate_id = input("Masukan nomor urut calon presiden yang dipilih anda: ")
            vote(candidate_id)
        elif choice == "3":
            get_results()
        elif choice == "4":
            vote("EXIT")
            break
        else:
            print("Nomer pilihan tidak valid.")

if __name__ == "__main__":
    main()
