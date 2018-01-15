# Simple example of a web applicaton
# pp05: Now with a form to enter protein name

from flask import Flask, render_template, url_for, redirect
import pandas as pd

# import libraries needed create and process forms
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

# create a flask application object
app = Flask(__name__)
# we need to set a secret key attribute for secure forms
app.config['SECRET_KEY'] = 'change this unsecure key'

# tell code where to find protein information
protein_table_filename = 'protein_table.tsv'

# create a class to define the form
class QueryForm(FlaskForm):
	protein_name = StringField('Enter a valid UniProt protein name:', validators=[Required()])
	submit = SubmitField('Submit')

# define the action for the top level route
@app.route('/', methods=['GET','POST'])
def index():
	# this route has been updated to use a template containing a form
	form = QueryForm()  # create form to pass to template
	protein_name = None
	if form.validate_on_submit():
		protein_name = form.protein_name.data
		print('\n\n\n'+protein_name+'\n\n\n')
		return redirect(url_for('protein', protein_name = protein_name))
	return render_template('index_page.html', form=form, protein_name=protein_name)

# define a route called 'protein' which accepts a protein name parameter
@app.route('/protein/<protein_name>')
def protein(protein_name):

	# load protein data from TSV file into pandas dataframe with protein name as index
	df = pd.read_csv(protein_table_filename,sep='\t',index_col=1)

	try:  # try to extract row for specified protein
		row = df.loc[protein_name]
		# if protein is found, return some information about it
		return render_template('protein_view.html', name=protein_name, fullname=row.Full_name, \
			mass=row.Mass, function=row.GO_molecular_function, image=row.Image_URL)
	except:
		# if protein is not found a key error is thrown and we end up here
		return 'We can\'t find any information about a protein called ' + protein_name + '.'

# start the wb server
if __name__ == '__main__':
	app.run(debug=True)