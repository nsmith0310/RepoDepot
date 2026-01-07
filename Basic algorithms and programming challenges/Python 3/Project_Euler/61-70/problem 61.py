###answer 28684

 

from itertools import permutations

def test(a,b):

    num1 = str(a)[2:]

    num2 = str(b)[0:2]

    return num1==num2

 

tri=[]

i = 1

while i <= 140:

    if len(str(int(i*(i+1)/2)))==4:

        tri.append(int(i*(i+1)/2))

    i+=1

sq=[]

i = 1

while i <= 99:

    if len(str(int(i*i)))==4:

        sq.append(int(i*i))

    i+=1

pnt=[]

i = 1

while i <= 81:

    if len(str(int(i*(3*i-1)/2)))==4:

        pnt.append(int(i*(3*i-1)/2))

    i+=1

hx=[]

i = 1

while i <= 70:

    if len(str(int(i*(2*i-1))))==4:

        hx.append(int(i*(2*i-1)))

    i+=1

hep=[]

i = 1

while i <= 63:

    if len(str(int(i*(5*i-3)/2)))==4:

        hep.append(int(i*(5*i-3)/2))

    i+=1

oc=[]

i = 1

while i <= 58:

    if len(str(int(i*(3*i-2))))==4:

        oc.append(int(i*(3*i-2)))

    i+=1

t = [tri,sq,pnt,hx,hep,oc]

 

big = list(permutations(t))

 

def test2(v):

    return len(list(set(v)))==len(list(v))

 

def find(t):

 

    for a in t[0]:

        for b in t[1]:

            if test(a,b)==True:

                for c in t[2]:

                    if test(b,c)==True:

                        for d in t[3]:

                            if test(c,d)==True:

                                for e in t[4]:

                                    if test(d,e)==True:

                                        for f in t[5]:

                                            if test(e,f)==True and test(f,a)==True and test2([a,b,c,d,e,f])==True:

                                                print(a+b+c+d+e+f)

                                                return True

    return False

                                

for x in big:

   if find(x)==True:

       break

 
