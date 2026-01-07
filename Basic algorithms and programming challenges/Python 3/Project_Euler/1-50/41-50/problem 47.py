###Answer: 134043

from euler import factorize

def strip(n):
    return list(set(factorize(n)))

def test(n,b):
    if len(strip(n+1))==4 and len(strip(n+2))==4 and len(strip(n+3))==4:
        return True
    t = 0
    i = 1
    while i<=b:
        if not len(strip(n+t))==b:
            return False
        t+=1
        i+=1
    return True

print("Consecutives:")
b = int(input())

i = 1
tmp=[]
while i!=-1:
    if len(strip(i))==b:
        if test(i,b)==True:
            print(i)
            break
    
    i+=1

'''
from euler import factorize

def strip(n):
    return list(set(factorize(n)))

def test(n):
    if len(strip(n+1))==4 and len(strip(n+2))==4 and len(strip(n+3))==4:
        return True

i = 1
tmp=[]
while i!=-1:
    if len(strip(i))==4:
        if test(i)==True:
            print(i)
            break
    
    i+=1
'''
