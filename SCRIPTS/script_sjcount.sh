#!/usr/bin/bash

for file in $(ls /data/fluhit/bam/*.bam)
do
	#Récupérer le basename (pour virer le Aligned, Sorted, .bam etc, faire des noms moins long)
	base=$(basename $file Aligned.sortedByCoord.out.bam)
        
	#Commande sjcount (A VERIFIER AVANT DE LANCER, NOTAMMENT POUR LE FICHIER OUTPUT !!) 
	./sjcount/sjcount -bam $file -ssj resultats/$base-Junction.txt -ssc resultats/$base-Count.txt

done




