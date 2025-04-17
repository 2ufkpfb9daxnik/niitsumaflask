
from flask import *

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def radiotest():
    if request.method == "GET" :
        return """
        選択してください。奇数か偶数か判定します
        <form action ="/" method="POST">
        <input type="radio" name="num" value=0> 0
        <input type="radio" name="num" value=1> 1
        <input type="radio" name="num" value=2 checked> 2
        <input type="submit" value="送信">
        </form>
        """
    else :
        #print(int(request.form["num"]))  #動作を確認
        return """
        {}は
        {}です!
        <form action="/" method="POST">
        <input name="num"></input>
        </form>""".format(str(request.form["num"]),["偶数","奇数"][int(request.form["num"])%2])

if __name__ == '__main__':
    app.run()
