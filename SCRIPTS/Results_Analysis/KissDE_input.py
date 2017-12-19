#!/usr/bin/python3.5
# -*- coding: Utf-8 -*-


def Make_Dict_File(File) :
	Dict_Supp = {}
	Dict_No_Supp = {}
	f = open(File, 'r')
	line = f.readline()
	Fini = False
	while not Fini :
		line = f.readline()
		if line == "" :
			Fini = True
		else :
			Line = line.split("\t")
			Segment = Line[0]
			FP = Line[1]
			SP = Line[2]
			Strand = Line[3]
			Supp = Line[4]
			NoSupp = Line[5]

			Junction = Segment + "_" + FP + "_" + SP + "_" + Strand
			Dict_Supp[Junction] = Supp
			Dict_No_Supp[Junction] = NoSupp


	return Dict_Supp, Dict_No_Supp

def get_lenght(junction) :
	jun = junction.split("_")
	print(jun)
	Len = int(jun[2]) - int(jun[1])
	return Len

def Write_Out(r1, r2, r3, r4, u1, u2, u3, u4, c1, c2, c3, c4, Nr1, Nr2, Nr3, Nr4, Nu1, Nu2, Nu3, Nu4, Nc1, Nc2, Nc3, Nc4, toWrite, output) :

	f = open(output, 'w')
	f.write("Junction\tLenght\tR2\tR3\tR4\tR5\tU2\tU3\tU4\tU5\tC2\tC3\tC4\tC5\n")
	for junction in sorted(toWrite) :
		### Line 1, junction 
		line = junction + "\t" + str(get_lenght(junction))
		try : 
			line = line + "\t" + r1[junction]
		except KeyError :
			line = line + "\t" + "0"
		try : 
			line = line + "\t" + r2[junction]
		except KeyError :
			line = line + "\t" + "0"
		try : 
			line = line + "\t" + r3[junction]
		except KeyError :
			line = line + "\t" + "0"
		try :
			line = line + "\t" + r4[junction]
		except KeyError :
			line = line + "\t" + "0"
		try : 
			line = line + "\t" + u1[junction]
		except KeyError :
			line = line + "\t" + "0"
		try : 
			line = line + "\t" + u2[junction]
		except KeyError :
			line = line + "\t" + "0"
		try : 
			line = line + "\t" + u3[junction]
		except KeyError :
			line = line + "\t" + "0"
		try : 
			line = line + "\t" + u4[junction]
		except KeyError :
			line = line + "\t" + "0"
		try : 
			line = line + "\t" + c1[junction]
		except KeyError :
			line = line + "\t" + "0"
		try : 
			line = line + "\t" + c2[junction]
		except KeyError :
			line = line + "\t" + "0"
		try : 
			line = line + "\t" + c3[junction]
		except KeyError :
			line = line + "\t" + "0"
		try : 
			line = line + "\t" + c4[junction]
		except KeyError :
			line = line + "\t" + "0"

		line = line + "\n"
		f.write(line)
		
		### Line 2, No junction
		
		line = junction + "\t" + str(get_lenght(junction))
		try : 
			line = line + "\t" + Nr1[junction]
		except KeyError :
			line = line + "\t" + "0"
		try : 
			line = line + "\t" + Nr2[junction]
		except KeyError :
			line = line + "\t" + "0"
		try : 
			line = line + "\t" + Nr3[junction]
		except KeyError :
			line = line + "\t" + "0"
		try :
			line = line + "\t" + Nr4[junction]
		except KeyError :
			line = line + "\t" + "0"
		try : 
			line = line + "\t" + Nu1[junction]
		except KeyError :
			line = line + "\t" + "0"
		try : 
			line = line + "\t" + Nu2[junction]
		except KeyError :
			line = line + "\t" + "0"
		try : 
			line = line + "\t" + Nu3[junction]
		except KeyError :
			line = line + "\t" + "0"
		try : 
			line = line + "\t" + Nu4[junction]
		except KeyError :
			line = line + "\t" + "0"
		try : 
			line = line + "\t" + Nc1[junction]
		except KeyError :
			line = line + "\t" + "0"
		try : 
			line = line + "\t" + Nc2[junction]
		except KeyError :
			line = line + "\t" + "0"
		try : 
			line = line + "\t" + Nc3[junction]
		except KeyError :
			line = line + "\t" + "0"
		try : 
			line = line + "\t" + Nc4[junction]
		except KeyError :
			line = line + "\t" + "0"

		line = line + "\n"
		f.write(line)
		
