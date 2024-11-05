<?php

/*
 * Complete the 'squares' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER a
 *  2. INTEGER b
 */

function squares($a, $b) {
    $counter = 0;
    for ($i = 1; $i <= $b; $i++) {
        $square = $i * $i;
        ($square >= $a && $square <= $b) ? $counter++ : 0;        
        if($square >= $b) break;
    }
    return $counter;
}

$fptr = fopen(getenv("OUTPUT_PATH"), "w");

$q = intval(trim(fgets(STDIN)));

for ($q_itr = 0; $q_itr < $q; $q_itr++) {
    $first_multiple_input = explode(' ', rtrim(fgets(STDIN)));

    $a = intval($first_multiple_input[0]);

    $b = intval($first_multiple_input[1]);

    $result = squares($a, $b);

    fwrite($fptr, $result . "\n");
}

fclose($fptr);
