#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re

infsuffixes = ['ar', 'er', 'ir']
suffixes = ['o', 'e', 'a', 'as', 'es', 'amos', 'emos',
            'ímos', 'áis', 'éis', 'ís', 'an', 'en',
            'aba', 'ía', 'ara', 'ase', 'iera', 'iese',
            'abas', 'ías', 'aras', 'ases', 'ieras', 'ieses',
            'ábamos', 'íamos', 'áramos', 'ásemos', 'iéramos',
            'iésemos', 'abais', 'arais', 'aseis', 'ierais',
            'ieseis', 'aban', 'ían', 'aran', 'asen', 'iesen',
            'iésen', 'é', 'í', 'aste', 'iste', 'ó', 'ió', 'imos',
            'asteis', 'isteis', 'aron', 'ieron', 'ás', 'are', 'iere',
            'ares', 'ieres', 'ieres', 'á', 'áremos', 'ieremos', 'areis',
            'iereis', 'án', 'aren', 'ieren', 'íais', 'ían', 'ad', 'ed',
            'ar', 'er', 'ir', 'ando', 'iendo', 'ido', 'ada',
            'adas', 'ado', 'ados', 'aremos', 'ará', 'arán', 'arás',
            'aré', 'aréis', 'aría', 'aríais', 'aríamos', 'arían',
            'arías']

def main():
    dictfile = None
    if len(sys.argv) < 2:
        print "usage: "+sys.argv[0]+" dict_file"
        exit(1)

    dictfile = open(sys.argv[1])

    dictwords = set([])
    for word in dictfile:
        word = word.strip('\n')
        dictwords.add(word)

    for line in sys.stdin:
        line = line.strip('\n\r')
        candidates = []
        for suff in suffixes:
            splitted = re.split(suff+'$', line);
            if len(splitted) == 2:
                for infsuff in infsuffixes:
                    candidate = splitted[0] + infsuff
                    rank = -len(infsuff)
                    if candidate in dictwords:
                        rank = -10
                    candidates.append((rank, candidate))
        candidates.sort()
        print line + "\t",
        if len(candidates) == 0:
            print "###"
        else:
            print candidates[0][1]+"+V"

if __name__ == "__main__":
    main()
