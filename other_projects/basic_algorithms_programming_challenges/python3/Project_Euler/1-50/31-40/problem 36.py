###answer:872187

from math import floor, ceil
print("Enter upper limit: (1000)")
num=int(input())
base_10=[]
base_2=[]


tmp10=[]
i=0
while i < num:
    tmp10.append(str(i))
    i+=1
    
i=0
while i < len(tmp10):
    base_10.append(str(tmp10[i])+str(tmp10[i][::-1]))
    i+=1


i=0
while i < len(tmp10):
    if len(str(i))==2:
        base_10.append(str(tmp10[i])+str(tmp10[i][0]))
    if len(str(i))==3:
        base_10.append(str(tmp10[i][:2])+str(tmp10[i][:3][::-1]))
    i+=1

base_10 = list(map(int, base_10))
base_10.sort()
base_10.remove(0)

###print(base_10)

base_2 = []
for x in base_10:
    base_2.append(str(bin(x))[2:])
total=[]
for x in base_2:
    if len(x)%2==0:
        if x[:int(len(x)/2)] == x[int(len(x)/2):][::-1]:
            total.append(int(x,2))
    else:
        if x[:int(floor(len(x)/2))]==x[int((ceil(len(x)/2))):][::-1]:
            total.append(int(x,2))
            
total = list(dict.fromkeys(total))


wamp=[]
i=1
for x in range(1,11):
    wamp.append(str(bin(x))[2:])
    
    
for x in wamp:
    if len(x)%2==0:
        if x[:int(len(x)/2)] == x[int(len(x)/2):][::-1]:
            total.append(int(x,2))
    else:
        if x[:int(floor(len(x)/2))]==x[int((ceil(len(x)/2))):][::-1]:
            total.append(int(x,2))
            
total.sort()
print(total)
print(sum(total))

