devanshmudgal96
4 months ago

while read lines
do 
    echo $lines >> file.txt
done
head -n 22 file.txt | tail -n 11 
