#!/usr/bin/env python

import sys
import re

"""
Assume that all word inflection is don via suffix chande. i.e. there is significant inmutable word part
thats length is greate then suffix length. Let's find this immutable prefix part for each pair
(form, lemma) from dictionary. And say that there is a relation between suffixes of form and lemma.

Split learn file, make correspondance between suffixes of forms and suffiexes of lemmas + theis POS tags
Correspondance is stored in 2D dict:
  1st key - form-suffix,
  2nd key - lemma-suffix+POS.
  Value - occurences number of this suffix pairs.
"""

extra_length = 10
suffix_replacement = {}

for row in sys.stdin:
  words = row.strip("\n\r").split("\t")
  form = words[0]
  for variant in words[1:]:
    lemma,pos = variant.split('+')
  
    index = 0
    while index < min(len(lemma), len(form)) and lemma[index] == form[index]:
      index += 1

    # Let's consider not only the least length suffix pair but some others
    for id in xrange(max(index - extra_length, 0), index):
      subkey = "%s+%s"%(lemma[id:],pos)
      suffix_replacement.setdefault(form[id:], dict()).setdefault(subkey, 0)
      suffix_replacement[form[id:]][subkey] += 1
#    print "%s\t%s\t%s\t%s"%(form[0:index], form, lemma, pos)

# Serialize correspondance 2d-dict
for sfx in suffix_replacement.keys():
  print "%s\t%s"%(sfx,"\t".join(["%s:%d"%(k, suffix_replacement[sfx][k]) for k in suffix_replacement[sfx].keys()]))
