class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        l1 = list(secret)
        l2 = list(guess)
        ls1=[]
        lg1=[]
        i = 0
        b = 0
        c = 0
        while i<len(l1):
            if l1[i]==l2[i]:
                b+=1
                
            else:
                ls1.append(l1[i])
                lg1.append(l2[i])
            i+=1
        
       
        i = 0
        lg3 = list(set(lg1))
        
        for x in lg3:
            n1 = lg1.count(x)
            n2 = ls1.count(x)
            if n1>n2:
                c+=n2
            elif n2>n1:
                c+=n1
            elif n2==n1:
                c+=n2
            
        return str(b)+"A"+str(c)+"B"
