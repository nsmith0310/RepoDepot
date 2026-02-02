###73162890

###algorithm suggested by Ubuntu forum user

###assumes no digits/ characters are repeated


from itertools import permutations as p

lp = [line.rstrip('\n') for line in open("keylog.txt")]


l=[]

for line in lp:

  l.append(list(map(int,line.split(" "))))

l2=[]

for x in l:

  for y in x:

    l2.append(y)

 

l3=[]

for x in l2:

  for y in list(str(x)):

    l3.append(y)

 

 

d = list(p(list(set(l3))))

 

for x in d:

  if x[0]=='0':

    del d[d.index(x)]

  else:

    c=0

    for y in l2:

      k = list(str(y))

      if x.index(k[2])<x.index(k[1]) or x.index(k[2])<x.index(k[0]) or x.index(k[1])<x.index(k[0]):

        c=1

        break

  if c==0:

    print(''.join(x))

    break
