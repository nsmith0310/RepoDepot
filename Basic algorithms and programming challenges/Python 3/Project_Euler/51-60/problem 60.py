###long 26033

from euler import primes,rmtest

p = primes(10000)

mn=9999999999999999999999999999999
for x in p:
    for y in p:
        if rmtest(int(str(x)+str(y)),5)==True and rmtest(int(str(y)+str(x)),5)==True:
            for a in p:
                
                if rmtest(int(str(x)+str(a)),5)==True and rmtest(int(str(a)+str(x)),5)==True and rmtest(int(str(y)+str(a)),5)==True and rmtest(int(str(a)+str(y)),5)==True:
                    for b in p:
                        if rmtest(int(str(x)+str(b)),5)==True and rmtest(int(str(b)+str(x)),5)==True and rmtest(int(str(y)+str(b)),5)==True and rmtest(int(str(b)+str(y)),5)==True and rmtest(int(str(b)+str(a)),5)==True and rmtest(int(str(a)+str(b)),5)==True:
                            for c in p:
                                if rmtest(int(str(x)+str(c)),5)==True and rmtest(int(str(c)+str(x)),5)==True and rmtest(int(str(y)+str(c)),5)==True and rmtest(int(str(c)+str(y)),5)==True and rmtest(int(str(b)+str(c)),5)==True and rmtest(int(str(c)+str(b)),5)==True and rmtest(int(str(a)+str(c)),5)==True and rmtest(int(str(c)+str(a)),5)==True:
                                    if (a+b+c+x+y)<mn:
                                        mn = (a+b+c+x+y)
                                        
    if x>mn:
        break
    p.remove(x)
print(mn)

