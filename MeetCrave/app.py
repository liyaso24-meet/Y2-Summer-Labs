#importings
from flask import Flask, render_template, request, redirect, url_for
from flask import session as login_session 
import pyrebase

#app load

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

#Firebase configuration
firebaseConfig = {
  "apiKey": "AIzaSyDp_Gq0-kY5GPTALhEvP0SCcC3R0BhccFg",
  "authDomain": "meetcrave-72326.firebaseapp.com",
  "projectId": "meetcrave-72326",
  "storageBucket": "meetcrave-72326.appspot.com",
  "messagingSenderId": "827426571497",
  "appId": "1:827426571497:web:a1cb69b22b3ec29bae5c78",
  "measurementId": "G-BJSJ1C75M9",
  "databaseURL": "https://meetcrave-72326-default-rtdb.europe-west1.firebasedatabase.app/" 
};

#Initialize firebase
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

#app route main
@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template("main.html")
 
#app route login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html") 
    else: 
        email = request.form['email']
        password = request.form['password']

        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            login_session['crave'] = []
            return redirect(url_for('crave'))

        except Exception as e:
            error = "login failed, try again."
            print(e)
            return render_template("login.html", error=error)


#app route signup
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template("signup.html") 
    else: 
        email = request.form['email']
        password = request.form['password']
        username = request.form['username']

        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            UID = login_session['user']['localId']
            user = {"email": email, "password": password, "username": username}
            db.child("users").child(UID).set(user)
            login_session['crave'] = []
            return redirect(url_for('crave'))
        except Exception as e:
            error = "Authentication error"
            print(e)
            return render_template("signup.html",error=error)
        
#app route Crave
@app.route('/crave', methods= ['GET', 'POST'])
def crave():
    if request.method == 'GET':
        return render_template("crave.html") 
    else: 
        UID = login_session['user']['localId']
        crave = {"crave":request.form['crave'], "whocraves": request.form['whocraves'], "comments": {}}
        db.child('crave').push(crave)
        return redirect(url_for('gallary'))

#app route gallary
@app.route('/gallary', methods= ['GET', 'POST'])
def gallary():
    if request.method == 'GET':
        crave = db.child("crave").get().val()
        return render_template("gallary.html", crave= crave)

    #else:
       # UID = login_session['user']['localId']
        #crave = {"crave":request.form['crave'], "whocraves": request.form['whocraves'], "comments": {}}
        #db.child('crave').push(crave)
        #return render_template("gallary.html")

#app route signout
@app.route('/signout')
def signout():
    login_session['user'] = None
    auth.current_user = None
    return redirect(url_for('main'))



if __name__ == '__main__':
    app.run(debug=True)
