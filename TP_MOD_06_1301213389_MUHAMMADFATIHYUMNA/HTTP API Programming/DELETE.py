import requests

url = 'https://api.restful-api.dev/objects/ff8081818b1b4123018b57875164551b'
response = requests.delete(url)

print('DELETE Request:')
print('Status Code:', response.status_code)

# Menyimpan hasil respons ke dalam file .json
with open('./TP_MOD_06_1301213389_MUHAMMADFATIHYUMNA/Respond/delete_response.json', 'w') as file:
    file.write(response.text)
