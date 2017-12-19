#!/usr/bin/python3.5
# -*- coding: Utf-8 -*-

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-g", "--genome", help = "genome format fasta")
parser.add_argument("-a", "--annotation", help = "annotation au format gff")
parser.add_argument("-csv", "--jonction_csv", help = "fichier au format csv (tabulé) contenant les jonctions sortie de sjcount")
parser.add_argument("-m", "--maxent", help = "fichier résultat de MaxEntScan")
parser.add_argument("-o", "--output_file", help = "output file")
args = parser.parse_args()


def calculGC (sequence):
	compt = 0
	for i in sequence:
		if i == 'G' or i == 'C':
			compt = compt+1
	return (compt/len(sequence))*100

def recup_jonction(args):
	print(args.output_file)
	if args.genome != None and args.jonction_csv != None and args.output_file != None and args.annotation != None and args.maxent != None:
		segment = False
		compt = 0
		j = {}
		j['Segment']=""
		j['First']=0	
		j['Second']=0
		j['Strand']=""
		j['taille_non_episse'] = 0
		j['taille_episse'] = 0
		j['GC_non_episse'] = 0
		j['GC_episse'] = 0
		j['Seq3'] = ''
		j['Seq5'] = ''
		j['MaxEntScan3'] = 0
		j['MaxEntScan5'] = 0
		j['non_episse'] = ''
		j['episse'] = ''
		j['prot'] = ''
		o = open(args.output_file,'w')
		o.write('Segment'+'\t'+'Gene'+'\t'+'Junction_First_Position'+'\t'+'Junction_Second_Position'+'\t'+'Strand'+'\t'+'Len_not_Spliced'+'\t'+'Len_Spliced'+'\t'+'GC_not_Spliced'+'\t'+'GC_Spliced'+'\t'+'Seq3(maxentscan)'+'\t'+'Seq5(maxentscan)'+'\t'+'MaxEntScan3'+'\t'+'MaxEntScan5'+'\t'+'not_Spliced'+'\t'+'Spliced'+"\n")
		f2 = open(args.jonction_csv,'r')
		for l in f2:
			print ('*******')
			if compt != 0:
				j['Segment'] = l.split('\t')[0]
				j['First'] = l.split('\t')[1]
				j['Second'] = l.split('\t')[2]
				j['Strand'] = l.split('\t')[3]
				f = open(args.genome,'r')	
				for line in f:
					if line[0] == '>':
						if line.split(' ')[0].split('>')[1] == j['Segment']:
							segment = True
							sequence = ""
						else:
							segment = False
					if segment:
						if line[0] != '>':
							sequence = sequence+line.strip()
				f.close()
				
				f3 = open(args.annotation,'r')
				un = 0
				deux = 0
				i = 0
				gene_exist = False
				for line in f3:
					if line.split('\t')[0] == j['Segment']:
						if line.split('\t')[2] == 'gene':
							if i == 0:
								gene_exist = True
								j['prot'] = line.split('\t')[8].split(';')[1].split('=')[1]
								un = int(line.split('\t')[3])
								deux = int(line.split('\t')[4])
								
								i = i+1
							elif int(line.split('\t')[3]) <= un and int(line.split('\t')[4]) >= deux:
								j['prot'] = line.split('\t')[8].split(';')[1].split('=')[1]
								un = int(line.split('\t')[3])
								deux = int(line.split('\t')[4])
							elif int(line.split('\t')[3]) < un:
								un = int(line.split('\t')[3])
							elif int(line.split('\t')[4]) > deux:
								deux = int(line.split('\t')[4])
				f3.close()
				if not gene_exist:
					j['GC_non_episse'] = None
					j['GC_episse'] = None
					j['taille_non_episse'] = None
					j['taille_episse'] = None
					j['non_episse'] = None
					j['episse'] = None
				else:
					if j['Strand'] == '-':
						sequence = sequence.upper()
						sequence = sequence.replace('A','t')
						sequence = sequence.replace('T','a')
						sequence = sequence.replace('C','g')
						sequence = sequence.replace('G','c')
						sequence = sequence.upper()
						sequence = sequence[::-1]
					non_episse = sequence[un-1:deux]
					episse = sequence[un-1 : int(j['First'])-1]+sequence[int(j['Second']):deux]
					
					j['GC_non_episse'] = calculGC (non_episse)
					j['GC_episse'] = calculGC (episse)
					j['taille_non_episse'] = len(non_episse)
					j['taille_episse'] = len(episse)
					j['non_episse'] = non_episse
					j['episse'] = episse
				f4 = open(args.maxent,'r')
				for line in f4:
					if line.split('\t')[0] == j['Segment'] and line.split('\t')[1] == j['First'] and line.split('\t')[2] == j['Second'] and line.split('\t')[3] == j['Strand']:
						j['Seq5'] = line.split('\t')[4].strip()
						j['Seq3'] = line.split('\t')[5].strip()
						j['MaxEntScan3'] = line.split('\t')[6].strip()
						j['MaxEntScan5'] = line.split('\t')[7].strip()
				f4.close()
				o.write(j['Segment']+'\t'+j['prot']+'\t'+str(j['First'])+'\t'+str(j['Second'])+'\t'+j['Strand']+'\t'+str(j['taille_non_episse'])+'\t'+str(j['taille_episse'])+'\t'+str(j['GC_non_episse'])+'\t'+str(j['GC_episse'])+'\t'+j['Seq3']+'\t'+j['Seq5']+'\t'+str(j['MaxEntScan3'])+'\t'+str(j['MaxEntScan5'])+'\t'+j['non_episse']+'\t'+j['episse']+"\n")

			compt = compt+1
		f2.close()
	else:
		raise('erreur dans les fichier passée')



recup_jonction(args)



