###Answer 73682

l=[]
l.append(1)
i = 0
while i <=199:
  l.append(0)
  i+=1


coins=[1,2,5,10,20,50,100,200]

for x in coins:
  for i in range (0,(200-x)+1,1):
    l[x+i] += l[i]

print(l[len(l)-1])
