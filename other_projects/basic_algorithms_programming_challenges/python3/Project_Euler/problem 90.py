###1217

from itertools import combinations as c, product as p

 

t= list(c(["0","1","2","3","4","5","6","7","8","9"],6))

u = list(c(t,2))

v=[]

 

 

f=[]       

for x in u:

    c = list(p(x[0],x[1]))

   

    g=[]

   

    for y in c:

        s=y[0]+y[1]

        g.append(s)

    f.append(g)

   

 

count=0

for x in f:

   

    if ("01" in x or "10" in x) and ("04" in x or "40" in x) and (("09" in x or "90" in x) or ("06" in x or "60" in x)) and (("16" in x or "61" in x) or ("19" in x or "91" in x)) and ("25" in x or "52" in x) and (("36" in x or "63" in x) or ("39" in x or "93" in x)) and (("49" in x or "94" in x) or ("46" in x or "64" in x)) and ("81" in x or "18" in x):

        count+=1

print(count)
