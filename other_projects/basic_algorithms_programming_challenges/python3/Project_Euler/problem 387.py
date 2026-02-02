###696067597313468

from euler import rmtest as r

def test(n):
    if n=='':
        return True
    return int(n)%sum(list(map(int,list(n))))==0

def f(n):
    s=["0","1","2","3","4","5","6","7","8","9"]
    
    if len(n[0])<=15:
        for x in n[:-1]:
            
            if len(x)>=1: 
                if test(x)==False:
                    
                    if r(int(x),5)==True and test(x[:-1])==True and r(int(int(x[:-1])/sum(list(map(int,list(x[:-1]))))),5)==True:
                        ###print(x)
                        if int(x)<10**14:
                            ###print(x)
                        
                            n[-1]=str(int(n[-1])+int(x))
                            n.remove(x)
                    else:
                        n.remove(x)
                    
                    
                        
                
            
                
        for x in n[:-1]:
            for y in s:
                ###print(x+y)
                n.insert(0,x+y)
            n.remove(x)
            
        ###print(n)
        return f(n)
    else:
        ###print(n[-1])
        return int(n[-1])


d = [1,2,3,4,5,6,7,8,9]

total=0
for x in d:
    total+=f([str(x),str(0)])
    
print(total)
    
