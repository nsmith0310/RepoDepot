###long 1918080160
###potential speedup involves checking in increments, rather than twice

from itertools import product

t = product(['a','o','l'],repeat=10)
count=0

q=[]
for x in t:
    y = ''.join(x)
    c1=0
    c2=0
    if y.count('l')>1:
        c1=1
        
    i = 3

    while i<=len(y):
        s=""
        h=1
        while h<=i:
            s+="a"
            h+=1
        if y.count(s)>0:
            c2=1
        i+=1
    if c1==0 and c2==0:
        q.append(y)
        

ab=[]
i = 3
while i<=20:
    t = 1
    s=""
    while t<=i:
        s+="a"
        t+=1
    ab.append(s)
    i+=1


tw=[]
for x in q:
    for y in q:
        s=x+y
        
        c1=0
        c2=0
        if s.count('l')>1:
            c1=1
        
        for g in ab:
            if s.count(g)>0:
                c2=1
                continue
            
        if c1==0 and c2==0:
            tw.append(s)
        

ab=[]
i = 3
while i<=30:
    t = 1
    s=""
    while t<=i:
        s+="a"
        t+=1
    ab.append(s)
    i+=1


count=0
for x in tw:
    for y in q:
        s=x+y
        
        c1=0
        c2=0
        if s.count('l')>1:
            c1=1
        
        for g in ab:
            if s.count(g)>0:
                c2=1
                continue
            
        if c1==0 and c2==0:
            count+=1
print(count)

