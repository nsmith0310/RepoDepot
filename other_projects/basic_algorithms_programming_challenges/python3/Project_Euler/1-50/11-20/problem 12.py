###answer 76576500

from euler import tau

i=1
j=1
k=0
tri=0

while i!=0:
    k=0
    j=1
    tri=(i*(i+1))/2
    num = tau(tri)
    if num > 500:
        print(tri)
        break
    i+=1















