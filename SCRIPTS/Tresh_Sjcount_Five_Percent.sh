#!/bin/bash

mkdir -p Tresh_From_Sjcount

for file in $(ls Junction/)
do
	base=$(basename $file -Junction.txt)
	./../SCRIPTS/Get_Junction.py -iJ Junction/$base-Junction.txt -iC Counts/$base-Count.txt -T 0.05 -o Tresh_From_Sjcount/$base-Five_Percent_Treshold.csv
done

