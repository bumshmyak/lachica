#!/usr/bin/python

from utility import *

def articles(line):
    columns = line.split('\t')

    wordform = columns[0]
    lemmas = columns[1:]

    return wordform, set(lemmas)

def matched_articles(pair_of_articles):
    left_article, right_article = pair_of_articles

    if left_article[0] != right_article[0]:
        raise RuntimeError, 'Wordforms are unmatched in canonical and user datasets'
    
    return left_article[0], left_article[1], right_article[0], right_article[1]

def evaluate(canonical_iterable, user_iterable):
    iterable = itertools.izip(canonical_iterable, user_iterable)
    result = []

    for item in read(matched_articles, iterable):
        wordform, canonical_lemmas, wordform, user_lemmas = item

        if len(user_lemmas) == 0:
            precision = 0.0
        else:
            precision = float(len(canonical_lemmas & user_lemmas)) / float(len(user_lemmas))

        if len(canonical_lemmas) == 0:
            recall = 0.0
        else:
            recall = float(len(canonical_lemmas & user_lemmas)) / float(len(canonical_lemmas))

        result.append({ 'precision' : precision, 'recall' : recall })

    EP = mean(select('precision', result))
    ER = mean(select('recall', result))
    EF = 2.0 * EP * ER / (EP + ER)

    result = { '_expected' : {
        'precision' : EP,
        'recall' : ER,
        'f1' : EF
    }}

    return result

def main():
    if len(sys.argv) < 3:
        print >>sys.stderr, 'Usage: {0} <canonical> <user>'.format(sys.argv[0])
        sys.exit(1)

    try:
        canonical = read(articles, from_file(sys.argv[1], encoding = 'latin1'))
        user = read(articles, from_file(sys.argv[2], encoding = 'latin1'))

        print json.dumps(evaluate(canonical, user))
    except Exception as e:
        print json.dumps({ '_error' : str(e) })

if __name__ == '__main__':
    main()

