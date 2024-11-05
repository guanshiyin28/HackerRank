<?php

/*
 * Complete the 'equalizeArray' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

function equalizeArray($arr) {
    $counter = [];
    $max = [];
    foreach ($arr as $el) {
        isset($counter[$el]) ? $counter[$el]++ : $counter[$el] = 1;
        if ($counter[$el] > $max['value']) {
            $max['value'] = $counter[$el];
            $max['index'] = $el;
        }
    }
    
    unset($counter[$max['index']]);
    return array_sum($counter);
}


$fptr = fopen(getenv("OUTPUT_PATH"), "w");

$n = intval(trim(fgets(STDIN)));

$arr_temp = rtrim(fgets(STDIN));

$arr = array_map('intval', preg_split('/ /', $arr_temp, -1, PREG_SPLIT_NO_EMPTY));

$result = equalizeArray($arr);

fwrite($fptr, $result . "\n");

fclose($fptr);
