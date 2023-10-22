import requests
import json

url = 'https://api.restful-api.dev/objects/ff8081818b1b4123018b57875164551b'
data = {
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 2049.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB",
      "color": "silver"
   }
}

headers = {'Content-Type': 'application/json'}  # Atur header Content-Type

# Konversi data ke format JSON
json_data = json.dumps(data)

response = requests.put(url, data=json_data, headers=headers)

print('PUT Request:')
print('Status Code:', response.status_code)

# Menyimpan hasil respons ke dalam file .json
with open('./TP_MOD_06_1301213389_MUHAMMADFATIHYUMNA/Respond/put_response.json', 'w') as file:
    file.write(response.text)
