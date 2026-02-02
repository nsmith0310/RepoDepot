###problem 123 (slow): 21035 (R)

def primes(high):

  numbers = set(range(high, 1, -1))

  primes = []

  while numbers:

    p = numbers.pop()

    primes.append(p)

    numbers.difference_update(set(range(p*2, high+1, p)))

  return primes

 

print("L:")

high=int(input())

 

p = primes(high)

p.sort()

 

m = pow(10,11)

tmp=[]

i = 0

while i < len(p):

  x = (pow(p[i]-1,i+1)+pow(p[i]+1,i+1))%((p[i])**2)

  if x > 10**10:

    if x < m:

        m = i+1

   

  i+=1

 

print(m)
