###longish 38182

from itertools import product as p

def par(s):
    if s[0]=='s': return 1*int(s[1:])
    if s[0]=='d': return 2*int(s[1:])
    if s[0]=='t': return 3*int(s[1:])
    


pos = []

for i in range(1,21):
    pos.append("s"+str(i))
    pos.append("d"+str(i))
    pos.append("t"+str(i))

pos.append("s"+"25")
pos.append("d"+"25")


k = p(pos,repeat = 3)

pos2=[]
for x in k:
    if x[2][0]=="d":
        t = 0
        for y in x:
            t+=par(y)
    
        if t<100:
            pos2.append(x)


arr = [[] for j in range(1,22)]

for x in pos2:
    if x[2][1:]!="25":
        arr[int(x[2][1:])-1].append(x)
        
    else:
        arr[-1].append(x)
    
    
for x in arr:
    for y in x:
        for z in x:
            if y!=z:
                n1 = [y[0],y[1]]
                if n1 == [z[1],z[0]]:
                    del arr[arr.index(x)][x.index(z)]

for x in arr:
    for z in x:
        t = 0
        for y in z:
            t+=par(y)
        if t==6:
            print(z)

###############################################################

l = p(pos,repeat = 2)

pos3=[]
for x in l:
    if x[1][0]=="d":
        t = 0
        for y in x:
            t+=par(y)
    
        if t<100:
            pos3.append(x)


arr2 = [[] for j in range(1,22)]

for x in pos3:
    if x[1][1:]!="25":
        arr2[int(x[1][1:])-1].append(x)
        
    else:
        arr2[-1].append(x)
    
for x in arr2:
    for z in x:
        t = 0
        for y in z:
            t+=par(y)
        if t==6:
            print(z)
         

t2 = 0
for x in arr:
    t2+=len(x)
for x in arr2:
    t2+=len(x)
print(t2+21)


            

