###answer:5482660 found with lim=10000
from math import sqrt

print("Lim:")
lim=int(input())
i = 1
pents=[]

while i < lim:
    pents.append(.5*i*(3*i-1))
    i+=1
    
    
i = 0
j = 0
while i < len(pents):
    j=0
    while j < len(pents):
        if  ((1 + sqrt(1 + 24*(pents[i]+pents[j])))/6).is_integer() and ((1 + sqrt(1 + 24*(abs(pents[i]-pents[j]))))/6).is_integer():
            print(abs(pents[i]-pents[j]))
            j = len(pents)
            i = len(pents)
        j+=1
    i+=1
