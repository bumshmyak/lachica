#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re

def getnouncandidates(word, dictwords, candidates):
    if word in dictwords and not(word.endswith('ar') or word.endswith('er') or word.endswith('ir')):
        candidates.append((1, word+"+N"))

    if word.endswith('s') and word[:-1] in dictwords:
        candidates.append((1, word[:-1]+"+N"))

    if word.endswith('es') and word[:-2] in dictwords:
        candidates.append((1, word[:-2]+"+N"))

    if word.endswith('iones'):
        candidates.append((1, word[:-5] + "ión"+"+N"))

def main():
    dictfile = None
    if len(sys.argv) < 2:
        print "usage: "+sys.argv[0]+" words_file"
        exit(1)

    dictfile = open(sys.argv[1])

    dictwords = set([])
    for word in dictfile:
        word = word.strip('\n\r')
        dictwords.add(word)

    for line in sys.stdin:
        line = line.strip('\n\r')
        words = line.split('\t')
        candidates = []
        getnouncandidates(words[0], dictwords, candidates)
        candidates.sort()
        if len(candidates) > 0 and candidates[0][1] not in words[1:]:
            changed = False
            for i in xrange(1, len(words)):
                if words[i].endswith("+N"):
                    changed = True
                    words[i] = candidates[0][1]
                    break

            if not changed:
                words.append(candidates[0][1])
            
        sys.stdout.write(words[0])
        for i in xrange(1, len(words)):
            sys.stdout.write("\t" + words[i])
        sys.stdout.write("\n")

if __name__ == "__main__":
    main()
