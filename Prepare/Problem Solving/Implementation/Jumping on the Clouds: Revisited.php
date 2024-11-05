<?php

// Complete the jumpingOnClouds function below.
function jumpingOnClouds($c, $k) {
    $energy = 100;
    $n = sizeof($c);
    $cloud = 0;
    
    do {
        $cloud = ($cloud + $k) % $n;
        if ($c[$cloud] == 1) {
            $energy = $energy - 3;
        } else {
            $energy--;
        }
    } while($cloud != 0);
    
    return $energy;
}

$fptr = fopen(getenv("OUTPUT_PATH"), "w");

$stdin = fopen("php://stdin", "r");

fscanf($stdin, "%[^\n]", $nk_temp);
$nk = explode(' ', $nk_temp);

$n = intval($nk[0]);

$k = intval($nk[1]);

fscanf($stdin, "%[^\n]", $c_temp);

$c = array_map('intval', preg_split('/ /', $c_temp, -1, PREG_SPLIT_NO_EMPTY));

$result = jumpingOnClouds($c, $k);

fwrite($fptr, $result . "\n");

fclose($stdin);
fclose($fptr);
