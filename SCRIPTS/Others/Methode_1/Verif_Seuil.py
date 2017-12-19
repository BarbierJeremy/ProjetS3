#!/usr/bin/python3.5
# -*- coding: Utf-8 -*-


import argparse

# 2 input, un pour le gros fichier bam et un pour le subsample à partir duquel on a pu faire les sashimi plot 
parser = argparse.ArgumentParser()
parser.add_argument("-iB", "--input_file_Big", help = "Big file metadata file")
parser.add_argument("-iL", "--input_file_Little", help = "Little file metadata file")
parser.add_argument("-o", "--output", help = "Output file")
args = parser.parse_args()

"""
Fonction récupérant le seuil et le nombre de read sur le segment associé à la condition donnée (C, R, U) et au réplicat
"""
def Get_Little(Little_File, Condition) :

	f = open(Little_File, "r")
	Fini = False
	while not Fini :
		line = f.readline().replace("\n", "")
		if line == "" :
			Fini = True
		else :
			Line = line.split(",")
			if Condition in Line[0] :
				Junction = Line[1]
				Nreads = Line[2]
				
				return Junction, Nreads
				
"""
Fonction mettant au point les seuils à partir des comptages sur les segments des gros fichier bam
"""

def Make_Treshold(Junction_L, Nreads_L, Big_File):

	f = open(Big_File, "r")
	Tresholds = {}
	
	Fini = False
	while not Fini :
		line = f.readline()
		if line == "" :
			Fini = True
		else :
			Line = line.split("\t")
			if Line[0] != '*' : 
				Long_Seg = int(Line[1])
				print(Long_Seg)
				Tresh = int(((int(Line[2])/Long_Seg) * (Junction_L/238)) / (Nreads_L/Long_Seg))
				##Tresh = Tresh * 238 
				Tresholds[Line[0]] = Tresh
			

	return Tresholds
	
			
def Write_Dict(Tresh, out) :
	f = open(out, 'w')

	for segment in sorted(Tresh.keys()) :
		f.write(segment + "\t" + str(Tresh[segment]) + "\n")



Condition =  args.input_file_Big.split('/')[2][:10]
print(Condition)
Junction_L, Nreads_L = Get_Little(args.input_file_Little, Condition)

Junction_L = int(Junction_L)
Nreads_L = int(Nreads_L)

Tresh_Dict = Make_Treshold(Junction_L, Nreads_L, args.input_file_Big)

Write_Dict(Tresh_Dict, args.output)


