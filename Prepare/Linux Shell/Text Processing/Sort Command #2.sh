while read TEXT;
do
    echo "${TEXT}" >> text.txt
done
sort -r < text.txt
