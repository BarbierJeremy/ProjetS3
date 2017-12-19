#!/bin/bash
## Rerend les résultats et les aggrègent 

mkdir -p ./Analyse/

for file in $(ls ./*virus*.csv)
do 
	base=$(basename $file .csv)
	python3 recup_all.py -g wsn_genome.fasta -a ../pipeline/wsn_genome.gff3 -csv $file -m ../pipeline/COMP/result_maxentscan/$base.csv_maxentscan.csv -o ./Analyse/$base.all.csv
done
