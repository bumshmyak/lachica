#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re

suffixes = []

def main():
    dictfile = None
    if len(sys.argv) < 2:
        print "usage: "+sys.argv[0]+" dict_file"
        exit(1)

    dictfile = open(sys.argv[1])

    dictwords = set([])
    for word in dictfile:
        word = word.strip('\n\r')
        dictwords.add(word)

    for word in sys.stdin:
        word = word.strip('\n\r')
        candidates = []
        candidates.append((-1, word))

        if word in dictwords:
            candidates.append((-10, word))

        if word.endswith('s') and word[:-1] in dictwords:
            candidates.append((-10, word[:-1]))

        if word.endswith('es') and word[:-2] in dictwords:
            candidates.append((-10, word[:-2]))

        if word.endswith('s'):
            candidates.append((-2, word[:-1]))

        if word.endswith('es'):
            candidates.append((-2, word[:-2]))

        if word.endswith('iones'):
            candidates.append((-3, word[:-5] + "ión"))
        
        candidates.sort()
        print word + "\t",
        if len(candidates) == 0:
            print "###"
        else:
            print candidates[0][1]+"+N"

if __name__ == "__main__":
    main()
