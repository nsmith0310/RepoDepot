###450186511399999

 

def pmod(a,b,m):

    if m==1 or m==0:

        return 0

    r=1

    a = a%m

    while b > 0:

        if b%2 == 1:

            r = (r*a)%m

        b = b >> 1

        a = a**2 % m

    return r

       

###A165736

def f(n,k):

    if n%10==0:

      return 0

    j = 1

    m = 10

    t=n

    while j<=k:

        t=pmod(n,t,m)

        m*=10

        j+=1

    return t

 

total=0

 

i=2

while i<=10**6:

    if i%10==0:

      total+=0

    else:

      x = f(i,10)

  

      total+=(pmod(i,x,10**9))

   

    i+=1

print(total)
