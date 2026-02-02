from math import sqrt
class Solution:
    
    def c(self,s):
        l = len(s)
        if l%2==0:
            return s[:l//2]==s[l//2:][::-1]
        else:
            return s[:l//2]==s[l//2 + 1:][::-1]
        
    def superpalindromesInRange(self, L: str, R: str) -> int:
        
        a = int(L)
        b = int(R)
        t = 0
        
        l = []
        
        i = 1
        while i<=99999:
            
            k = str(i)
            
            l.append(k+k[::-1])
            l.append(k+k[:-1][::-1])
            i+=1
        
        
        
        
        
        
        for x in l:
            
            n = int(x)**2
            if n>=a and n<=b:
                
                if self.c(str(n))==True:
                    t+=1
        return t
            
        
        
        
        
