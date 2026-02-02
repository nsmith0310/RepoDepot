###answer: long 55374
def pent(j):
    l = []
    i = 1
    while i <= j:
        l.append(i)
        l.append(-i)
        i+=1
    n = []
    for x in l:
        if (j - x*(3*x-1)/2)>=0:
            n.append(int(j - x*(3*x-1)/2))
    n = list(map(int, n))
    return n

tmp = [1,1,2,3]
i = 4
while i <=100000000000:
    t = pent(i)
    total=0
    spl = [t[x:x+2] for x in range(0, len(t),2)]
    
    
    for x in spl:
        if (spl.index((x))+2)%2==0:
            for y in x:
                total+=tmp[y]
        else:
            for y in x:
                total-=tmp[y]
    if total%1000000==0:
        print(i)
        break
    tmp.append(total)
    i+=1
    
