###18522

###basically the only part of this I figured out was 2*(x*y + y*z + z*x) (which others did as well)

###the rest of the layer formula can be found on mathblog.dk

###the main help was with the structure of the nested loops

###from www.cnblogs.com/zhuohan123

 

def f(x,y,z,n):
  return 2*(x*y + y*z + z*x)+(4*(x+y+z + n - 2))*(n-1)

d = [0 for i in range(1,10**7)]

c=0

x = 1
y = 1
z = 1

while f(x,x,x,1)<20000:
  y = x
  while f(x,y,y,1)<20000:
    z = y
    while f(x,y,z,1)<20000:
      t = 1
      while f(x,y,z,t)<20000:
        d[f(x,y,z,t)]+=1

        t+=1
      z+=1
    y+=1
  x+=1

for x in d:
  if x==1000:
    print(d.index(x))
    break
