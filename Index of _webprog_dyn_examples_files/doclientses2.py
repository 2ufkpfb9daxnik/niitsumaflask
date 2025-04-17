import requests

ses = requests.Session()
url="http://localhost:5000/"

response = ses.post(url)
print(response.text)

response = ses.post(url)
print(response.text)

response = ses.post(url)
print(response.text)
