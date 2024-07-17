#importing libraries etc
from flask import Flask, render_template
import random

app = Flask(__name__)

#route 1
@app.route('/')
def home():
	return render_template("home.html")

#route 2
@app.route('/fortune')
def fortune():
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
	return render_template("fortune.html", random_fortune= (random.choice(fortune))
)


if __name__ == '__main__':
	app.run(debug = True)
