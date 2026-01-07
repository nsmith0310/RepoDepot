###95962097 algorithm suggested by dreamshire

 

def tetra(x,y):

    i = 1

    total=1

    while i<=y:

        total=pow(x,total,100000000)

        i+=1

    return total   

    

print(tetra(1777,1855))
