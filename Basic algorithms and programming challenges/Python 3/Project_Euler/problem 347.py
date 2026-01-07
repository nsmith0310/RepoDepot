###long 11109800204052
###random suggestion cleverly suggested using string representation of list of
###prime factors as key name (massive speedup)

from euler import factorize as f
from time import time
def check(n):
    x = list(set(f(n)))
    x.sort()
    return x

data={}
t = []
i = 1
total=0

t0 = time()
count=0
while i<=10000000:
    z = check(i)
    if len(z)==2:
        data[repr(z)]=i
    i+=1

y=[]

for x in data:
      
    total+=data.get(x)
print(total, time()-t0)

