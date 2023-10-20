import requests

url = 'https://restful-api.dev/'
response = requests.delete(url)

print('DELETE Request:')
print('Status Code:', response.status_code)
