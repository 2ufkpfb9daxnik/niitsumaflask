import sys
import requests
import lxml.html


#set dummy user-agent
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/602.4.8 (KHTML, like Gecko) Version/10.0.3 Safari/602.4.8'}


url="https://ja.wikipedia.org/wiki/ChatGPT"

#response = requests.get(url, headers = headers)
response = requests.get(url)

htmldata = lxml.html.fromstring(response.content)

# p_content = htmldata.xpath("//p")
# for content in p_content:
#     print(content.text)



contents1 = htmldata.xpath('//*[@id="mw-content-text"]/div[1]/table/tbody/tr[3]/td')
print(len(contents1))
for content in contents1:
    print(dir(content))
    
    print(content.text)
    
    print(content.text_content)
    print(content.values)



    
#/html/body
