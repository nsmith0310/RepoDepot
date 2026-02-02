###long 476001479068717
###alot of help from OEIS and mainly by a paper by C Ashbacher
from euler import power,rmtest as r,factorize as f
from math import factorial 



def prod(n):
    t = 1
    for x in n:
        t*=x
    return t

def f2(m,p):
    s = 0
    while m//p!=0:
        s+=m//p
        m=m//p
    return s
    
def le(n,m,p):
    if m<p:
        return m*p
    else:
        st = 1
        while st*p<=n:
            ins = f2(st,p)
            if ins>=m:
                return st            
            st+=1

def el(num):
    m = f(num)
    d = list(set(m))
    totest=[]
    for x in d:
        totest.append(pow(x,m.count(x)))

    final=[]
    ###print(totest)
    for x in totest:
        if len(d)==1 and num <=len(m):
            final.append(n[0]*num)
        elif len(d)==1 and num >len(m):
            final.append(le(num,len(m),d[0]))
        else:
            final.append(primary(x))
        
    return max(final)

total=0

num = 2
def primary(num):
    total=0
    v = f(num)
    v.sort()
    b = list(set(v))
    b.sort()
    if len(v)==1:
        return num

    elif len(b)==len(v):
        return max(b)
        
    elif num**.5 in b:
        return 2*num**.5
    elif prod(b[:-1])*max(b)==num and max(b[:-1])<max(b):
        return max(b)
    else:
        return el(num)
        
i = 2
while i<=100000000:
    total+=primary(i)
    ###print(i,primary(i))
    i+=1
    
print(int(total))


















