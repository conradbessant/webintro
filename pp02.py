# Simple example of a web application
# pp02: Now with basic protein route

from flask import Flask

# create a flask application object
app = Flask(__name__)

# define the action for the top level route
@app.route('/')
def index():
	return 'Welcome to the QMUL protein portal!'

# define a routed called 'protein' that accepts a protein name parameter
@app.route('/protein/<protein_name>')
def protein(protein_name):
	protein_name = protein_name.upper()  # ensure name is in capital letters
	return "We don't have any information about a protein called %s." % protein_name

# start the web server
if __name__ == '__main__':
	app.run(debug=True)
