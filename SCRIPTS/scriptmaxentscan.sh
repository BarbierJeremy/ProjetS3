



genome=$2 # chemin vers genome en fasta 
dossier_sortit= $3 #chemin vers dossier ou les fichier seront creer 
FOLDER=$1 #dossier qui contient les csv auquel on veut ajouter les info maxentscan 
data=$(ls ${FOLDER}/*.csv)



for f in $data
do	
	python fonction-tsvmaxentscan.py $f $2 $3/$(basename $f)"_maxentscan.csv"
done	
echo 



