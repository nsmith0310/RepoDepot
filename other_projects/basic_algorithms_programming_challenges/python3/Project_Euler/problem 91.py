###longish 14234

from math import sqrt
from itertools import product as p, combinations as c
i = 50
total=0
while i<=50:
    count=0
    triangle=i
    
    a = [p for p in range(0,i+1)]
    
    nums = list(p(a,repeat=2))
    ###print(nums)
    nums.remove((0,0))
    
    test = list(c(nums,2))
                               
    for x in test:
        a = [0,0]
        b=x[0]
        g=x[1]

        d1=sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
        d2=sqrt((a[0]-g[0])**2 + (a[1]-g[1])**2)
        d3=sqrt((b[0]-g[0])**2 + (b[1]-g[1])**2)        
        
        tmp =[d1,d2,d3]
        tmp.sort()
        
        d1=(tmp[0])
        d2=(tmp[1])
        d3=(tmp[2])
        ###print(d1,d2,d3,'---',d1**2,d2**2,d3**2)
        if round(d3**2)== round(d2**2) + round(d1**2):
            ###print(round(d3**2),round(d2**2),round(d1**2))
            count+=1
                
    ###print(i,count)
    total+=count
    i+=1
print(total)
