from flask import *
from urllib.request import *
import os
import random

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Response static file
@app.route("/")
def index():
    return send_file("./static/index.html","text/html")

# Response content
@app.route("/content")
def content():
    return "Hello Flask"

# Template Engines
@app.route("/template")
def template():
    return render_template('hello.html', name = "Jinja2 Template Engines")

# Response JsonString 
@app.route("/json")
def json():
    return {
        "Name": "Flask",
        "Lang": "Python",
        "Template Engines": "Jinja2"
    }

# Redirect
@app.route("/redirect")
def redirectTest():
    return redirect("https://docs.python.org/zh-cn/3/library/index.html")

# QueryString
@app.route("/querystring")
def queryString():
    return request.args

# Form
@app.route("/form", methods=["post"])
def form():
    return request.form

# FormFile
# enctype="multipart/form-data"
@app.route("/formfile", methods=["post"])
def formFile():
    tempFile = request.files["file"]
    tempFile.save("./temp.txt")
    return "上传成功"

# Set Cookie
@app.route("/cookie")
def setCookie():
    resp = make_response('''
        <p>Already set Cookie</p>
        <a href='/getCookie'>Show Cookies</a>
    ''')
    resp.set_cookie(
        str(random.random()), 
        str(random.random())
    )
    return resp

# Get Cookies
@app.route("/getCookie")
def getCookie():
    return request.cookies

# Set Session
@app.route("/session")
def setSession():
    session["user"] = str(random.random())
    return '''
        <p>Already set Session</p>
        <a href='/getSession'>Show Sessions</a>
    '''

# Get Session
@app.route("/getSession")
def getSession():
    return session["user"]

# Proxy
@app.route("/proxy")
def proxy():
    # return urlopen("https://www.baidu.com")
    return urlopen("https://www.baidu.com").read().decode("utf-8")

app.run()