###long 8319823

from euler import phi

def check(m,n):
    q = list(str(m))
    q.sort()
    r = list(str(n))
    r.sort()
    return q==r

mn =2
win = 0

for i in range(2,10**7):
    x = phi(i)
    if check(x,i)==True:
        if float(i/x)<mn:
            mn = float(i/x)
            win = i

print(win)
