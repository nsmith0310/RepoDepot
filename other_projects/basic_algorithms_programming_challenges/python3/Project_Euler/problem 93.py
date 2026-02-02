###long 1258

from itertools import product,permutations as p,combinations as com

 

d = com(["1","2","3","4","5","6","7","8","9"],4)

c=[]

for x in d:

    b = []

    for y in x:

        b.append(y)

    c.append(b)

 

final=[]

top=""

mx=0

 

 

t = list(product(["+","-","/","*"],repeat=3))

r=[]

for x in t:

    q=[]

    for y in x:

        q.append(y)

    r.append(q)

 

mx=0

for y in c:

    d = list(p(y))

       

    final=[]

    for x in r:

        i = 50

       

        while i >=1:

            for w in d:   

                num1 = str(float(eval(str(i)+x[0]+w[0])))

           

                num2 = str(float(eval(num1+x[1]+w[1])))

           

                num3 = (float(eval(num2+x[2]+w[2])))

                if num3.is_integer():

                    if str(int(num3)) == w[3]:

                        final.append(i)

            i-=1

    count=0

    key = list(set(final))

    i = 0

    while i<len(key)-1:

        if key[i]==key[i+1]-1:

            count+=1

        i+=1

    if count+1>mx:

        mx=count+1
        s=""
        dt=y
        dt.sort()
        top=''.join(dt)

        

       

print(top)
