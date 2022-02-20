from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    character_name = StringField('Name of your favorite character', validators=[DataRequired()])
    submit = SubmitField('Search')
