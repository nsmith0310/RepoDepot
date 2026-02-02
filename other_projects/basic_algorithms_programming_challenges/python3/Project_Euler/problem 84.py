###101524
###values for original example are off (though both the example modal string
###and the question value are in correct order)
from random import randint

def cc(n):
    k = randint(1,16)
    if k==1:
        return 0
    elif k==2:
        return 10
    else:
        return n
def c(n):
    k = randint(1,16)
    if k==1:
        return 0
    elif k==2:
        return 10
    elif k==3:
        return 11
    elif k==4:
        return 24
    elif k==5:
        return 39
    elif k==6:
        return 5
    elif k==7:
        return "NR"
    elif k==8:
        return "NR"
    elif k==9:
        return "NU"
    elif k==10:
        return "B3"
    else:
        return n

def roll(n):
    k1 = randint(1,4)
    k2 = randint(1,4)
    
    return [k1,k2]


scores=[0 for i in range(0,40)]
    
trials = 10**6

i = 1
s=0

c1=0
while i<=trials:
    rz = roll(s)
    if rz[0]==rz[1]:
        c1+=1
    if c1>=3:
        s=10
        
        
    else:
        c1=0
        r = sum(rz)
        r = (r+s)%40
        if r==2 or r ==17 or r==33:
            s=cc(r)
        elif r==7 or r==22 or r==36:
            r1 = c(r)
            if r1=="NR":
                if r==36:
                    s=5
                elif r == 7:
                    s=15
                elif r==22:
                    s=25
                else:
                    s=35
            elif r1=="NU":
                if r >=36 or r<=12:
                    s=12
                elif r>12 or r<=28:
                    s=28
            elif r1=="B3":
                if s<=2:
                    if s==2:
                        s=39
                    elif s==1:
                        s=38
                    else:
                        s=37
                else:
                    s-=3
                    if s==30:
                        s=10
            else:
                s=r1
        elif r==30:
            s=10
        else:
            s=r
            
    scores[s]+=1
    
    i+=1

s=""
n1 = scores.index(max(scores))
if n1<10:
    s+="0"+str(n1)
else:
    s+=str(n1)
scores[n1]=0
n2 = scores.index(max(scores))
if n2<10:
    s+="0"+str(n2)
else:
    s+=str(n2)
scores[n2]=0
n3 = scores.index(max(scores))
if n3<10:
    s+="0"+str(n3)
else:
    s+=str(n3)
scores[n3]=0
print(s)


