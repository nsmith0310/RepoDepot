###ANSWER: 1587000

def inc(n):
    x = list(map(int,list(str(n))))
    
    status = False
    mx = 0
    for i in x:
        if i>=mx:
            mx=i
        else:
            
            status = True
    return status

def dec(n):
    x = list(map(int,list(str(n))))
    
    status = False
    mn = 999999999999
    for i in x:
        if i <=mn:
            mn = i
        else:
            
            status = True
            
    return status

b = 0
nb = 0
i = 1

while i !=-1:
    if inc(i)==True and dec(i)==True:
        
        b+=1
    else:
        nb+=1
    if b/(nb+b)==.99:
        print(i)
        break
    i+=1

        
