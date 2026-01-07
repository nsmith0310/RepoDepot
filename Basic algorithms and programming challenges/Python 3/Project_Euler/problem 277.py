###1125977393124310
###I took about half of the sequence, and found the two numbers after 10^15 which
###could have been possible, took their difference (the increment value of n:
###129140163) and began hunting from the first discovered number using the half sequence,
###1000000001856343

from decimal import *

getcontext().prec = 30


def f(n):
  s = "UDDDUdddDDUDDddDdDddDDUDDdUUDd"
  
  i = 0
  while i<len(s):
    
    if s[i]=="U":
      n = (4*n + 2)/3
    elif s[i]=="D":
      n/=3
    else:
      n = (2*n - 1)/3
    if not n.is_integer():
      return 0
    i+=1
  return n


n = 1000000001856343
while 1!=-1:
  if f(n)!=0:
    print(n)
    break
  n+=129140163

