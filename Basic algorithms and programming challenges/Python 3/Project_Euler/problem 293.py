###2209 I have no words for this problem
###issues:
###finding the highest possible power of each of the numbers in each of the sets of consecutive primes
###finding a way of iterating through them: I resorted to a manual approach (wont work for cases higher than 10^9)

from euler import primes, power, factorize,rmtest as r
from itertools import product as p
from math import floor

lim = 10**9

def multiply(n):
    t = 1
    for x in n:
        t*=x
    return t

def getnum(a,b):
    n = 1
    for x in a:
        n*=pow(x,b[a.index(x)])
    return n

prime = primes(100)
i = 0
t=[]
while i!=-1:
    b = multiply(prime[:i])
    
    if b>=lim:
        t = prime[:i]
        break
    i+=1
    
dis=[]
i = 1
fort=[]
while i<=len(t):
    pos = t[:i]
    dis.append(pos)
    
    i+=1

i=1
while pow(2,i)<=lim:
    fort.append(pow(2,i))
    
    i+=1

a = 1
while a<=23:
    b = 1
    while b<=19:
        if pow(2,a)*pow(3,b)<=lim:
            fort.append(pow(2,a)*pow(3,b))
        ###print(power(2,a)*power(3,b),a,b)
        b+=1
    a+=1

a=1
while a<=23:
    b = 1
    while b<=17:
        c=1
        while c<=13:
            if pow(2,a)*pow(3,b)*pow(5,c)<=lim:
                fort.append(pow(2,a)*pow(3,b)*pow(5,c))
            c+=1
        b+=1
    a+=1

a = 1
while a<=21:
    b=1
    while b<=11:
        c = 1
        while c<=16:
            d = 1
            while d<=11:
                if pow(2,a)*pow(3,b)*pow(5,c)*pow(7,d)<=lim:
                    fort.append(pow(2,a)*pow(3,b)*pow(5,c)*pow(7,d))
                d+=1
            c+=1
        b+=1
    a+=1

a = 1
while a<=19:
    b=1
    while b<=15:
        c = 1
        while c<=13:
            d = 1
            while d<=11:
                e=1
                while e<=11:
                    if pow(2,a)*pow(3,b)*pow(5,c)*pow(7,d)*pow(11,e)<=lim:
                        fort.append(pow(2,a)*pow(3,b)*pow(5,c)*pow(7,d)*pow(11,e))
                    e+=1
                d+=1
            c+=1
        b+=1
    a+=1
###F
a = 1
while a<=17:
    b=1
    while b<=13:
        c = 1
        while c<=11:
            d = 1
            while d<=11:
                e=1
                while e<=9:
                    f = 1
                    while f<=9:
                        if pow(2,a)*pow(3,b)*pow(5,c)*pow(7,d)*pow(11,e)*pow(13,f)<=lim:
                            fort.append(pow(2,a)*pow(3,b)*pow(5,c)*pow(7,d)*pow(11,e)*pow(13,f))
                        f+=1
                    e+=1
                d+=1
            c+=1
        b+=1
    a+=1

a = 1
while a<=12:
    b=1
    while b<=10:
        c = 1
        while c<=8:
            d = 1
            while d<=8:
                e=1
                while e<=8:
                    f = 1
                    while f<=7:
                        g=1
                        while g<=7:
                            if pow(2,a)*pow(3,b)*pow(5,c)*pow(7,d)*pow(11,e)*pow(13,f)*pow(17,g)<=lim:
                                fort.append(pow(2,a)*pow(3,b)*pow(5,c)*pow(7,d)*pow(11,e)*pow(13,f)*pow(17,g))
                            g+=1
                        f+=1
                    e+=1
                d+=1
            c+=1
        b+=1
    a+=1

a = 1
while a<=10:
    b=1
    while b<=8:
        c = 1
        while c<=7:
            d = 1
            while d<=7:
                e=1
                while e<=6:
                    f = 1
                    while f<=6:
                        g=1
                        while g<=6:
                            h = 1
                            while h<=6:
                                if pow(2,a)*pow(3,b)*pow(5,c)*pow(7,d)*pow(11,e)*pow(13,f)*pow(17,g)*pow(19,h)<=lim:
                                    fort.append(pow(2,a)*pow(3,b)*pow(5,c)*pow(7,d)*pow(11,e)*pow(13,f)*pow(17,g)*pow(19,h))
                                h+=1
                            g+=1
                        f+=1
                    e+=1
                d+=1
            c+=1
        b+=1
    a+=1

a = 1
while a<=6:
    b=1
    while b<=5:
        c = 1
        while c<=4:
            d = 1
            while d<=4:
                e=1
                while e<=4:
                    f = 1
                    while f<=4:
                        g=1
                        while g<=4:
                            h = 1
                            while h<=4:
                                i=1
                                while i<=4:
                                    if pow(2,a)*pow(3,b)*pow(5,c)*pow(7,d)*pow(11,e)*pow(13,f)*pow(17,g)*pow(19,h)*pow(23,i)<=lim:
                                        fort.append(pow(2,a)*pow(3,b)*pow(5,c)*pow(7,d)*pow(11,e)*pow(13,f)*pow(17,g)*pow(19,h)*pow(23,i))
                                    i+=1
                                h+=1
                            g+=1
                        f+=1
                    e+=1
                d+=1
            c+=1
        b+=1
    a+=1


    
totals=[]
admissable=list(set(fort))





for x in admissable:
    if x>=lim:
        admissable.remove(x)
for x in admissable:
    l = x+1
    i=1
    while r(l+i,3)==False:
        i+=1
    totals.append((l+i)-x)

print(sum(list(set(totals))))




