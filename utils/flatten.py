#!/usr/bin/python

import sys
import os

def flatten(iterable):
    for line in iterable:
        columns = line.split()
        wordform, lemmas = columns[0], columns[1:]

        for lemma_with_tag in lemmas:
            lemma, tag = lemma_with_tag.split('+')
            yield wordform, lemma, tag

if __name__ == '__main__':
    for item in flatten(sys.stdin):
        print '\t'.join(str(x) for x in item)
