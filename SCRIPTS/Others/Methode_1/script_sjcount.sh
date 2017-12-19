#!/bin/bash

# $1 : dossier avec les bam 
# $2 : dossier resultats
# $3 : dossier sjcount

for file in $(ls $1/*.bam)
do
	#Récupérer le basename (pour virer le Aligned, Sorted, .bam etc, faire des noms moins long)
	base=$(basename $file .bam)
        
	#Commande sjcount (A VERIFIER AVANT DE LANCER, NOTAMMENT POUR LE FICHIER OUTPUT !!) 
	./$3/sjcount -bam $file -ssj $2/Sjcount/Junction/$base-Junction.txt -ssc $2/Sjcount/Count/$base-Count.txt

done




