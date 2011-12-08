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
            'arías', 'id', 'idos', 'ídos', 'ído', 'ídas', 'ída',
            'erais', 'ereis', 'eron', 'eseis', 'ida', 'idas']

def inflate(stem, suff, infsuff):
    if (stem.endswith('qu')):
        stem = stem[:-2] + 'c'
        return stem + infsuff

    if (stem.endswith('gu')):
        stem = stem[:-2] + 'g'
        return stem + infsuff

    if (stem.endswith('ic') and (suff.startswith('e') or suff.startswith('é'))):
        stem = stem[:-1] + 'z'
        return stem + infsuff

    if (stem.endswith('zc') and (suff.startswith('a') or suff.startswith('o'))):
        stem = stem[:-2] + 'c'
        return stem + infsuff

    if (stem.endswith('duj')):
        stem = stem[:-1] + 'c'
        return stem + infsuff

    if (infsuff != 'ar' and stem.endswith(infsuff)):
       return stem

    if stem.endswith(infsuff[0]):
        return stem + 'r'

    return stem + infsuff

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

    for line in sys.stdin:
        line = line.strip('\n\r')
        candidates = []
        for suff in suffixes:
            if line != suff and line.endswith(suff):
                stem = line[:-len(suff)]
                for infsuff in infsuffixes:
                    candidate = inflate(stem, suff, infsuff)
                    rank = len(stem)
                    if candidate in dictwords:
                        rank -= 10
                    candidates.append((rank, candidate))
        candidates.sort()
        print line + "\t",
        if len(candidates) == 0:
            print "###"
        else:
            print candidates[0][1]+"+V"

if __name__ == "__main__":
    main()
