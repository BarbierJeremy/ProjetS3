#!/bin/bash

#Boucle pour exécuter sjcount sur chaque fichier bam 
for file in $(ls /data/fluhit/bam/*.bam)
do	
	#Commande sjcount (A VERIFIER AVANT DE LANCER, NOTAMMENT POUR LE FICHIER OUTPUT !!) 
	./sjcount/sjcount -bam $file -ssj resultats/$file-Junction.txt -ssc resultats/$file-Count.txt
done




