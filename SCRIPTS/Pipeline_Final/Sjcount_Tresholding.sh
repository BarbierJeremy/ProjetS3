#!/bin/bash


# $1 = Dossier resultat sjcount
# $2 = Dossier resultat 
# $3 = seuil

for file in $(ls $1/Junction/*Junction*)
do
	base=$(basename $file -Junction.txt)
	./SCRIPTS/Pipeline_Final/Get_Junction.py -iJ $1/Junction/$base-Junction.txt -iC $1/Count/$base-Count.txt -T $3 -o $2/Junctions/$base-Filtered_On_Sjcount.csv
done


