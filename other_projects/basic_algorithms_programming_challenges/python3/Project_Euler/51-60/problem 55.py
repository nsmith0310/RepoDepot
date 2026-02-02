###ANSWER: 249

from math import floor, ceil
def count(n):
  h1 = str(n)
  
  i = 0
  while i < 50:
    h2 = h1[::-1]
    num = str(int(h1)+int(h2))
    
    if len(num)%2==0:
      n1=num[:(int(len(num)/2))]
      n2=num[(int(len(num)/2))+1:]
    else:
      n1 = num[:int(floor(len(num)/2))]
      n2 = num[int(ceil(len(num)/2))+1:]

    if h1==h2 and i != 0:
      break
    h1=num
    
    i+=1
  return(i)

t=0
i = 1
while i <= 10000:
  if count(i)>49:
    
    t+=1
  i+=1
print(t)