def add_TW(toWrite, Dict) :
	for jun in Dict.keys() :
		if jun not in toWrite :
			toWrite.append(jun)
		else :
			pass


def main() :

	c1Supp, c1NoSupp = Make_Dict_File("/home/jeremy/Documents/Cours/M2/Projet/pipeline/COMP/Tresh_From_Sjcount/C-virus-R2-Five_Percent_Treshold.csv")
	c2Supp, c2NoSupp = Make_Dict_File("/home/jeremy/Documents/Cours/M2/Projet/pipeline/COMP/Tresh_From_Sjcount/C-virus-R3-Five_Percent_Treshold.csv")
	c3Supp, c3NoSupp = Make_Dict_File("/home/jeremy/Documents/Cours/M2/Projet/pipeline/COMP/Tresh_From_Sjcount/C-virus-R4-Five_Percent_Treshold.csv")
	c4Supp, c4NoSupp = Make_Dict_File("/home/jeremy/Documents/Cours/M2/Projet/pipeline/COMP/Tresh_From_Sjcount/C-virus-R5-Five_Percent_Treshold.csv")
	r1Supp, r1NoSupp = Make_Dict_File("/home/jeremy/Documents/Cours/M2/Projet/pipeline/COMP/Tresh_From_Sjcount/R-virus-R2-Five_Percent_Treshold.csv")
	r2Supp, r2NoSupp = Make_Dict_File("/home/jeremy/Documents/Cours/M2/Projet/pipeline/COMP/Tresh_From_Sjcount/R-virus-R3-Five_Percent_Treshold.csv")
	r3Supp, r3NoSupp = Make_Dict_File("/home/jeremy/Documents/Cours/M2/Projet/pipeline/COMP/Tresh_From_Sjcount/R-virus-R4-Five_Percent_Treshold.csv")
	r4Supp, r4NoSupp = Make_Dict_File("/home/jeremy/Documents/Cours/M2/Projet/pipeline/COMP/Tresh_From_Sjcount/R-virus-R5-Five_Percent_Treshold.csv")
	u1Supp, u1NoSupp = Make_Dict_File("/home/jeremy/Documents/Cours/M2/Projet/pipeline/COMP/Tresh_From_Sjcount/U-virus-R2-Five_Percent_Treshold.csv")
	u2Supp, u2NoSupp = Make_Dict_File("/home/jeremy/Documents/Cours/M2/Projet/pipeline/COMP/Tresh_From_Sjcount/U-virus-R3-Five_Percent_Treshold.csv")
	u3Supp, u3NoSupp = Make_Dict_File("/home/jeremy/Documents/Cours/M2/Projet/pipeline/COMP/Tresh_From_Sjcount/U-virus-R4-Five_Percent_Treshold.csv")
	u4Supp, u4NoSupp = Make_Dict_File("/home/jeremy/Documents/Cours/M2/Projet/pipeline/COMP/Tresh_From_Sjcount/U-virus-R5-Five_Percent_Treshold.csv")

	toWrite = []
	add_TW(toWrite, c1Supp)
	add_TW(toWrite, c2Supp)
	add_TW(toWrite, c3Supp)
	add_TW(toWrite, c4Supp)
	add_TW(toWrite, r1Supp)
	add_TW(toWrite, r2Supp)
	add_TW(toWrite, r3Supp)
	add_TW(toWrite, r4Supp)
	add_TW(toWrite, u1Supp)
	add_TW(toWrite, u2Supp)
	add_TW(toWrite, u3Supp)
	add_TW(toWrite, u4Supp)

	
	Write_Out(r1Supp, r2Supp, r3Supp, r4Supp, u1Supp, u2Supp, u3Supp, u4Supp, c1Supp, c2Supp, c3Supp, c4Supp, r1NoSupp, r2NoSupp, r3NoSupp, r4NoSupp, u1NoSupp, u2NoSupp, u3NoSupp, u4NoSupp, c1NoSupp, c2NoSupp, c3NoSupp, c4NoSupp, toWrite, "/home/jeremy/Documents/Cours/M2/Projet/pipeline/COMP/Input_KissDE.csv")

if __name__ == "__main__" :
	main()
	
		
		
	
	































			
			
