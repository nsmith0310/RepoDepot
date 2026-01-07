###long 2178309

def xor(a,b):
    return int(str(a),2)^int(str(b),2)
def b(n):
    return str(bin(n)[2:])

t = 1
c=0
while t<=2**30:
    i=b(t)
    j = b(2*t)
    k = b(3*t)
    
    if (xor(b(xor(str(i),str(j))),str(k)))==0:
        c+=1
        
    
    t+=1
print(c)
