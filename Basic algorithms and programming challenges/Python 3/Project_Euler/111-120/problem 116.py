###long 20492570929

def c(n,i):
    total=0
    spaces=n-i
    hop=[j for j in range(0,spaces+1)]
    hop.sort(reverse=True)
    for x in hop:
        total+=1
        if x-i>=0:
            total+=c(n-x,i)
        else:
            continue
    return total

'''
i = 4

while i<=20:
    print(i,c(i,2),c(i,3),c(i,4),(c(i,2)+c(i,3)+c(i,4)))
    i+=1
'''

t = 4
f=[3,5]
while len(f)<=50:
    f.append(f[-1]+f[-2])
    
i = 1
while i<=46:
    t+=f[i-1]
    i+=1
    
print(t+(c(50,3)+c(50,4)))



