

# $1 : dossier qui contient les csv auquel on veut ajouter les info maxentscan
# $2 : chemin vers genome en fasta 
# $3 : chemin vers dossier ou les fichier seront creer 
# $4 : chemin vers maxentscan

data=$(ls $1/*.csv)

for f in $data
do	
	python SCRIPTS/Pipeline_Final/fonction-tsvmaxentscan.py $f $2 $3/$(basename $f .csv)"-maxentscan.csv" $4
done




