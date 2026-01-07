###long 7130034

from itertools import product as p
t= 1

nums = [0,1,2,3,4,5,6,7,8,9]

total=0

z = list(p(nums,repeat=4))
a = [[] for i in range(0,37)]
for x in z:
  a[sum(x)].append(x)

for x in a:
  f = sum(x[0])
  tmp=0
  for i in x:
    for j in x:
      pt1 = i[0]+j[0]
      if pt1>f:
        continue
      pt2 = i[1]+j[1]
      if pt2>f:
        continue
      pt3 = i[2]+j[2]
      if pt3>f:
        continue
      pt4 = i[3]+j[3]
      if pt4>f:
        continue
      pt5 = i[0]+j[1]
      if pt5>f:
        continue
      pt6 = i[3]+j[2]
      if pt6>f:
        continue

      for k in x:
        qt1=pt1+k[0]
        if qt1>f:
          continue
        qt2=pt2+k[1]
        if qt2>f:
          continue
        qt3=pt3+k[2]
        if qt3>f:
          continue
        qt4=pt4+k[3]
        if qt4>f:
          continue
        qt5=pt5+k[2]
        if qt5>f:
          continue
        qt6=pt6+k[1]
        if qt6>f:
          continue

        n1 = f - qt1
        n2 = f - qt2
        n3 = f - qt3
        n4 = f - qt4

        if qt5+n4!=f:
          continue
        if qt6+n1!=f:
          continue
        if n1<10 and n2<10 and n3<10 and n4<10:
          tmp+=1
  ###The totals are symmetric around 18
  if f==18:
      total*=2
      total+=tmp
      break
  ###print(f,tmp)
  total+=tmp

print(total)
