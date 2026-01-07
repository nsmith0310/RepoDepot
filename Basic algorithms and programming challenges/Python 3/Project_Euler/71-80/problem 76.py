###Answer 190569291

l=[]
l.append(1)
i = 0
while i <=99:
  l.append(0)
  i+=1


coins=[i for i in range(1,101,1)]

for x in coins:
  for i in range (0,(101-x),1):
    l[x+i] += l[i]

print(l[len(l)-1]-1)
