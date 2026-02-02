###answer: 49 

i = 0

j = 0

count=0

 

while i <= 100:

  j = 0

  while j <= 100:

    if len(str(pow(i,j)))==j:

      count+=1

    j+=1

  i+=1

 

print(count-1)
