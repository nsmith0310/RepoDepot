###answer: 2772 (R) 

i = 1

j = 1

i1 = 0

j1=0

mx = 0

 

while i< 500:

  j = 1

  while j < 500:

    if (.25*(i**2+i)*(j**2+j)).is_integer() and (.25*(i**2+i)*(j**2+j)) < 2000000:

      if (.25*(i**2+i)*(j**2+j))>mx:

        mx = (.25*(i**2+i)*(j**2+j))

        i1=i

        j1=j

    j+=1

  ###print(i)

  i+=1

print(i1,j1,"(",(i1*j1),")")
