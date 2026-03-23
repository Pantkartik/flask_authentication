from flask import Flask,session,render_template,request,redirect
import sqlite3

app=Flask(__name__)
app.secret_key="secret123"

# database
def init_db():
    conn=sqlite3.connect('users.db')
    curr=conn.cursor()

    curr.execute('''
                 CREATE A TABLE IF NOT AVAILABLE
                 ''')
    conn.commit()
    conn.close()
    init_db()

# home page 
@app.route('/')
def home():
    return redirect('/login')

# sign in page 
@app.route('/signup',method=['GET','POST'])
def signup():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        