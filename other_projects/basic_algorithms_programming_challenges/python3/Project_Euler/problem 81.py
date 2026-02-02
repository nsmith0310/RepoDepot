###427337
###algorithm ripped from dreamshire


d=[]
with open('matrix.txt','r') as file:
    for line in file:
        
        g = list(map(int,list(line.split(","))))
        d.append(g)

i = 0
j = 0



while i<=79:
    j = 0
    while j<=79:
        if i*j!=0:
            d[i][j]+=min([d[i-1][j],d[i][j-1]])
        elif j:
            
            d[i][j]+=d[i][j-1]
        elif i:
            d[i][j]+=d[i-1][j]
        else:
            d[i][j]+=0
        j+=1
    i+=1
print(d[-1][-1])
