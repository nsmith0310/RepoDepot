###long 878454337159
###(a**3 * b * c**2) + (b**2 * c) was entirely derived by mathblog.dk as
###well as the boundary values for a,b,c


a = 2
f=[]
while a<=10000:
    b = 1
    while b<=a:
        c = 1
        while ((a**3 * b * c**2) + (b**2 * c))<10**12:
            
            if ((((a**3 * b * c**2) + (b**2 * c)))**.5).is_integer():
                f.append(((a**3 * b * c**2) + (b**2 * c)))
            c+=1
        b+=1
    a+=1


print(sum(list(set(f))))
