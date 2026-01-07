###265695031399260211
###A144677 describes the increase in count with each larger triangle

from math import floor

def f(n):
    return ( (2+floor((n/3)))**3 - floor((n+4)/3) + floor((n+4)/3)**3 - floor((n+5)/3)+floor((n+5)/3)**3 - floor((n+6)/3))//6


t = 1
i = 1
k = 1
p = 3
while p<12345:
    k+=f(i)
    
    t+=k
    i+=1
    p+=1
print(t)
