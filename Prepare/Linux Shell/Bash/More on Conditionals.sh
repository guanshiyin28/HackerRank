read x
read y
read z

if [ "$x" -eq "$y" ]; then
    if [ "$z" -eq "$y" ]; then
        echo "EQUILATERAL"
    else
        echo "ISOSCELES"
    fi
else
    if [ "$z" -eq "$y" ]; then
        echo "ISOSCELES"
    else
        echo "SCALENE"
    fi 
fi
