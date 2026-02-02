class Solution:
    def fractionAddition(self, expression: str) -> str:
        
        if expression[0]!="-":
            expression = "+"+expression
        lim = len(expression)
        pl=[]
        mn=[]
        num = 0
        denom = 0
        tmp = ""
        i = 0
        while i<lim:
            if expression[i]=="+":
                j = i+1
                
                while j<lim:
                    if expression[j]=="+":
                    
                        break
                    elif expression[j]=="-":
                        
                        break
                    
                    tmp+=expression[j]
                    j+=1
                pl.append(tmp)
                tmp=""
            elif expression[i]=="-":
                j = i+1
                while j<lim:
                    if expression[j]=="+":
                    
                        break
                    elif expression[j]=="-":
                        
                        break
                    
                    tmp+=expression[j]
                    j+=1
                mn.append(tmp)
                tmp=""
            i+=1
            
            
        if pl!=[]:
            n = pl[0].split("/")
            num = int(n[0])
            denom = int(n[1])
            del pl[0]
            for x in pl:
                n = x.split("/")
                n1 = int(n[0])
                n2 = int(n[1])
                tmp = n2*denom
                n1=denom*n1
                num = n2*num + n1
                denom = tmp

        if mn!=[]:
            if num==0 and denom==0:
                n = mn[0].split("/")
                num = -1*int(n[0])
                denom = int(n[1])
                del mn[0]
                for x in mn:
                    n = x.split("/")
                    n1 = int(n[0])
                    n2 = int(n[1])
                    tmp = n2*denom
                    n1=denom*n1
                    num = n2*num - n1
                    denom = tmp
            else:
            
            
                for x in mn:
                    n = x.split("/")
                    n1 = int(n[0])
                    n2 = int(n[1])
                    tmp = n2*denom
                    n1=denom*n1
                    num = n2*num - n1
                    denom = tmp
        p = 1
        if num<0:
            p = -1
        num = abs(num)
        denom = abs(denom)
        mx = 1
        lg = 1
        while lg<min([num,denom]):
            if num%lg==0 and denom%lg==0:
                mx = lg
            lg+=1
        num//=mx
        denom//=mx
        if num%denom==0:
            return str(p*num//denom)+"/"+"1"
        elif denom%num==0:
            return str(p)+"/"+str(denom//num)
        else:
            return str(p*num)+"/"+str(denom)
                
            
        
        
