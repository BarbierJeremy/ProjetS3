#!/usr/bin/python3.5
# -*- coding: Utf-8 -*-

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input_file", help = "input file", default = "/home/jeremy/Documents/Cours/M2/Projet/COMP/Junction/220-C-virus-R2_GCCAAT_L004-Junction.txt")
parser.add_argument("-t", "--treshold", help = "output file", default = "/home/jeremy/Documents/Cours/M2/Projet/COMP/Seuil/220-C-virus-R2_GCCAAT_L004Aligned.sortedByCoord.out-seuil.txt")
parser.add_argument("-o", "--output_file", help = "output file", default = "Test_1")
args = parser.parse_args()



## On prend 90 % du seuil, parce que sinon on ne retrouve pas NS1/NS2

"""
Fonction pour établir le dictionnaire des seuils, à partir du fichier seuil.txt
Cle = Segment, Valeur = Seuil
"""
def Make_Treshold_Dict(Tresh_File) :
	#Ouvrir le fichier seuil
	f = open(Tresh_File, 'r')
	Dict = {}
	Fini = False
	while not Fini :
		line = f.readline()
		if line == "" :
			Fini = True
		else :
			#Pour chaque ligne, récupérer le segment, et 10% du seuil 
			Line = line.split("\t")
			Tresh = int(Line[1])
			Tresh_10 = (Tresh/100) * 10
			Dict[Line[0]] = Tresh_10
	return Dict



"""
Fonction qui applique les seuils aux comptages de sjcount sur les jonction
Retourne un dictionnaire contenant les jonctions conservées 
"""
def Apply_Treshold(Input_file, Tresh_Dict) :
	# Ouvrir le fichier 
	f = open(Input_file, 'r')
	Fini = False
	Kept = {} 
	while not Fini :
		line = f.readline()
		if line == "" :
			Fini = True
		else :
			# Pour chaque ligne, récupérer le segment, et comparer le comptage associé à la jonction au seuil correspondant au segment. Si supérieur, on conserve la jonction. 
			Line = line.replace("\n", "")
			Line = Line.split("\t")
			Segment = Line[0]
			Count = int(Line[3])
			Segment = Segment.split('_')[0]
			Place = Line[0]
			if Count >= int(Tresh_Dict[Segment]) :
				Kept[Place] = Count 
	return Kept


"""
Ecrire les jonctions conservées dans le fichier output
"""
def Write_Kept(Kept, output) :
	f = open(output, "w")
	for Key in sorted(Kept.keys()) :
		f.write(Key + "\t" + str(Kept[Key]) + "\n")

		



	
Tresh_Dict = Make_Treshold_Dict(args.treshold)

Kept = Apply_Treshold(args.input_file, Tresh_Dict)

Write_Kept(Kept, args.output_file)

## On print les jonctions conservées à l'écran en plus de les écrire dans l'output. 
for Key in sorted(Kept.keys()) :
	print(Key + " kept (" + str(Kept[Key]) + ")")
	

