###longish 1004195061

from math import floor,ceil,sqrt

pal=[]

i = 1

while i<=99999:
    a = str(i)

    n1 = a[::-1]
    pal.append(int(a+n1))

    m1 = a[:-1]
    m2 = a[-1]
    
    pal.append(int(m1+m2+m1[::-1]))
    i+=1

cubes=[]
pal.sort()
i = 1
while i**3<=9999999999:
    cubes.append(i**3)
    i+=1

f=[]
for x in pal:
    if x>0:
        c=0
        
        for y in cubes:
            if y>=x:
                break
            if (sqrt(x-y)).is_integer():
                
                c+=1
               
            if c>4:
                break
        if c==4:
            f.append(x)
    if len(f)==5:
        print(sum(f))
        break
        
