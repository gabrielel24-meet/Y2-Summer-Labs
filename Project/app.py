from flask import Flask, render_template, request, redirect, url_for
from flask import session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config["SECRET_KEY"] = "big-pink-elephant"


firebaseConfig = {
  "apiKey": "AIzaSyAHNQFfuuu7Wyxod5Hz9DOeNLFRCwkn6hQ",
  "authDomain": "database-lab-ca862.firebaseapp.com",
  "databaseURL": "https://database-lab-ca862-default-rtdb.europe-west1.firebasedatabase.app",
  "projectId": "database-lab-ca862",
  "storageBucket": "database-lab-ca862.appspot.com",
  "messagingSenderId": "273172455040",
  "appId": "1:273172455040:web:ff982c964858c9d7285065",
  "databaseURL":"https://database-lab-ca862-default-rtdb.europe-west1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db =firebase.database()



# CODE

@app.route('/',methods=['GET', 'POST'])
def home():
  if request.method == 'GET':
    return render_template("Home.html")


@app.route('/signup',methods=['GET', 'POST'])
def signup():
  if request.method == 'GET':
    return render_template("Signup.html")
  else:
    try:
      email = request.form['email']
      password = request.form['password']
      firstname = request.form['firstname']
      lastname = request.form['lastname']
      session['user'] = auth.create_user_with_email_and_password(email, password)
      session['email'] = email
      session['password'] = password
      session['firstname'] = firstname
      session['lastname'] = lastname
      Watchlist = [""]

      uid = session['user']['localId']
      UserInfo = {'firstname':firstname, 'lastname':lastname, "Watchlist":Watchlist}
      db.child('users').child(uid).set(UserInfo)
      print(db.child('users').child(uid).get().val())
      return render_template("Library.html")
    except:
      return render_template("error.html")

@app.route('/login',methods=['GET', 'POST'])
def login():
  if request.method == 'GET':
    return render_template("Login.html")
  else:
    try:
      email = request.form['email']
      password = request.form['password']
      session['user'] = auth.sign_in_with_email_and_password(email, password)
      return render_template("Library.html")
    except:
      return render_template("error.html")


@app.route('/library',methods=['GET', 'POST'])
def library():
  if request.method == 'GET':
    return render_template("Library.html")


@app.route('/ratatouille',methods=['GET', 'POST'])
def ratatouille():
  if request.method == 'GET':
    return render_template("Movies/ratatouille.html")
  else:
    uid = session['user']['localId']
    New_Watchlist = db.child('users').child(uid).child("Watchlist").get().val()
    New_Watchlist.append("ratatouille")
    db.child('users').child(uid).update({"Watchlist":New_Watchlist})
    return render_template("Home.html", New_Watchlist = New_Watchlist)


@app.route('/signout',methods=['GET', 'POST'])
def signout():
  if request.method == "POST":
    session["user"] = None
    auth.current_user = None
    return render_template("Login.html")

if __name__ == '__main__':
    app.run(debug = True)