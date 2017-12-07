#!/bin/bash

#Boucle pour appliquer les seuils à chaque condition/replicat
for file in $(ls ../RESULTS/Intersect/*IdxStats*.txt)
do	
	python3 Seuil.py $file
done
