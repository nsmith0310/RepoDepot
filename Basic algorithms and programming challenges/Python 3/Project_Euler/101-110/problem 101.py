###37076114526

from euler import power as p
import numpy as np
total=0
def poly(x):
    return 1-x+p(x,2)-p(x,3)+p(x,4)-p(x,5)+p(x,6)-p(x,7)+p(x,8)-p(x,9)+p(x,10)

l = [poly(i) for i in range(1,11)]

x = [1,2,3,4,5,6,7,8,9,10]
y = [poly(i) for i in range(1,11)]

i = 0
while i<=len(x)-1:
    
    rded=[]
    val = np.array(x[:i+1],dtype='float64')
    yval = np.array(y[:i+1],dtype='float64')
    g = np.array((np.polyfit(val,yval,i)))[::-1]
    for e in g:
        rded.append(round(e))
    l = i+2
    largest=i-1
    tmp = rded[0]
     
    j = 1
    while j<len(rded):
        tmp+=rded[j]*p(l,j)
        j+=1
    
    
    total+=tmp
    i+=1
print(int(total))
