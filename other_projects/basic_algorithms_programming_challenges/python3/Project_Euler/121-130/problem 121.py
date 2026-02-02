###2269
import itertools
from math import factorial,floor


def conv(n):
  return [n[1]-1,n[1]]


s=[[1,2],[1,3],[1,4],[1,5],[1,6],[1,7],[1,8],[1,9],[1,10],[1,11],[1,12],[1,13],[1,14],[1,15],[1,16]]
total1 = 0
total2 = 0
k = 8
while k <=15:
  t = list(itertools.combinations(s,k))

  p  = [list(elem) for elem in t]
  
  for x in p:
    for y in s:
      if y not in x:
        i = conv(y)
        x.append(i)

  for l in p:
    ###print(l)
    tmp = 1
    tmp2 = 1
    for m in l:
      tmp*=(m[0])
      tmp2*=(m[1])
    total1 +=tmp
    total2 +=tmp2
  k+=1
print(floor(factorial(16)/total1))



'''
open version
###2269
import itertools
from math import factorial,floor,ceil

print("Number of rounds: ")
rounds=int(input())
def conv(n):
  return [n[1]-1,n[1]]


s=[]
for d in range(2,rounds+2):
  s.append([1,d])


total1 = 0
total2 = 0
if rounds&1==True:
  k = ceil(rounds/2)
else:
  k = int((rounds/2)+1)
while k <=rounds:
  t = list(itertools.combinations(s,k))

  p  = [list(elem) for elem in t]
  
  for x in p:
    for y in s:
      if y not in x:
        i = conv(y)
        x.append(i)

  for l in p:
    ###print(l)
    tmp = 1
    tmp2 = 1
    for m in l:
      tmp*=(m[0])
      tmp2*=(m[1])
    total1 +=tmp
    total2 +=tmp2
  k+=1
print((floor(factorial(rounds+1)/total1)))
'''
