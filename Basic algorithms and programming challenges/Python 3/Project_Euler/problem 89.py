###743

def count(n):
    total=0
    n+="Z"
    if n[0]=="M":
        
        while n[0]=="M":
            total+=1000
            n=n[1:]
    if n[0]=="D":
        total+=500
        n=n[1:]
    if n[0]=="C":
        if len(n)-1>=2:
            if n[1]=="D":
                total+=400
                n=n[2:]
            elif n[1]=="M":
                total+=900
                n=n[2:]
            else:
                while n[0]=="C":
                    total+=100
                    n=n[1:]
        else:
            total+=100
            n=n[1:]
    if n[0]=="L":
        total+=50
        n=n[1:]
    if n[0]=="X":
        if len(n)-1>=2:
            if n[1]=="L":
                total+=40
                n=n[2:]
            elif n[1]=="C":
                total+=90
                n=n[2:]
            else:
                while n[0]=="X":
                    total+=10
                    n=n[1:]
        else:
            total+=10
            n=n[1:]
    if n[0]=="V":
        total+=5
        n=n[1:]
    if n[0]=="I":
        if len(n)-1>=2:
            if n[1]=="V":
                total+=4
                n=n[2:]
            elif n[1]=="X":
                total+=9
                n=n[2:]
            else:
                while n[0]=="I":
                    total+=1
                    n=n[1:]
        else:
            total+=1
            n=n[1:]
                
    return total

def digs(n):
    num = count(n)
    
   
    i = 1
    l=[]
    while i<=len(str(num)):
        l.append((str(num)[::-1][i-1]+''.join(['0' for k in range(0,i-1)])))
        i+=1
    
    return l

def repl(num):
    l = digs(num)
    m=[]
    for x in l:
        if len(x)==1:
            if x=="1":
                m.append("I")
            elif x=="2":
                m.append("II")
            elif x=="3":
                m.append("III")
            elif x=="4":
                m.append("IV")
            elif x=="5":
                m.append("V")
            elif x=="6":
                m.append("VI")
            elif x=="7":
                m.append("VII")
            elif x=="8":
                m.append("VIII")
            elif x=="9":
                m.append("IX")
        elif len(x)==2:
            if x=="10":
                m.append("X")
            elif x=="20":
                m.append("XX")
            elif x=="30":
                m.append("XXX")
            elif x=="40":
                m.append("XL")
            elif x=="50":
                m.append("L")
            elif x=="60":
                m.append("LX")
            elif x=="70":
                m.append("LXX")
            elif x=="80":
                m.append("LXXX")
            elif x=="90":
                m.append("XC")
        elif len(x)==3:
            if x=="100":
                m.append("C")
            elif x=="200":
                m.append("CC")
            elif x=="300":
                m.append("CCC")
            elif x=="400":
                m.append("CD")
            elif x=="500":
                m.append("D")
            elif x=="600":
                m.append("DC")
            elif x=="700":
                m.append("DCC")
            elif x=="800":
                m.append("DCCC")
            elif x=="900":
                m.append("CM")
        else:
            s=''.join(["M" for j in range(0,int(x[0]))])
            m.append(s)
    ###print(''.join(m[::-1]),num)
    count=0
    for x in m:
        count+=len(x)
    return count
l = [line.rstrip('\n') for line in open("roman.txt")]
            
save=0
for x in l:
    save+=len(x)-repl(x)
print(save)
    
