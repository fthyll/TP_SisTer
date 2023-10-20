import requests

url = 'https://restful-api.dev/'
data = {'key': 'updated_value'}
response = requests.put(url, data=data)

print('PUT Request:')
print('Status Code:', response.status_code)
print('Response Content (HTML):', response.text)
