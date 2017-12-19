# NASA

## Rôle du pipeline

Le but du pipeline est de détecter de nouveaux évènements d’épissages chez le virus de la grippe à partir d'un fichier d'aligment au format .bam (sortie de [STAR](https://github.com/alexdobin/STAR)) 

**Fichier d'entrée** : Les fichiers d'entrées sont les fichiers d'alignement des reads RNAseq viraux contre le génome du virus (souche A/WSN/33)

**Fichier de sortie** : 

    Segment	Junction_First_Position	Junction_Second_Position	Strand	Len_not_Spliced	Len_Spliced	GC_not_Spliced	GC_Spliced	Seq3(maxentscan)	Seq5(maxentscan)	MaxEntScan3	MaxEntScan5	not_Spliced	Spliced

il faut biopython en dependance pour maxentscan

offset 1 : ns1/ns2
offset 8 : reste

 
