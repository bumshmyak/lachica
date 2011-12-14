#!/usr/bin/env python

import sys
import re
import operator
import math

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
 
    #if int(num) > 1:
    suffix_replacement.setdefault(suffix, {})[replacement] = int(num)

def combine_variants(sfx_dict):
  result={}
  for key in sfx_dict.keys():
    variants = sfx_dict[key]
    weight_by_sfx = {}
    for k in variants.keys():
      sfx, pos = k.split("+")
      weight_by_sfx.setdefault(sfx, {}).setdefault(pos,0)
      weight_by_sfx[sfx][pos] += variants[k]
    
    new_variants={}
    for k in weight_by_sfx.keys():
      v = weight_by_sfx[k]
      new_variants["%s+%s"%(k,"+".join(v.keys()))] = sum(v.values())
    result[key] = new_variants
  return result

def unglue_variants(str):
  parts = str.split('+')
  variants = []
  for pos in parts[1:]:
    variants.append("%s+%s"%(parts[0],pos))
  return variants

# cals score for lemma-suffixes variants
# now ratio of max item is used,
# maybe we should use IGain or something else
def score_variants(variants):
  if len(variants) == 0:
    return 0
  sum_weight = sum(variants.values())
  max_weight = max(variants.values())
  return float(max_weight) / sum_weight

def score_first_threshold(variants):
  if len(variants) == 0:
    return 0
  elif len(variants) == 1:
    return 1.0
  sum_weight = sum(variants.values())
  sorted_pairl_list = sorted(suffix_replacement.get(form[best_id:],{'+N':1}).iteritems(), key=operator.itemgetter(1))
  max_val = sorted_pairl_list[0][1]
  threshold = len(sorted_pairl_list) <= 1 and sorted_pairl_list[0][1] or (sorted_pairl_list[0][1] - sorted_pairl_list[1][1])
  return float(threshold)/max_val 

#suffix_replacement = combine_variants(suffix_replacement)

for row in sys.stdin:
  words = row.strip("\n\r").split("\t")
  form = words[0]

  best_id = len(form)
  best_score = 0
  for id in xrange(len(form)):
    variants = suffix_replacement.get(form[id:], {})
    score = score_first_threshold(variants)
    if score > best_score:
      best_score = score
      best_id = id

  # max_arg of choosen variants list. i.e. variant with maximal weights from best suffix probe.
  best_variant = max(suffix_replacement.get(form[best_id:],{'+N':1}).iteritems(), key=operator.itemgetter(1))[0]

  # pront best variant, maybe we need an algorith for finding few best variants.

  print "%s\t%s"%(form, "\t".join("%s%s"%(form[:best_id],variant) for variant in unglue_variants(best_variant)))
  

