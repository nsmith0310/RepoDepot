###answer: 48861552

 

from fractions import Fraction

from math import e,floor

 

def ex(n):

  return round(n/e)

 

def re(q):

  u = ex(q)

  num = q

  denom = u

  a = Fraction(num,denom)

  ###print(q, a.denominator)

  return a.denominator

 

 

 

 

def term(x):

  den = re(x)

  while den%2==0:

    den/=2

  while den%5==0:

    den/=5

  return den==1

 

 

i = 5

total=0

while i <= 10000:

  if term(i)==True:

    total-=i

  else:

    total+=i

  i+=1
