#!/bin/bash

DATAFILE=../data/spanish.txt.learn
echo "total verbs:" `grep +V ../data/spanish.txt.learn | wc -l`

suffixes=('amos' 'emos' 'an' 'en' 'aba' 'abas' 'ara' 'aras' \
          'iera' 'iese' 'ieras' 'ieses' 'abais' 'aban' 'aste' 'iste'\
          'asteis' 'imos' 'aron' 'ieron' 'ar' 'er' 'ir' 'ando' 'iendo' 'ado' 'ido')

totalverbsfound=0
for suffix in ${suffixes[@]}
do
   maybeverbs=`grep "${suffix}\s" ${DATAFILE} | wc -l`
   realverbs=`grep "${suffix}\s" ${DATAFILE} | grep +V | wc -l`
   echo $suffix ":" $realverbs "of" $maybeverbs
   let totalverbsfound=totalverbsfound+maybeverbs
done

echo "total verbs found" $totalverbsfound 


