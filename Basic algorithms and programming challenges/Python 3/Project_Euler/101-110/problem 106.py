###long 21384
###significant conceptual help from s braumme

from itertools import combinations as c

f=[]

l = [1,2,3,4,5,6,7,8,9,10,11,12]
m=[]
i = len(l)-1
count=0
while i >=1:
    k = list(c(l,i))
    for x in k:
        m.append(x)
    i-=1

g = list(c(m,2))
n=[]
for x in g:
    t1=[]
    t2=[]
    for y in x[0]:
        t1.append(y)
    for y in x[1]:
        t2.append(y)
    n.append([t1,t2])
count=0


for y in n:
    tmp=[]
    for x in y:
        for z in x:
            tmp.append(z)
    if len(list(set(tmp)))==len(tmp):
        if len(y[1])==len(y[0]):
            f.append(y)
    
count=0

for x in f:
    mc = 0
    for a in x[0]:
        if a> x[1][x[0].index(a)]:
           
            count+=1
            break
print(count)
