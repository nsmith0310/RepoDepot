###answer: 45228

import itertools

def sp(s):
    tmp=[]
    i = 1
    k=0
    j = i+k
    while i <=len(s):
        k = 0
        while k <=len(s):
            j = i+k
            if s[:i]!='' and s[i:j]!='' and s[j:]!='':
                t = [s[:i],s[i:j],s[j:]]
                t = list(map(int, t))
                tmp.append(t)
            k+=1
        i+=1
    return tmp

p=[]
final=[]
z = list(itertools.permutations(['1','2','3','4','5','6','7','8','9']))
for x in z:
    p.append(''.join(x))

for n in p:
    l = sp(n)
    for v in l:
        if v[2]==v[0]*v[1]:
            final.append(v[2])

final = list(dict.fromkeys(final))

print(sum(final))
