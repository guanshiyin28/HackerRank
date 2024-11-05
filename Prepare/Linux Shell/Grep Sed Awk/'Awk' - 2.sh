awk '{if (($2+$3+$4)/3>=50) {b="Pass"} else {b="Fail"}} {print $1" : "b}'
