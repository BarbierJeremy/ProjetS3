#!/bin/bash

# $1 = Dossier resultats 
# $2 = fasta file 
# $3 = gff file 

## Rerend les résultats et les aggrègent 

for file in $(ls $1/Junctions/*virus*.csv)
do 
	base=$(basename $file .csv)
	python3 SCRIPTS/Pipeline_Final/recup_all.py -g $2 -a $3 -csv $file -m $1/MaxEntScan/$base-maxentscan.csv -o $1/Analyse/$base-all.csv
done
