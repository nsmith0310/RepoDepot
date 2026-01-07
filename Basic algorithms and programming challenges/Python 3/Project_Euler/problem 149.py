###52852124
###array search algorithm from geeksforgeeks called 'Kadane's' algorithm

import numpy as np
from euler import power
def gen(n):
    t=[]
    i = 1
    while i<=55:
        t.append(((100003 - 200003*i + 300007*power(i,3))%1000000) - 500000)
        
        i+=1
    while i <=n:
        t.append((t[i-25] + t[i-56] + 1000000)%1000000 - 500000)
        
        i+=1
    return t

z = gen(4000000)
final=[]
a=np.array(z)
a.shape=((2000,2000))

totald=[]
totale=[]
diags=[]

b = np.fliplr(a)

i = 0
while i<=2000:
    diags.append((np.diag(a, k=i)))
    diags.append((np.diag(b, k=i)))
    diags.append((np.diag(a, k=-i)))
    diags.append((np.diag(b, k=-i)))
    i+=1
e=[]

for x in a:
    e.append(x)
for x in a.T:
    e.append(x)
for x in diags:
    e.append(x)


###this part was not my idea 'Kadane's algorithm'
###the basic idea seems to be to keep track of elements as possible
###members of the maximum segment where they are greater than 0
###every time the tracker goes above 0, set the running maximum to
###that number. Besides that, max_so_far pulls values from max_ending_here
###my final addition involves tracking the maximums between total segments

top=0
for x in e:
    max_so_far = 0
    max_ending_here = 0
    for y in x:
        max_ending_here +=y
        if max_ending_here<0:
            max_ending_here=0
        if max_so_far<max_ending_here:
            max_so_far=max_ending_here
    if max_so_far>top:
        top=max_so_far
print(top)


