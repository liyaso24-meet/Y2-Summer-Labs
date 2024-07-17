#importing libraries etc
from flask import Flask, render_template, url_for, redirect, request
import random

app = Flask(__name__, template_folder = 'templates')

#route 1
@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'GET':
		return render_template("home.html")
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
	app.run(debug = True)


