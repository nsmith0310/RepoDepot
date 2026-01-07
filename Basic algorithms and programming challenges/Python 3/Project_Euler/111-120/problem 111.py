###612407567715

from sympy.utilities.iterables import multiset_permutations as m
from euler import rmtest as r
from itertools import product as p,product as per
final=[]
l = 10
i = 0
t= 0
while i <=9:
    d = [0,1,2,3,4,5,6,7,8,9]
    d.remove(i)
    j = l
    while j>=2:
        k=0
        z = list(p(d,repeat=l-j))
        tmp=[]
        for x in z:
            tmp = list(x)
            q = 1
            while q<=j:
                tmp.append(i)
                q+=1
            tmp2=m(tmp)
            
            for y in tmp2:
                e = list(map(str,y))
                b = ''.join(e)
                ###print(b)
                if len(str(int(b)))==l:
                    
                    if r(int(b),3)==True:
                        if int(b) not in final:
                            final.append(int(b))
                            k=1
                            
        if k==1:
            break
        j-=1
    i+=1

for x in final:
    if r(x,3)==True:
        t+=x
print(t)
            
        
