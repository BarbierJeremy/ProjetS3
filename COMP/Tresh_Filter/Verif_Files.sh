

for file in $(ls *.txt) 
do
	if grep -q "CY010792.1_43_516_+" $file 
	then
		echo $file Okay
	else
		echo $file Not Okay
	fi
done

