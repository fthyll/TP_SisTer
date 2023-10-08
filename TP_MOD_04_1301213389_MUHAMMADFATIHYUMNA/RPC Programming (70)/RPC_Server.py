from xmlrpc.server import SimpleXMLRPCServer

candidates = {
    "1": "Prabowo Subianto",
    "2": "Anies Baswedan",
    "3": "Ganjar Pranowo"
}

votes = {candidate_id: 0 for candidate_id in candidates.keys()}

def is_valid_candidate(candidate_id):
    return candidate_id in candidates

def get_candidates():
    return candidates

def vote(candidate_id):
    if is_valid_candidate(candidate_id):
        votes[candidate_id] += 1
        return f"Vote untuk {candidates[candidate_id]} telah di catat."
    else:
        return "ID kandidat tidak valid."

def get_results():
    return votes

if __name__ == "__main__":
    server = SimpleXMLRPCServer(('localhost', 8888))
    server.register_function(get_candidates, 'get_candidates')
    server.register_function(vote, 'vote')
    server.register_function(get_results, 'get_results')

    print("Server siap menerima voting")
    while True:
        try:
            server.handle_request()
        except KeyboardInterrupt:
            print("\nServer stopped.")
            break

