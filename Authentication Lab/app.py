from flask import Flask, render_template, request, redirect, url_for
from flask import session as session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config["SECRET_KEY"] = "big-pink-elephant"


firebaseConfig = {
  "apiKey": "AIzaSyAqFD7zHbDG0VD-k6J3pcV_WuohJpsP1nI",
  "authDomain": "auth-lab-gabi.firebaseapp.com",
  "projectId": "auth-lab-gabi",
  "storageBucket": "auth-lab-gabi.appspot.com",
  "messagingSenderId": "433593331448",
  "appId": "1:433593331448:web:44b3f84f6dafef322b150d",
  "databaseURL":""
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()


# CODE

@app.route('/',methods=['GET', 'POST'])
def signup():
  if request.method == 'GET':
    return render_template("signup.html")
  else:
    try:
      email = request.form['email']
      password = request.form['password']
      session['user'] = auth.create_user_with_email_and_password(email, password)
      session['quotes']=[]
      session['email'] = email
      session['password'] = password
      return redirect(url_for('home'))
    except:
      error = "Authentication failed"
      return render_template("signin.html")




@app.route('/signin',methods=['GET', 'POST'])
def signin():
  if request.method == 'GET':
    return render_template("signin.html")
  else:
    try:
      email = request.form['email']
      password = request.form['password']
      session['user'] = auth.sign_in_with_email_and_password(email, password)
      return redirect(url_for('home'))
    except:
      error = "Authentication failed"
      return render_template("home.html")


@app.route('/home',methods=['GET', 'POST'])
def home():
  if request.method == 'GET':
    return render_template("home.html")
  else:
    quote = request.form["quote"]
    session["quotes"].append(quote)
    session.current_user = True
    return redirect(url_for("thanks"))


@app.route('/signout',methods=['GET', 'POST'])
def signout():
  if request.method == "GET":
    session["user"] = None
    auth.current_user = None
    return redirect(url_for("signin"))


@app.route('/thanks',methods=['GET', 'POST'])
def thanks():
  if request.method == 'GET':
    return render_template("thanks.html")

@app.route('/display',methods=['GET', 'POST'])
def display():
  if request.method == 'GET':
    quotes = session["quotes"]
    return render_template("display.html" , quotes = quotes)

if __name__ == '__main__':
    app.run(debug = True)
