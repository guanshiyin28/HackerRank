<?php

/*
 * Complete the 'circularArrayRotation' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY a
 *  2. INTEGER k
 *  3. INTEGER_ARRAY queries
 */

function circularArrayRotation($a, $k, $queries) {
    $result = [];
    
    foreach ($queries as $queryIndex) {
        $lastIterationOffset = $k % count($a); // eliminate iterations over whole array
        $index = $queryIndex - $lastIterationOffset; // calculate initial index before shifting
        if ($index < 0) { // initial index exceeded beggining of array limit
            $index = count($a) + $index; // counting index from the end of array
        }
        $result[] = $a[$index];
    }
    
    return $result;
}

$fptr = fopen(getenv("OUTPUT_PATH"), "w");

$first_multiple_input = explode(' ', rtrim(fgets(STDIN)));

$n = intval($first_multiple_input[0]);

$k = intval($first_multiple_input[1]);

$q = intval($first_multiple_input[2]);

$a_temp = rtrim(fgets(STDIN));

$a = array_map('intval', preg_split('/ /', $a_temp, -1, PREG_SPLIT_NO_EMPTY));

$queries = array();

for ($i = 0; $i < $q; $i++) {
    $queries_item = intval(trim(fgets(STDIN)));
    $queries[] = $queries_item;
}

$result = circularArrayRotation($a, $k, $queries);

fwrite($fptr, implode("\n", $result) . "\n");

fclose($fptr);
