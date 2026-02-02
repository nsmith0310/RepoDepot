###likely 1.002322108633 (one confirmation)
###basically narrowed the possible interval down by trial and error


from decimal import *
getcontext().prec = 12
i = 1.0

def f(x):
    j = 1
    t = 0
    while j<=5000:
        t+=(900-3*j)*pow(x,j-1)
        j+=1
    return t



j = 1.0023221086328755
while j<=1.0023221086328766:
    n = f(round(j,16))
    if n>-600000000000:
        if n==-600000000000:
            print(round(j,16))
            break
        j+=0.000000000000001

    if n<-600000000000.0:
        print(round(j,12))
        break
    
