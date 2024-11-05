read expression

result=$(echo "scale=4; $expression" | bc -l)


if (( $(echo "$result >= 0" | bc -l) )); then
    rounded_result=$(echo "$result + 0.0005" | bc -l)
else
    rounded_result=$(echo "$result - 0.0005" | bc -l)
fi


final_result=$(echo "scale=3; $rounded_result / 1" | bc -l) # dividing the rounded_result by 1 to ommit the zero at end (if there's any)



echo $final_result
