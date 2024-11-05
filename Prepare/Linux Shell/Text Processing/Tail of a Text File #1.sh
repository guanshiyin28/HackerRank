while read lines
do 
    echo $lines >> file.txt
done 
tail -n 20 file.txt
