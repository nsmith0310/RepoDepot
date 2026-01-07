###7587457 long
###used same method (slow) used in p159
###time can probably be improved by reducing the number of numbers factored

from euler import factorize as f,primes,rmtest
from math import ceil,log

total=0
def div(i):
    comp=[[i]]
    tmp=[[i]]
    pz = f(i)
    d = list(set(f(i)))
    final=[]
        

    
    for y in tmp:
        
        u = y[-1]
        t=[]
        for x in range(2,ceil(u/2)):
            if x<u:
                if u%x==0:
                    nums=y[:-1]
                    nums.append(x)
                    nums.append(int(u/x))
                    nums.sort()
                    
                    if nums not in comp:
                        
                        comp.append(nums)
                        tmp.append(nums)
    if pz not in comp:
        
        comp.append(pz)
    
    
    return comp

total=0
i = 2
mins=[10**9 for j in range(0,11999)]
a = [i for i in range(4,100000)]
a.sort(reverse=True)
for i in a:
    if rmtest(i,3)==False:
        w = list(div(i))
        sums=[]
        for x in w:
            if len(x)==1:
                x.append(1)
            
            sums.append(i-sum(x)+len(x))
        ###print(i,x,sums)
        for x in sums:
            if x<=12000 and x>=2:
                
                if mins[x-2]>=i:
                    mins[x-2]=i
                    
    i+=1
             
print(sum(list(set(mins))))

