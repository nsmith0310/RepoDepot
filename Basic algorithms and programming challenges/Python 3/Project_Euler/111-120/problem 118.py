###longish 44680

from euler import primes,rmtest
from itertools import combinations, permutations

numb = ['1','2','3','4','5','6','7','8','9']

st = list(combinations(numb,8))
counter=0
mas = []

for x in st:
  y = permutations(x)
  for zs in y:
    gh = int(''.join(zs))
    if rmtest(gh,3)==True:
      mas.append(str(gh))

def pan(s):
  q = ''.join(s)
  return len(list(set(str(q)))) == len(list(str(q)))

par=[[1,1,1,2,2,2],
[1,2,2,2,2],
[1,1,1,3,3],
[3,3,3],
[1,1,1,1,4],
[1,1,1,2,4],
[1,2,2,4],
[1,1,3,4],
[1,4,4],
[1,1,1,1,5],
[1,1,1,6],
[1,1,7],
[1,8],
[2,2,2,3],
[1,1,1,1,2,3],
[1,2,3,3],
[2,3,4],
[1,1,2,2,3],
[1,3,5],
[2,2,5],
[1,1,2,5],
[1,2,6],
[3,6],
[2,7],
[4,5]]

arr2=[[] for i in range(0,8)]

for x in par:
  if sum(x)==9:
    arr2[len(x)-1].append(x)

for x in arr2:
  if x==[]:
    del arr2[arr2.index(x)]
del arr2[-1]

l = primes(10**8)

arr = [[] for i in range(0,8)]

for x in l:
    s = list(str(x))
    if len(list(set(s)))==len(s) and '0' not in s:
        arr[len(s)-1].append(str(x))

f=[]
f1=[]
for a in arr2[0]:
    if a==[1,8]:
        for c in arr[a[0]-1]:
            for d in mas:
                tmp1 = [c,d]
                
                if pan(tmp1)==True:
                    
                    z = list(map(int, tmp1))
                    z.sort()
                    t = list(map(str,z))
                    tmp3=''
                    for u in t:
                        tmp3+=u+"."
                    f1.append(tmp3)
    else:
        
        for c in arr[a[0]-1]:
          
            for d in arr[a[1]-1]:
                tmp2 = [c,d]
                if pan(tmp2)==True:
                    z = list(map(int, tmp2))
                    z.sort()
                    t = list(map(str,z))
                    tmp3=''
                    for u in t:
                        tmp3+=u+"."
                    f.append(tmp3)
        

cd = list(set(f))
f=cd

for a in arr2[1]:
    for c in arr[a[0]-1]:
        for d in arr[a[1]-1]:
            for e in arr[a[2]-1]:
                tmp = [c,d,e]
                if pan(tmp)==True:
                    z = list(map(int, tmp))
                    z.sort()
                    t = list(map(str,z))
                    tmp3=''
                    for u in t:
                        tmp3+=u+"."
                    f.append(tmp3)

cd = list(set(f))
f = cd

for a in arr2[2]:
    for c in arr[a[0]-1]:
        for d in arr[a[1]-1]:
            for e in arr[a[2]-1]:
                for g in arr[a[3]-1]:
                    tmp = [c,d,e,g]
                    if pan(tmp)==True:
                        z = list(map(int, tmp))
                        z.sort()
                        t = list(map(str,z))
                        tmp3=''
                        for u in t:
                            tmp3+=u+"."
                        f.append(tmp3)

 

cd = list(set(f))

f = cd

for a in arr2[3]:
    for c in arr[a[0]-1]:
        for d in arr[a[1]-1]:
            for e in arr[a[2]-1]:
                for g in arr[a[3]-1]:
                    for h in arr[a[4]-1]:
                        tmp = [c,d,e,g,h]
                        if pan(tmp)==True:
                            z = list(map(int, tmp))
                            z.sort()
                            t = list(map(str,z))
                            tmp3=''
                            for u in t:
                                tmp3+=u+"."
                            f.append(tmp3)

cd = list(set(f))
f = cd

for a in arr2[4]:
    for c in arr[a[0]-1]:
        for d in arr[a[1]-1]:
            for e in arr[a[2]-1]:
                for g in arr[a[3]-1]:
                    for h in arr[a[4]-1]:
                        for i in arr[a[5]-1]:
                            tmp = [c,d,e,g,h,i]
                            if pan(tmp)==True:
                                z = list(map(int, tmp))
                                z.sort()
                                t = list(map(str,z))
                                tmp3=''
                                for u in t:
                                    tmp3+=u+"."
                                f.append(tmp3)
cd = list(set(f))
f = cd
print(len(f)+len(list(set(f1))))

