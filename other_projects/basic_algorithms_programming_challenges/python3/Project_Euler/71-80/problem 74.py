###answer: longish 402

from math import factorial

def chain(n):
  count = 0
  tmp=[]
  tmp.append(n)
  m = list(map(int,(list(str(n)))))
  while count<=60:
    t = 0
    for x in m:
      t+=factorial(x)
    tmp.append(t)
    m = list(map(int, list(str(t))))
    if len(tmp)!=len(set(tmp)):
      return count+1
      break
    count+=1
  return count

i = 1
count = 0
while i < 1000000:
  if chain(i)==60:
    count+=1
  i+=1
print(count)
