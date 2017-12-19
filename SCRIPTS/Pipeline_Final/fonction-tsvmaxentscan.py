#!/usr/bin/python3
#coding: utf-8
#on donne tsv en premier puis genome en multi fasta puis fichier de sortie https://github.com/kepbod/maxentpy    
from Bio import SeqIO
import sys
import os

sys.path.append(sys.argv[4])

from maxentpy import maxent




fichsorti= open(sys.argv[3], 'w') # ouvre fichier pour ecrire 
di={}
##print(sys.argv[2])
for seq_record in SeqIO.parse(str(sys.argv[2]), "fasta"): #parse le fasta pour mettre sequence et id dans dictionaire 
	di[seq_record.id]=seq_record
	##print(seq_record.id)


with open(sys.argv[1]) as f: # ouvre le fichier avec les jonction 
		for line in f:
			lig=line.split('\t') 
			if lig[0]=="Segment":
				 fichsorti.write("{}\t{}\t{}\t{}\tseq5\tseq3\tscore5\tscore3\n".format(lig[0],lig[1],lig[2],lig[3]))
			else:
				seq=di[lig[0]] #on recupere la séquence du segment  qui correspont a cette ligne 
				seq=seq.seq
				seq=str(seq)

				pos5=int(lig[1])-1 # position jontion 5'  le -1 car python compte a partir de zero 
				pos3=int(lig[2])-1 # position jonction 3' 
				
				
				d=int(pos5)-3
				fi=int(pos5)+6
				
				seq5=seq[d:fi] 

				deb=int(pos3)-20
				fin=int(pos3)+3
				seq3=seq[deb:fin]


				sco5=maxent.score5(seq5)

				sco3=maxent.score3(seq3)
				fichsorti.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(lig[0],lig[1],lig[2],lig[3],seq5,seq3,sco5,sco3))


f.closed
fichsorti.close









