
<!-- saved from url=(0054)http://10.133.2.200/webprog/dyn/examples/lxmlsample.py -->
<html><head><meta http-equiv="Content-Type" content="text/html; charset=Shift_JIS"></head><body>from lxml import html

htmltext = """

    
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

load_html = html.fromstring(htmltext)


p_content = load_html.xpath("//p")

for content in p_content:
    print(content.attrib)
    
# {'class': 'title'}
# {'class': 'recent books'}
# {'class': 'end'}



ret=load_html.xpath("/html/head/title/text()")
print(ret)	
#['�&#65533;��義孝�&#65533;著書']



ret=load_html.xpath('//a[@id="link1"]')
for a in ret:
    print(a.attrib) #{'class': 'book', 'href': 'https://www.amazon.co.jp/dp/B07TN4D3HG', 'id': 'link1'}
    print(a.text) #Python3によるビジネスに役立つ�&#65533;&#65533;タ�&#65533;��入門
</body></html>