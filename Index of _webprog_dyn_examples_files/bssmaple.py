
<!-- saved from url=(0052)http://10.133.2.200/webprog/dyn/examples/bssample.py -->
<html><head><meta http-equiv="Content-Type" content="text/html; charset=Shift_JIS"></head><body>from bs4 import BeautifulSoup
html = """

    
        <title>�&#65533;��義孝�&#65533;著書</title>
    
    
        <p class="title">
            <b>�&#65533;��義孝�&#65533;最新の著書には、次の本があります�&#65533;</b>
        </p>
        <p class="recent books">
            <a class="book" href="https://www.amazon.co.jp/dp/B07TN4D3HG" id="link1">
                Python3によるビジネスに役立つ�&#65533;&#65533;タ�&#65533;��入門
            </a>
            <a class="book" href="http://www.amazon.co.jp/dp/B07SRLRS4M" id="link2">
                よくわかるPython3入門2.NumPy・Matplotlib編
            </a>
            <a class="book" href="http://www.amazon.co.jp/dp/B07T9SZ96B" id="link3">
                よくわかるPython3入門4.Pandasで�&#65533;&#65533;タ�&#65533;��編
            </a>
        </p>
        <p class="end">
            <b>そして、これらの本は好評発売中です�&#65533;</b>
        </p>
    

"""
soup = BeautifulSoup(html,'html.parser')

## 基礎的な使�&#65533;��　実行してそれぞれの出力を確認してみよう


print(soup.get_text())

print('--')

print(soup.html.head.title)

print('--')

print(soup.title)

print('--')

print(soup.title.string)

print('--')


for p in soup.body.find_all("p"):
    print(p)

print('--')


print(soup.body.p["class"])

print('--')


for child in soup.body.contents:
    print(child)

print('--')


print(soup.select(".end"))

print('--')


print(soup.select("p.end"))

print('--')
	
print(soup.select(".recent.books"))

print('--')

print(soup.select("#link2"))

print('--')

print(soup.select('a[href*="amazon"]'))

print('--')

print(soup.select("body &gt; p.end"))

print('--')



## 応用�&#65533;

## <p> で　#link2 のある要�&#65533;の親要�&#65533;
for p in soup.body.find_all("p"):
    ret=p.select("#link2")
    if len(ret)&gt;0:
        print(ret[0].parent)
</p></body></html>