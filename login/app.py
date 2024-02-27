from flask import Flask, redirect, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config['SESSION_PERMAMENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', name=session.get('name'))


@app.route('/login', methods=["POST", 'GET'])
def login():
    if request.method == 'POST':
        session['name'] = request.form.get('name')
        return redirect('/')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')