declare -A mat
rows=63
cols=100
read n
f=16
for ((i=0; i<$rows; ++i)) do
    for ((j=0; j<$cols; ++j)) do
        mat[$i,$j]="_"
    done
done

pow(){
    local v=1
    for((i=1; i<$1; ++i)) do
        v=$(($v*2))
    done
    echo $v
}

it() { # mid, iteration, row
    local nums=$(($f/$(pow $2)))
    local a=$3
    local b=$(($3+$nums))

    for((i=$a; i<$b; ++i)) do
        mat[$i,$1]=1
    done

    local ml=$1
    local mr=$1

    a=$b
    b=$(($b+$nums))
    for((i=$a; i<$b; ++i)) do
        ml=$(($ml-1))
        mat[$i,$ml]=1
    done    

    for((i=$a; i<$b; ++i)) do
        mr=$(($mr+1))
        mat[$i,$mr]=1
    done
    local x=$(($2+1))
    if (( $x <= $n )) then
        it $ml $x $b;
        it $mr $x $b;
    fi
};

it 49 1 0;

for ((i=$(($rows-1)); i>=0; --i)) do
    for ((j=0; j<$cols; ++j)) do
        echo -n ${mat[$i,$j]}
    done
    echo
done
