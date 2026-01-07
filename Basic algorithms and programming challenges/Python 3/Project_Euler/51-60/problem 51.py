###121313

from euler import primes,rmtest
kill=0
t = primes(10000000)
pr=[]
for x in t:
    
    pr.append(str(x))

for m in pr:
    l=[m]
    pos=[]
    for y in m:
        
        if m.count(y)>1:
            pos.append(y)
    pos=list(set(pos))
    
    
    for z in pos:
        l=[]
        i=0
        while i<=9:
            sh=(str(m))
            a = sh.replace(str(z),str(i))
            
            
            if len(str(int(a)))==len(m) and rmtest(int(a),5)==True:
                l.append(a)
            i+=1
        l=list(set(l))
        
        if len(l)==8:
            final = list(map(int,l))
            print(min(final))
            kill=1
    if kill==1:
        break
            
