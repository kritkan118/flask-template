from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='My Home Page')

@app.route('/about')
def about():
    title='About Page'
    name='kritkan'
    email='std.67122420118@ubru.ac.th'
    phone='099-682-3419'
    return render_template('about.html',
                           title=title,
                           name=name,
                           email=email,
                           phone=phone)

@app.route('/favorite/foods')
def favorite_foods():
    title='Favorite Foods Page'
    foods = ['ส้มตำ','ข้าวผัด','ไก่ย่าง','คอหมูย่าง','ก๋วยเตี๋ยวเรือ','ลาบเป็ด']
    return render_template('favorite_foods.html',
                           foods=foods,
                           title=title)

@app.route('/sports')
def sports():
    title='Favorite Sports Page'
    sports = ['ฟุตบอล','ฟุตซอล','วอลเลย์บอล','แบดมินตัน','เปตอง']
    return render_template('sports.html',
                           sports=sports,
                           title=title)

@app.route('/greeting/<username>')
def geeting(username):
    title='Welcome Page'
    return render_template('welcome.html',
                           title=title,
                           username=username)

@app.route('/movies')
def movies():
    title='Favorite Movies Page'
    movies = ['ไทยบ้าน เดอะซีรี่ย์','ธี่หยด','สัปเหร่อ','เซียนหรั่ง เดอะมูฟวี่','คิดถึงวิทยา']
    return render_template('movies.html',
                           title=title,
                            movies=movies,)