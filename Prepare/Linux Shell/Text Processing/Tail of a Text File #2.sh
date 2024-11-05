while read lines
do 
    echo $lines >> file.txt
done
tail -c 20 file.txt
