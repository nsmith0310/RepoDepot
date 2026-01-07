###343047

###one of the most ridiculous generating equations I have seen yet (A210687)

 

def mod(a,b):

    return a%b

 

t = []

n=36
t = ((1678*(n**3) + 3117*(n**2) +(88*n) -345*mod(n,2) - 320*mod(n,3) - 90*mod(n,4) - 288*mod(n**3 - n**2 + n,5))/240)

    

print(int(t))
