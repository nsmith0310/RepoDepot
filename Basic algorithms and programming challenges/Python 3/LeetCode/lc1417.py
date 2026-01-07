class Solution:
    def reformat(self, s: str) -> str:
        
        f = ""
        
        alph = ""
        num = ""
        
        a = 0
        n = 0
        
        i = 0
        while i<len(s):
            if ord(s[i])>=97 and ord(s[i])<=122: 
                alph+=s[i]
                a+=1
            else: 
                num+=s[i]
                n+=1
            i+=1
        
        
        if abs(a-n)>1: return ""
        
        if a>n:
            f = alph[0]
            alph = alph[1:]
            i = 0
            while i<n:
                f+=num[i]+alph[i]
                i+=1
            return f
        elif n>a:
            f = num[0]
            num = num[1:]
            i = 0
            while i<a:
                f+=alph[i]+num[i]
                i+=1
            return f
        else:
            i = 0
            while i<a:
                f+=alph[i]+num[i]
                i+=1
            return f
            
