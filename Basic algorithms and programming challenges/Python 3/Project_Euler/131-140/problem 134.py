###long 18613426663617118

from euler import primes

def ch(n,m):
    t = str(n)
    if t[::-1][:len(str(m))][::-1]==str(m):
        return True

p = primes(1000004)
p.remove(2)
p.remove(3)
p.sort()
tmp=[]
i = 0
while i < len(p)-1:
    j=1
    while j !=-1:
        t = j*p[i+1]
        if ch(t,p[i])==True:
            ###print(j,t,p[i+1],p[i])
            tmp.append(t)
            break
        j+=2
    
    i+=1
    
print(sum(tmp))

