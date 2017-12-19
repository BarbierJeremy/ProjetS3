#!/bin/bash

for file in $(ls /data/fluhit/bam/*virus*.bam)
do
	base=$(basename $file .sortedByCoord.out.bam)
	samtools view -s 0.01 -b $file > $base-Subsample_1PerCent.bam 
done

