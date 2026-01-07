###ANSWER: 153 

 

x = 3

y = 2

count=0

track=0

while count <=1000:

  t1 = x + y + y

  t2 = x + y

  if len(str(t1))>len(str(t2)):

    track+=1

  x = t1

  y = t2

  count+=1

print(track)
