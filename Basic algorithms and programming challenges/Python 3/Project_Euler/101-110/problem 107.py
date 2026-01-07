###259679
###most of the work was done by scipy

from scipy.sparse import csr_matrix,find
from scipy.sparse.csgraph import minimum_spanning_tree

l = [line.rstrip('\n') for line in open("network.txt")]

mat=[]

for line in l:

  mat.append(line.split(","))

m2=[]
for x in l:
    
    tmp=x.split(",")
    tmp2=[]
    for y in tmp:
        if y=='-':
            tmp2.append(0)
        else:
            tmp2.append(int(y))
    m2.append(tmp2)
init=0

toadd=[]
for x in m2:
    toadd.append([int(k) for k in x])

i = 0
while i<len(toadd):
    j = 0
    while j<len(toadd[i]):
        init+=toadd[i][j]
        toadd[j][i]=0
        j+=1
    i+=1

z = csr_matrix(m2)

tz = minimum_spanning_tree(z)

tz.toarray().astype(int)
final=[]
tz.toarray()
for x in tz:
    k = str(x)
    final.append(k.split())

f2=0
for x in final:
    if x!=[]:
        for z in x:
            if '.' in z:
                f2+=float(z)
    
print(int(init-f2))
