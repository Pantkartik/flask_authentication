# routing the dynamic templates to the server

from flask import Flask,render_template,request,Response,session

app=Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/submit',method=["POST"])
def submit():
    username=request.form("username")
    password=request.form("password")

    if username=="kartik" and password=='123':
        return render_template('welcome.html',name="username")