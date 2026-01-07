###4989

###some help from a blog about this problem and the lower limit on j, as well as the list append method for counting

from math import ceil,floor

a = [0 for i in range(1,10**6 + 1)]

i = 1
j = 1

while i<=10**6:
    j = floor(i/3 + 1)
    while j<=10**6:
        z = (3*j - i)*(i+j)
        ###print(z)
        if z<10**6:
            a[z-1]+=1
        else:
            break
        j+=1
    i+=1

t = 0

for x in a:
    if x==10:
        t+=1
print(t)
