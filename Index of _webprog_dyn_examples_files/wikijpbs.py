import requests
from bs4 import BeautifulSoup
import urllib.parse

url="https://ja.wikipedia.org/wiki/ChatGPT"
response = requests.get(url)
soup = BeautifulSoup(response.text)


# title タグの文字列を取得する
title_text = soup.find('title').get_text()
print(title_text)

# ページに含まれるリンクを全て取得する
links = [url.get('href') for url in soup.find_all('a')]
print(links)

