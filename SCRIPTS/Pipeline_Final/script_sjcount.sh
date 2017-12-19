#!/bin/bash

# $1 : dossier avec les bam 
# $2 : dossier resultats
# $3 : dossier sjcount

for file in $(ls $1/*.bam)
do

	base=$(basename $file .bam)
        
	./$3/sjcount -bam $file -ssj $2/Sjcount/Junction/$base-Junction.txt -ssc $2/Sjcount/Count/$base-Count.txt

done

