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

  # test for invalid language coce
  valid_languages = True
  if form.languages.data is None:
    language_codes = []
  else:
    language_codes = re.findall("[^\s]+", form.languages.data)
  for code in language_codes:
    if code not in enchant.list_languages():
      valid_languages = False

  if form.validate_on_submit() and (valid_languages):
    print "Request Submitted (" + form.letters.data + ", " + form.languages.data + ")"
    
    # get results
    result_dict = unscrambler.unscramble(form.letters.data, language_codes)
    print "Unscrambled Results:", result_dict

    # make human readable and embed in page
    results = ''
    for lang in result_dict.keys():
      freq_dict = {i:[] for i in range(2, len(form.letters.data)+1)}
      for word in result_dict[lang]:
        freq_dict[len(word)].append(word)
      results += "<h3>"+ lang + ":</h3>" + '<br>'.join([', '.join(sorted(freq_dict[i])) for i in range(2, len(form.letters.data)+1)]) 
  else:
    results = "<h3>Unable to Run Query</h3> Check number of letters and language codes"
  
  # write page and pass relevant values
  return render_template('index.html', form=form, results=results, languages=enchant.list_languages())
