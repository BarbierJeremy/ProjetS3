#!/usr/bin/python3.5
# -*- coding: Utf-8 -*-

"""
Ce script récupère les seuils pour NS1/NS2 pour chaque conditions/replicats et les écrit dans un fichier output 
"""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i1", "--input_file_1", help = "input file 1")
parser.add_argument("-i2", "--input_file_2", help = "input file 2")
parser.add_argument("-i3", "--input_file_3", help = "input file 3")
parser.add_argument("-i4", "--input_file_4", help = "input file 4")
parser.add_argument("-i5", "--input_file_5", help = "input file 5")
parser.add_argument("-i6", "--input_file_6", help = "input file 6")
parser.add_argument("-i7", "--input_file_7", help = "input file 7")
parser.add_argument("-i8", "--input_file_8", help = "input file 8")
parser.add_argument("-i9", "--input_file_9", help = "input file 9")
parser.add_argument("-i10", "--input_file_10", help = "input file 10")
parser.add_argument("-i11", "--input_file_11", help = "input file 11")
parser.add_argument("-i12", "--input_file_12", help = "input file 12")
parser.add_argument("-o", "--output_file", help = "output file")
args = parser.parse_args()



"""
Récupérer le nombre de reads sur le segment, ainsi que le nombre de reads supportant la jonction NS1/NS2
"""
def Get_N(File, Liste):

	Liste.append(File)
	
	f = open(File)
	
	Fini = False

	while not Fini :
		line = f.readline()
		if line == "" :
			Fini = True 
		else :
			Line = line.split("\t")
			if Line[2] == "region" :
				if Line[0] == "CY010792.1" :
					Liste.append(Line[9].replace("\n", ""))

Liste_N = []

### Appliquer Get_N à chaque conditions. C'est très laid comme fonctionnement, mais peu importe, c'est pas très important comme script.

Get_N(args.inout_file_1, Liste_N)
Get_N(args.inout_file_2, Liste_N)
Get_N(args.inout_file_3, Liste_N)
Get_N(args.inout_file_4, Liste_N)
Get_N(args.inout_file_5, Liste_N)
Get_N(args.inout_file_6, Liste_N)
Get_N(args.inout_file_7, Liste_N)
Get_N(args.inout_file_8, Liste_N)
Get_N(args.inout_file_9, Liste_N)
Get_N(args.inout_file_10, Liste_N)
Get_N(args.inout_file_11, Liste_N)
Get_N(args.inout_file_12, Liste_N)


### Ecrire les résultats dans le fichier output

f = open(args.output_file, "w")
for i in range(0, len(Liste_N), 2) :
	f.write(Liste_N[i] + "\t" + Liste_N[i+1] + "\n")

	
	
	


