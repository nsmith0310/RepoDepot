###long 1096883702440585

###good god this problem spiralledout of control

###drew from basically everywhere I  could find except for s braumme

 

 

def primes(n):

    """ Returns  a list of primes < n """

    sieve = [True] * n

    for i in range(3,int(n**0.5)+1,2):

        if sieve[i]:

            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)

    return [2] + [i for i in range(3,n,2) if sieve[i]]

def prod(n):

  t =1

  for x in n:

    t*=x

  return t

def m_prod(n,m):

  t = 1

  for x in n:

    t*=x%m

  return t

from itertools import combinations as c, chain

def pset(l):

    xs = list(l)

    return chain.from_iterable(c(xs,n) for n in range(len(xs)+1))

#############################################################################

mod = 10**16

 

nums = primes(190)

 

 

lim = int((prod(nums))**.5)

h = len(nums)//2

 

###main problem was that the binary search lists were split incorrectly

###originally, I split the final list in half, rather than half 1 consisting of the products

###of the first 21 primes and the second of the last 21 primes (correct split)

n1 = pset(nums[:h])

n2 = pset(nums[h:])

 

t1 = []

t2= []

for x in n1:

    k = prod(x)

    if k<=lim:

        t1.append(k)

 

for x in n2:

    k = prod(x)

    if k<=lim:

        t2.append(k)

 

t1.sort()

t2.sort()

 

 

def search(n2,lim, s,e,x):

  if s==e:

    if x*n2[s]<=lim:

      return x*n2[s-1]

    else:

      return 0

  mid = int(s + (e-s)//2)

 

  if lim < x*n2[mid-1]:

    return search(n2, lim, s, mid, x)

  ret = search(n2, lim, mid+1,e,x)

  if ret==0:

    return x*n2[mid-1]

  else:

    return ret

 

  

 

f=[]

top =0

mx=0

###uses a binary search to narrow down segments of the list to check

count = 0

for x in t1:

  l = 0

  u = len(t2)-1

  while l<=u:

    m = (l+u)//2

    if x*t2[m]<lim:

      l=m+1

    else:

      u=m-1

  mx = x*t2[u]

  if mx>top and mx<=lim:

    top=mx

print(top%mod)
