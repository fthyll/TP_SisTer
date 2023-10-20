import requests

url = 'https://restful-api.dev/'
data = {'key': 'value'}
response = requests.post(url, data=data)

print('POST Request:')
print('Status Code:', response.status_code)
print('Response Content (HTML):', response.text)
