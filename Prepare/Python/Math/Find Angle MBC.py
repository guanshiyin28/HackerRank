# Enter your code here. Read input from STDIN. Print output to STDOUTimport math

import math
ab=int(input())
bc=int(input())
ac=math.sqrt(ab**2+bc**2)
mc=ac/2
rad_c = math.asin(ab/ac) 
mb=math.sqrt(bc**2+mc**2-math.cos(rad_c)*(2*bc*mc))
rad_mb=math.acos((mb**2+bc**2-mc**2)/(2*mb*bc))
print(str(round(180/math.pi*rad_mb))+chr(176))
