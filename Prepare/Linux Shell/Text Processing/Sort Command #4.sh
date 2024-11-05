while read FILE;
do
echo "$FILE" >> file.txt
done
sort -g -r < file.txt
