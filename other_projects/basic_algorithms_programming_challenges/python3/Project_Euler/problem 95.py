###long 14316
import itertools
flatten_iter = itertools.chain.from_iterable

def f(n):
    l= list(set(flatten_iter((i, n//i) 
                for i in range(1, int(n**0.5)+1) if n % i == 0)))
    if n in l:
        
        l.remove(n)
    l.sort()
    return (l)

def sumdiv(n):
    x = f(n)
    return sum(x)

def chain(n):
    p = sumdiv(n)
    t=[n]
    while 1 !=2:
        if p not in t:
            t.append(p)
            if p>1000000:
                break
            p = sumdiv(p)
        elif sumdiv(t[len(t)-1])==n: 
            return len(t)
        else:
            return 0
           
def chain2(n):
    p = sumdiv(n)
    t=[n]
    while 1 !=2:
        if p not in t:
            t.append(p)
            if p>1000000:
                break
            p = sumdiv(p)
        else:
            break
    return min(t)

mx = 0
longest=0
for i in range(100,1000001):
        l = chain(i)
        if l != None and l>mx:
            mx=l
            longest=i

print(chain2(longest))
