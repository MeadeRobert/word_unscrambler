from flask import render_template, flash, redirect
from app import app
from .forms import LetterForm
from . import unscrambler
import re

@app.route('/', methods=['GET', 'POST'])
def index():
  form = LetterForm()
  results = ''
  if form.validate_on_submit():
    print "submitted"
    print form.letters.data
    print form.languages.data
    result_dict = unscrambler.unscramble(form.letters.data, re.findall("[^\s]+", form.languages.data))
    print result_dict
    results = ''
    for i in result_dict.keys():
      results += i + ": " + ', '.join(result_dict[i]) + '<br>'
  return render_template('index.html', form=form, results=results)
