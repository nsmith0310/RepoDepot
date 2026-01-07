###answer: 428570

from euler import totients
mx = 0

tmp = totients(1000000)

i = 1

while i < len(tmp):

  if tmp[i]/1000000 < (3/7) and tmp[i]/1000000 > (299999/700000):

    if tmp[i]/1000000 > mx:

      mx = tmp[i]

  i+=1

 

found = False

final = 0

i = 999999

while found == False:

  tmp1 = totients(i)

  j = 1

  while j < len(tmp1):

    if tmp1[j]/i > mx/1000000 and tmp1[j]/i < (300000/700000):

      final=tmp1[j]

      found=True

    j+=1


  i-=1

print(final)
