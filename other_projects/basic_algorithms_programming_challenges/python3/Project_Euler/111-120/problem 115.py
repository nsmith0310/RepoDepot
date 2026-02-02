###168

###https://oeis.org/A005251/a005251_1.pdf

 

from math import factorial as f,floor

 

def b(n,k):

    return f(n)/(f(n-k)*f(k))

   

nums=[]

 

n = 0

 

while n<=1000:

    u=[]

    t = [i for i in range(0,floor(n/51)+1)]

    for x in t:

        u.append(b(n-49*x,2*x))

    nums.append(sum(u))

    n+=1

   

for x in nums:

    if x>10**6:

        print(nums.index(x)-1)

        break
