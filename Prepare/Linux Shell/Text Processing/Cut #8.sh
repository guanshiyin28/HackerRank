while IFS=' ' read -r -a line;do
    echo "${line[0]} ${line[1]} ${line[2]}"
done
