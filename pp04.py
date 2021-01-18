# Simple example of a web application
# pp04: Same functionality as pp03 but now using a template

from flask import Flask, render_template
import pandas as pd

# create a flask application object
app = Flask(__name__)

# tell code where to find protein information
protein_table_filename = 'protein_table.tsv'

# define the action for the top level route
@app.route('/')
def index():
	return 'Welcome to the QMUL protein portal!'

# define a route called 'protein' which accepts a protein name parameter
@app.route('/protein/<protein_name>')
def protein(protein_name):

	# load protein data from TSV file into pandas dataframe with protein name as index
	df = pd.read_csv(protein_table_filename,sep='\t',index_col=1)

	protein_name = protein_name.upper()  # ensure name is in capital letters

	try:  # try to extract row for specified protein
		row = df.loc[protein_name]
		# if protein is found, return some information about it
		return render_template('protein_view.html', name=protein_name, fullname=row.Full_name, \
			mass=row.Mass, function=row.GO_molecular_function, image=row.Image_URL)
	except:
		# if protein is not found a key error is thrown and we end up here
		return "We can't find any information about a protein called %s." % protein_name

# start the web server
if __name__ == '__main__':
	app.run(debug=True)