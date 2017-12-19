#!/usr/bin/python3.5
# -*- coding: Utf-8 -*-
'''Ce script récupère la séquence des jonctions présente dans les fichiers csv contenant les résultats de sjcount'''


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-g", "--genome", help = "genome format fasta")
parser.add_argument("-csv", "--jonction_csv", help = "fichier au format csv (tabulé) contenant les jonctions sortie de sjcount")
parser.add_argument("-o", "--output_file", help = "output file")
args = parser.parse_args()




def recup_jonction(args):
	if args.genome != None and args.jonction_csv != None and args.output_file != None:
		segment = False
		compt = 0
		j = {}
		j['Segment']=""
		j['First']=0	
		j['Second']=0
		j['Strand']=""
		o = open(args.output_file,'w')
		f2 = open(args.jonction_csv,'r')
		for l in f2:
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
				if j['Strand'] == '+':
					o.write('> '+j['Segment']+'\t'+j['First']+'\t'+j['Second']+'\t'+j['Strand']+'\n'+sequence[int(j['First'])-1:int(j['Second'])-1]+"\n"+"\n"+"\n")
				else:
					sequence = sequence.replace('A','t')
					sequence = sequence.replace('T','a')
					sequence = sequence.replace('C','g')
					sequence = sequence.replace('G','c')
					sequence = sequence.upper()
					sequence = sequence[::-1]
					o.write('> '+j['Segment']+'\t'+j['First']+'\t'+j['Second']+'\t'+j['Strand']+'\n'+sequence[int(j['First'])-1:int(j['Second'])-1]+"\n"+"\n"+"\n")





			compt = compt+1
	else:
		raise('erreur dans les fichier passée')



recup_jonction(args)



