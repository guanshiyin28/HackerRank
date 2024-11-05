mapfile -t array

output=$(grep -vi "a" <(printf "%s\n" "${array[@]}"))

if [ -z "$output" ]; then
 echo ""
else
 echo "$output"
fi
