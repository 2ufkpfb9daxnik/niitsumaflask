from flask import Flask, request, redirect,  session

app = Flask(__name__)
app.config['SECRET_KEY']='secret_key'
app.config['USERNAME']='userxyz'
app.config['PASSWORD']='pass123'

@app.route('/')
def index():
    if "flag" in session and session["flag"]:
        return "Welcome"
    return redirect('/login')

@app.route('/login', methods=['GET'])
def login():
    # print(session["flag"],'login:GET')

    if "flag" in session and session["flag"]:
        return redirect('/welcome')
    txt=""
    if "userflag" in session and not session["userflag"]:
        txt = txt + "username wrong<br>"
    if "passflag" in session and not session["passflag"]:
        txt = txt + "password wrong<br>"
    if "logoutflag" in session and not session["logoutflag"]:
        txt = txt + "logout<br>"
    return txt+"""
    <form action="/login" method="post">
      <div>
        <label for="user">user name</label>
        <input type="text" id="user" name="username">
      </div>
      <div>
        <label for="pass">password</label>
        <input type="password" id="pass" name="password">
      </div>
      <button type="submit">login</button>
    </form>

    """

@app.route('/login', methods=['POST'])
def login_post():
    # print(session["flag"],'login:POST')

    username = request.form["username"]
    password = request.form["password"]
    if username != app.config['USERNAME']:
        session["userflag"]=False
    elif password != app.config['PASSWORD']:
        session["userflag"]=True
        session["passflag"]=False
    else:
        session["flag"] = True
        session["logoutflag"]=False
        
        session["username"] = username
        
        session["userflag"]=True
        session["passflag"]=True
        
    if "flag" in session and session["flag"]:
        return "Welcome"
    else:
        return redirect('/login')

@app.route('/welcome')
def welcome():
    if "flag" in session and session["flag"]:
        return "Welcome"
    return redirect('/login')

@app.route('/contents')
def contents():
    if "flag" in session and session["flag"]:
        return "contents"
    return redirect('/login')

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop("flag", None)
    session["username"] = None
    session["flag"] = False
    session["logoutflag"]=True
    return redirect("/login")

if __name__ == '__main__':
    app.run()
