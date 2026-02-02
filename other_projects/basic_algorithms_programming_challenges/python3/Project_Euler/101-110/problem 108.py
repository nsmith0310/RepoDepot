###answer: 180180
from euler import pfactorize as p,factorize as f,power
from euler import tau as t
i = 1

while i!=-1:
    x = (len(p((i*1260)**2))+2)/2
    if x>1000:
        print(i*1260)
        break
    i+=1


'''
while i!=-1:
    x = ((t(i**2))+2)/2
    if x>1000:
        print(i)
        break
    i+=1
'''


