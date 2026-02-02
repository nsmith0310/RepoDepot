###longish 2544559
from math import ceil,floor

a = [0 for i in range(1,5*10**7 + 1)]

i = 1
j = 1

while i<=5*10**7:
    j = floor(i/3 + 1)
    while j<=5*10**7:
        z = (3*j - i)*(i+j)
        ###print(z)
        if z<5*10**7:
            a[z-1]+=1
        else:
            break
        j+=1
    i+=1

t = 0

for x in a:
    if x==1:
        t+=1
print(t)
