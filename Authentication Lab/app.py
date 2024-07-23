from flask import Flask, render_template, request, redirect, url_for
from flask import session
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
  "databaseURL":"https://auth-lab-gabi-default-rtdb.europe-west1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db =firebase.database()


# CODE

@app.route('/',methods=['GET', 'POST'])
def signup():
  if request.method == 'GET':
    return render_template("signup.html")
  else:
    try:
      email = request.form['email']
      password = request.form['password']
      name = request.form['name']
      username = request.form['username']
      session['user'] = auth.create_user_with_email_and_password(email, password)
      session['quotes']=[]
      session['email'] = email
      session['password'] = password
      session['name'] = name
      session['username'] = username
      user = {'email':email, 'name':name, 'username': username}
      uid = session['user']['localId']
      db.child('users').child(uid).set(user)
      return redirect(url_for('home'))
    except:
      error = "Authentication failed"
      return render_template("error.html")




@app.route('/signin',methods=['GET', 'POST'])
def signin():
  if request.method == 'GET':
    return render_template("signin.html")
  else:
    try:
      email = request.form['email']
      password = request.form['password']
      session['quotes']=[]
      session['user'] = auth.sign_in_with_email_and_password(email, password)
      return redirect(url_for('home'))
    except:
      error = "Authentication failed"
      return render_template("error.html")


@app.route('/home',methods=['GET', 'POST'])
def home():
  if request.method == 'GET' and session['user'] != None:
    return render_template("home.html")
  elif request.method == 'GET' and session['user'] == None:
    return render_template("error.html")
  else:
    quote = request.form["quote"]
    quote_name = request.form['quote_name']
    uid = session['user']['localId']
    quote_dic = {'quote':quote, 'quote_name':quote_name, 'uid':uid}
    db.child('quote').push(quote_dic)
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
    quotes = db.child('quote').get().val()
    return render_template("display.html" , quotes = quotes)

if __name__ == '__main__':
    app.run(debug = True)