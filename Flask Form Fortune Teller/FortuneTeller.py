import random

from flask import Flask, render_template,url_for,redirect,request
app = Flask(__name__, template_folder='templates',static_folder='static')



@app.route('/',methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template("home.html")
    else:
        Birth = request.form["birth"]
        Num_birth = len(Birth) -1
        return redirect(url_for("fortune", Num_birth = Num_birth))


@app.route('/fortune/<int:Num_birth>')
def fortune(Num_birth):
    fortune_list=["Abdalla is going to chase you around IASA”","You will eat IASA food for the rest of your life","You will be incredibly poor", "You will have no friends", "You are gonna get killed by a bear", "Lilac will let you speak in yout language", "You will be rich", "Your phone is going to fall to the toilet", "Extreme diarrhea", "You will have a great day"]
    Num = random.randint(0,9)
    
    return render_template("fortune.html",fortune_list =fortune_list, Num = Num,Num_birth = Num_birth)

if __name__ == '__main__':
    app.run(debug = True)
