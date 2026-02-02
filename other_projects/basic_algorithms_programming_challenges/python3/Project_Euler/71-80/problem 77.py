###answer: 71

from euler import primes

def ways(n):
  l=[]
  l.append(1)
  i = 0
  while i <=n-1:
    l.append(0)
    i+=1


  coins=primes(n)

  for x in coins:
    for i in range (0,((n+1)-x),1):
      l[x+i] += l[i]

  return (l[len(l)-1])


i = 1
while i!=-1:
  if ways(i)>5000:
    print(i)
    break
  i+=1
