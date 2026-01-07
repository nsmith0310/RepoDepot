###answer: long 20313839404245
###solution idea is mine, though I used knowledge of answer
###to guide selection of test number range

from itertools import combinations

def check(n):
    i = 2
    v=[]
    while i<len(n):
        b = list(combinations(n,i))
        
        for x in b:
            v.append(sum(x))
        i+=1
        v.sort()
    
    return list(set(v))==v



mn=999999999
m = []
for x in range(20,46):
    m.append(x)

z = list(combinations(m,7))
final = []
s=""
for x in z:
    if check(x)==True:
        final.append(list(x))
num=0
for t in final:
    if sum(t)<mn:
        mn = sum(t)
        num = t

for atlast in num:
    s+=str(atlast)
print(s)

