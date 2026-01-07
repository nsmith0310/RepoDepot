###long 4037526
###A027862
from euler import rmtest as r

i = 2

c=1

while i!=-1:

    x = int(((2*i+1)**2 + 1)/2)
    if x>=5*10**15:
        break
    else:
        if r(x,5)==True:
            c+=1
    i+=1

print(c)
