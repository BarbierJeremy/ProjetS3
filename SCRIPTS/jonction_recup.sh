#!/bin/bash
## Execute samtools idxstats sur chaque bam, pour avoir le nombre de reads par segments. 
'''Ce script récupère la séquence des jonctions présente dans les fichiers csv contenant les résultats de sjcount'''


mkdir -p ../Splicing_analysis

for file in $(ls ../COMP/Tresh_From_Sjcount/*virus*.csv)
do 
	base=$(basename $file .csv)
	python3 junction_recup.py -g ./wsn_genome.fasta -csv $file -o ../Analyse/$base.txt
done
