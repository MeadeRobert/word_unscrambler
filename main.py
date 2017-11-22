import sys
from itertools import permutations

file = open("corncob_lowercase.txt")
english = set(word.strip() for word in file.readlines())
file.close()

perm = [''.join(p) for p in permutations(sys.argv[1])]
words = set()
for i in range(0, len(sys.argv[1])):
  words |= set([p[0:i] for p in perm])
#print words
#print "last" in english
#print english
print english & words
