readarray -t countries

multCountries=("${countries[@]}" "${countries[@]}" "${countries[@]}")
echo ${multCountries[@]}
