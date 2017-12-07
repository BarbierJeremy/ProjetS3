

for file_1 in $(ls Junction)
do
base_1=$(basename $file_1 _Junction.txt)
for file_2 in $(ls Seuil/)
do
base_2=$(basename $file_2 _seuil.txt)
if [ "$base_1" == "$base_2" ]
then
echo $file_1
echo $file_2
fi
done
done



