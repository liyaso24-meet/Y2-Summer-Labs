#importing flask libraries
from flask import Flask

#configuring app settings
app = Flask(__name__)


#main
@app.route('/')
def home():
	return('''<html><header>Welcome to the photo galary food</header>
		<body><a href='/food1'>Go to the food galary number 1</a><br><a href='/food3'>Go to food galary number 3</a><br><a href='/pets'>Go to the pets galary</a><br>
		<a href='outer_space2'>Go to the outer space 2 galary</a></body></html>''')



#food routes
@app.route('/food1')
def food():
	return('''<html><body><p>The first food photo<br><a href= '/'>click here to go to Home page</a><br><a href= '/food2'>Next Food galary</a></p>
		<img src= https://cdn.shopify.com/s/files/1/0070/7032/files/food-photgraphy-tips.png?v=1657891849 width= 1000px</img></body></html>''')

@app.route('/food2')
def food2():
	return('''<html><body><p>The second food photo<br><a href= '/'>click here to go to Home page</a></p>
		<img src= https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSV1wdLPlvaWSTrIQr6CbHp2EuXK2NsPyJhKg&s width= 1000px</img></body></html>''')

@app.route('/food3')
def food3():
	return('''<html><body><p>The last food photo<br><a href= '/'>click here to go back to Home page</a></p>
		<img src= https://www.foodiesfeed.com/wp-content/uploads/2023/06/burger-with-melted-cheese.jpg width= 1000px</img></body></html>''')




#pet routes
@app.route('/pets2')
def pets2():
	return('''<html><body><p>The second pets photo<br><a href= '/'>click here to go to Home page</a><br><a href= '/pets3'>Next pets galary</a></p>
		<img src= https://hips.hearstapps.com/hmg-prod/images/low-maintenance-pets-hamsters-in-hand-1643914343.jpg?fill=16:9 width= 1000px</img></body></html>''')

@app.route('/pets')
def pets():
	return('''<html><body><p>The first pets photo<br><a href= '/pets2'>Next pets galary</a></p>
		<img src= https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSmdrvCoofM1s2X155newV6ptaTFvvb6wqt3g&s width= 1000px</img></body></html>''')


@app.route('/pets3')
def pets3():
	return('''<html><body><p>The last pets photo<br><a href= '/pets2'>click here to go back to the second picture page</a></p>
		<img src= https://content.skyscnr.com/m/5b44817b2ba6c833/original/GettyImages-478914527.jpg?resize=1800px:1800px&quality=100 width= 1000px</img></body></html>''')





#outer space routes
@app.route('/outer_space')
def outer_space():
	return('''<html><body><p>The first spcae photo<br><a href= '/'>click here to go to Home page</a><br><a href= '/outer_space2'>Next space galary</a><br><a href='/outer_space3'>Space galary number 3</p>
		<img src= https://res.cloudinary.com/momentum-media-group-pty-ltd/image/upload/v1686795211/Space%20Connect/space-exploration-sc_fm1ysf.jpg width= 1000px</img></body></html>''')

@app.route('/outer_space2')
def outer_space2():
		return('''<html><body><p>The second spcae photo<br><a href= '/'>click here to go to Home page</a><br><a href= '/outer_space3'>Next space galary</a></p>
		<img src= https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTJpaWTviBwKxlBCAQujz_Jr3Fb2baDw7eRrg&s width= 1000px</img></body></html>''')

@app.route('/outer_space3')
def outer_space3():
	return('''<html><body><p>The last space photo<br><a href= '/outer_space2'>click here to go to galary 2</a><a href='/outer_space1'>click here to go to galary 1!</p>
		<img src= https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQPevZcapaw0UrpzSfbp6baVvcO2CFtGalb9w&s width= 1000px</img></body></html>''')




if __name__ == '__main__':
	app.run(debug=True)
	

