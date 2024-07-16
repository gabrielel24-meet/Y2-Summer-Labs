from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return (''' <html>
                    <h1>Home</h1>
                    <br/>
                    <p>Welcome to my page!</p>
                    <img src="https://www.eatingwell.com/thmb/m5xUzIOmhWSoXZnY-oZcO9SdArQ=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/article_291139_the-top-10-healthiest-foods-for-kids_-02-4b745e57928c4786a61b47d8ba920058.jpg" width="20%" height="20%">
                    <img src="https://static.scientificamerican.com/sciam/cache/file/2AE14CDD-1265-470C-9B15F49024186C10_source.jpg?w=600" width="20%" height="20%">
                    <img src="https://live-production.wcms.abc-cdn.net.au/8393f16b3a14cd32d0d5d75c1c05d56b?impolicy=wcms_crop_resize&cropH=1080&cropW=1918&xPos=1&yPos=0&width=862&height=485" width="20%" height="20%">
                    </br>
                    <a href="/food1">Food1</a>
                    <a href="/food3">Food3</a>
                    <a href="/space1">Space1</a>
                    <a href="/pet2">Pet2</a>
                </html>''')


@app.route('/food1')
def food1():
    return (''' <html>
                    <img src="https://www.tastingtable.com/img/gallery/what-makes-restaurant-burgers-taste-different-from-homemade-burgers-upgrade/intro-1662064407.jpg" width="50%" height="50%">
                    </br>
                    <a href="/">Home</a>
                    <a href="/food2">Food2</a>
                    <a href="/food3">Food3</a>
                </html>
                ''')


@app.route('/food2')
def food2():
    return (''' <html>
                    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR0Lj3_8eh0xYQLDhyh1pYwOF6l00mL7hIfww&s" width="50%" height="50%">
                    </br>
                    <a href="/food1">Food1</a>
                    <a href="/food3">Food3</a>
                </html>''')

@app.route('/food3')
def food3():
    return (''' <html>
                    <img src="https://bakerbynature.com/wp-content/uploads/2015/02/Sweet-and-Spicy-Sriracha-Chicken-Wings-0-6.jpg" width="30%" height="60%">
                    </br>
                    <a href="/">Home</a>
                    <a href="/food2">Food2</a>
                </html>''')


@app.route('/pet2')
def pet2():
    return (''' <html>
                    <img src="https://www.thesprucepets.com/thmb/hxWjs7evF2hP1Fb1c1HAvRi_Rw0=/2765x0/filters:no_upscale():strip_icc()/chinese-dog-breeds-4797219-hero-2a1e9c5ed2c54d00aef75b05c5db399c.jpg" width="50%" height="50%">
                    </br>
                    <a href="/">Home</a>
                    <a href="/pet1">Pet1</a>
                    <a href="/pet3">Pet3</a>
                </html>''')


@app.route('/pet1')
def pet1():
    return (''' <html>
                    <img src="https://i.natgeofe.com/n/9135ca87-0115-4a22-8caf-d1bdef97a814/75552.jpg" width="50%" height="50%">
                    </br>
                    <a href="/pet2">Pet2</a>
                </html>''')


@app.route('/pet3')
def pet3():
    return (''' <html>
                    <img src="https://t4.ftcdn.net/jpg/06/08/41/09/360_F_608410951_8OhMYUIq37acegYgSrKdFN0kAw0xRKx9.jpg" width="50%" height="50%">
                    </br>
                    <a href="/pet2">Pet2</a>
                </html>''')


@app.route('/space1')
def space1():
    return (''' <html>
                    <img src="https://starwalk.space/gallery/images/what-is-space/1920x1080.jpg" width="50%" height="50%">
                    </br>
                    <a href="/">Home</a>
                    <a href="/space2">Space2</a>
                    <a href="/space3">Space3</a>
                </html>''')


@app.route('/space2')
def space2():
    return (''' <html>
                    <img src="https://live-production.wcms.abc-cdn.net.au/8393f16b3a14cd32d0d5d75c1c05d56b?impolicy=wcms_crop_resize&cropH=1080&cropW=1918&xPos=1&yPos=0&width=862&height=485" width="50%" height="50%">
                    </br>
                    <a href="/space1">Space1</a>
                    <a href="/space3">Space3</a>
                </html>''')


@app.route('/space3')
def space3():
    return (''' <html>
                    <img src="https://t4.ftcdn.net/jpg/03/86/82/73/360_F_386827376_uWOOhKGk6A4UVL5imUBt20Bh8cmODqzx.jpg" width="50%" height="50%">
                    </br>
                    <a href="/space2">Space2</a>
                    <a href="/space1">Space1</a>
                </html>''')



if __name__ == '__main__':
    app.run(debug=True)