import requests

url = 'https://api.restful-api.dev/objects'  # URL tempat Anda ingin membuat POST request
data = {
    "name": "Apple MacBook Pro 16",
    "data": {
        "year": 2019,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB"
    }
}

response = requests.post(url, json=data)  # Menggunakan metode POST

print('POST Request:')
print('Status Code:', response.status_code)

# Menyimpan hasil respons ke dalam file .json
with open('./TP_MOD_06_1301213389_MUHAMMADFATIHYUMNA/Respond/post_response.json', 'w') as file:
    file.write(response.text)
