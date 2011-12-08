#!/bin/bash

if [ $# -lt 1 ]
then
    echo "usage: "$0" [verbs | nouns | adjectives]"
    exit 1
fi

cut -f 1 ../data/spanish.txt.learn.$1 | ./gen$1.py ../data/spanish.dict > ../data/spanish.txt.result.$1
./evaluate.py ../data/spanish.txt.learn.$1 ../data/spanish.txt.result.$1

# best result on 09.11
# verbs
#{"_expected": {"recall": 0.9395885611338255, "precision": 0.9420218646357942, "f1": 0.9408036395075975}}

