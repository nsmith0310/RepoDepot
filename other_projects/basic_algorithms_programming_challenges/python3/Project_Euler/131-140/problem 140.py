###5673835352990
###https://oeis.org/A228210 and lots of help from mathexchange

from math import sqrt
f = [7,8,13,17]

while len(f)<=100:
    f.append(3*f[-2]-f[-4])
    

t=0
c=0
i = 1
while i<=60:
    a = f[i]
    if ((a-7)/5).is_integer():
        
        t+=((a-7)/5)
    i+=1
print(int(t))
