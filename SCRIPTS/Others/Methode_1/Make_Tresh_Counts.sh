
for file in $(ls COMP/Intersect/*IdxStats*)
do
	base=$(basename $file _IdxStats.txt)
	./SCRIPTS/Verif_Seuil.py -iB $file -iL COMP/Intersect/Junction_NS1NS2.csv -o COMP/Seuil_Verified/$base-Tresholds.txt
done

