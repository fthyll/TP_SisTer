import requests

url = 'https://api.restful-api.dev/objects'
response = requests.get(url)

print('GET Request:')
print('Status Code:', response.status_code)

# Menyimpan hasil respons ke dalam file .txt
with open('./TP_MOD_06_1301213389_MUHAMMADFATIHYUMNA/Respond/get_response.json', 'w') as file:
    file.write(response.text)
