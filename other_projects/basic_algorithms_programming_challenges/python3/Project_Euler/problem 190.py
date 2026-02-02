###371048281

###formula from user on Quora

 

def power(a,b):

    if b&1==True:

        return a*(a**2)**int((b-1)/2)

    else:

        return (a**2)**int(b/2)

 

 

total=0

 

i = 2

 

while i<=15:

    t = 1

    f=0

    j = 1

    while j<=i:

        t*=power(j,j)

        j+=1

    f = ((2/(i+1))**((i*(i+1)/2)))

   

    f*=t

    part = str(f).index('.')

   

    

    total+=int(str(f)[:part])

    i+=1

print(total)
