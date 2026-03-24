# from flask import Flask,session,render_template,request,redirect
# import sqlite3

# app=Flask(__name__)
# app.secret_key="secret123"

# # database
# def init_db():
#     conn=sqlite3.connect('users.db')
#     curr=conn.cursor()

#     curr.execute('''
#                  CREATE A TABLE IF NOT AVAILABLE
#                  ''')
#     conn.commit()
#     conn.close()
#     init_db()

# # home page 
# @app.route('/')
# def home():
#     return redirect('/login')

# # sign in page 
# @app.route('/signup',method=['GET','POST'])
# def signup():
#     if request.method=='POST':
#         username=request.form['username']
#         password=request.form['password']


# # making a post request for signin 
# @app.route('/submit',methods=["GET","POST"])
# def submit():
#     if request.method=="POST":
#         return ''' 
#         This is the post request 
#  '''

        



#  Login page 

from flask import Flask,request,redirect,session,url_for,Response

app=Flask(__name__)

@app.route('/',methods=["GET","POST"])
def login():
    if request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")

        if username=="admin" and password=="123":
            session["user"]=username
            return redirect(url_for('welcome'))
        else :
            return Response("Invalid crendentials ",mimetype="text/plain") #text/plain is used to return plain text response
        # login html page 
    return '''
<h1/>Login Page
<form method="POST">
Username:<input type="text" name="Username">
Password:<input type="text" name="Password">
<input type="submit" value="Login">
<form/>
'''

# redirect to welcome page after login 
@app.route('/welcome')
def welcome():
    if "user" in session:
        return f'''<h1/>Welcome!{session["user"]}
            <a href={url_for("Logout")}logout</a>
'''
    return redirect(url_for("login"))
                