import sys, os
path_nb_read = sys.argv[1]

def read(path_nb_read):
	sortie = path_nb_read.rstrip('IdxStats.txt')
	sortie = sortie.split('/')[-1]+'seuil.txt'
	test=sortie.split('_')[0]
	print(test)

	f = open(path_nb_read,'r')
	nb_read_g ={}
	for line in f:
		line = line.split('\t')
		if (int(line[2]) != 0):
			nb_read_g[line[0]]=int(line[2])
		else :
			nb_read_g[line[0]]=1
	f.close()

	f2 = open('../RESULTS/Intersect/Junction_NS1NS2.csv','r')

	for line in f2:
		
		line = line.rstrip().split(',')
		if (line[0].split('_')[0] == test):
			junction_p_ns1 = int(line[1]) 
			nb_read_p_ns1 = int(line[2])
	f2.close()
	nom = 'CY010792.1'
	junction_g_ns1 = ((junction_p_ns1*nb_read_g[nom])/nb_read_p_ns1)
	print (junction_g_ns1)

	
	o = open('../RESULTS/Seuil/'+sortie,'w')
	for k,v in nb_read_g.items():
		calcul = int((junction_g_ns1*v)/(nb_read_g[nom]))              
		o.write(k+'\t'+str(calcul)+'\n')
	o.close()



read(path_nb_read)
