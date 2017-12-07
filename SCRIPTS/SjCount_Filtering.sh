#!/usr/bin/bash

#Script servant à tester le filtering. Il filtre selon un seuil, indiqué en argument du script python (ici, 10, valeur arbitraire). 

mkdir -p resultats/Sjcount_Filtered_10

for file in $(ls /data/home/gsiekaniec/projetS3/resultats/*Count*)
do
	#Récupérer le basename (pour virer le Aligned, Sorted, .bam etc, faire des noms moins long)
	base=$(basename $file -Count.txt)
	
	# Commande script Filtering
	./Parse_And_Filter_Sjcount.py -ssj resultats/$base-Junction.txt -ssc resultats/$base-Count.txt -t 10 -o resultats/Sjcount_Filtered_10/$base-Filtered_10.tsv
	
done
