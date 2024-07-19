import random

from flask import Flask, render_template,url_for,redirect,request
from flask import session as session
app = Flask(__name__, template_folder='templates',static_folder='static')

app.config["SECRET_KEY"] = "big-pink-elephant"

@app.route('/',methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        Start = False
        return render_template("login.html", Start = Start)
    else:
        fortune_list=["Abdalla is going to chase you around IASA”","You will eat IASA food for the rest of your life","You will be incredibly poor", "You will have no friends", "You are gonna get killed by a bear", "Lilac will let you speak in yout language", "You will be rich", "Your phone is going to fall to the toilet", "Extreme diarrhea", "You will have a great day"]
        Start = True
        Name = request.form["Name"]
        Birth = request.form["Birth"]
        session["Name"] = Name
        session["Birth"] = Birth
        Num_birth = len(Birth) -1
        Num = random.randint(0,9)
        return render_template("login.html", Num_birth = Num_birth,fortune_list = fortune_list, Num = Num, Start = Start)


if __name__ == '__main__':
    app.run(debug = True)


