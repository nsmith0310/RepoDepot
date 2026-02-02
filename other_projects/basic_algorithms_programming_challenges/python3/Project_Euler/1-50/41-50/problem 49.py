###answer: 296962999629

from euler import primes
from itertools import permutations, combinations
sub_p=[]
p = primes(10000)
for x in p:
    if len(str(x))==4:
        sub_p.append(x)
final=[]


def perms(n):
    a = []
    k = list(permutations(list(str(n))))
    for y in k:
        a.append(int(''.join(y)))
    a.sort()
    return a

def ch(a):
    b = []
    for z in perms(a):
        if pow(2,z-1)%z==1:
            b.append(z)
    return b

def diff(a,b,c):
    if abs(a-b) == abs(b-c):
        return True
    else:
        return False

def ch2(n):
    k = ch(n)
    if len(k)>=3:
        t = list(combinations(k,3))
        for o in t:
            
            if o[0]<o[1] and o[1]<o[2] and len(str(o[0]))==4 and len(str(o[1]))==4 and len(str(o[2]))==4:
                if (o[0]-o[1])==(o[1]-o[2]):
                    s0 =str(o[0])
                    s1 =str(o[1])
                    s2 =str(o[2])
                    return(s0+s1+s2)
    

tmp=[]
for t in sub_p:
    tmp.append(ch2(t))
    
tmp = list(dict.fromkeys(tmp))
print(tmp)
                


        


