import sys
import enchant
from itertools import permutations

# generate possible words with more then 2 chars O(n!) :(
perm = [''.join(p) for p in permutations(sys.argv[1])]
words = set(perm)
# get all permutations of lesser length than number of letters
for i in range(2, len(sys.argv[1])):
  words |= set([p[0:i] for p in perm])


# reference against selected dictionaries to find words
########################################################

# define common dictionary structure and function for verifying words
results = {}
def valid_words(words, lang):
  valid_words = []
  dict = enchant.Dict(lang)
  for i in words:
    if dict.check(i):
      valid_words.append(i)
  print "Completed:", lang
  results[lang] = valid_words
  #print valid_words

# run a thread to check against each language
for lang in enchant.list_languages():
  valid_words(words, lang)
  '''
  try:
    print "Trying to start thread for", lang
    thread.start_new_thread(valid_words, (words, lang))
  except:
    print "Error: unable to start thread for", lang
  '''

# wait for threads
'''
while len(results.keys()) < len(enchant.list_languages()):
  print "Completed Languages:",set(results.keys()) & set(enchant.list_languages())
  time.sleep(.25)  
'''

#print results
for i in results.keys():
  print i+":",', '.join(results[i])


