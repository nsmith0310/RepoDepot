class Solution:
    
    def r(self, s) -> str:
        l = list(s)
        
        rear = 0
        front = 0
        tmp = ""
        
        t = 0
        i = 0
        
        while i<len(s):
            st = ""
            j = i
            while j<len(s) and s[j]!="]":
                j+=1
            if s[j]=="]":
                t = 1
            rear = j
            
            j-=1
            
            while s[j]!="[":
                st+=s[j]
                j-=1
            
            st=st[::-1]
            
            num = ""
            j-=1
            
            while j>=0 and ord(s[j])>=48 and ord(s[j])<=57:
                num+=s[j]
                j -=1
            front = j
            num = int(num[::-1])
            
            k = 0
            while k<num:
                tmp+=st
                k+=1
            
            l[front+1:rear+1]=tmp
            if "[" not in l:
                
                return ''.join(l)
            
            else:
                return self.r(''.join(l))
            i+=1
        
        
    
    def decodeString(self, s: str) -> str:
        if s=="" or "[" not in s:
            return s
        else:
            return (self.r(s))
