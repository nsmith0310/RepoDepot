###Answer: long 17427258
from euler import factorize

def check(n):
    t = factorize(n)
    if len(t)==2:
        return True
    else:
        return False

i = 1
count=0
for i in range(1,pow(10,8),1):
    if check(i)==True:
        count+=1

print(count)
    
