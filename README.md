# New Approach for Splicing Analysis (NASA)

## Rôle du pipeline

Le but du pipeline est de détecter de nouveaux évènements d’épissages chez le virus de la grippe à partir d'un fichier d'aligment au format .bam (sortie de [STAR](https://github.com/alexdobin/STAR)) 

**Fichier d'entrée** : Les fichiers d'entrées sont les fichiers d'alignement des reads RNAseq viraux contre le génome du virus (souche A/WSN/33) : un fichier par condition et par réplicat

**Fichier de sortie** : Les fichiers de sortie contiennent la liste des jonctions retrouvées dans les différents fichiers .bam (un fichier résultat par fichier .bam).

L'en-tête des fichiers est le suivant : 

    Segment	Gene	Junction_First_Position	Junction_Second_Position	Strand	Len_not_Spliced	Len_Spliced	GC_not_Spliced	GC_Spliced	Seq3(maxentscan)	Seq5(maxentscan)	MaxEntScan3	MaxEntScan5	not_Spliced	Spliced
   
Exemple de résultat obtenue :

    CY010795.1	PB2	167	2195	+	2280	251	44.07894736842105	44.6215139442231	GAAGGCTAATGTGCTAATTGGGC	TGATGGCAA	-31.9136840922	-6.74180412924	ATGGAAAGAATAAAAGAACTAAGGAATCTAATGTCGCAGTCTCGCACTCGCGAGATACTCACAAAAACCACCGTGGACCATATGGCCATAATCAAGAAGTACACATCAGGAAGACAGGAGAAGAACCCAGCACTTAGGATGAAATGGATGATGGCAATGAAATATCCAATTACAGCAGACAAGAGGATAACGGAAATGATTCCTGAGAGAAATGAGCAGGGACAAACTTTATGGAGTAAAATGAATGACGCCGGATCAGACCGAGTGATGGTATCACCTCTGGCTGTGACATGGTGGAATAGGAATGGACCAGTGACAAGTACAGTTCATTATCCAAAAATCTACAAAACTTATTTTGAAAAAGTCGAAAGGTTAAAACATGGAACCTTTGGCCCTGTCCATTTTAGAAACCAAGTCAAAATACGTCGAAGAGTTGACATAAATCCTGGTCATGCAGATCTCAGTGCCAAAGAGGCACAGGATGTAATCATGGAAGTTGTTTTCCCTAACGAAGTGGGAGCCAGGATACTAACATCGGAATCGCAACTAACGACAACCAAAGAGAAGAAAGAAGAACTCCAGGGTTGCAAAATTTCTCCTCTGATGGTGGCATACATGTTGGAGAGAGAACTGGTCCGCAAAACGAGATTCCTCCCAGTGGCTGGTGGAACAAGCAGTGTGTACATTGAAGTGTTGCATTTGACCCAAGGAACATGCTGGGAACAGATGTACACTCCAGGAGGGGAGGCGAGGAATGATGATGTTGATCAAAGCTTAATTATTGCTGCTAGAAACATAGTAAGAAGAGCCACAGTATCAGCAGATCCACTAGCATCTTTATTGGAGATGTGCCACAGCACGCAGATTGGTGGAATAAGGATGGTAAACATCCTTAGGCAGAACCCAACAGAAGAGCAAGCCGTGGATATTTGCAAGGCTGCAATGGGACTGAGAATTAGCTCATCCTTCAGTTTTGGTGGATTCACATTTAAGAGAACAAGCGGATCATCAGTCAAGAGAGAGGAAGAGGTGCTTACGGGCAATCTTCAGACATTGAAGATAAGAGTGCATGAGGGATATGAAGAGTTCACAATGGTTGGGAGAAGAGCAACAGCTATACTCAGAAAAGCAACCAGGAGATTGATTCAGCTGATAGTGAGTGGGAGAGACGAACAGTCGATTGCCGAAGCAATAATTGTGGCCATGGTATTTTCACAAGAGGATTGTATGATAAAAGCAGTTAGAGGTGACCTGAATTTCGTCAATAGGGCGAATCAGCGATTGAATCCCATGCACCAACTTTTGAGACATTTTCAGAAGGATGCAAAGGTGCTCTTTCAAAATTGGGGAATTGAATCCATCGACAATGTGATGGGAATGATCGGGATATTGCCCGACATGACTCCAAGCACCGAGATGTCAATGAGAGGAGTGAGAATCAGCAAAATGGGGGTAGATGAGTATTCCAGCGCGGAGAAGATAGTGGTGAGCATTGACCGTTTTTTGAGAGTTAGGGACCAACGTGGGAATGTACTACTGTCTCCCGAGGAGGTCAGTGAAACACAGGGAACAGAGAAACTGACAATAACTTACTCATCGTCAATGATGTGGGAGATTAATGGTCCTGAATCAGTGTTGGTCAATACCTATCAGTGGATCATCAGAAACTGGGAAACTGTTAAAATTCAGTGGTCCCAGAATCCTACAATGCTGTACAATAAAATGGAATTTGAGCCATTTCAGTCTTTAGTTCCAAAGGCCGTTAGAGGCCAATACAGTGGGTTTGTGAGAACTCTGTTCCAACAAATGAGGGATGTGCTTGGGACATTTGATACCGCTCAGATAATAAAACTTCTTCCCTTCGCAGCCGCTCCACCAAAGCAAAGTGGAATGCAGTTCTCCTCATTGACTATAAATGTGAGGGGATCAGGAATGAGAATACTTGTAAGGGGCAATTCTCCAGTATTCAACTACAACAAGACCACTAAAAGACTCACAGTTCTCGGAAAGGATGCTGGCCCTTTAACTGAAGACCCAGATGAAGGCACAGCTGGAGTTGAGTCCGCAGTTCTGAGAGGATTCCTCATTCTGGGCAAAGAAGACAGGAGATATGGACCAGCATTAAGCATAAATGAACTGAGCAACCTTGCGAAAGGAGAGAAGGCTAATGTGCTAATTGGGCAAGGAGACGTGGTGTTGGTAATGAAACGGAAACGGAACTCTAGCATACTTACTGACAGCCAGACAGCGACCAAAAGAATTCGGATGGCCATCAATTAG	ATGGAAAGAATAAAAGAACTAAGGAATCTAATGTCGCAGTCTCGCACTCGCGAGATACTCACAAAAACCACCGTGGACCATATGGCCATAATCAAGAAGTACACATCAGGAAGACAGGAGAAGAACCCAGCACTTAGGATGAAATGGATGAGCAAGGAGACGTGGTGTTGGTAATGAAACGGAAACGGAACTCTAGCATACTTACTGACAGCCAGACAGCGACCAAAAGAATTCGGATGGCCATCAATTAG

    
## Logiciel requis

biopython  
sjcount  


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
Sjcount va compter les reads supportant les jonctions d'épissages (fichier Junction.txt) et les comptages correspondant au transcrit non épissé (Fichier Count.txt).
 
2. Les jonctions d'intérêt sont ensuite récupérées par rapport au seuil donné en argument du pipeline (seuil = pourcentage de read confirmant l'épissage par rapport aux reads totaux s'alignant à cet endroit) : `Get_Junction.py` et `Sjcount_Tresholding.sh`. Par défaut, le seuil 5% est utilisé, c'est à dire que sont conservées les jonctions pour lesquelles les reads supportant la version épissée du transcrit représentent au minimum 5% des reads s'alignant à cet endroit. 
Les fichiers créés contiennent les jonctions d'intérêt au format csv.

3. MaxEntScan est ensuite exécuté sur les jonctions d'intérêt pour déterminer la force des sites d'épissages : `fonction-tsvmaxentscan.py` et `scriptmaxentscan.sh` 

4. Enfin le dernier scripts permet d'assembler les résultats précedemments obtenus, et calcule quelques statistiques basiques telles que les taux de gc des séquences épissées et non épissées : `recup_all.py` et `recup_all.sh`

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



 
