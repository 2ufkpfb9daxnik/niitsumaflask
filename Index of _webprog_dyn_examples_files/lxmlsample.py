
<!-- saved from url=(0054)http://10.133.2.200/webprog/dyn/examples/lxmlsample.py -->
<html><head><meta http-equiv="Content-Type" content="text/html; charset=Shift_JIS"></head><body>from lxml import html

htmltext = """

    
        <title>貂&#65533;ｰｴ鄒ｩ蟄昴&#65533;闡玲嶌</title>
    
    
        <p class="title">
            <b>貂&#65533;ｰｴ鄒ｩ蟄昴&#65533;譛譁ｰ縺ｮ闡玲嶌縺ｫ縺ｯ縲∵ｬ｡縺ｮ譛ｬ縺後≠繧翫∪縺吶&#65533;</b>
        </p>
        <p class="recent books">
            <a class="book" href="https://www.amazon.co.jp/dp/B07TN4D3HG" id="link1">
                Python3縺ｫ繧医ｋ繝薙ず繝阪せ縺ｫ蠖ｹ遶九▽繝&#65533;&#65533;繧ｿ蛻&#65533;梵蜈･髢
            </a>
            <a class="book" href="http://www.amazon.co.jp/dp/B07SRLRS4M" id="link2">
                繧医￥繧上°繧輝ython3蜈･髢2.NumPy繝ｻMatplotlib邱ｨ
            </a>
            <a class="book" href="http://www.amazon.co.jp/dp/B07T9SZ96B" id="link3">
                繧医￥繧上°繧輝ython3蜈･髢4.Pandas縺ｧ繝&#65533;&#65533;繧ｿ蛻&#65533;梵邱ｨ
            </a>
        </p>
        <p class="end">
            <b>縺昴＠縺ｦ縲√％繧後ｉ縺ｮ譛ｬ縺ｯ螂ｽ隧慕匱螢ｲ荳ｭ縺ｧ縺吶&#65533;</b>
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
#['貂&#65533;ｰｴ鄒ｩ蟄昴&#65533;闡玲嶌']



ret=load_html.xpath('//a[@id="link1"]')
for a in ret:
    print(a.attrib) #{'class': 'book', 'href': 'https://www.amazon.co.jp/dp/B07TN4D3HG', 'id': 'link1'}
    print(a.text) #Python3縺ｫ繧医ｋ繝薙ず繝阪せ縺ｫ蠖ｹ遶九▽繝&#65533;&#65533;繧ｿ蛻&#65533;梵蜈･髢
</body></html>