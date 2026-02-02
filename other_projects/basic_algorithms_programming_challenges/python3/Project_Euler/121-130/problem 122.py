###longish 1582
###A lot of help from S braumme
###my attempt was much faster, but unfortunately the result was very slightly
###off due to storage of list values which were successful (this usually worked,
###but several values required lists which my algorithm discarded)

from math import log, floor

def u(n):
    return (9/log(71,2))*log(n,2)


i = 3
t = 1
while i<=200:
    l = [[1,2]]
    for x in l:
        kill=0
        for y in x:
            if x[-1]+y==i:
                t+=len(x)
                ###print(i,len(x))
                
                kill=1
            else:
                tmp = [j for j in x]
                tmp.append(x[-1]+y)
                l.append(tmp)
        if kill==1:
            break
    i+=1
print(t)
