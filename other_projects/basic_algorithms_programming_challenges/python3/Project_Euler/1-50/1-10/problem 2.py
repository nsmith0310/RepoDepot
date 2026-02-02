i= 1
t = 1
j = 4000000
k=[]

while t < 4000000:
    k.append(i)
    k.append(t)
    t=t+i
    i=i+t

z = 0

while z < len(k):
    if k[z] > 4000000:
        k.pop(z)
    z+=1

k.sort()
z=0
while z < len(k):
    print(k[z])
    z+=1

evens=[]
m=0

while m < len(k):
    if k[m]%2==0:
        evens.append(k[m])
    m+=1


print("Sum of even valued numbers: ", sum(evens) )



    
