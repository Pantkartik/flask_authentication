# lets make a flask login page using a simple logic 

from flask import Flask ,request,Response,session,url_for,redirect,render_template

app=Flask(__name__)

@app.route('/',methods=["GET","POST"])
def login():
    if request.method=="POST":
        username=request.form("username")
        password=request.form("password")

        if username=="admin" and password=="123":
            session[username]="username"

            return redirect(url_for(main))
        
    return render_template('/login.html')

@app.route('/main')
def main():
    return render_template('catalogoue.html')


if __name__=='__main__':
    app.run(debug=True)