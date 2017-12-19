#!/usr/bin/python3.5
# -*- coding: Utf-8 -*-


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-iJ", "--input_Junction", help="Junction file from sjcount", default = "/home/jeremy/Documents/Cours/M2/Projet/pipeline/COMP/Junction/C-virus-R2-Junction.txt")
parser.add_argument("-iC", "--input_Count", help = "Count file from sjcount", default = "/home/jeremy/Documents/Cours/M2/Projet/pipeline/COMP/Counts/C-virus-R2-Count.txt")
parser.add_argument("-T", "--Treshold", help = "Treshold for junction percentage", default = 0.05)
parser.add_argument("-o", "--output_file", help = "output file", default = "Test_1")
args = parser.parse_args()


def Get_Junction(Junction_File, Dict_Counts, output, Treshold) :

	f = open(Junction_File, 'r')
	g = open(output, 'w')
	g.write("Segment\tJunction_First_Position\tJunction_Second_Position\tStrand\tSupport_Junction\tSupport_No_Junction\tPercentage_spliced\tPercentage_No_spliced\n")
	Fini = False

	Dict_Junction = {}
	while not Fini :
		line = f.readline().replace("\n", "")
		if line == "" :
			Fini = True
		else :
			Line = line.split("\t")
			Name = Line[0].split('_')
			Count = int(Line[3])

			Segment = Name[0]
			First_Pos = Name[1]
			Sec_Pos = Name[2]
			Strand = Name[3]

			String = Segment + '_' + First_Pos + '_' + Strand
			Perc_J = (Count/(Dict_Counts[String] + Count))
			Perc_C = 1 - Perc_J
			
			
			if Perc_J > float(Treshold) :
				To_Write = Segment + "\t" + First_Pos + "\t" + Sec_Pos + "\t" + Strand + "\t" + str(Count) + "\t" + str(Dict_Counts[String]) + "\t" + str(round(Perc_J, 2)) + "\t" + str(round(Perc_C, 2)) + "\n"
				g.write(To_Write)
			

def Get_Counts(Count_File) :

	f = open(Count_File, 'r')
	Fini = False

	Dict_Counts = {}
	while not Fini :
		line = f.readline().replace("\n", "")
		if line == "" :
			Fini = True
		else :
			Line = line.split("\t")
			Dict_Counts[Line[0]] = int(Line[3])
	return Dict_Counts

			

Dict_Counts = Get_Counts(args.input_Count)

Get_Junction(args.input_Junction, Dict_Counts, args.output_file, args.Treshold)


