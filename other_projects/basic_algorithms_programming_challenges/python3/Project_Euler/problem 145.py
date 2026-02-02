###method and formula from geeksforgeeks: 608720

import numpy as np

def gg(n):
    if n == 2 or n == 4 or n == 6 or n == 8:
        return 20*pow(30,((n/2)-1))
    if n == 3 or n == 7 or n == 11:
        return 100*pow(500,((n-3)/4))
    else:
        return 0




'''
much slower version of the above
def rev(n):
    i = n
    j = str(i)[::-1]
    if len(str(i))!=len(str(int(j))):
        return False
    j = int(j)
    k = list(map(int,list(str(i+j))))
    
    if np.prod(k)&1==True:
        return True
    else:
        return False
    
'''

count=0
i = 1
while i <= 9:
    count+=gg(i)
    i+=1
print(count)

