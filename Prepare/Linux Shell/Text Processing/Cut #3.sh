N=1
while [[ $N -ge 1 && $N -le 100 ]]; do
        let N++
        read n
        echo "$n" | cut -b 2-7
done
