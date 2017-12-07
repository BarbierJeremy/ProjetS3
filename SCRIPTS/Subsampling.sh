#!/usr/bin/bash

#Exécution de samtools view pour ne récupérer qu'une partie des fichiers bam (1%, au hasard), afin de pourvoir utiliser igv de manière correcte (question de complexité mémoire). 

for file in $(ls /data/fluhit/bam/*virus*.bam)
do
	base=$(basename $file .sortedByCoord.out.bam)
	samtools view -s 0.01 -b $file > $base-Subsample_1PerCent.bam 
done

