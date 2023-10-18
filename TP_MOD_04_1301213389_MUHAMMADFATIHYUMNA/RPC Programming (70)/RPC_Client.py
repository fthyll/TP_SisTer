import xmlrpc.client

def main():
    proxy = xmlrpc.client.ServerProxy("http://localhost:8888/")

    while True:
        print("\nOptions:")
        print("1. Daftar Calon Presiden 2024")
        print("2. Vote")
        print("3. Hasil Pemilihan")
        print("4. Exit")
        choice = input("Masukan pilihanmu: ")

        if choice == "1":
            candidates = proxy.get_candidates()
            print("Daftar Calon Presiden 2024:")
            for candidate_id, candidate_name in candidates.items():
                print(f"{candidate_id}. {candidate_name}")
        elif choice == "2":
            candidates = proxy.get_candidates()
            print("Daftar Calon Presiden 2024:")
            for candidate_id, candidate_name in candidates.items():
                print(f"{candidate_id}. {candidate_name}")

            candidate_id = input("Masukan nomor urut calon presiden yang dipilih anda: ")
            if candidate_id in ["1", "2", "3"]:
                result = proxy.vote(candidate_id)
                print(result)
            else:
                print("Invalid candidate ID.")
        elif choice == "3":
            results = proxy.get_results()
            print("Voting Results:")
            for candidate_id, vote_count in results.items():
                candidates = proxy.get_candidates()
                candidate_name = candidates.get(candidate_id, "Invalid Candidate")
                print(f"{candidate_name}: {vote_count} votes")
        elif choice == "4":
            break
        else:
            print("Nomer pilihan tidak valid.")

if __name__ == "__main__":
    main()
