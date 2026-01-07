###1006193 longish
###basically ripped s braumme's solution again


def s(n):
    return (1.0*n**.5).is_integer()


a = 3
b = 1
c = 1

while a<=1000:
    if a&1==True:
        b=1
    else:
        b=2
    while b<a:
        x = .5*(a**2 + b**2)
        y = a**2 - x
        if x<=y:
            break
        
        c = int(x**.5)+1
        while c!=-1:
            z = c**2 - x
            if y<=z:
                break
            if s(z+y)==True and s(x-z)==True and s(y-z)==True:
                print(int(x+y+z))
            c+=1
        
        b+=2
     
    a+=1
