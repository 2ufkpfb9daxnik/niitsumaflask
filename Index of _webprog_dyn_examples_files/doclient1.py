import requests

url="http://128.199.144.38:5100/"
response = requests.get(url)
print(response.text)
