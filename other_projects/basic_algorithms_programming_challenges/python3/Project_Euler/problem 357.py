###long 1739023853137

from euler import pfactorize as p, rmtest as r

def div(n):
    x=p(n)
    x.append(n)
    return x

def check(n):
    c = div(n)
    for x in c:
        t = int(x+(n/x))
        if r(t,5)==False:
            return False
    return True
count=0
total=0
for i in range(1,100000001,2):
    if check(i)==True:
        total+=i
    
print(total+2)
        
