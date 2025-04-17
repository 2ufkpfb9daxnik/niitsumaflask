import requests
import lxml.html

url="https://ja.wikipedia.org/wiki/ChatGPT"

response = requests.get(url)

htmldata = lxml.html.fromstring(response.content)

p_content = htmldata.xpath("//p")
for content in p_content:
    print(content.text)
