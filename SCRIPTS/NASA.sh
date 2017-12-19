#!/bin/bash

set -e

# $1 = dossier .bam
# $2 = dossier où travailler/placer les fichiers
# $3 = fasta contenant le génome
# $4 = dossier sjcount
# $5 = gff associé au génome
# $6 = seuil

if [ -n "$6" ]
then
	arg=$6
else
	echo "Using default treshold (0.05)"
	arg="0.05"
fi


mkdir -p $2
mkdir -p $2/Logs/
mkdir -p $2/Sjcount/
mkdir -p $2/Sjcount/Junction/
mkdir -p $2/Sjcount/Count/


# Count with sjcount

echo "Running Sjcount ..."

./SCRIPTS/Pipeline_Final/script_sjcount.sh $1 $2 $4 &> $2/Logs/Sjcount.log

echo "Sjcount : Success !"

### Get Junction from sjcount counts

echo "Searching for junctions ..."

mkdir -p $2/Junctions/

./SCRIPTS/Pipeline_Final/Sjcount_Tresholding.sh $2/Sjcount $2 $arg

echo "Junction search : Success !"

### Run maxentscan on these Junction

echo "Running MaxEntScan ..."

mkdir -p $2/MaxEntScan/

./SCRIPTS/Pipeline_Final/scriptmaxentscan.sh $2/Junctions $3 $2/MaxEntScan/ SCRIPTS/Pipeline_Final/maxentpy/

echo "MaxEntScan : Success !"
### Recapitulate results in a tab

echo "Making recap table ..."

mkdir -p $2/Analyse/

./SCRIPTS/Pipeline_Final/recup_all.sh $2 $3 $5 

echo "Recap : Success ! "

echo "All done" 




