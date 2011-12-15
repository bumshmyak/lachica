#!/bin/bash

../try/common_prefix.py < ../data/spanish.txt.learn > ../data/dict.txt
../try/best_suffix.py ../data/dict.txt < ../data/spanish.txt.test.clean > ../data/result1.txt
cat ../data/result1.txt | ./genverbs.py ../data/spanish.dict | ./gennouns.py ../data/spanish.dict > ../data/result2.txt
iconv -f utf-8 -t ISO-8859-1 ../data/result2.txt > ../data/submit_me.txt