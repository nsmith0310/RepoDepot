###long 1111981904675169
###slight help from S Braumme in coming up with the method for the eight
###special cases
###lots of help from OEIS for determining the length of the target products
###in the eight cases in the thousands
###program tries one brute force method which if exceeding 5 mins will try
###the alternative method for the special cases

###because uses timer, not gauranteed to work on all machines: ie, a slower
###processor will still keep time like a faster one, but will may trigger the
###second brute force search only meant for certain numbers

from itertools import product as p
from time import time

###uses a search throguh the end products where the basic search exceeds 4 mins

big4=p(['1','0','2'],repeat=13)
big3=p(['1','0','2'],repeat=14)
big=p(['1','0','2'],repeat=15)
big2=p(['1','0','2'],repeat=16)
big5=p(['1','0','2'],repeat=12)
big6=p(['1','0','2'],repeat=11)
big7=p(['1','0','2'],repeat=10)
mass=[]
for x in big:
    c = ''.join(x)
    if len(str(int(c)))==15:
        mass.append(int(c))
for x in big2:
    c = ''.join(x)
    if len(str(int(c)))==16:
        mass.append(int(c))
for x in big3:
    c = ''.join(x)
    if len(str(int(c)))==14:
        mass.append(int(c))
for x in big4:
    c = ''.join(x)
    if len(str(int(c)))==13:
        mass.append(int(c))
for x in big5:
    c = ''.join(x)
    if len(str(int(c)))==12:
        mass.append(int(c))
for x in big6:
    c = ''.join(x)
    if len(str(int(c)))==11:
        mass.append(int(c))
for x in big7:
    c = ''.join(x)
    if len(str(int(c)))==10:
        mass.append(int(c))

s = list(set(mass))
s.sort()

def check(n):
    m = list(map(int,list(set(str(n)))))
    m.sort()
    return m == [1] or m ==[2] or m==[0,1] or m==[0,2] or m==[1,2] or m==[0,1,2]
###function I made to deal with the truly massive nubmers consisting of all nines
###ie only works on 9, 99, 999, 9999 ...
def allnines(n):
    l = str(n)
    x = l.count('9')
    s = ""
    i = 1
    while i<=x:
        s+='1'
        i+=1
    while int(s)%n!=0:
        s=s+"2"
    return int(s)/n

def huge(n,o):
    print('search for ', n)
    for x in o:
        ###print(n,x,x/n)
        if x%n==0:
            print(n,x/n,x)
            return x/n
    print(n," not found")
    return 0

def eight(n,k,o):
    t0=time()
    j = 0
    b = n
    if check(b)==True:
        return 1
    while check(b)==False:
        ###if it takes more than 5 mins on this method, try the second brute
        ###force method above
        if time()-t0>300:
            return huge(n,o)
        for x in k:
            b = (int(str(j)+str(x))*n)
            if check(b)==True:
                return int(str(j)+str(x))
        j+=1
total = 0
kl =10000
nums=[]
i = 1

while i<=kl:
    nums.append(i)
    i+=1
i = 1
f=0
for y in nums:
    if list(set(str(y)))==['9']:
        b = allnines(y)
        total+=int(b)
        ###print(y,b,y*b)
        if 10*y<=kl:
            nums.remove(10*y)
            total+=int(b)

    elif str(y)[-1]=='8':
        v = eight(y,[4,5,9],s)
        total+=v
        ###print(y,v,y*v)
        if 10*y<=kl:
            nums.remove(10*y)
            total+=int(v)
    elif str(y)[-1]=='7':   
        v = eight(y,[3,6],s)
        total+=v
        ###print(y,v,y*v)
        if 10*y<=kl:
            nums.remove(10*y)
            total+=int(v)
    elif str(y)[-1]=='6':   
        v = eight(y,[2,5,7],s)
        total+=v
        ###print(y,v,y*v)
        if 10*y<=kl:
            nums.remove(10*y)
            total+=int(v)
    elif str(y)[-1]=='5':   
        v = eight(y,[2,4,6,8],s)
        total+=v
        ###print(y,v,y*v)
        if 10*y<=kl:
            nums.remove(10*y)
            total+=int(v)
    elif str(y)[-1]=='4':   
        v = eight(y,[3,5,8],s)
        total+=v
        ###print(y,v,y*v)
        if 10*y<=kl:
            nums.remove(10*y)
            total+=int(v)
    elif str(y)[-1]=='3':   
        v = eight(y,[4,7],s)
        total+=v
        ###print(y,v,y*v)
        if 10*y<=kl:
            nums.remove(10*y)
            total+=int(v)
    elif str(y)[-1]=='2':   
        v = eight(y,[1,5,6],s)
        total+=v
        ###print(y,v,y*v)
        if 10*y<=kl:
            nums.remove(10*y)
            total+=int(v)
    elif str(y)[-1]=='1':   
        v = eight(y,[1,2],s)
        total+=v
        ###print(y,v,y*v)
        if 10*y<=kl:
            nums.remove(10*y)
            total+=int(v)
    else:
        j=1
        while check(j*y)==False:
            j+=1
        total+=j
        ###print(y,j,y*j)
        if 10*y<=kl:
            nums.remove(10*y)
            total+=j
print(total)
