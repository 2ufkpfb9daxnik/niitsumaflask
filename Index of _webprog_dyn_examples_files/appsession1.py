from flask import *

app = Flask(__name__)

app.secret_key = 'abcdefghijklmn'

@app.route("/", methods=["GET", "POST"])
def root1():
    txt=""
    if request.method == "POST":
        if "ccount" in session:
            session["ccount"] += 1 #ここで数えている 
        else:
            session["ccount"] = 1
        txt = txt + "count "+ str(session["ccount"]) +"<br>"
    
    return txt+"""
    <form action="/" method="POST">
    <input type="submit" value="submit">
    </form>"""

if __name__ == "__main__":
    app.run()
