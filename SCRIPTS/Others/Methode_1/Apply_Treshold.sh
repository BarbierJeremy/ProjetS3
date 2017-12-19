#!/bin/bash

mkdir -p Tresh_Filter_True

for file_1 in $(ls Junction)
do
	base_1=$(basename $file_1 -Junction.txt)
	for file_2 in $(ls Seuil_Verified/)
	do
		base_2=$(basename $file_2 -Tresholds.txt)
		if [ "$base_1" == "$base_2" ]
		then
			./../SCRIPTS/Filter_Seuil.py -i Junction/$file_1 -t Seuil_Verified/$file_2 -o Tresh_Filter_True/$base_1-Filtered_Treshold.txt
		fi
	done
done



