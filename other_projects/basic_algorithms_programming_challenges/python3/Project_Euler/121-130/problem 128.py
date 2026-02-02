###longish 14516824220
###solution ripped from mathblog.dk

from math import floor,ceil

from euler import rmtest as r

c = 1
i = 1

while i!=-1:
    if r(6*i - 1,3) and r(6*i + 1,3) and r(12*i + 5,3):
        c+=1
        ###print(i,(3*i*i) - 3*i + 2)
        if c==2001:
            print((3*i*i) - 3*i + 2)
            break
    if r(6*i + 5,3) and r(6*i - 1,3) and r(12*i -7,3):
        c+=1
        ###print(i,(3*i*i) + 3*i + 1)
        if c==2001:
            print((3*i*i) + 3*i + 1)
            break
    i+=1


'''
###my code: might work, but is incredibly slow (calculates the
whole hexagon)
total=0
h=[]
k = 6
i = 2
while k<=60000:
    d=1
    tmp=[]
    while d<=k:
        tmp.append(i)
        i+=1
        d+=1
    h.append(tmp)
    k+=6
print(h[-1][-1])
'''
'''

i = 1
l=[1,2,17]
while i<len(h)-1:
    kill=0
    for x in h[i]:
        o=0
        c = len(h[i])/6
        if h[i].index(x)==0 or (h[i].index(x)+c)%c==0:
            if h[i].index(x)==0:
                k = (h[i].index(x)+1)/len(h[i])
                n1=h[i][h[i].index(x)+1]
                n2=h[i][len(h[i])-1]
                n3=h[i-1][floor(k*len(h[i-1]))]
                n4=h[i+1][floor(k*(len(h[i+1])))]
                n5=h[i+1][-1]
                n6=h[i+1][h[i+1].index(n4)-1]
                b = [abs(x-n1),abs(x-n2),abs(x-n3),abs(x-n4),abs(x-n5),abs(x-n6)]
                for z in b:
                    if r(z,3)==True:
                        o+=1
                        if o==3 and x!=19:
                            l.append(x)
                            total+=1
                            if total==2000:
                                print(x)
                                kill=1
                                break
                            break
            else:
                k = (h[i].index(x)+1)/len(h[i])
                n1=h[i][h[i].index(x)+1]
                n2=h[i][h[i].index(x)-1]
                n3=h[i-1][floor(k*len(h[i-1]))]
                n4=h[i+1][floor(k*(len(h[i+1])))]
                n5=h[i+1][h[i+1].index(n4)-2]
                n6=h[i+1][h[i+1].index(n4)-1]
                b = [abs(x-n1),abs(x-n2),abs(x-n3),abs(x-n4),abs(x-n5),abs(x-n6)]
                for z in b:
                    if r(z,3)==True:
                        o+=1
                        if o==3 and x!=19:
                            l.append(x)
                            total+=1
                            if total==2000:
                                print(x)
                                kill=1
                                break
                            break
                
        else:
            if h[i].index(x)!=len(h[i])-1:
                
                k = (h[i].index(x)+1)/len(h[i])
                n1=h[i][h[i].index(x)+1]
                n2=h[i][h[i].index(x)-1]
                
                n3=h[i-1][floor(k*len(h[i-1]))]
                n4=h[i-1][h[i-1].index(n3)-1]
                n5=h[i+1][floor(k*len(h[i+1])-1)]
                n6=h[i+1][h[i+1].index(n5)-1]
                b = [abs(x-n1),abs(x-n2),abs(x-n3),abs(x-n4),abs(x-n5),abs(x-n6)]
                for z in b:
                    if r(z,3)==True:
                        o+=1
                        if o==3 and x!=19:
                            l.append(x)
                            total+=1
                            if total==2000:
                                print(x)
                                kill=1
                                break
                            break
                
            else:
                
                k = (h[i].index(x)+1)/len(h[i])
                n1=h[i][0]
                n2=h[i][h[i].index(x)-1]
                
                n3=h[i-1][floor(k*len(h[i-1])-1)]
                n4=h[i-1][0]
                
                n5=h[i+1][floor(k*len(h[i+1])-1)]
                n6=h[i+1][h[i+1].index(n5)-1]
                b = [abs(x-n1),abs(x-n2),abs(x-n3),abs(x-n4),abs(x-n5),abs(x-n6)]
                for z in b:
                    if r(z,3)==True:
                        o+=1
                        if o==3 and x!=19:
                            l.append(x)
                            total+=1
                            if total==2000:
                                print(x)
                                kill=1
                                break
                            break
  
    if kill==1:
        break
    print(total,max(l))
    i+=1
'''
