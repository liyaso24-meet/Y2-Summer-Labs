#importings
from flask import Flask, render_template, request, redirect, url_for
from flask import session as login_session 
import pyrebase

#app load

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

#Firebase configuration
firebaseConfig = {
  "apiKey": "AIzaSyAr6GBfiEUoSs7PU1Iz6RsXY973W3mpW-8",
  "authDomain": "authlab-44360.firebaseapp.com",
  "projectId": "authlab-44360",
  "storageBucket": "authlab-44360.appspot.com",
  "messagingSenderId": "436236602790",
  "appId": "1:436236602790:web:253dfc8a1613048218d367",
  "measurementId": "G-LJ60N5MB83",
  "databaseURL": ""
};

#Initialize firebase
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

#app route main
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html") 
    else: 
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            login_session['quotes'] = []
            print(login_session['user'])
            print(auth.current_user)
            return redirect(url_for('home'))

        except:
            error = "login failed, try again."
            return render_template("login.html", error=error)

#app route signup
@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == 'GET':
        return render_template("signup.html") 
    else: 
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            login_session['quotes'] = []
            return redirect(url_for('/home'))
        except:
            error = "Authentication error"
            return render_template("signup.html",error=error)
        
#app route home
@app.route('/home', methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("home.html")
    else:
        quote = request.form['quote']
        login_session['quotes'].append(quote)
        login_session.modified = True
        print(login_session['quotes'])
        return redirect(url_for('thanks'))


#app route thanks
@app.route('/thanks')
def thanks():
    return render_template("thanks.html")


@app.route('/signout')
def signout():
    login_session['user'] = None
    auth.current_user = None
    return redirect(url_for('login'))


#app route display
@app.route('/display', methods=['GET','POST'])
def display():
    getquote = login_session['quotes']
    return render_template("display.html", getquote= getquote)

if __name__ == '__main__':
    app.run(debug=True)
