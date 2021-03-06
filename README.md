# New Approach for Splicing Analysis (NASA)

## Rôle du pipeline

Le but du pipeline est de détecter de nouveaux évènements d’épissage chez le virus de la grippe (Influenza virus A) à partir d'un fichier d'alignement au format .bam (sortie de [STAR](https://github.com/alexdobin/STAR)). 

**Fichier d'entrée** : Les fichiers d'entrées sont les fichiers d'alignement des reads RNAseq viraux contre le génome du virus (souche A/WSN/33) : un fichier par condition et par réplicat.

**Fichier de sortie** : Les fichiers de sortie contiennent la liste des jonctions retrouvées dans les différents fichiers .bam (un fichier résultat par fichier .bam).

L'en-tête des fichiers est le suivant : 

    Segment	Gene	Junction_First_Position	Junction_Second_Position	Strand	Len_not_Spliced	Len_Spliced	GC_not_Spliced	GC_Spliced	Seq3(maxentscan)	Seq5(maxentscan)	MaxEntScan3	MaxEntScan5	not_Spliced	Spliced
   
Exemple de résultats obtenus :

    CY010795.1	PB2	167	2195	+	2280	251	44.07894736842105	44.6215139442231	GAAGGCTAATGTGCTAATTGGGC	TGATGGCAA	-31.9136840922	-6.74180412924	ATGGAAAGAATAAAAGAACTAAGGAATCTAATGTCGCAGTCTCGCACTCGCGAGATACTCACAAAAACCACCGTGGACCATATGGCCATAATCAAGAAGTACACATCAGGAAGACAGGAGAAGAACCCAGCACTTAGGATGAAATGGATGATGGCAATGAAATATCCAATTACAGCAGACAAGAGGATAACGGAAATGATTCCTGAGAGAAATGAGCAGGGACAAACTTTATGGAGTAAAATGAATGACGCCGGATCAGACCGAGTGATGGTATCACCTCTGGCTGTGACATGGTGGAATAGGAATGGACCAGTGACAAGTACAGTTCATTATCCAAAAATCTACAAAACTTATTTTGAAAAAGTCGAAAGGTTAAAACATGGAACCTTTGGCCCTGTCCATTTTAGAAACCAAGTCAAAATACGTCGAAGAGTTGACATAAATCCTGGTCATGCAGATCTCAGTGCCAAAGAGGCACAGGATGTAATCATGGAAGTTGTTTTCCCTAACGAAGTGGGAGCCAGGATACTAACATCGGAATCGCAACTAACGACAACCAAAGAGAAGAAAGAAGAACTCCAGGGTTGCAAAATTTCTCCTCTGATGGTGGCATACATGTTGGAGAGAGAACTGGTCCGCAAAACGAGATTCCTCCCAGTGGCTGGTGGAACAAGCAGTGTGTACATTGAAGTGTTGCATTTGACCCAAGGAACATGCTGGGAACAGATGTACACTCCAGGAGGGGAGGCGAGGAATGATGATGTTGATCAAAGCTTAATTATTGCTGCTAGAAACATAGTAAGAAGAGCCACAGTATCAGCAGATCCACTAGCATCTTTATTGGAGATGTGCCACAGCACGCAGATTGGTGGAATAAGGATGGTAAACATCCTTAGGCAGAACCCAACAGAAGAGCAAGCCGTGGATATTTGCAAGGCTGCAATGGGACTGAGAATTAGCTCATCCTTCAGTTTTGGTGGATTCACATTTAAGAGAACAAGCGGATCATCAGTCAAGAGAGAGGAAGAGGTGCTTACGGGCAATCTTCAGACATTGAAGATAAGAGTGCATGAGGGATATGAAGAGTTCACAATGGTTGGGAGAAGAGCAACAGCTATACTCAGAAAAGCAACCAGGAGATTGATTCAGCTGATAGTGAGTGGGAGAGACGAACAGTCGATTGCCGAAGCAATAATTGTGGCCATGGTATTTTCACAAGAGGATTGTATGATAAAAGCAGTTAGAGGTGACCTGAATTTCGTCAATAGGGCGAATCAGCGATTGAATCCCATGCACCAACTTTTGAGACATTTTCAGAAGGATGCAAAGGTGCTCTTTCAAAATTGGGGAATTGAATCCATCGACAATGTGATGGGAATGATCGGGATATTGCCCGACATGACTCCAAGCACCGAGATGTCAATGAGAGGAGTGAGAATCAGCAAAATGGGGGTAGATGAGTATTCCAGCGCGGAGAAGATAGTGGTGAGCATTGACCGTTTTTTGAGAGTTAGGGACCAACGTGGGAATGTACTACTGTCTCCCGAGGAGGTCAGTGAAACACAGGGAACAGAGAAACTGACAATAACTTACTCATCGTCAATGATGTGGGAGATTAATGGTCCTGAATCAGTGTTGGTCAATACCTATCAGTGGATCATCAGAAACTGGGAAACTGTTAAAATTCAGTGGTCCCAGAATCCTACAATGCTGTACAATAAAATGGAATTTGAGCCATTTCAGTCTTTAGTTCCAAAGGCCGTTAGAGGCCAATACAGTGGGTTTGTGAGAACTCTGTTCCAACAAATGAGGGATGTGCTTGGGACATTTGATACCGCTCAGATAATAAAACTTCTTCCCTTCGCAGCCGCTCCACCAAAGCAAAGTGGAATGCAGTTCTCCTCATTGACTATAAATGTGAGGGGATCAGGAATGAGAATACTTGTAAGGGGCAATTCTCCAGTATTCAACTACAACAAGACCACTAAAAGACTCACAGTTCTCGGAAAGGATGCTGGCCCTTTAACTGAAGACCCAGATGAAGGCACAGCTGGAGTTGAGTCCGCAGTTCTGAGAGGATTCCTCATTCTGGGCAAAGAAGACAGGAGATATGGACCAGCATTAAGCATAAATGAACTGAGCAACCTTGCGAAAGGAGAGAAGGCTAATGTGCTAATTGGGCAAGGAGACGTGGTGTTGGTAATGAAACGGAAACGGAACTCTAGCATACTTACTGACAGCCAGACAGCGACCAAAAGAATTCGGATGGCCATCAATTAG	ATGGAAAGAATAAAAGAACTAAGGAATCTAATGTCGCAGTCTCGCACTCGCGAGATACTCACAAAAACCACCGTGGACCATATGGCCATAATCAAGAAGTACACATCAGGAAGACAGGAGAAGAACCCAGCACTTAGGATGAAATGGATGAGCAAGGAGACGTGGTGTTGGTAATGAAACGGAAACGGAACTCTAGCATACTTACTGACAGCCAGACAGCGACCAAAAGAATTCGGATGGCCATCAATTAG

    
## Logiciels requis

Pour exécuter le pipeline les logiciels suivant doivent être installés.

### [Sjcount](https://github.com/pervouchine/sjcount-full)

Sjcount est nécessaire au bon fonctionnement du pipeline, il permet de compter les reads qui se trouvent sur les jonctions d'épissage. 
La documentation de Sjcount se trouve à l'adresse suivante : [https://github.com/pervouchine/sjcount-full/blob/master/latex/sjcount.pdf](https://github.com/pervouchine/sjcount-full/blob/master/latex/sjcount.pdf)

### [MaxEntScan](http://genes.mit.edu/burgelab/maxent/Xmaxentscan_scoreseq.html)

MaxEntScan est également nécessaire au bon fonctionnement du pipeline.
Cependant, une [version](https://github.com/kepbod/maxentpy) python des scripts originaux est déjà présente dans l'archive github actuel. Il n'est donc à priori **pas nécessaire de le réinstaller**. 

### [Python3](https://doc.ubuntu-fr.org/python) et [Biopython](http://biopython.org/wiki/Download)

[Python3](https://doc.ubuntu-fr.org/python) est plus que nécessaire à l'exécution du pipeline (car de nombreux scripts sont écrits en python3). 

    sudo apt update
    sudo apt install python3.6 

Il est également nécessaire d'avoir installé [biopython](http://biopython.org/wiki/Download)

    sudo apt install python3-pip
    python3.6 -m pip install biopython
  


## Pipeline

Le pipeline s'exécute via le script NASA.sh (Attention ! Il faut être à la racine pour exécuter le script):

    ./SCRIPTS/NASA.sh 1 2 3 4 5 6 

Arguments :   
  
OBLIGATOIRES :   
1 : Chemin vers le dossier contenant les fichiers au format bam à utiliser  
2 : Chemin vers le dossier où placer les résultats (s'il n'existe pas, il sera créé)   
3 : Chemin vers le génome au format fasta   
4 : Chemin vers le dossier contenant sjcount (voir sjcount - installation)  
5 : Chemin vers le fichier gff contenant l'annotation du génome   
  
Optionnel  
6 : Seuil à utiliser pour le rapport épissé/non-épissé (voir étapes, partie 2.). Si aucun seuil n'est indiqué, le seuil 5% (0.05) sera utilisé.   
  

# Etapes de l'analyse :

1. Utilisation de Sjcount sur chaque fichier .bam présents dans le dossier fournis en argument : `script_sjcount.sh`  
Sjcount va compter les reads supportant les jonctions d'épissages (fichier Junction.txt) et les comptages correspondants au transcrit non épissé (Fichier Count.txt).
 
2. Les jonctions d'intérêt sont ensuite récupérées par rapport au seuil donné en argument du pipeline (seuil = pourcentage de reads confirmant l'épissage par rapport aux reads totaux s'alignant à cet endroit) : `Get_Junction.py` et `Sjcount_Tresholding.sh`.  Par défaut, le seuil 5% est utilisé, c'est à dire que sont conservées les jonctions pour lesquelles les reads supportants la version épissée du transcrit représentent au minimum 5% des reads s'alignant à cet endroit. 
Les fichiers créés contiennent les jonctions d'intérêt au format csv.

3. MaxEntScan est ensuite exécuté sur les jonctions d'intérêts pour déterminer la force des sites d'épissages en 5' et 3' : `fonction-tsvmaxentscan.py` et `scriptmaxentscan.sh`  

4. Enfin le dernier script permet d'assembler les résultats précedemments obtenus, et calcule quelques statistiques basiques telles que les taux de GC des séquences épissées et non épissées : `recup_all.py` et `recup_all.sh`

L'arborescence de la sortie est la suivante :

    $ NASA
    .
    ├── Logs
    │   ├── sjcount.log
    ├── Sjcount
    │   ├── Junction
    │   │   └── Fichiers_Junction.txt 
    │   └── Count
    │       └── Fichiers_Count.txt
    ├── Junctions
    │   └── Fichiers_Junction_Filter.csv
    ├── MaxEntScan
    │   └── Fichiers_MaxEntScan.csv    
    └── Analyse
        └── Fichiers_All.csv



 
