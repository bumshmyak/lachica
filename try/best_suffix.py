#!/usr/bin/env python

import sys
import re
import operator

"""
Load suffix correspondance 2D-dict

for each word from testing set find the form-suffix, matching any form-suffix from 2D-dict for wich
the probability of being transformed to some lemma is maximal.

"""

source = None
if len(sys.argv) < 2:
  exit(1)
else:
  source = open(sys.argv[1])

suffix_replacement = {}

for row in source:
  words = row.strip("\n\r").split("\t")
  suffix = words[0]
  for variant in words[1:]:
    replacement,num = variant.split(':')
  
    suffix_replacement.setdefault(suffix, {})[replacement] = int(num)

# cals score for lemma-suffixes variants
# now ratio of max item is used,
# maybe we should use IGain or something else
def score_variants(variants):
  if len(variants) == 0:
    return 0
  sum_weight = sum(variants.values())
  return max(variants.values()) / sum_weight

for row in sys.stdin:
  words = row.strip("\n\r").split("\t")
  form = words[0]

  best_id = len(form)
  best_score = 0
  for id in xrange(len(form)):
    variants = suffix_replacement.get(form[id:], {})
    if score_variants(variants) > best_score:
      best_score = score_variants(variants)
      best_id = id

  # max_arg of choosen variants list. i.e. variant with maximal weights from best suffix probe.
  best_variant = max(suffix_replacement.get(form[best_id:],{'+N':1}).iteritems(), key=operator.itemgetter(1))[0]

  # pront best variant, maybe we need an algorith for finding few best variants.
  print "%s\t%s%s"%(form, form[:best_id], best_variant)
  

