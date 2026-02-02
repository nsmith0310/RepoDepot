###Answer: 1389019170

from math import sqrt

 

i = 9
j = 9
k = 9
l = 9
m = 9
n = 9
o = 9
p = 9
q = 9

while i >=0:
  j=9
  while j>=0:
    k=9
    while k>=0:
      l=9
      while l>=0:
        m=9
        while m>=0:
          n=9
          while n>=0:
            o=9
            while o >=0:
              p=9
              while p>=0:
                q=9
                while q >=0:
                  if (sqrt(int("1"+str(i)+"2"+str(j)+"3"+str(k)+"4"+str(l)+"5"+str(m)+"6"+str(n)+"7"+str(o)+"8"+str(p)+"9"+str(q)+"0"))).is_integer()==True:

                    print(int(sqrt(int(str("1"+str(i)+"2"+str(j)+"3"+str(k)+"4"+str(l)+"5"+str(m)+"6"+str(n)+"7"+str(o)+"8"+str(p)+"9"+str(q)+"0")))))
                    i=0
                    j = 0
                    k =0
                    l = 0
                    m = 0
                    n=0
                    o=0
                    p=0
                    q=0
                  q-=1
                p-=1
              o-=1
            n-=1
          m-=1
        l-=1
      k-=1
    j-=1
  i-=1
