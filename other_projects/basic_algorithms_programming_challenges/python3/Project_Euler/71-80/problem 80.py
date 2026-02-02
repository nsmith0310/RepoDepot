###Answer: 40308

from decimal import *
from math import sqrt
getcontext().prec = 100


i=1
sm=[]
tmp=""
count=0
while i <=100:
    sm=[]
    tmp=""
    if not str(Decimal(sqrt(i))).isdigit():
        tmp=str(Decimal(i).sqrt())[2:]
       
        sm = list(tmp)
        sm = list(map(int, sm))
        
        count=count+sum(sm)
    
    i+=1
    
print("Count:",count)
        
