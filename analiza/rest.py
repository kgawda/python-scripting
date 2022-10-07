import requests

response = requests.get("https://wttr.in/Warsaw?format=j1")
response.raise_for_status()
# print(response.text[:1024])
j = response.json()
print(j['current_condition'][0]['temp_C'])

# requests.post("https://...", data={'key': 'value'})
