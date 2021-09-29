import requests

response = requests.get("https://api.chucknorris.io/jokes/random")
data = response.text
print(response.json()['value'])
print(response.request.url)
print(response.request.body)
print(data)
