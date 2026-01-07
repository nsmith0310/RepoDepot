### 850481152593119296

###DOES NOT HANDLE ALL TEST CASES

### a lot of help from stack explainer regarding the finding of the index of
### the block, f[0] or f[1] which our target digit is in
### I did figure out how to grab the digit when the block is known, as well
### as that actually computing the strings will not work


l = [((127+19*i)*7**i) for i in range(0,18)]

f=["1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679","8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196"]

g = ["1415926535", "8979323846"]

t = 0

for x in l:
    s = [1,1]
    while 1!=-1:
        s.append(s[-2]+s[-1])
        if s[-1]>x:
            break
        
    s.remove(s[0])
    
    
    tar = x//100
    
    i = len(s)-1
    while 1!=-1:
        
        if i==1:
            x2 = 1
            break
        if i==2 and tar==0:
            x2 = 0
            break
        if i==2 and tar==1:
            x2 = 1
            break
        if i==3 and tar==1:
            x2 = 0
            break
        if i==2 and tar==3:
            x2 = 0
            break
        if tar<s[i-1]:
            i-=2
        else:
            tar-=s[i-1]
            i-=1
        
        
  
        
    n1 = x%100
    
    ###print(x,int(f[x2][n1-1]),tar,f[0][n1-1],f[1][n1-1])
    t+=(10**(l.index(x)))*int(f[x2][n1-1])
print(t)

