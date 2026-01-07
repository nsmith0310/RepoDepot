class Solution:
    def validPalindrome(self, s: str) -> bool:
        lim = len(s)
        
        if lim<=1:return True
        
        if lim%2!=0:
            c = 0
            
            i = 0
            while i<lim//2:
                
                if s[i]!=s[0-i-1]:
                    tmp1 = list(s)
                    tmp2 = list(s)
                    
                    del tmp1[i]
                    del tmp2[0-i-1]
                    
                    s1 = ''.join(tmp1[:len(tmp1)//2])
                    s2 = ''.join(tmp1[len(tmp1)//2:])
                    
                    t1 = ''.join(tmp2[:len(tmp2)//2])
                    t2 = ''.join(tmp2[len(tmp2)//2:])
                    
                    
                    if s1!=s2[::-1] and t1!=t2[::-1]:return False
                    if s1==s2[::-1]:
                        s=''.join(tmp1)
                    if t1==t2[::-1]:
                        s=''.join(tmp2)
                    
                    i-=1
                    c+=1
                    
                if c>1:return False  
                i+=1
           
            return True
        else:
            c=0
            i = 0
            while i<lim//2:
                if s[i]!=s[0-i-1]:
                
                    tmp1 = list(s)
                    tmp2 = list(s)
                    
                    del tmp1[i]
                    del tmp2[0-i-1]
                    
                    s1 = ''.join(tmp1[:len(tmp1)//2])
                    s2 = ''.join(tmp1[len(tmp1)//2+1:])
                    
                    t1 = ''.join(tmp2[:len(tmp2)//2])
                    t2 = ''.join(tmp2[len(tmp2)//2+1:])
                    
                    
                    if s1!=s2[::-1] and t1!=t2[::-1]:return False
                    if s1==s2[::-1]:
                        s=''.join(tmp1)
                    if t1==t2[::-1]:
                        s=''.join(tmp2)
                    
                    i-=1
                    c+=1
                    
                if c>1:return False  
                i+=1
           
            return True
