###ANSWER: 661!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
###My crown jewel to date

def eq(n1,n2,n3):
    v = n1
    w = n2
    x = abs(n3)
    i = 0
    while ((w*i)+v)%x!=0:
        i+=1
    
    return(i)

def gm(n1,n2,n4):
    num1 = n1
    num2 = n2
    kl = n4
    i =0
    x=0
    while i!=-1:
        val = abs((abs(n1)*(i+1) + tmp)**2 - kl)
        if abs((abs(n1)*(i) + tmp)**2 - kl) < val:
            x = abs(n1)*i + tmp
            break
        i+=1
    return x

value = 0
best = 0
mo = 1

while mo <= 1000:
    if not (mo**.5).is_integer():
        b = 1
        a = 5
        bf=0
        af=0
        k= int(a**2 - mo*b**2)
        m=0
        t = 2
        mx=0
        at = 0
        bt = 0
        while k!=1:
  
            tmp = eq(a,b,k)
            ###print(a,b,k,tmp)
            m = gm(k, tmp, mo)
            
            at = (a*m + (mo*b))//abs(k)
            bt = (a+(b*m))//abs(k)
            a = at
            b = bt
            k = ((m**2 - mo)//k)
            ###print(k)
            
            
        if a>best:
            best=a
            ###print(best, mo)
            value=mo
    ###print(mo)
    mo+=1
  
print(value)
