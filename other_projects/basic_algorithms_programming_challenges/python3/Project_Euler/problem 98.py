###long 18769

from itertools import combinations as c,permutations as p1
from math import sqrt

with open("words.txt", "r") as ins:
   for line in ins:
     items = line.split(",")

t=[]
for x in items:
    t.append(x.strip('"'))

def check(x,y):
    x=list(x)
    x.sort()
    y=list(y)
    y.sort()
    return x==y

def check2(x,y):
    u = list(str(x))
    v = list(str(y))
    u.sort()
    v.sort()
    return u==v
    
z=[]
for x in t:
    for y in t:
        if x!=y and check(x,y)==True:
            
            z.append([x,y])
            
ass=[]
for x in z:
    p = list(set(x[0]))
    pos = []
    for y in p:
        g = [y]
        i = 0
    
        while i<=9:
            g.append(i)
            i+=1
        pos.append(g)
    ass.append(pos)
    
mx=0
        
for x in z:
    gh = c(['0','1','2','3','4','5','6','7','8','9'],len(x[0]))
    for ty in gh:
        b = p1(ty)
        for y in b:
            word1=x[0]
            word2=x[1]
            tmp=[]
            for a in y:
                tmp.append([word1[y.index(a)],a])
                word1 = word1.replace(word1[y.index(a)],a)
        
            for a in tmp:
                if a[0] in word2:
                    word2 = word2.replace(word2[word2.index(a[0])],a[1])
            
            if word1[0]!='0' and word2[0]!='0':
                e1 = int(word1)
                e2= int(word2)
          
                if (sqrt(e1)).is_integer() and (sqrt(e2)).is_integer():
                    if max(e1,e2)>mx:
                        mx=max(e1,e2)
                        for we in z:
                            if len(we[0])<len(str(mx)) and we!=x:
                                z.remove(we)
                        
print(mx)
