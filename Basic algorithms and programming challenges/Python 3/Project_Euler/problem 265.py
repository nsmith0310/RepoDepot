###long 209110240768

from itertools import product

def conv(n):
  s = (''.join(n))
  
  return int(s,2)

x = (product(['0','1'],repeat=27))


a=[]
for i in x:
  if i.count('1')==16:
    a.append(i)

trial=[]

for x in a:
  no=0
  nums=[]
  i = 0
  while i<len(x)-4:
    t = x[i:i+5]
    if t not in nums:
      nums.append(t)
    else:
      no = 1
      break
    i+=1
  if no == 0:
    trial.append(x)

tmp = []

for x in trial:
  nums = ['0','0','0','0','0']
  for y in x:
    nums.append(y)
  tmp.append(nums)

final = []

for x in tmp:
  no=0
  nums=[]
  i = 0
  while i<len(x)-4:
    t = x[i:i+5]
    if t not in nums:
      nums.append(t)
    else:
      no = 1
      break
    i+=1
  if no == 0:
    final.append(x)

total = 0

for x in final:
  total +=conv(x)

print(total)
