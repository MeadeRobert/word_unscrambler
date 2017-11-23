from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LetterForm(Form):
  letters = StringField('letters', validators=[DataRequired()])
  languages = StringField('languages', validators=[DataRequired()])
