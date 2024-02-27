from cs50 import SQL
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

db = SQL('sqlite:///froshims.db')

SPORTS = ['Basketball', 'Soccer', 'Football', 'Ultimate Frisbee']


@app.route('/')
def index():
    return render_template('index.html', sports=SPORTS)


@app.route('/deregister', methods=['POST'])
def deregister():
    # Forget registrant
    id = request.form.get('id')
    if id:
        db.execute('DELETE FROM registrants WHERE id = ?', id)
    return redirect('/registrants')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        sport = request.form.get('sport')
        if not request.form.get('name') or request.form.get('sport') not in SPORTS:
            return render_template('failure.html')
        for sport in request.form.getlist('sport'):
            if sport not in SPORTS:
                return render_template('failure.html')
        db.execute('INSERT INTO registrants (name,sport) VALUES(?, ?)', name, sport)

        return redirect('/registrants')

    return render_template('success.html')


@app.route('/registrants')
def registrants():
    registrants = db.execute('SELECT * FROM registrants')
    return render_template('registrants.html', registrants=registrants)
