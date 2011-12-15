#!/bin/bash

../try/common_prefix.py < ../data/learn.1.txt > ../data/dict.txt
../try/best_suffix.py ../data/dict.txt < ../data/learn.2.txt > ../data/check1.txt
cat ../data/check1.txt | ./genverbs.py ../data/spanish.dict | ./gennouns.py ../data/spanish.dict > ../data/check2.txt
./evaluate.py ../data/learn.2.txt ../data/check2.txt
