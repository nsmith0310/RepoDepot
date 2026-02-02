###376
def order(l):
    m = []
    for x in l:
        if x[0]=="A":
            m.append(14)
        elif x[0]=="K":
            m.append(13)
        elif x[0]=="Q":
            m.append(12)
        elif x[0]=="J":
            m.append(11)
        elif x[0]=="T":
            m.append(10)
        else:
            m.append(int(x[0]))
    m.sort()
    return m

def kind(l,s):
    if l==[10,11,12,13,14]:
        if s[0][1]==s[1][1]==s[2][1]==s[3][1]==s[4][1]:
            return "RF"
    if s[0][1]==s[1][1]==s[2][1]==s[3][1]==s[4][1]:
            
        if l[0]==l[1]-1==l[2]-2==l[3]-3==l[4]-4:
            return "SF"
    for x in l:
        if l.count(x)==4:
            return "FK"
    if l[0]==l[1] and l[2]==l[3]==l[4]:
        return "FH"
    if s[0][1]==s[1][1]==s[2][1]==s[3][1]==s[4][1]:
            return "F"
    if l[0]==l[1]-1==l[2]-2==l[3]-3==l[4]-4:
        return "S"
    for x in l:
        if l.count(x)==3:
            return "T"
    
    
    for x in l:
        for y in l:
            if x!=y:
                if l.count(x)==2 and l.count(y)==2:
                    return "TP"
            
    
    for x in l:
        if l.count(x)==2:
            return "P"
    else:
        return "N"
def judge(a1,a2):
    ###print(a1[1])
    if a1[1]=="N" and a2[1]=="N":
        
        if max(a1[0])>max(a2[0]):
            return 1
        elif max(a2[0])>max(a1[0]):
            return 2
        else:
            return 0
    if a1[1]=="RF" or a2[1]=="RF":
        if a1[1]=="RF" !=a2[1]:
            return 1
        elif a2[1]=="RF" !=a1[1]:
            return 2
        else:
            return 0
    if a1[1]=="SF" or a2[1]=="SF":
        if a1[1]=="SF" !=a2[1]:
            return 1
        elif a2[1]=="SF" !=a1[1]:
            return 2
        else:
            return 0
    if a1[1]=="FK" or a2[1]=="FK":
        if a1[1]=="FK" !=a2[1]:
            return 1
        elif a2[1]=="FK" !=a1[1]:
            return 2
        else:
            if max(a1[0])>max(a1[1]):
                return 1
            elif max(a1[1])>max(a1[0]):
                return 2
            else:
                return 0
    #############
    if a1[1]=="FH" or a2[1]=="FH":
        if a1[1]=="FH" !=a2[1]:
            return 1
        elif a2[1]=="FH" !=a1[1]:
            return 2
        else:
            if max(a1[0])>max(a1[1]):
                return 1
            elif max(a1[1])>max(a1[0]):
                return 2
            else:
                if a1[0][0]>a2[0][0]:
                    return 1
                elif a1[0][0]<a2[0][0]:
                    return 2
                else:
                    return 0

            
    if a1[1]=="F" or a2[1]=="F":
        if a1[1]=="F" !=a2[1]:
            return 1
        elif a2[1]=="F" !=a1[1]:
            return 2
        else:
            if max(a1[0])>max(a1[1]):
                return 1
            elif max(a1[1])>max(a1[0]):
                return 2
            else:
                for x in a1[0]:
                    if x-a2[0][a1[0].index(x)]>0:
                        return 1
                    elif x-a2[0][a1[0].index(x)]<0:
                        return 2
                return 0
            
    if a1[1]=="S" or a2[1]=="S":
        if a1[1]=="S" !=a2[1]:
            return 1
        elif a2[1]=="S" !=a1[1]:
            return 2
        else:
            if max(a1[0])>max(a1[1]):
                return 1
            elif max(a1[1])>max(a1[0]):
                return 2
            else:
                for x in a1[0]:
                    if x-a2[0][a1[0].index(x)]>0:
                        return 1
                    elif x-a2[0][a1[0].index(x)]<0:
                        return 2
                return 0
    if a1[1]=="T" or a2[1]=="T":
        if a1[1]=="T" !=a2[1]:
            return 1
        elif a2[1]=="T" !=a1[1]:
            return 2
        else:
            for x in a1[0]:
                if a1[0].count(x)==3:
                    d1=x
            for x in a2[0]:
                if a2[0].count(x)==3:
                    d2=x
            if d1>d2:
                return 1
            elif d2>d1:
                return 2
            else:
                return 0
            

    if a1[1]=="TP" or a2[1]=="TP":
        if a1[1]=="TP" !=a2[1]:
            return 1
        elif a2[1]=="TP" !=a1[1]:
            return 2
        else:
            m1 = 0
            m2 = 0
            for x in a1[0]:
                if a1[0].count(x)==2:
                    if x>m1:
                        m1=x
                    
            for x in a2[0]:
                if a2[0].count(x)==2:
                    if x>m2:
                        m2=x
            if m1>m2:
                return 1
            elif m2>m1:
                return 2
            else:
                return 0
            
    if a1[1]=="P" or a2[1]=="P":
        if a1[1]=="P" !=a2[1]:
            return 1
        elif a2[1]=="P" !=a1[1]:
            return 2
        else:
            for x in a1[0]:
                if a1[0].count(x)==2:
                    d1=x
            for x in a2[0]:
                if a2[0].count(x)==2:
                    d2=x
            if d1>d2:
                return 1
            elif d2>d1:
                return 2
            else:
                return 0
        
p = [line.rstrip('\n') for line in open("poker.txt")]
l=[]
for x in p:
    d = x.split(" ")
    t1 = [y for y in d[:5]]
    t2 = [y for y in d[5:]]
    l.append([t1,t2])

c=0
for x in l:
    s1 = order(x[0])
    s2 = order(x[1])
    k1 = kind(s1,x[0])
    k2 = kind(s2,x[1])
    val = judge([s1,k1],[s2,k2])
    
    if val==1:
        c+=1
print(c)


