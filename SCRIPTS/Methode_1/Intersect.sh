#!/bin/bash
## Execute samtools idxstats sur chaque bam, pour avoir le nombre de reads par segments. 

for file in $(ls /data/fluhit/bam/*virus*.bam)
do 
	base=$(basename $file .bam)
	samtools idxstats $file > RESULTS/Intersect/$base-IdxStats.txt
done

