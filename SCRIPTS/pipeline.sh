#!/usr/bin/env bash

set -e 


folder_bam=$1
folder_out=$2
seuil=$3 
list_bam=$(ls ${FOLDER}/*.bam)



for file in list_bam
do	
	#Récupérer le basename (pour virer le Aligned, Sorted, .bam etc, faire des noms moins long)
	nom=$(basename $file)
        
	#Commande sjcount (A VERIFIER AVANT DE LANCER, NOTAMMENT POUR LE FICHIER OUTPUT !!) 
	./sjcount/sjcount -bam $file -ssj $folder_out/$nom-Junction.txt -ssc $folder_out/$nom-Count.txt

done 


