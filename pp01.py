# Simple example of a web application
# pp01: Hello world

from flask import Flask

# create a flask application object
app = Flask(__name__)

# define the action for the top level route
@app.route('/')
def index():
	return 'Welcome to the QMUL protein portal!'

# start the web server
if __name__ == '__main__':
	app.run(debug=True)
