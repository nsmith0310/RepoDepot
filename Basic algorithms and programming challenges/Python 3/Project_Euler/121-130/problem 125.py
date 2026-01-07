###long 2906969179

from math import floor,ceil

def p(o):
    n = str(o)
    if len(n)&1==True:
        n1 = n[floor(len(n)/2):]
        n2 = n[:ceil(len(n)/2)]
        return n2[::-1]==n1
    else:
        n1 = n[int(len(n)/2):]
        n2 = n[:int(len(n)/2)]
        return n2[::-1]==n1
    


l = []
n = 1
c = 0
while n*(n+1)*(2*n+1)/6 <10**2:
    l.append(n*(n+1)*(2*n+1)/6)
    
    n+=1
t=0
f=[]
i = 1
j = 0
d = [k**2 for k in range(1,7100)]
while i<len(d):
    j = 0
    while j<i-1:
        a = sum(d[j:i])
        if p(a)==True and a<10**8:
            f.append(a)
            e = list(set(f))
            f=e
        j+=1
    i+=1
    
print(sum(list(set(e))))
