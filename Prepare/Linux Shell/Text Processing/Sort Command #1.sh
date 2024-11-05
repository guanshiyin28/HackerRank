while read TEXT;
do
    echo "${TEXT}" >> text.txt
done
sort -k 1n < text.txt
