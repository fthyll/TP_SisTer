import requests

# Fungsi untuk mengirim permintaan
def send_request():
    method = input("Masukkan metode (GET, POST, PUT, DELETE): ").upper()
    url = input("Masukkan URL: ")
    data = {}

    if method in ['POST', 'PUT']:
        key = input("Masukkan key: ")
        value = input("Masukkan value: ")
        data = {key: value}

    response = None

    if method == 'GET':
        response = requests.get(url)
    elif method == 'POST':
        response = requests.post(url, data=data)
    elif method == 'PUT':
        response = requests.put(url, data=data)
    elif method == 'DELETE':
        response = requests.delete(url)

    if response:
        print('Status Code:', response.status_code)
        print('Response Content (HTML):', response.text)
    else:
        print('Metode tidak valid.')

# Meminta pengguna untuk mengirim permintaan
while True:
    send_request()
    another = input("Kirim permintaan lagi? (y/n): ")
    if another.lower() != 'y':
        break
