#!/usr/bin/python3
# -*- coding: Utf-8 -*-

## For now, only keep + strand 

def Analyze_Count(Count) :

	#Open file 
	f = open(Count, "r")
	
	Fini = False

	#Dictionary to get Positions
	Positions = {}

	# Loop to iterate on each line
	
	while not Fini :
		line = f.readline()
		if line == "" :
			Fini = True
		else :
			Line = line.split()
			# First Column = Position
			# Second = Idk
			# Third = Idk
			# Fourth = Number of reads supporting
			# Need to get first and last

			# The position of the Junction 
			Position = Line[0][:-2]
			#The count of reads without the junction 
			Support = int(Line[3])

			# Put that in dictionnary
			Positions[Position] = Support
		
	return Positions 



def Analyze_Junction(Junction, Counts, Treshold, Output) :

	f = open(Junction, "r")
	g = open(Output, "w")
	g.write("Chromosome\tFirst Position of Junction\tSecond Position of Junction\tReads with Junction\tRead overlapping without Junction\n")
	
	Fini = False
	while not Fini :
		line = f.readline()
		if line == "" :
			Fini = True
		else :
			Line = line.split()

			Position = Line[0][:-2]
			Support = int(Line[3])
			
			if Support > Treshold :

				# Get Chromosome, Position 1 and 2 of the junction
				Pos = Position.split("_")
				Chr = Pos[0]
				Pos1 = Pos[1]
				Pos2 = Pos[2]

				# Search for Pos1 in dictionnary 
				To_Search = Pos[0] + "_" + Pos[1]
				Count = Counts[To_Search]

				
				To_Print = Chr + "\t" + Pos1 + "\t" + Pos2 + "\t" + str(Support) + "\t" + str(Count) + "\n"
				g.write(To_Print)


def main():

	import argparse

	parser = argparse.ArgumentParser()

	parser.add_argument("-ssj", "--Junction", help = "Junction file")
	parser.add_argument("-ssc", "--Count", help = "Count file")
	parser.add_argument("-t", "--treshold", help = "Beyond this treshold, we keep the junction")
	parser.add_argument("-o", "--output", help = "output file")

	args = parser.parse_args()

	# Test base
	Count = args.Count
	Junction = args.Junction
	Treshold = int(args.treshold)
	Output = args.output

	Counts = Analyze_Count(Count)
	Analyze_Junction(Junction, Counts, Treshold, Output)
	
	
    


if __name__ == '__main__':
    main()
