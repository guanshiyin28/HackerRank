while read lines
do 
    echo $lines >> file.txt
done 
head -c 20 < file.txt
