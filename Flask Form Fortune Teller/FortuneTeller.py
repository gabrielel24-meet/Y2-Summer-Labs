import random

from flask import Flask, render_template
app = Flask(__name__, template_folder='templates',static_folder='static')



@app.route('/')
def home():
    return render_template("home.html")


@app.route('/fortune')
def fortune():
    fortune_list=["Abdalla is going to chase you around IASA”","You will eat IASA food for the rest of your life","You will be incredibly poor", "You will have no friends", "You are gonna get killed by a bear", "Lilac will let you speak in yout language", "You will be reach", "Your phone is going to fall to the toilet", "Extreme diarrhea"]
    Num = random.randint(0,9)
    return render_template("fortune.html",fortune_list =fortune_list, Num = Num)

if __name__ == '__main__':
    app.run(debug = True)
