import sys
import requests
import lxml.html


import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

url="https://en.wikipedia.org/wiki/ChatGPT"

response = requests.get(url)
htmldata = lxml.html.fromstring(response.content)

pns=[]

for i in range(2,5):
    xp='/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/p['+str(i)+']'

    p_content = htmldata.xpath(xp)
    for content in p_content:
        text=content.text_content()
        print(text)
        tokenized_words = nltk.word_tokenize(text)
        pos_tagged_text = nltk.pos_tag(tokenized_words)
        #print(pos_tagged_text)

        proper_nouns = [w[0] for w in pos_tagged_text  if w[1]=='NNP' ]
        print(proper_nouns)

        pns += proper_nouns

print(pns)

for t in set(pns):
     print(t,pns.count(t))
