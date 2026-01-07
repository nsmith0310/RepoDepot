###long 44043947822
###can be sped up primarily in the section which backtracks and
###reduces the list size until it shoots past the target regressively
###A020522 and A002378
b=1
t = [2,12]
g=[]
d=[]
while len(t)<=200:
    t.append(6*t[-1]-8*t[-2])
    while b*(b+1)<=t[-1]:
        g.append(b*(b+1))
        b+=1
    print(len(t),len(g))
    ###here
    if (len(t))/(len(g)) < 1/12345:
        while len(g)>1:
            t.remove(t[-1])
            while g[-1]!=t[-1]:
                if (len(t))/(len(g)) < 1/12345:
                    d.append(g[-1])
                    
                g.remove(g[-1])
        break
print(d[-1])
