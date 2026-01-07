###28123-> answer = 297604909
i = 1
j = 1
ab=[]
tmp=[]
sums=[]
while i < 28123:
    tmp=[]
    j=1
    while j < i:
        if i%j==0:
            tmp.append(j)
        j+=1
    
    if sum(tmp) > i:
        ab.append(i)
    i+=1

i=0
j=0

while i < len(ab)-1:
    j=0
    while j < len(ab)-1:
        if ab[i]+ab[j]< 28123:
            sums.append(ab[i]+ab[j])
        j+=1
    i+=1

all = []
i=1
while i < 28123:
    all.append(i)
    i+=1
try:
    for x in sums:
        all.remove(x)
except:
    pass
print(sum(all))








        
        
        
