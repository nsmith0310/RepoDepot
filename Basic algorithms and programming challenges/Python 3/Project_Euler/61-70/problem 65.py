###ANSWER: 272 

from math import floor, e
from decimal import *
getcontext().prec=6
i = 0
tmp=[]
tmp.append(2)
tmp.append(1)
z = e
j = 1
x=0
while i<=100:
   x = x+ 2
   tmp.append(x)
   tmp.append(1)
   tmp.append(1)
   i+=1
nums=[]
print(tmp)

nums.append(1)
nums.append(2)
last=[]
i = 2
while i <= 200:
   final=[]
   nums.append(tmp[i-1]*nums[i-1] + nums[i-2])


   
   final = list(str(nums[i-1]))
   final = list(map(int, final))
   last.append(sum(final))
      
   i+=1

print(last[99])
