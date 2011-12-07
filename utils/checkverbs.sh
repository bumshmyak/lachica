#!/bin/bash
cut -f 1 ../data/spanish.txt.learn.verbs | ./genverbs.py ../data/spanish.dict > ../data/spanish.txt.result.verbs
./evaluate.py ../data/spanish.txt.learn.verbs ../data/spanish.txt.result.verbs

# best result on 07.11
#{"_expected": {"recall": 0.8847163973069878, "precision": 0.8870444136381982, "f1": 0.8858788760166966}}
