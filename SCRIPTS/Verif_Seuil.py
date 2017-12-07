#!/usr/bin/python3.5
# -*- coding: Utf-8 -*-


import argparse

# 2 input, un pour le gros fichier bam et un pour le subsample à partir duquel on a pu faire les sashimi plot 
parser = argparse.ArgumentParser()
parser.add_argument("-iB", "--input_file_Big", help = "input file")
parser.add_argument("-iL", "--input_file_Little", help = "output file")
args = parser.parse_args()

"""
Fonction récupérant le seuil et le nombre de read sur le segment associé à la condition donnée (C, R, U) et au réplicat
"""
def Get_Little(Little_File, Condition) :

	f = open(Little_File, "r")
	Fini = False
	while not Fini :
		line = f.readline()
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
	Segment = []
	Treshold = []
	
	Fini = False
	while not Fini :
		line = f.readline()
		if line == "" :
			Fini = True
		else :
			Line = line.split("\t")
			Segment.append(Line[0])
			Tresh = int((int(Line[2]) * Junction_L) / Nreads_L)
			Treshold.append(Tresh)
			print(Line[0] + " : " + str(Tresh))
			




Condition =  args.input_file_Big[:14]

Junction_L, Nreads_L = Get_Little(args.input_file_Little, Condition)

Junction_L = int(Junction_L)
Nreads_L = int(Nreads_L)
Make_Treshold(Junction_L, Nreads_L, args.input_file_Big)


