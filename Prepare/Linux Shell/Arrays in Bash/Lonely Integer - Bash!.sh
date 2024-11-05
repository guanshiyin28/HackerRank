awk '  
BEGIN { res = 0 }  

NR == 2 {  
    for (i = 1; i <= NF; i++) {  
    el = $i  
    if (el in arr) {  
          res -= el  
      } else {  
          arr[el] = el  
          res += el  
      }                  
  }          
  print res  
}'
