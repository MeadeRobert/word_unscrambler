from flask import render_template, flash, redirect
from app import app
from .forms import LetterForm
from . import unscrambler
import enchant
import re

@app.route('/', methods=['GET', 'POST'])
def index():
  form = LetterForm()
  results = ''
  # unscramble
  if form.validate_on_submit():
    print "submitted"
    print form.letters.data
    print form.languages.data
    
    # get results
    result_dict = unscrambler.unscramble(form.letters.data, re.findall("[^\s]+", form.languages.data))
    print result_dict

    # make human readable and embed in page
    results = ''
    for lang in result_dict.keys():
      freq_dict = {i:[] for i in range(2, len(form.letters.data)+1)}
      for word in result_dict[lang]:
        freq_dict[len(word)].append(word)
      results += "<h3>"+ lang + ":</h3>" + '<br>'.join([', '.join(sorted(freq_dict[i])) for i in range(2, len(form.letters.data)+1)]) 
  
  # write page and pass relevant values
  return render_template('index.html', form=form, results=results, languages=enchant.list_languages())
