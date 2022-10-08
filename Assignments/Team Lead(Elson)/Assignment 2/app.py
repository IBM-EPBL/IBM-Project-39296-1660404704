from flask import Flask, render_template, request, redirect, url_for, flash
import ibm_db
import secrets

conn = ibm_db.connect("DATABASE="+DATABASE_NAME+";HOSTNAME="+HOST+";PORT="+PORT+";SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID="+USER_ID+";PWD="+PASSWORD,'','')

app = Flask(__name__)
app.secret_key = "69420"


@app.route('/')
def index():
    return render_template('index.html', title='Home')


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/signin', methods=('GET', 'POST'))
def signin():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        user = db.execute(
            'SELECT password FROM users WHERE username = ?', (username, )
        ).fetchone()
        
        if user is None:
            error = 'Incorrect Username/Password.'
        elif password != user['password']:
            print(user)
            error = 'Incorrect Password.'

        if error is None:
            return redirect(url_for('index'))
        flash(error)
        db.close()

    return render_template('signin.html', title='Sign In', error=error)


@app.route('/signup', methods=('POST', 'GET'))
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        name = request.form['name']
        db = get_db()
        curr = db.cursor()
        
        curr.execute(
            'INSERT INTO users (username, password, email, name) VALUES (?, ?, ?, ?);', (username, password, email, name)
        )
        db.commit()
        curr.close()
        db.close()
        return render_template('index.html', title="Home", succ="Registration Successfull!")
        

    return render_template('signup.html', title='Sign Up')
