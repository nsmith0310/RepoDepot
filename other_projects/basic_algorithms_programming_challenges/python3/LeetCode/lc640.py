class Solution:
    def solveEquation(self, equation: str) -> str:
        l = equation.split("=")
        
        s1 = l[0]
        s2 = l[1]
        
        if s1[0]!="-":
            s1="+"+s1
        if s2[0]!="-":
            s2="+"+s2
        
        l1 = list(s1)
        l2 = list(s2)
       
        i = 0
        while i<len(l1):
            if l1[i]=="+" or l1[i]=="-":
                l1.insert(i,"n")
                i+=2
            else:
                i+=1
            
        s1 = ''.join(l1)
        
        i = 0
        while i<len(l2):
            if l2[i]=="+" or l2[i]=="-":
                l2.insert(i,"n")
                i+=2
            else:
                i+=1
            
        s2 = ''.join(l2)
        
        l1 = s1.split("n")
        l2 = s2.split("n")
        
        while '' in l1:
            del l1[l1.index('')]
            
        while '' in l2:
            del l2[l2.index('')]
          
        var = []
        num = []
        
        for x in l1:
            if "x" in x:
                rev = list(x)
                
                if rev[1]=="x":
                    rev[1]="1"
                else:
                    del rev[-1]                
                var.append(''.join(rev))
            else:
                rev = list(x)
                if rev[0]=="-":
                    rev[0]="+"
                else:
                    rev[0]="-"
                num.append(''.join(rev))
                var.append('+0')
        
        for x in l2:
            if "x" in x:
                rev = list(x)
                if rev[0]=="-":
                    rev[0]="+"
                else:
                    rev[0]="-"
                if rev[1]=="x":
                    rev[1]="1"
                else:
                    del rev[-1]
                var.append(''.join(rev))
                num.append('+0')
            else:
                num.append(x)
                
        s1 = eval(''.join(var))
        s2 = eval(''.join(num))
        if s1==0 and s2==0: return "Infinite solutions"
        if s1==0: return "No solution"
        else:
            return "x="+str(int(s2/s1))
        
