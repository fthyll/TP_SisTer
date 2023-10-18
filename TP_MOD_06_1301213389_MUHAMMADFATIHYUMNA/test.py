#POST
import requests

data = {
    'field1': 130
}

write_api_key = 'GBZW4DXEPO65SJ1X'

url = f'https://api.thingspeak.com/update?api_key={write_api_key}'
response = requests.post(url, data=data)

#GET
read_api_key = 'J7CGFZRXJLG8QRM1'

url = f'https://api.thingspeak.com/channels/1114436/feeds.json?api_key={read_api_key}'
response = requests.get(url)

data = response.json()

print(data)
