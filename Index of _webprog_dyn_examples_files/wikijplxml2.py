import sys
import requests
import lxml.html
import MeCab
m = MeCab.Tagger("-Ochasen")

url="https://ja.wikipedia.org/wiki/ChatGPT"

response = requests.get(url)
htmldata = lxml.html.fromstring(response.content)

pns=[]

xp='/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/p[4]'
p_content = htmldata.xpath(xp)
for content in p_content:
    text=content.text_content()
    result = m.parse(text)
    proper_nouns = [line for line in m.parse(text).splitlines()  if "固有名詞" in line.split()[-1]]
    #print(proper_nouns)
    
    proper_nouns1=[s.split()[0] for s in proper_nouns]
    #print(proper_nouns1)

    pns += proper_nouns1
    
#sys.exit()

for i in range(5,9):
    xp='/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/p['+str(i)+']'
    p_content = htmldata.xpath(xp)
    for content in p_content:
        text=content.text_content()
        result = m.parse(text)
        
        proper_nouns = [line for line in m.parse(text).splitlines()  if "固有名詞" in line.split()[-1]]
        proper_nouns1=[s.split()[0] for s in proper_nouns]
        #print(proper_nouns1)
    
        pns += proper_nouns1

print(pns)

for t in set(pns):
    print(t,pns.count(t))
