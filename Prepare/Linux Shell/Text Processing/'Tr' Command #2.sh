while read FILE;
do
    echo "${FILE}" >> file.txt
done
tr -d 'a-z' < file.txt
