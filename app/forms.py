from flask_wtf import Form
from wtforms import StringField, BooleanField, validators
from wtforms.validators import DataRequired

class LetterForm(Form):
  letters = StringField('letters', [validators.Length(min=2, max=9)])
  languages = StringField('languages', validators=[DataRequired()])
