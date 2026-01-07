###answer: 34029210557338
from euler import factorize, primes


###the insight that no primes in the triangle will exceed the number 51 is not
###mine: I did come up with the triangle generator
def check(n):
    b = primes(52)
    for x in b:
        if n%x**2==0:
            return False
    return True
tri = [[1],[1,1],[1,2,1]]


i = 2
j = 1
while i <=49:
    j=1
    temp=[]
    while j < len(tri[i]): 
        temp.append(tri[i][j-1]+tri[i][j])
        j+=1
    temp.insert(0,1)
    temp.append(1)
    tri.append(temp)
    i+=1


total=0
m = [item for sublist in tri for item in sublist]
m = list(set(m))
m.sort()

for z in m:
    if check(z)==True:
        total+=z
print(total)
    

