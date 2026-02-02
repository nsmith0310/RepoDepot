###Answer: 248155780267521

i=1

j=1

 

tmp=[]

while i<=100:

  j=1

  while j<=100:

    x = list(map(int,list(str(i**j))))

    if i==sum(x) and len(str((i**j)))>=2:

      tmp.append(i**j)

     

    j+=1

  i+=1

 

tmp.sort()

print(tmp[29])
