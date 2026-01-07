###1120149658760
###https://oeis.org/A081018

from math import sqrt
i = 10

f=[0,2,15,104]
i = 3
while len(f)<=15:
    f.append(8*f[-1]-8*f[-2]+f[-3])

print(f[-1])
    
