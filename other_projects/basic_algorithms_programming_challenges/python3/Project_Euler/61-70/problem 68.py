###6531031914842725
###nothing to be proud of

from itertools import combinations as c,permutations as per

 

final=[]

fv= [1,2,3,4,5,6,7,8,9,10]

nums = list(c(fv,5))

for x in nums:

    if x[0]>6:

        nums.remove(x)

       

t = sorted(nums, key= lambda x: x[0], reverse=True)

mx=0

for x in t:

    y = x[1:5]

    f=[]

    z = list(per(y))

    for b in z:

        c = []

        for e in b:

            c.append(e)

        f.append(c)

   

    for a in f:

        a.insert(0,x[0])

   

    n = []

    for g in fv:

        if g not in x:

            n.append(g)

   

    o = list(per(n))

    p = []

    for b in o:

        c = []

        for e in b:

            c.append(e)

        p.append(c)

    for q in f:

        lt1=[q[0]]

        lt2=[q[1]]

        lt3=[q[2]]

        lt4=[q[3]]

        lt5=[q[4]]

       

        for r in p:

            lt1.append(r[0])

            lt2.append(r[1])

            lt3.append(r[2])

            lt4.append(r[3])

            lt5.append(r[4])

            lt1.append(r[1])

            lt2.append(r[2])

            lt3.append(r[3])

            lt4.append(r[4])

            lt5.append(r[0])

           

            if sum(lt1)==sum(lt2)==sum(lt3)==sum(lt4)==sum(lt5):

                i = ""

                for xy in lt1:

                    i+=str(xy)

                for xy in lt2:

                    i+=str(xy)

                for xy in lt3:

                    i+=str(xy)

                for xy in lt4:

                    i+=str(xy)

                for xy in lt5:

                    i+=str(xy)

                if len(i)==16:

                    if int(i)>mx:

                        final.append(int(i))

                        mx=int(i)

            lt1=[q[0]]

            lt2=[q[1]]

            lt3=[q[2]]

            lt4=[q[3]]

            lt5=[q[4]]

           

print(max(final))
