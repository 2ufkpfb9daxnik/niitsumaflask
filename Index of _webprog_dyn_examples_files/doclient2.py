import requests

url="http://128.199.144.38:5100/"
response = requests.post(url,data={'qjan':1})
print(response.text)
