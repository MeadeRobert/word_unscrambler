import sys
import enchant
from itertools import permutations

# get valie words from list in desired language
def get_valid_words(words, lang):
  valid_words = []
  dict = enchant.Dict(lang)
  for i in words:
    if dict.check(i):
      valid_words.append(i)
  print "Completed:", lang
  return valid_words


# unscramble words in desired language and return dict of results
def unscramble(letters, languages):
  # generate possible words with more then 2 chars O(n!) :(
  perm = [''.join(p) for p in permutations(letters)]
  words = set(perm)
  # get all permutations of lesser length than number of letters
  for i in range(2, len(letters)):
    words |= set([p[0:i] for p in perm])

  # check against desired languages
  results = {}
  for lang in languages:
    results[lang] = get_valid_words(words, lang)
  
  return results

#print unscramble('dogs', ['en_US'])
