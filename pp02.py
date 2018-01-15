# Simple example of a web applicaton
# pp02: Now with basic protein route

from flask import Flask

# create a flask application object
app = Flask(__name__)

# define the action for the top level route
@app.route('/')
def index():
	return 'Welcome to the QMUL protein portal!'

# define a routed called 'protein' which accepts a protein name parameter
@app.route('/protein/<protein_id>')
def protein(protein_id):
	protein_id = protein_id.upper()  # ensure name is in capital letters
	return 'We don\'t have any information about a protein called %s.' % protein_id

# start the wb server
if __name__ == '__main__':
	app.run(debug=True)
