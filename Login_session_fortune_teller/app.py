#importing libraries etc
"""from flask import Flask, render_template, url_for, redirect, request
import random
from flask import session as login_sessiion

app = Flask(__name__, template_folder = 'templates')
app.config['SECRET_KEY']="ADMINpass"

#route login
@app.route('/', methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		return render_template("login_fortune.html")
	else: 
		myname = request.form['username']
		password = request.form['username']
		if myname == 'Liya':
			login_session["admin"] = True
		else:
			login_session["admin"] = False
		return redirect(url_for('home'))



#route 1
@app.route('/home', methods=['GET', 'POST'])
def home():
	if request.method == 'GET':
		return render_template("user(1).html",admin=login_sessiion['admin'])
	else:
		name = request.form['birth_month']
		return redirect(url_for('fortune', name=name, length=len(name)))


#route 2
@app.route('/fortune/<string:name>/<int:length>')
def fortune(name, length):
	fortune = ["Good things come to those who wait.",
	 "Patience is a virtue.","The early bird gets the worm.",
     "A wise man once said, everything in its own time and place.",
	 "Fortune cookies rarely share fortunes.",
	 "Do not be afraid of competition.",
	 "You love peace.",
	 "You are kind and friendly.",
	 "Y2 summer is good for you",
	 "You will always be surrounded by true friends.",
	 "You should be able to undertake and complete anything."] 
	if len(name) > 10:
		return redirect(url_for('home'))
	fortune_length = fortune[length]	
	return render_template("fortune.html", random_fortune= fortune_length
		)





if __name__ == '__main__':
	app.run(debug = True)"""

























#imports and calling app
from flask import Flask, render_template, request, redirect, url_for
from flask import session as login_sessiion
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  

#route for login page
@app.route('/', methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		return render_template("login.html")
	else:
		if 'username' in request.form and 'password' in request.form:
			username = request.form['username']
			password = request.form['password']
			return render_template('home.html', username=username, password=password, length=len(password))
		#doesn't seem to work (next 2 lines)
		else:
			return "Missing username or birth month"
			login_session['username'] = username
			login_session['password'] = password

#route to loged in users
@app.route('/fortune/<string:password>/<int:length>')
def fortune(password, length):
	fortune = ["Good things come to those who wait.",
	"Patience is a virtue.","The early bird gets the worm.",
    "A wise man once said, everything in its own time and place.",
	"Fortune cookies rarely share fortunes.",
	"Do not be afraid of competition.",
	"You love peace.",
	"You are kind and friendly.",
	"Y2 summer is good for you",
	"You will always be surrounded by true friends.",
	"You should be able to undertake and complete anything.",
	"NOVEMBER IS THE BEST MONTH OF THE YEAR",
	"You will have good new today!"]
	#I do not think it works (the next 2 lines of code)
	if len(password) > 12:
		return redirect(url_for('login'))
	birthlength = password[length]
	return render_template("newfortune.html", randomfortune= birthlength)


if __name__ == '__main__':
    app.run(debug=True)


#Can't find why it doesnt lead me to the fortune route after clicking on the button, it worked but then stopped.
#(I've bee working on it for most parts of the weekend) 