import sys
import enchant
from itertools import permutations

'''
file = open("corncob_lowercase.txt")
english = set(word.strip() for word in file.readlines())
file.close()
'''

perm = [''.join(p) for p in permutations(sys.argv[1])]
words = set()
for i in range(2, len(sys.argv[1])):
  words |= set([p[0:i] for p in perm])
#print words
#print "last" in english
#print english
d = enchant.Dict("en_US")
english_words = set()
for i in words:
  if d.check(i):
    english_words.add(i)
print english_words
#print '\n'.join(english & words)
